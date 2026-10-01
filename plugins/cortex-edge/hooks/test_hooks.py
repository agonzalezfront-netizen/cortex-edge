"""Tests of the Cortex Edge hooks: they run each script the way Claude Code does (JSON on
stdin, JSON on stdout) against a temporary memory folder. Nothing touches your real memory.

Run:  python -m unittest test_hooks      (from this folder)
"""
import json
import os
import pathlib
import shutil
import subprocess
import sys
import tempfile
import unittest
from datetime import datetime

AQUI = pathlib.Path(__file__).resolve().parent
LIMITE_CLAUDE_CODE = 10_000  # Claude Code truncates a hook's additionalContext beyond this


def correr(script, memoria, stdin='{"hook_event_name": "test"}', temporal=None):
    env = dict(os.environ, CORTEX_MEMORY_PATH=str(memoria), PYTHONIOENCODING="utf-8")
    if temporal:  # where vigia-sesion.py keeps its per-session state
        env.update(TEMP=str(temporal), TMP=str(temporal), TMPDIR=str(temporal))
    r = subprocess.run([sys.executable, str(AQUI / script)], input=stdin, capture_output=True,
                       text=True, encoding="utf-8", env=env, timeout=30)
    return r.returncode, r.stdout


class Base(unittest.TestCase):
    def setUp(self):
        self.mem = pathlib.Path(tempfile.mkdtemp())

    def tearDown(self):
        shutil.rmtree(self.mem, ignore_errors=True)

    def contexto(self, script, evento):
        rc, out = correr(script, self.mem)
        self.assertEqual(rc, 0)
        datos = json.loads(out)  # valid JSON for Claude Code
        hso = datos["hookSpecificOutput"]
        self.assertEqual(hso["hookEventName"], evento)
        ctx = hso["additionalContext"]
        self.assertIsInstance(ctx, str)
        self.assertLessEqual(len(ctx.encode("utf-16-le")) // 2, LIMITE_CLAUDE_CODE)
        return ctx


class TestNucleo(Base):
    def test_postura_y_protocolo(self):
        ctx = self.contexto("cargar-nucleo.py", "SessionStart")
        for esperado in ("Critical stance", "Postura crítica",           # stance
                         "Memory protocol", "Protocolo de memoria",      # protocol
                         "`feedback`", "`reference`", "`project`", "`user`",
                         "that's a bug", "es un bug", "Verify before narrating",
                         "190", str(self.mem)):
            self.assertIn(esperado, ctx)

    def test_sin_frontmatter_ni_comentarios(self):
        ctx = self.contexto("cargar-nucleo.py", "SessionStart")
        self.assertNotIn("mundo:", ctx)
        self.assertNotIn("<!--", ctx)

    def test_idioma_conocido_solo_esa_seccion(self):
        (self.mem / "prefiere-idioma-es.md").write_text("x", encoding="utf-8")
        ctx = self.contexto("cargar-nucleo.py", "SessionStart")
        self.assertIn("Postura crítica", ctx)
        self.assertIn("Protocolo de memoria", ctx)
        self.assertNotIn("Critical stance", ctx)

    def test_ambos_idiomas_caben_sin_truncar(self):
        # Without a known language both sections load; the last line of the ES protocol must arrive whole.
        ctx = self.contexto("cargar-nucleo.py", "SessionStart")
        self.assertLess(len(ctx), 9500)
        self.assertTrue(ctx.rstrip().endswith("sin jerga innecesaria."))

    def test_pensar_vs_ejecutar_y_honestidad(self):
        ctx = self.contexto("cargar-nucleo.py", "SessionStart")
        for esperado in ("Think vs. execute", "Pensar vs. ejecutar", "No objective judge", "Sin juez objetivo",
                         "Opus > Fable", "not verified", "sin verificar"):
            self.assertIn(esperado, ctx)

    def test_idioma_por_config(self):
        (self.mem / "cortex-edge.json").write_text('{"idioma": "en"}', encoding="utf-8")
        ctx = self.contexto("cargar-nucleo.py", "SessionStart")
        self.assertIn("Critical stance", ctx)
        self.assertNotIn("Postura crítica", ctx)


class TestMemoria(Base):
    def test_crea_semilla_y_la_carga(self):
        ctx = self.contexto("cargar-memoria.py", "SessionStart")
        self.assertTrue((self.mem / "MEMORY.md").exists())
        self.assertIn("MEMORY.md", ctx)

    def test_inyecta_el_indice(self):
        (self.mem / "MEMORY.md").write_text("# MEMORY\n\n- [Prefers tests first](tests.md) — TDD\n",
                                            encoding="utf-8")
        ctx = self.contexto("cargar-memoria.py", "SessionStart")
        self.assertIn("[Prefers tests first](tests.md)", ctx)
        self.assertNotIn("⚠️", ctx)

    def test_aviso_de_tamano_sobre_20kb(self):
        lineas = [f"- [Memory {i}](m{i}.md) — something worth remembering number {i}" for i in range(400)]
        (self.mem / "MEMORY.md").write_text("\n".join(lineas), encoding="utf-8")
        self.assertGreater((self.mem / "MEMORY.md").stat().st_size, 20 * 1024)
        ctx = self.contexto("cargar-memoria.py", "SessionStart")  # also checks <= 10 000
        self.assertIn("Consolidate", ctx)
        self.assertIn("INDEX TRUNCATED", ctx)          # says so instead of being cut silently
        self.assertIn("[Memory 0](m0.md)", ctx)        # keeps the beginning, whole lines

    def test_aviso_antes_de_truncar(self):
        lineas = [f"- [Memory {i}](m{i}.md) — something worth remembering {i}" for i in range(150)]
        (self.mem / "MEMORY.md").write_text("\n".join(lineas), encoding="utf-8")
        ctx = self.contexto("cargar-memoria.py", "SessionStart")
        self.assertIn("Consolidate", ctx)
        self.assertNotIn("INDEX TRUNCATED", ctx)

    def test_aviso_lineas_largas(self):
        (self.mem / "MEMORY.md").write_text("- [x](x.md) — " + "a" * 200 + "\n", encoding="utf-8")
        ctx = self.contexto("cargar-memoria.py", "SessionStart")
        self.assertIn("190", ctx)


class TestReloj(Base):
    def test_fecha_y_hora(self):
        ctx = self.contexto("reloj.py", "UserPromptSubmit")
        hoy = datetime.now().astimezone()
        self.assertIn(hoy.strftime("%Y-%m-%d"), ctx)
        self.assertRegex(ctx, r"\d{2}:\d{2}")
        self.assertIn(("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",
                       "Sunday")[hoy.weekday()], ctx)

    def test_interruptor_apagado(self):
        (self.mem / "cortex-edge.json").write_text('{"reloj": false}', encoding="utf-8")
        rc, out = correr("reloj.py", self.mem)
        self.assertEqual(rc, 0)
        self.assertEqual(out.strip(), "")

    def test_config_rota_no_apaga_ni_rompe(self):
        (self.mem / "cortex-edge.json").write_text("{esto no es json", encoding="utf-8")
        self.assertIn(datetime.now().strftime("%Y-%m-%d"), self.contexto("reloj.py", "UserPromptSubmit"))


def transcript(ruta, contexto, sidechain_final=False):
    """Synthetic transcript: one main-session call with `contexto` tokens (and optionally a bigger subagent call)."""
    filas = [
        {"type": "user", "message": {"content": "hola"}},
        {"type": "assistant", "message": {"usage": {"input_tokens": 10, "cache_read_input_tokens": contexto - 10,
                                                    "output_tokens": 5}}},
    ]
    if sidechain_final:
        filas.append({"type": "assistant", "isSidechain": True,
                      "message": {"usage": {"cache_read_input_tokens": 900_000}}})
    pathlib.Path(ruta).write_text("\n".join(json.dumps(f) for f in filas) + "\n", encoding="utf-8")


class TestVigia(Base):
    def setUp(self):
        super().setUp()
        self.tmp = pathlib.Path(tempfile.mkdtemp())

    def tearDown(self):
        super().tearDown()
        shutil.rmtree(self.tmp, ignore_errors=True)

    def turno(self, sesion="s1", transcript_path=""):
        stdin = json.dumps({"session_id": sesion, "transcript_path": transcript_path, "prompt": "x"})
        rc, out = correr("vigia-sesion.py", self.mem, stdin=stdin, temporal=self.tmp)
        self.assertEqual(rc, 0)
        if not out.strip():
            return ""
        ctx = json.loads(out)["hookSpecificOutput"]["additionalContext"]
        self.assertEqual(json.loads(out)["hookSpecificOutput"]["hookEventName"], "UserPromptSubmit")
        return ctx

    def config(self, **kw):
        (self.mem / "cortex-edge.json").write_text(json.dumps(kw), encoding="utf-8")

    def test_recordatorio_cada_n_sin_guardar(self):
        self.config(recordatorio_guardado=3, tope_contexto=False)
        self.assertEqual(self.turno(), "")
        self.assertEqual(self.turno(), "")
        self.assertIn("💾", self.turno())          # 3rd message, nothing saved
        self.assertEqual(self.turno(), "")

    def test_si_guardo_no_recuerda(self):
        self.config(recordatorio_guardado=2, tope_contexto=False)
        self.turno()
        (self.mem / "decision-x.md").write_text("---\ntype: project\n---\nx", encoding="utf-8")
        self.assertEqual(self.turno(), "")          # a memory was written during the stretch

    def test_sesiones_separadas(self):
        self.config(recordatorio_guardado=2, tope_contexto=False)
        self.turno("a")
        self.assertEqual(self.turno("b"), "")       # counters don't mix across sessions
        self.assertIn("💾", self.turno("a"))

    def test_tope_de_contexto(self):
        self.config(recordatorio_guardado=False)
        t = self.tmp / "t.jsonl"
        transcript(t, 520_000)
        ctx = self.turno(transcript_path=str(t))
        self.assertIn("📏", ctx)
        self.assertIn("520", ctx)
        self.assertEqual(self.turno(transcript_path=str(t)), "")   # doesn't repeat every message

    def test_bajo_el_tope_y_subagentes_no_cuentan(self):
        self.config(recordatorio_guardado=False)
        t = self.tmp / "t.jsonl"
        transcript(t, 120_000, sidechain_final=True)   # the 900k subagent call is not this session's context
        self.assertEqual(self.turno(transcript_path=str(t)), "")

    def test_tope_configurable(self):
        self.config(recordatorio_guardado=False, tope_contexto=100_000)
        t = self.tmp / "t.jsonl"
        transcript(t, 120_000)
        self.assertIn("📏", self.turno(transcript_path=str(t)))

    def test_todo_apagado(self):
        self.config(recordatorio_guardado=False, tope_contexto=False)
        for _ in range(3):
            self.assertEqual(self.turno(), "")

    def test_idioma(self):
        self.config(recordatorio_guardado=1, tope_contexto=False, idioma="es")
        ctx = self.turno()
        self.assertIn("Llevas 1 mensajes", ctx)
        self.assertNotIn("messages into", ctx)


class TestNuncaRompe(Base):
    def test_stdin_basura_y_vacio(self):
        tmp = tempfile.mkdtemp()
        for script in ("cargar-nucleo.py", "cargar-memoria.py", "reloj.py", "vigia-sesion.py"):
            for entrada in ("", "no es json", "[]", '{"transcript_path": "/no/existe.jsonl"}'):
                rc, _ = correr(script, self.mem, stdin=entrada, temporal=tmp)
                self.assertEqual(rc, 0, script)
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    unittest.main()
