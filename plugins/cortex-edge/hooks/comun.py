"""
Cortex Edge · piezas compartidas por los hooks (núcleo, memoria y reloj).

Todo es fail-silent: ante cualquier error se devuelve un valor neutro. Un hook de
Cortex Edge nunca debe romper la sesión de Claude Code.
"""
from __future__ import annotations
import json, os, re, sys
from pathlib import Path

# Raíz del plugin: la carpeta que contiene hooks/. Los textos del núcleo viven ahí
# (POSTURA-CRITICA.md, PROTOCOLO-MEMORIA.md): los hooks los LEEN, no los copian.
RAIZ_PLUGIN = Path(__file__).resolve().parent.parent

# Claude Code corta el additionalContext de un hook a 10 000 caracteres: lo que sobra
# se guarda en un archivo y al modelo solo le llega una vista previa de 2 000. Por eso
# cada hook se mantiene por debajo, con margen (los emoji cuentan doble en UTF-16).
LIMITE_CONTEXTO = 9500

CONFIG = "cortex-edge.json"


def carpeta_memoria() -> Path:
    """$CORTEX_MEMORY_PATH si está definida; si no, ~/.claude/cortex-memory/."""
    return Path(os.environ.get("CORTEX_MEMORY_PATH")
                or str(Path.home() / ".claude" / "cortex-memory"))


def leer_config(base: Path | None = None) -> dict:
    """Lee <memoria>/cortex-edge.json. Si no existe o está mal escrito: {} (valores por defecto)."""
    try:
        datos = json.loads((base or carpeta_memoria()).joinpath(CONFIG).read_text(encoding="utf-8"))
        return datos if isinstance(datos, dict) else {}
    except Exception:
        return {}


def idioma(base: Path | None = None) -> str | None:
    """'es', 'en' o None (desconocido → se usan ambos idiomas).

    Fuentes, en orden: la clave "idioma" de cortex-edge.json, y el recuerdo que deja
    /cortex-edge:setup (prefiere-idioma-es.md / prefiere-idioma-en.md)."""
    base = base or carpeta_memoria()
    valor = str(leer_config(base).get("idioma", "")).lower()
    if valor in ("es", "en"):
        return valor
    try:
        if (base / "prefiere-idioma-es.md").exists():
            return "es"
        if (base / "prefiere-idioma-en.md").exists():
            return "en"
    except Exception:
        pass
    return None


def limpiar_md(texto: str) -> str:
    """Quita el frontmatter YAML y los comentarios HTML: al modelo solo le sirve el cuerpo."""
    texto = texto.replace("\r\n", "\n")
    texto = re.sub(r"\A---\n.*?\n---\n", "", texto, flags=re.S)
    texto = re.sub(r"<!--.*?-->\n?", "", texto, flags=re.S)
    return texto.strip()


def seccion(texto: str, lang: str | None) -> str:
    """De un archivo bilingüe (## EN — … / ## ES — …) devuelve la sección del idioma.
    Sin idioma, o si el archivo no tiene esa sección, devuelve el texto completo."""
    if lang not in ("es", "en"):
        return texto
    partes = re.split(r"(?m)^(?=## (?:EN|ES)\b)", texto)
    for p in partes:
        if p.startswith(f"## {lang.upper()}"):
            return p.strip()
    return texto


def texto_nucleo(nombre: str, lang: str | None) -> str:
    """Lee un archivo del núcleo desde la raíz del plugin. '' si no está."""
    try:
        return seccion(limpiar_md((RAIZ_PLUGIN / nombre).read_text(encoding="utf-8")), lang)
    except Exception:
        return ""


def txt(lang: str | None, es: str, en: str, sep: str = "\n") -> str:
    """El texto en el idioma de la persona; si no se sabe, ambos."""
    if lang == "es":
        return es
    if lang == "en":
        return en
    return f"{en}{sep}{es}"


def drenar_stdin() -> None:
    """Claude Code manda un JSON por stdin que estos hooks no necesitan."""
    try:
        sys.stdin.read()
    except Exception:
        pass


def emitir(evento: str, contexto: str) -> None:
    """Escribe la respuesta en el formato de Claude Code (hookSpecificOutput.additionalContext)."""
    if not contexto:
        return
    respuesta = {"hookSpecificOutput": {"hookEventName": evento, "additionalContext": contexto}}
    # ensure_ascii=True: en Windows evita que se corrompan tildes, ñ y emoji en la consola.
    sys.stdout.write(json.dumps(respuesta, ensure_ascii=True))
    sys.stdout.flush()
