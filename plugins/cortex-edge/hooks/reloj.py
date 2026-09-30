"""
🌱 Cortex Edge · Hook UserPromptSubmit — fecha y hora local en cada turno.

Claude no tiene reloj: sin esto, "hoy", "mañana" o "hace dos semanas" se calculan a
ciegas, y en sesiones largas la fecha del inicio queda vieja. Este hook agrega una sola
línea al contexto de cada mensaje: día de la semana, fecha ISO, hora y zona horaria.

Activo por defecto. Para apagarlo, crea en tu carpeta de memoria el archivo
cortex-edge.json con:   {"reloj": false}

Es fail-silent: si algo falla, no rompe la sesión.
"""
from __future__ import annotations
import os, sys
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import comun  # noqa: E402

# Tablas propias: no dependen del locale del sistema (en Windows suele venir mal).
DIAS_ES = ("lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo")
DIAS_EN = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")


def linea(ahora: datetime, lang: str | None) -> str:
    off = ahora.strftime("%z")
    zona = f"UTC{off[:3]}:{off[3:]}" if off else ""
    fecha = ahora.strftime("%Y-%m-%d")
    hora = ahora.strftime("%H:%M")
    es = f"🕒 Ahora: {DIAS_ES[ahora.weekday()]} {fecha}, {hora} {zona} (hora local)".rstrip()
    en = f"🕒 Now: {DIAS_EN[ahora.weekday()]} {fecha}, {hora} {zona} (local time)".rstrip()
    return comun.txt(lang, es, en, sep=" / ")


def construir() -> str:
    base = comun.carpeta_memoria()
    if comun.leer_config(base).get("reloj", True) is False:
        return ""
    return linea(datetime.now().astimezone(), comun.idioma(base))


def main() -> int:
    try:
        comun.drenar_stdin()
        comun.emitir("UserPromptSubmit", construir())
    except Exception:
        pass  # nunca rompas la sesión
    return 0


if __name__ == "__main__":
    sys.exit(main())
