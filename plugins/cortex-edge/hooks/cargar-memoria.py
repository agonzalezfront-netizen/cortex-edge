"""
🌱 Cortex Edge · Hook SessionStart — carga tu memoria al inicio de cada sesión.

Qué hace: lee tu índice de memoria (MEMORY.md) y lo inyecta en el contexto de Claude
al empezar CADA conversación. Esto es lo que hace que Claude "recuerde" lo de antes.

CERO CONFIGURACIÓN: si no defines nada, usa ~/.claude/cortex-memory/ y la crea sola
la primera vez, con un MEMORY.md semilla. Si prefieres guardar la memoria en tu
Obsidian (o donde quieras), define la variable de entorno CORTEX_MEMORY_PATH con esa
ruta y el hook la usará en su lugar.

REQUIERE Python 3 en el PATH (este archivo es un script de Python). Si no lo tienes,
la memoria no se carga — el resto del plugin sigue funcionando igual.

Es fail-silent: si algo falla, NO rompe la sesión (simplemente no carga memoria).
"""
from __future__ import annotations
import json, os, sys
from pathlib import Path

# Ruta de la memoria: la variable de entorno manda; si no, un default que siempre existe.
MEMORY_DIR = os.environ.get(
    "CORTEX_MEMORY_PATH",
    str(Path.home() / ".claude" / "cortex-memory"),
)

SEMILLA = """# MEMORY.md — índice de tu memoria

Una línea por recuerdo. Cada recuerdo vive en su propio archivo dentro de esta carpeta.

<!-- Formato: - [Título](archivo.md) — de qué se trata en pocas palabras -->
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


def main() -> int:
    try:
        # Drenar stdin (el hook recibe un JSON que no necesitamos).
        try:
            sys.stdin.read()
        except Exception:
            pass

        base = Path(MEMORY_DIR)
        asegurar_carpeta(base)
        index = base / "MEMORY.md"
        if not index.exists():
            return 0  # todavía no hay memoria: silencioso

        try:
            content = index.read_text(encoding="utf-8").strip()
        except Exception:
            return 0
        if not content:
            return 0

        header = (
            "🧠 TU MEMORIA (cargada automáticamente al inicio). Esto es lo que "
            "recuerdas de conversaciones anteriores — úsalo como contexto. Cuando "
            "surja algo nuevo e importante, GUÁRDALO siguiendo el protocolo de tu "
            "CLAUDE.md.\n\n"
        )

        hook_response = {
            "hookSpecificOutput": {
                "hookEventName": "SessionStart",
                "additionalContext": header + content,
            }
        }
        # ensure_ascii=True: en Windows evita que se corrompan tildes/ñ/em-dash.
        sys.stdout.write(json.dumps(hook_response, ensure_ascii=True))
        sys.stdout.flush()
        return 0
    except Exception:
        return 0  # nunca rompas la sesión


if __name__ == "__main__":
    sys.exit(main())
