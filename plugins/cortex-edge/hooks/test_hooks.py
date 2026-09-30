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


def correr(script, memoria, stdin='{"hook_event_name": "test"}'):
    env = dict(os.environ, CORTEX_MEMORY_PATH=str(memoria), PYTHONIOENCODING="utf-8")
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


class TestNuncaRompe(Base):
    def test_stdin_basura_y_vacio(self):
        for script in ("cargar-nucleo.py", "cargar-memoria.py", "reloj.py"):
            for entrada in ("", "no es json"):
                rc, _ = correr(script, self.mem, stdin=entrada)
                self.assertEqual(rc, 0, script)


if __name__ == "__main__":
    unittest.main()
