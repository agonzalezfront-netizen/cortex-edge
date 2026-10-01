#!/usr/bin/env python3
"""
🌱 Cortex Edge · tokens — where do your Claude Code tokens go? / ¿dónde se van tus tokens?

Reads the local Claude Code transcripts (~/.claude/projects/**/*.jsonl, including the
subagent transcripts stored under <session>/subagents/) and adds up the `usage` of every
model call by day, model, what triggered the turn, and session, with the context size of
each call (median, p90 and the latest one).

Why: the feeling of "I'm using it a lot" points at the wrong lever. When output is ~1 % of
the volume, the spend is not reasoning: it's a big context being re-read on every message,
and automatic wake-ups (background notifications, scheduled prompts) re-reading it again.
The lever is a smaller context and fewer wake-ups, not a cheaper model.

Privacy: it only reads local files and prints numbers. It never prints message contents
and never sends anything anywhere. Python 3 standard library only.

Usage:
  python tokens.py                         # last 7 days, report in the person's language
  python tokens.py --dias 14               # another window
  python tokens.py --idioma es|en          # force the language
  python tokens.py --tope 300000           # context ceiling for live sessions (default 500000)
  python tokens.py --json                  # raw aggregates as JSON
  python tokens.py --verificar             # exit 1 if a live session is over the ceiling
"""
from __future__ import annotations
import argparse
import collections
import datetime as dt
import json
import os
import re
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

# Relative prices published by Anthropic, normalised to input = 1.
PESOS = {"input_tokens": 1.0, "cache_creation_input_tokens": 1.25, "cache_read_input_tokens": 0.1,
         "output_tokens": 5.0}
TOPE_DEFECTO = 500_000
HORAS_VIVA = 6  # a session touched in the last N hours counts as live

DISPARADORES = ("persona", "automatico", "arranque", "subagente")
NOMBRES = {
    "es": {"persona": "la persona", "automatico": "automático (notificación/programado)",
           "arranque": "arranque", "subagente": "subagente"},
    "en": {"persona": "the person", "automatico": "automatic (notification/scheduled)",
           "arranque": "startup", "subagente": "subagent"},
}


def raiz_defecto() -> Path:
    base = os.environ.get("CLAUDE_CONFIG_DIR") or str(Path.home() / ".claude")
    return Path(base) / "projects"


def idioma_defecto() -> str:
    """The person's language as the plugin knows it (hooks/comun.py); English if unknown."""
    try:
        sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "hooks"))
        import comun  # noqa: E402
        return comun.idioma() or "en"
    except Exception:
        return "en"


# ---------- classification ----------
def texto_de(contenido) -> str:
    if isinstance(contenido, str):
        return contenido
    if isinstance(contenido, list):
        return " ".join(b.get("text", "") for b in contenido if isinstance(b, dict) and b.get("type") == "text")
    return ""


ARRANQUE = re.compile(r"^(<command-name>)?/?(cortex-edge:)?(arranca|start)\b", re.I)


def clasificar(entrada: dict) -> str | None:
    """What woke the model up. None = this user entry doesn't change the trigger
    (tool results, skill text loaded by the harness, summaries after compaction, images)."""
    t = texto_de((entrada.get("message") or {}).get("content")).strip()
    if not t:
        return None
    tl = t.lower()
    if "<task-notification>" in tl or "monitor event" in tl:
        return "automatico"
    if entrada.get("isMeta"):
        # Harness-injected text. Only scheduled prompts and messages from other sessions are wake-ups.
        if "[cron" in tl or "scheduled task" in tl or "another claude session sent" in tl:
            return "automatico"
        return None
    if tl.startswith("this session is being continued") or tl.startswith("[request interrupted"):
        return None
    if ARRANQUE.match(tl):
        return "arranque"
    return "persona"


def modelo_corto(m) -> str:
    m = str(m or "").replace("claude-", "")
    return m or "?"


def contexto_de(u: dict) -> int:
    return sum(int(u.get(k, 0) or 0) for k in ("input_tokens", "cache_read_input_tokens",
                                                  "cache_creation_input_tokens"))


# ---------- aggregation ----------
def nuevo() -> dict:
    return {"bruto": 0, "ponderado": 0.0, "llamadas": 0, "salida": 0, "cache_lectura": 0}


def sumar(a: dict, u: dict) -> None:
    a["llamadas"] += 1
    for k, w in PESOS.items():
        v = int(u.get(k, 0) or 0)
        a["bruto"] += v
        a["ponderado"] += v * w
    a["salida"] += int(u.get("output_tokens", 0) or 0)
    a["cache_lectura"] += int(u.get("cache_read_input_tokens", 0) or 0)


def percentil(valores, p) -> int:
    if not valores:
        return 0
    s = sorted(valores)
    return s[min(len(s) - 1, int(len(s) * p))]


def agregar(transcripts: dict, desde: dt.datetime) -> dict:
    """transcripts: {path: iterable of jsonl entries}. desde: aware datetime.
    Files inside a `subagents` folder belong to the session that launched them."""
    por_dia = collections.defaultdict(lambda: collections.defaultdict(nuevo))
    por_modelo = collections.defaultdict(nuevo)
    por_disp = collections.defaultdict(nuevo)
    por_sesion: dict[str, dict] = {}
    herramientas = collections.defaultdict(collections.Counter)
    for ruta, entradas in transcripts.items():
        p = Path(ruta)
        es_sub = "subagents" in p.parts
        if es_sub:
            i = p.parts.index("subagents")
            clave, proyecto = str(Path(*p.parts[:i])), p.parts[i - 2] if i >= 2 else "?"
        else:
            clave, proyecto = str(p.with_suffix("")), p.parent.name
        disparador = "persona"
        for e in entradas:
            if not isinstance(e, dict) or not e.get("timestamp"):
                continue
            try:
                t = dt.datetime.fromisoformat(str(e["timestamp"]).replace("Z", "+00:00"))
            except ValueError:
                continue
            if t.tzinfo is None:
                t = t.replace(tzinfo=dt.timezone.utc)
            if t < desde:
                continue
            sub = es_sub or bool(e.get("isSidechain"))
            if e.get("type") == "user" and not sub:
                d = clasificar(e)
                if d:
                    disparador = d
                continue
            if e.get("type") != "assistant":
                continue
            msg = e.get("message") or {}
            u = msg.get("usage") or {}
            m = modelo_corto(msg.get("model"))
            if not u or m.startswith("<"):  # <synthetic>: harness messages, no real model call
                continue
            disp = "subagente" if sub else disparador
            sumar(por_dia[t.astimezone().strftime("%Y-%m-%d")][m], u)
            sumar(por_modelo[m], u)
            sumar(por_disp[disp], u)
            s = por_sesion.get(clave)
            if s is None:
                s = por_sesion[clave] = {"sesion": Path(clave).name[:8], "proyecto": proyecto,
                                         "modelos": collections.Counter(), "ctx": [], "ultima": t,
                                         "ctx_ultimo": 0, "_t_ctx": None, **nuevo()}
            sumar(s, u)
            s["modelos"][m] += 1
            s["ultima"] = max(s["ultima"], t)
            if not sub:  # the session's own context, not its subagents'
                s["ctx"].append(contexto_de(u))
                if s["_t_ctx"] is None or t >= s["_t_ctx"]:
                    s["_t_ctx"], s["ctx_ultimo"] = t, contexto_de(u)
            for b in msg.get("content") or []:
                if isinstance(b, dict) and b.get("type") == "tool_use":
                    herramientas[m][b.get("name", "?")] += 1
    for s in por_sesion.values():
        s["ctx_mediano"] = percentil(s["ctx"], 0.5)
        s["ctx_p90"] = percentil(s["ctx"], 0.9)
        s["modelos"] = dict(s["modelos"])
        s["ultima"] = s["ultima"].isoformat()
        del s["ctx"], s["_t_ctx"]
    return {"por_dia": {d: dict(ms) for d, ms in sorted(por_dia.items())},
            "por_modelo": dict(por_modelo),
            "por_disparador": dict(por_disp),
            "por_sesion": por_sesion,
            "herramientas": {m: c.most_common(5) for m, c in herramientas.items()}}


def leer_transcripts(raiz: Path, desde: dt.datetime) -> dict:
    """Every *.jsonl under the projects folder (subagents included) touched inside the window."""
    out = {}
    for ruta in raiz.rglob("*.jsonl"):
        try:
            if dt.datetime.fromtimestamp(ruta.stat().st_mtime, dt.timezone.utc) < desde:
                continue
        except OSError:
            continue

        def gen(r=ruta):
            with open(r, encoding="utf-8", errors="ignore") as f:
                for linea in f:
                    try:
                        yield json.loads(linea)
                    except ValueError:
                        continue
        out[str(ruta)] = gen()
    return out


def vivas_sobre_tope(res: dict, tope: int, ahora: dt.datetime) -> list[dict]:
    limite = ahora - dt.timedelta(hours=HORAS_VIVA)
    return [s for s in res["por_sesion"].values()
            if dt.datetime.fromisoformat(s["ultima"]) >= limite and s["ctx_ultimo"] > tope]


# ---------- report ----------
_ES = False  # number format of the current report (es: 1.234.567 · 0,2 %)


def _local(s: str) -> str:
    return s.replace(",", "_").replace(".", ",").replace("_", ".") if _ES else s


def n(x) -> str:
    return _local(f"{int(x):,}")


def k(x) -> str:
    return _local(f"{int(x) / 1000:,.0f}") + (" mil" if _ES else "k")


def pct(x: float) -> str:
    return _local(f"{x:.1f}") + (" %" if _ES else "%")


def nombre_proyecto(carpeta: str) -> str:
    """Project folders encode their path (/home/ana/app becomes -home-ana-app). Drop the home-folder prefix."""
    casa = re.sub(r"[^A-Za-z0-9]", "-", str(Path.home()))
    return carpeta[len(casa) + 1:] if carpeta.startswith(casa + "-") and len(carpeta) > len(casa) + 1 else carpeta


def informe(res: dict, dias: int, tope: int, lang: str, ahora: dt.datetime) -> str:
    global _ES
    es = _ES = lang == "es"
    T = (lambda a, b: a if es else b)
    nom = NOMBRES["es" if es else "en"]
    total = nuevo()
    for a in res["por_modelo"].values():
        for c in total:
            total[c] += a[c]
    pct_salida = 100 * total["salida"] / max(1, total["bruto"])
    pct_cache = 100 * total["cache_lectura"] / max(1, total["bruto"])
    L = [T(f"# Tokens de Claude Code — últimos {dias} días (al {ahora:%Y-%m-%d %H:%M})",
           f"# Claude Code tokens — last {dias} days (as of {ahora:%Y-%m-%d %H:%M})"), ""]
    if not total["llamadas"]:
        L.append(T("No hay llamadas en esa ventana. ¿La carpeta de transcripts es otra? Usa --raiz.",
                   "No calls in that window. Is the transcripts folder elsewhere? Use --raiz."))
        return "\n".join(L) + "\n"
    L += [T(f"**{n(total['llamadas'])} llamadas · {n(total['bruto'])} tokens brutos · salida {pct(pct_salida)} · "
            f"lectura de caché {pct(pct_cache)}**",
            f"**{n(total['llamadas'])} calls · {n(total['bruto'])} raw tokens · output {pct(pct_salida)} · "
            f"cache reads {pct(pct_cache)}**"),
          T("Ponderado = costo relativo: entrada 1 · escritura de caché 1,25 · lectura de caché 0,1 · salida 5.",
            "Weighted = relative cost: input 1 · cache write 1.25 · cache read 0.1 · output 5."), ""]

    def tabla(titulo, cab, filas):
        L.extend([f"## {titulo}", "", "| " + " | ".join(cab) + " |", "|" + "---|" * len(cab)])
        L.extend("| " + " | ".join(f) + " |" for f in filas)
        L.append("")

    pond_total = max(1.0, sum(a["ponderado"] for a in res["por_modelo"].values()))
    tabla(T("Por modelo", "By model"),
          [T("Modelo", "Model"), T("Llamadas", "Calls"), T("Brutos", "Raw"), T("Ponderado", "Weighted"), "%"],
          [[m, n(a["llamadas"]), n(a["bruto"]), n(a["ponderado"]), f"{100 * a['ponderado'] / pond_total:.0f}"]
           for m, a in sorted(res["por_modelo"].items(), key=lambda kv: -kv[1]["ponderado"])])
    tabla(T("Qué despertó al modelo", "What woke the model up"),
          [T("Disparador", "Trigger"), T("Llamadas", "Calls"), T("Ponderado", "Weighted"), "%"],
          [[nom.get(d, d), n(a["llamadas"]), n(a["ponderado"]), f"{100 * a['ponderado'] / pond_total:.0f}"]
           for d, a in sorted(res["por_disparador"].items(), key=lambda kv: -kv[1]["ponderado"])])
    tabla(T("Por día", "By day"),
          [T("Día", "Day"), T("Llamadas", "Calls"), T("Ponderado", "Weighted"), T("Modelo principal", "Main model")],
          [[d, n(sum(a["llamadas"] for a in ms.values())), n(sum(a["ponderado"] for a in ms.values())),
            max(ms.items(), key=lambda kv: kv[1]["ponderado"])[0]] for d, ms in res["por_dia"].items()])
    sesiones = sorted(res["por_sesion"].values(), key=lambda s: -s["ponderado"])[:8]
    tabla(T("Sesiones más caras (contexto = lo que se relee en cada mensaje)",
            "Most expensive sessions (context = what gets re-read on every message)"),
          [T("Sesión", "Session"), T("Proyecto", "Project"), T("Llamadas", "Calls"), T("Ponderado", "Weighted"),
           T("Ctx mediano", "Median ctx"), "Ctx p90", T("Ctx último", "Latest ctx")],
          [[f"`{s['sesion']}`", nombre_proyecto(s["proyecto"]), n(s["llamadas"]), n(s["ponderado"]),
            k(s["ctx_mediano"]), k(s["ctx_p90"]), k(s["ctx_ultimo"])] for s in sesiones])
    if res["herramientas"]:
        L.append(f"## {T('Herramientas más llamadas', 'Most-called tools')}")
        L.append("")
        for m, hs in sorted(res["herramientas"].items()):
            L.append(f"- **{m}**: " + " · ".join(f"{h} {c}" for h, c in hs))
        L.append("")

    L.append(f"## {T('Veredicto', 'Verdict')}")
    L.append("")
    sobre = vivas_sobre_tope(res, tope, ahora.astimezone(dt.timezone.utc))
    for s in sobre:
        L.append(T(f"- AVISO · sesión viva `{s['sesion']}` ({nombre_proyecto(s['proyecto'])}) relee {k(s['ctx_ultimo'])} "
                   f"por mensaje, sobre el tope de {k(tope)}. No cortes la tarea: en el próximo cierre natural, "
                   "cierra con handoff y sigue en una sesión nueva. No esperes la compactación automática.",
                   f"- WARNING · live session `{s['sesion']}` ({nombre_proyecto(s['proyecto'])}) re-reads "
                   f"{k(s['ctx_ultimo'])} per message, over the {k(tope)} ceiling. Don't cut the task short: at the "
                   "next natural stopping point, close with a handoff and continue in a fresh session. Don't wait "
                   "for automatic compaction."))
    if not sobre:
        L.append(T(f"- OK · ninguna sesión viva sobre el tope de contexto ({k(tope)}).",
                   f"- OK · no live session over the context ceiling ({k(tope)})."))
    auto = res["por_disparador"].get("automatico", {}).get("ponderado", 0) / pond_total
    if auto >= 0.2:
        L.append(T(f"- AVISO · {100 * auto:.0f} % del costo lo dispararon despertares automáticos, no la persona. "
                   "Un vigilante que solo despierta al modelo ante un hecho nuevo (script, no agente) lo reduce.",
                   f"- WARNING · {100 * auto:.0f}% of the cost was triggered by automatic wake-ups, not the person. "
                   "A watcher that only wakes the model on a new fact (a script, not an agent) cuts it down."))
    if pct_salida < 1:
        L.append(T(f"- Lectura · la salida es {pct(pct_salida)} del volumen: el gasto es releer contexto, no "
                   "razonar. La palanca es contexto más chico y menos despertares, no un modelo más barato.",
                   f"- Reading · output is {pct(pct_salida)} of the volume: the spend is re-reading context, not "
                   "reasoning. The lever is a smaller context and fewer wake-ups, not a cheaper model."))
    return "\n".join(L) + "\n"


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Where do your Claude Code tokens go?")
    ap.add_argument("--dias", type=int, default=7)
    ap.add_argument("--tope", type=int, default=TOPE_DEFECTO, help="context ceiling for live sessions")
    ap.add_argument("--idioma", choices=("es", "en"))
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--verificar", action="store_true", help="exit 1 if a live session is over the ceiling")
    ap.add_argument("--raiz", default=str(raiz_defecto()), help="Claude Code projects folder")
    a = ap.parse_args(argv)
    ahora = dt.datetime.now().astimezone()
    desde = ahora - dt.timedelta(days=a.dias)
    res = agregar(leer_transcripts(Path(a.raiz), desde), desde)
    if a.json:
        print(json.dumps(res, ensure_ascii=False, default=str))
    else:
        print(informe(res, a.dias, a.tope, a.idioma or idioma_defecto(), ahora), end="")
    if a.verificar and vivas_sobre_tope(res, a.tope, ahora):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
