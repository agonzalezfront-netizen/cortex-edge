"""Tests of tokens.py — no network, synthetic transcripts in temporary folders.

Run:  python -m unittest test_tokens      (from this folder)
"""
import datetime as dt
import io
import json
import os
import pathlib
import shutil
import sys
import tempfile
import unittest
from contextlib import redirect_stdout

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tokens as tk  # noqa: E402

GRANDE = {"input_tokens": 10, "cache_read_input_tokens": 520_000, "cache_creation_input_tokens": 1000,
          "output_tokens": 500}
CHICO = {"input_tokens": 5, "cache_read_input_tokens": 20_000, "output_tokens": 100}


def e(tipo, ts, texto=None, usage=None, modelo="claude-opus-5-5", sidechain=False, meta=False, tools=()):
    x = {"type": tipo, "timestamp": ts, "isSidechain": sidechain, "message": {}}
    if meta:
        x["isMeta"] = True
    if tipo == "user":
        x["message"]["content"] = [{"type": "text", "text": texto or ""}]
    else:
        x["message"].update(model=modelo, usage=usage or {},
                            content=[{"type": "tool_use", "name": t} for t in tools])
    return x


def iso(t):
    return t.isoformat().replace("+00:00", "Z")


class TestClasificar(unittest.TestCase):
    def c(self, texto, meta=False):
        return tk.clasificar(e("user", "2026-10-01T00:00:00Z", texto, meta=meta))

    def test_disparadores(self):
        self.assertEqual(self.c("<task-notification><task-id>x</task-id>"), "automatico")
        self.assertEqual(self.c("/cortex-edge:arranca"), "arranque")
        self.assertEqual(self.c("<command-name>/cortex-edge:start</command-name>"), "arranque")
        self.assertEqual(self.c("let's review the plan"), "persona")
        self.assertEqual(self.c("[cron-check] tick", meta=True), "automatico")

    def test_no_cambian_el_disparador(self):
        self.assertIsNone(self.c("   "))                                   # tool result without text
        self.assertIsNone(self.c("Base directory for this skill: /x", meta=True))
        self.assertIsNone(self.c("This session is being continued from a previous conversation"))
        self.assertIsNone(self.c("[Request interrupted by user]"))


class TestAgregar(unittest.TestCase):
    def setUp(self):
        self.desde = dt.datetime(2026, 9, 30, tzinfo=dt.timezone.utc)
        sesion = "/p/C--home-x-app/aaaa1111-2222.jsonl"
        sub = "/p/C--home-x-app/aaaa1111-2222/subagents/agent-1.jsonl"
        self.datos = {
            sesion: [
                e("user", "2026-10-01T12:00:00Z", "/cortex-edge:arranca"),
                e("assistant", "2026-10-01T12:00:05Z", usage=CHICO, tools=("Bash", "Read")),
                e("user", "2026-10-01T12:01:00Z", "review the flow"),
                e("assistant", "2026-10-01T12:01:05Z", usage=GRANDE, tools=("Bash",)),
                e("user", "2026-10-01T12:02:00Z", ""),                       # tool result: still 'persona'
                e("assistant", "2026-10-01T12:02:05Z", usage=GRANDE),
                e("user", "2026-10-01T12:10:00Z", "<task-notification>done</task-notification>"),
                e("assistant", "2026-10-01T12:10:05Z", usage=GRANDE),
                e("assistant", "2026-10-01T12:11:00Z", usage=GRANDE, modelo="<synthetic>"),  # not a real call
                e("assistant", "2026-09-01T12:00:00Z", usage=GRANDE),       # outside the window
            ],
            sub: [  # subagent transcript stored apart from its session (newer Claude Code layout)
                e("user", "2026-10-01T12:20:00Z", "do the chore"),
                e("assistant", "2026-10-01T12:20:05Z", usage={"cache_read_input_tokens": 900_000},
                  modelo="claude-haiku-5-5", sidechain=True),
            ],
        }

    def test_disparador_y_modelo(self):
        r = tk.agregar(self.datos, self.desde)
        d = r["por_disparador"]
        self.assertEqual(d["arranque"]["llamadas"], 1)
        self.assertEqual(d["persona"]["llamadas"], 2)
        self.assertEqual(d["automatico"]["llamadas"], 1)
        self.assertEqual(d["subagente"]["llamadas"], 1)
        self.assertEqual(r["por_modelo"]["opus-5-5"]["llamadas"], 4)
        self.assertEqual(r["por_modelo"]["haiku-5-5"]["llamadas"], 1)

    def test_subagentes_se_suman_a_su_sesion_sin_inflar_el_contexto(self):
        r = tk.agregar(self.datos, self.desde)
        self.assertEqual(len(r["por_sesion"]), 1)
        s = next(iter(r["por_sesion"].values()))
        self.assertEqual(s["llamadas"], 5)
        self.assertEqual(s["ctx_mediano"], 521_010)       # the 900k subagent call isn't this session's context
        self.assertEqual(s["ctx_ultimo"], 521_010)
        self.assertEqual(s["proyecto"], "C--home-x-app")
        self.assertEqual(s["sesion"], "aaaa1111")
        self.assertEqual(s["ultima"], "2026-10-01T12:20:05+00:00")

    def test_ponderado(self):
        r = tk.agregar(self.datos, self.desde)
        self.assertAlmostEqual(r["por_disparador"]["arranque"]["ponderado"], 5 + 20_000 * 0.1 + 100 * 5)
        self.assertEqual(r["herramientas"]["opus-5-5"][0], ("Bash", 2))


class TestFinAFin(unittest.TestCase):
    def setUp(self):
        self.raiz = pathlib.Path(tempfile.mkdtemp())
        self.ahora = dt.datetime.now(dt.timezone.utc)

    def tearDown(self):
        shutil.rmtree(self.raiz, ignore_errors=True)

    def escribir(self, rel, filas):
        f = self.raiz / rel
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text("\n".join(json.dumps(x) if isinstance(x, dict) else x for x in filas) + "\n", encoding="utf-8")

    def correr(self, *args):
        buf = io.StringIO()
        with redirect_stdout(buf):
            rc = tk.main(["--raiz", str(self.raiz), "--dias", "1", *args])
        return rc, buf.getvalue()

    def test_lee_subcarpetas_y_tolera_basura(self):
        ts = iso(self.ahora)
        self.escribir("proj/s1.jsonl", [e("user", ts, "hi"), "not json", e("assistant", ts, usage=CHICO)])
        self.escribir("proj/s1/subagents/workflows/wf_1/agent-a.jsonl",
                      [e("assistant", ts, usage=CHICO, modelo="claude-sonnet-5-5", sidechain=True)])
        rc, out = self.correr("--json")
        self.assertEqual(rc, 0)
        j = json.loads(out)
        self.assertEqual(j["por_modelo"]["sonnet-5-5"]["llamadas"], 1)
        self.assertEqual(j["por_disparador"]["subagente"]["llamadas"], 1)

    def test_informe_en_ambos_idiomas_sin_contenido_de_mensajes(self):
        ts = iso(self.ahora)
        self.escribir("proj/s1.jsonl", [e("user", ts, "secret plan for the launch"), e("assistant", ts, usage=CHICO)])
        _, es = self.correr("--idioma", "es")
        _, en = self.correr("--idioma", "en")
        self.assertIn("## Qué despertó al modelo", es)
        self.assertIn("## What woke the model up", en)
        self.assertIn("OK", es)
        for out in (es, en):
            self.assertNotIn("secret plan", out)   # numbers only, never message contents

    def test_tope_de_contexto(self):
        ts = iso(self.ahora)
        self.escribir("proj/s2.jsonl", [e("user", ts, "hi"), e("assistant", ts, usage=GRANDE)])
        rc, out = self.correr("--idioma", "en", "--verificar")
        self.assertEqual(rc, 1)
        self.assertIn("WARNING · live session", out)
        rc, out = self.correr("--idioma", "en", "--verificar", "--tope", "600000")
        self.assertEqual(rc, 0)
        self.assertIn("OK · no live session", out)
        rc, _ = self.correr("--idioma", "en")           # without --verificar it only reports
        self.assertEqual(rc, 0)

    def test_sesion_vieja_no_es_viva(self):
        viejo = iso(self.ahora - dt.timedelta(hours=10))
        self.escribir("proj/s3.jsonl", [e("user", viejo, "hi"), e("assistant", viejo, usage=GRANDE)])
        rc, out = self.correr("--idioma", "en", "--verificar")
        self.assertEqual(rc, 0)

    def test_carpeta_vacia(self):
        rc, out = self.correr("--idioma", "es")
        self.assertEqual(rc, 0)
        self.assertIn("No hay llamadas", out)


if __name__ == "__main__":
    unittest.main()
