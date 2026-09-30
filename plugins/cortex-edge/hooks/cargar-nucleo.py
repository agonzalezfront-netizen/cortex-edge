"""
🌱 Cortex Edge · Hook SessionStart — carga el NÚCLEO al inicio de cada sesión.

Qué inyecta en el contexto de Claude:
  1. La postura crítica           (POSTURA-CRITICA.md, en la raíz del plugin)
  2. El protocolo de memoria      (PROTOCOLO-MEMORIA.md, en la raíz del plugin)
  3. Dónde está la carpeta de memoria

Los textos NO están copiados aquí: se leen de esos archivos, que son la fuente única.
La memoria (MEMORY.md) la carga otro hook, cargar-memoria.py, porque Claude Code corta
cada hook a 10 000 caracteres y así cada parte tiene su propio espacio.

Idioma: si se sabe (cortex-edge.json {"idioma": "es"} o el recuerdo prefiere-idioma-*.md),
inyecta solo esa sección; si no, ambas.

REQUIERE Python 3. Es fail-silent: si algo falla, no rompe la sesión.
"""
from __future__ import annotations
import os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import comun  # noqa: E402


def construir() -> str:
    base = comun.carpeta_memoria()
    lang = comun.idioma(base)
    postura = comun.texto_nucleo("POSTURA-CRITICA.md", lang)
    protocolo = comun.texto_nucleo("PROTOCOLO-MEMORIA.md", lang)
    if not postura and not protocolo:
        return ""
    cabecera = comun.txt(
        lang,
        "🧭 CORTEX EDGE — NÚCLEO (se carga solo al inicio de cada sesión). Estas directrices "
        "rigen toda la sesión, desde el primer mensaje.",
        "🧭 CORTEX EDGE — CORE (loaded automatically at the start of every session). These "
        "directives apply to the whole session, from the first message.",
    )
    carpeta = comun.txt(lang, "Carpeta de memoria", "Memory folder", sep=" / ") + f": {base}"
    partes = [cabecera, carpeta, postura, protocolo]
    return "\n\n".join(p for p in partes if p)[: comun.LIMITE_CONTEXTO]


def main() -> int:
    try:
        comun.drenar_stdin()
        comun.emitir("SessionStart", construir())
    except Exception:
        pass  # nunca rompas la sesión
    return 0


if __name__ == "__main__":
    sys.exit(main())
