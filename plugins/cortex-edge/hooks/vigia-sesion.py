"""
🌱 Cortex Edge · Hook UserPromptSubmit — vigía de la sesión.

Dos avisos, cada uno en una sola línea y solo cuando hay un hecho que lo justifica:

1. RECORDATORIO DE GUARDADO. Cada N mensajes de la persona (por defecto 20), si en ese
   tramo no se escribió ningún recuerdo en la carpeta de memoria, recuerda guardar ahora
   lo que la próxima sesión debería saber, en vez de dejarlo todo para el cierre (que a
   veces no llega: la ventana se cierra, se corta la luz, la sesión se compacta).
   Si hubo escritura en la memoria, no dice nada.

2. TOPE DE CONTEXTO. Cada mensaje relee todo el contexto de la sesión. Cuando el
   contexto de la última llamada pasa del tope (por defecto 500 000 tokens), avisa: no
   cortar la tarea en curso; en el siguiente cierre natural, cerrar con handoff y seguir
   en una sesión nueva. Nunca esperar la compactación automática. Se mide el contexto
   ACTUAL (la última llamada), no el promedio: tras una compactación el aviso se apaga solo.
   Repite el aviso cada 10 mensajes como máximo, para no volverse ruido.

Configuración opcional en <memoria>/cortex-edge.json:
   {"recordatorio_guardado": 20}   cada cuántos mensajes (false lo apaga)
   {"tope_contexto": 500000}       tope en tokens (false lo apaga). Con ventanas de
                                   200 000 tokens conviene bajarlo, p. ej. a 150000.

Estado: un archivo pequeño por sesión en la carpeta temporal del sistema (no en tu
memoria). Es fail-silent: si algo falla, no rompe la sesión.
"""
from __future__ import annotations
import json, os, re, sys, tempfile, time
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import comun  # noqa: E402

RECORDATORIO_DEFECTO = 20
TOPE_DEFECTO = 500_000
REPETIR_TOPE_CADA = 10          # mensajes entre avisos de tope
COLA_TRANSCRIPT = 512 * 1024    # solo se lee el final del transcript (puede pesar decenas de MB)
CADUCIDAD_ESTADO = 7 * 86400    # archivos de estado de sesiones viejas se borran


def carpeta_estado() -> Path:
    return Path(tempfile.gettempdir()) / "cortex-edge"


def leer_entrada(texto: str) -> dict:
    try:
        datos = json.loads(texto or "{}")
        return datos if isinstance(datos, dict) else {}
    except Exception:
        return {}


def ajuste(config: dict, clave: str, defecto: int) -> int:
    """Entero positivo de la config; 0 si está apagado (false/0); el defecto si falta o es inválido."""
    v = config.get(clave, defecto)
    if v is False or v == 0:
        return 0
    if isinstance(v, bool) or not isinstance(v, int) or v < 0:
        return defecto
    return v


def contexto_actual(transcript: str | None) -> int:
    """Tokens de contexto de la última llamada del modelo en la sesión principal (0 si no se sabe)."""
    if not transcript:
        return 0
    try:
        with open(transcript, "rb") as f:
            f.seek(0, os.SEEK_END)
            tam = f.tell()
            f.seek(max(0, tam - COLA_TRANSCRIPT))
            cola = f.read().decode("utf-8", "ignore")
    except Exception:
        return 0
    for linea in reversed(cola.splitlines()):
        if '"usage"' not in linea:
            continue
        try:
            e = json.loads(linea)
        except ValueError:
            continue
        if e.get("type") != "assistant" or e.get("isSidechain"):
            continue
        u = (e.get("message") or {}).get("usage") or {}
        total = sum(int(u.get(k, 0) or 0) for k in
                    ("input_tokens", "cache_read_input_tokens", "cache_creation_input_tokens"))
        if total:
            return total
    return 0


def ultima_escritura_memoria(base: Path) -> float:
    """mtime más reciente de un recuerdo (*.md) en la carpeta de memoria; 0 si no hay."""
    try:
        return max((p.stat().st_mtime for p in base.glob("*.md")), default=0.0)
    except Exception:
        return 0.0


def miles(n: int) -> str:
    return f"{round(n / 1000):,}".replace(",", ".")


def limpiar_estados_viejos(d: Path) -> None:
    try:
        ahora = time.time()
        for p in d.glob("*.json"):
            if ahora - p.stat().st_mtime > CADUCIDAD_ESTADO:
                p.unlink()
    except Exception:
        pass


def construir(entrada: dict) -> str:
    base = comun.carpeta_memoria()
    config = comun.leer_config(base)
    cada = ajuste(config, "recordatorio_guardado", RECORDATORIO_DEFECTO)
    tope = ajuste(config, "tope_contexto", TOPE_DEFECTO)
    if not cada and not tope:
        return ""
    lang = comun.idioma(base)

    sesion = re.sub(r"[^A-Za-z0-9_-]", "", str(entrada.get("session_id") or "")) or "sin-id"
    d = carpeta_estado()
    d.mkdir(parents=True, exist_ok=True)
    archivo = d / f"{sesion}.json"
    try:
        estado = json.loads(archivo.read_text(encoding="utf-8"))
        if not isinstance(estado, dict):
            estado = {}
    except Exception:
        estado = {}
        limpiar_estados_viejos(d)

    ahora = time.time()
    turno = int(estado.get("turnos", 0)) + 1
    estado["turnos"] = turno
    estado.setdefault("desde", ahora)          # inicio del tramo actual del recordatorio
    avisos = []

    if cada and turno % cada == 0:
        if ultima_escritura_memoria(base) < float(estado["desde"]):
            avisos.append(comun.txt(
                lang,
                f"💾 Llevas {turno} mensajes en esta sesión y en los últimos {cada} no se guardó ningún "
                "recuerdo. Si surgió algo que la próxima sesión deba saber (una decisión y su porqué, una "
                "corrección, el estado de un proyecto), guárdalo ahora con el protocolo de memoria; no "
                "esperes al cierre. Si no hay nada, sigue sin mencionarlo.",
                f"💾 {turno} messages into this session and nothing was saved to memory in the last {cada}. "
                "If something came up that the next session should know (a decision and its why, a "
                "correction, a project's state), save it now following the memory protocol; don't wait "
                "for the close. If there's nothing, carry on without mentioning it.",
            ))
        estado["desde"] = ahora

    if tope:
        ctx = contexto_actual(entrada.get("transcript_path"))
        ultimo = int(estado.get("aviso_tope", -REPETIR_TOPE_CADA))
        if ctx > tope and turno - ultimo >= REPETIR_TOPE_CADA:
            avisos.append(comun.txt(
                lang,
                f"📏 Esta sesión relee ~{miles(ctx)} mil tokens de contexto en cada mensaje (tope: "
                f"{miles(tope)} mil). No cortes la tarea en curso: en el próximo cierre natural, cierra con "
                "/cortex-edge:cierra (handoff con el estado vigente) y sigue en una sesión nueva. No esperes "
                "la compactación automática. Díselo a la persona en una línea.",
                f"📏 This session re-reads ~{miles(ctx)}k tokens of context on every message (ceiling: "
                f"{miles(tope)}k). Don't cut the current task short: at the next natural stopping point, "
                "close with /cortex-edge:close (handoff with the current state) and continue in a fresh "
                "session. Don't wait for automatic compaction. Tell the person in one line.",
            ))
            estado["aviso_tope"] = turno

    try:
        archivo.write_text(json.dumps(estado), encoding="utf-8")
    except Exception:
        pass
    return "\n".join(avisos)


def main() -> int:
    try:
        entrada = leer_entrada(sys.stdin.read())
    except Exception:
        entrada = {}
    try:
        comun.emitir("UserPromptSubmit", construir(entrada))
    except Exception:
        pass  # nunca rompas la sesión
    return 0


if __name__ == "__main__":
    sys.exit(main())
