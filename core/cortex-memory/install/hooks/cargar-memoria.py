"""
🌱 Cortex Edge · Hook SessionStart — carga la memoria del usuario al inicio de cada sesión.

Qué hace: lee tu índice de memoria (MEMORY.md) y lo inyecta en el contexto de Claude
al empezar CADA conversación. Esto es lo que hace que Claude "recuerde" lo de antes.

Es fail-silent: si algo falla, NO rompe la sesión (simplemente no carga memoria).

── CÓMO CONFIGURAR ──
Editá la línea MEMORY_DIR de abajo con la ruta REAL de tu carpeta de memoria
(dentro de tu Obsidian). O definí la variable de entorno CORTEX_MEMORY_PATH.
"""
from __future__ import annotations
import json, os, sys
from pathlib import Path

# ═══════════════════════════════════════════════════════════════════
# CONFIGURÁ ESTO — ruta a tu carpeta de memoria (dentro de tu Obsidian):
MEMORY_DIR = os.environ.get(
    "CORTEX_MEMORY_PATH",
    r"C:\Users\TU_USUARIO\Obsidian\TU_VAULT\memoria",
)
# ═══════════════════════════════════════════════════════════════════


def main() -> int:
    try:
        # Drenar stdin (el hook recibe un JSON que no necesitamos).
        try:
            sys.stdin.read()
        except Exception:
            pass

        index = Path(MEMORY_DIR) / "MEMORY.md"
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
