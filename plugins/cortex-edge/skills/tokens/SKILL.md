---
description: 'Measure where Claude Code tokens go — by day, model, what triggered each turn (the person, automatic wake-ups, startup, subagents) and session, with the context re-read on every message. Use when the person asks "where are my tokens going", "por qué se me acaba el cupo", "cuánto contexto llevo", "tokens", or before deciding to switch models or change how they work.'
---

# Tokens — dónde se van / where they go

Mide el consumo desde los transcripts locales de Claude Code, no desde la sensación.
Measures usage from Claude Code's local transcripts, not from the feeling.

## Cómo correrlo / How to run it

El script está junto a este archivo (`tokens.py`, en la carpeta base de esta skill, que aparece
arriba como *Base directory for this skill*). Solo usa la biblioteca estándar de Python:
The script sits next to this file (`tokens.py`, in this skill's base directory, shown above as
*Base directory for this skill*). Python standard library only:

```bash
python "<base directory>/tokens.py" --idioma es      # o --idioma en, según la persona
```

Opciones / options: `--dias 14` (ventana / window, por defecto 7) · `--tope 300000` (tope de contexto /
context ceiling, por defecto 500000) · `--json` · `--verificar` (sale con 1 si una sesión viva pasa el
tope / exits 1 if a live session is over the ceiling) · `--raiz <carpeta>` (si los transcripts no están
en `~/.claude/projects`).

**Privacidad / Privacy:** solo lee archivos locales e imprime números. Nunca muestra el contenido de
los mensajes ni envía nada. / It only reads local files and prints numbers; it never shows message
contents and never sends anything.

## Cómo leerlo y qué decirle a la persona / How to read it

No le pegues la tabla entera: dale el **veredicto** en tres o cuatro líneas, en lenguaje simple, y
ofrece el detalle si lo quiere. / Don't paste the whole table: give the **verdict** in three or four
plain lines and offer the detail.

- **Salida < 1 % del volumen** → el gasto no es razonamiento: es releer un contexto grande en cada
  mensaje. La palanca es **contexto más chico** y **menos despertares**, no un modelo más barato (una
  llamada de un modelo chico con 800 mil de contexto cuesta más que una de un modelo grande con 20 mil).
  / **Output under 1 %** → the spend isn't reasoning, it's re-reading a big context on every message.
  The lever is a **smaller context** and **fewer wake-ups**, not a cheaper model.
- **Mucho "automático"** → notificaciones o tareas programadas despiertan al modelo con todo su
  contexto cargado para decir "nada nuevo". Un vigilante determinista (un script que solo avisa ante un
  hecho nuevo) lo reemplaza. / **Lots of "automatic"** → notifications or scheduled prompts wake the
  model, with its whole context loaded, to say "nothing new". A deterministic watcher replaces that.
- **Una sesión con contexto mediano alto** → ahí está el costo; ver el tope de abajo. / **One session
  with a high median context** → that's where the cost is; see the ceiling below.

## Tope de contexto / Context ceiling

Cada mensaje relee todo el contexto de la sesión. Regla: **cuando una sesión viva pasa de 500 mil
tokens de contexto, no se corta la tarea en curso; en el siguiente cierre natural se cierra con
`/cortex-edge:cierra` (handoff con el estado vigente) y se sigue en una sesión nueva. Nunca esperar la
compactación automática** (resume a ciegas lo que tú elegirías conscientemente en un handoff). El
hook vigía de Cortex Edge avisa solo cuando se cruza el tope; este informe lo muestra como `AVISO`.
Si la ventana del modelo es de 200 mil, baja el tope (`{"tope_contexto": 150000}` en `cortex-edge.json`).

Every message re-reads the whole session context. Rule: **when a live session passes 500k tokens of
context, don't cut the current task short; at the next natural stopping point, close with
`/cortex-edge:close` (handoff with the current state) and continue in a fresh session. Never wait for
automatic compaction.** The Cortex Edge watcher hook warns on its own when the ceiling is crossed; this
report shows it as `WARNING`. With a 200k context window, lower the ceiling.

## Límites honestos / Honest limits

- Mide **tokens**, no dinero ni el cupo de tu plan: el "ponderado" usa precios relativos (entrada 1 ·
  escritura de caché 1,25 · lectura 0,1 · salida 5) para comparar, no para facturar.
- El disparador se infiere del último mensaje antes de cada llamada; si Claude Code cambia el formato
  de sus transcripts, algún turno puede caer en "la persona".
- It measures **tokens**, not money or your plan's quota; triggers are inferred from the last message
  before each call.
