"""
🌱 Cortex Edge · Hook SessionStart — carga tu memoria al inicio de cada sesión.

Qué hace: lee tu índice de memoria (MEMORY.md) y lo inyecta en el contexto de Claude
al empezar CADA conversación. Esto es lo que hace que Claude "recuerde" lo de antes.
(La postura crítica y el protocolo de memoria los carga cargar-nucleo.py.)

CERO CONFIGURACIÓN: si no defines nada, usa ~/.claude/cortex-memory/ y la crea sola
la primera vez, con un MEMORY.md semilla. Si prefieres guardar la memoria en tu
Obsidian (o donde quieras), define la variable de entorno CORTEX_MEMORY_PATH con esa
ruta y el hook la usará en su lugar.

CONTROL DE TAMAÑO: Claude Code corta el contexto de cada hook a 10 000 caracteres, y
desde adentro un índice truncado no se nota (lo que quedó fuera simplemente no existe
para el modelo). Por eso este hook:
  - avisa en el contexto cuando el índice pasa de UMBRAL_AVISO caracteres (consolida),
  - avisa si hay líneas de más de 190 caracteres,
  - y si aun así no cabe, corta por líneas completas y lo DICE, en vez de dejar que
    Claude Code lo corte en silencio.

REQUIERE Python 3 en el PATH. Si no lo tienes, la memoria no se carga — el resto del
plugin sigue funcionando igual. Es fail-silent: si algo falla, NO rompe la sesión.
"""
from __future__ import annotations
import os, sys
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import comun  # noqa: E402

# ~80 % del espacio de un hook: a partir de aquí conviene consolidar antes de que se corte.
UMBRAL_AVISO = 8000
MAX_LINEA = 190

SEMILLA = """# MEMORY.md — índice de tu memoria / your memory index

Una línea por recuerdo; cada recuerdo vive en su propio archivo dentro de esta carpeta.
One line per memory; each memory lives in its own file in this folder.

<!-- Formato / Format: - [Título](archivo.md) — de qué se trata (máx. 190 caracteres) -->
"""


def asegurar_carpeta(d: Path) -> None:
    """Crea la carpeta y el índice semilla la primera vez. Silencioso si falla."""
    try:
        d.mkdir(parents=True, exist_ok=True)
        idx = d / "MEMORY.md"
        if not idx.exists():
            idx.write_text(SEMILLA, encoding="utf-8")
    except Exception:
        pass


def avisos(contenido: str, lang: str | None) -> list[str]:
    out = []
    if len(contenido) > UMBRAL_AVISO:
        out.append(comun.txt(
            lang,
            f"⚠️ El índice (MEMORY.md, {len(contenido)} caracteres) se acerca al límite de lo que "
            f"se carga al inicio (~{comun.LIMITE_CONTEXTO}). Consolida: fusiona recuerdos "
            "relacionados, acorta líneas y quita lo obsoleto. Díselo a la persona en esta sesión.",
            f"⚠️ The index (MEMORY.md, {len(contenido)} characters) is approaching the limit of what "
            f"loads at startup (~{comun.LIMITE_CONTEXTO}). Consolidate: merge related memories, "
            "shorten lines and drop what's stale. Tell the person during this session.",
        ))
    largas = sum(1 for l in contenido.splitlines() if len(l) > MAX_LINEA)
    if largas:
        out.append(comun.txt(
            lang,
            f"⚠️ {largas} línea(s) del índice superan {MAX_LINEA} caracteres: acórtalas (el detalle "
            "va en el archivo del recuerdo, no en el índice).",
            f"⚠️ {largas} index line(s) exceed {MAX_LINEA} characters: shorten them (details belong "
            "in the memory file, not in the index).",
        ))
    return out


def recortar(contenido: str, espacio: int, lang: str | None) -> str:
    """Si no cabe, corta por líneas completas y agrega una nota explícita."""
    if len(contenido) <= espacio:
        return contenido
    lineas = contenido.splitlines()
    nota_max = 400
    guardadas, usado = [], 0
    for l in lineas:
        if usado + len(l) + 1 > espacio - nota_max:
            break
        guardadas.append(l)
        usado += len(l) + 1
    faltan = len(lineas) - len(guardadas)
    nota = comun.txt(
        lang,
        f"⚠️ ÍNDICE TRUNCADO: {faltan} de {len(lineas)} líneas NO se cargaron y no están en tu "
        "contexto. Lee MEMORY.md completo si lo necesitas, y consolida el índice hoy.",
        f"⚠️ INDEX TRUNCATED: {faltan} of {len(lineas)} lines did NOT load and are not in your "
        "context. Read the full MEMORY.md if you need it, and consolidate the index today.",
    )
    return "\n".join(guardadas) + "\n\n" + nota


def construir() -> str:
    base = comun.carpeta_memoria()
    asegurar_carpeta(base)
    index = base / "MEMORY.md"
    try:
        contenido = index.read_text(encoding="utf-8").strip()
    except Exception:
        return ""  # todavía no hay memoria: silencioso
    if not contenido:
        return ""
    lang = comun.idioma(base)
    cabecera = comun.txt(
        lang,
        "🧠 TU MEMORIA (cargada automáticamente al inicio). Esto es lo que recuerdas de "
        "conversaciones anteriores — úsalo como contexto. Cuando surja algo nuevo e importante, "
        "GUÁRDALO siguiendo el protocolo de memoria.",
        "🧠 YOUR MEMORY (loaded automatically at startup). This is what you remember from "
        "previous conversations — use it as context. When something new and important comes up, "
        "SAVE it following the memory protocol.",
    ) + f"\n{comun.txt(lang, 'Índice', 'Index', sep=' / ')}: {index}"
    previo = "\n\n".join([cabecera] + avisos(contenido, lang)) + "\n\n"
    return previo + recortar(contenido, comun.LIMITE_CONTEXTO - len(previo), lang)


def main() -> int:
    try:
        comun.drenar_stdin()
        comun.emitir("SessionStart", construir())
    except Exception:
        pass  # nunca rompas la sesión
    return 0


if __name__ == "__main__":
    sys.exit(main())
