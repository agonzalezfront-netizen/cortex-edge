---
description: Resume the session — load where you left off last time
---

You are starting a work session. Help the user pick up without re-reading everything:

1. Find the user's memory folder (the same one the SessionStart hook loads, where `MEMORY.md` lives; the
   path is in the CLAUDE.md).
2. Look for `HANDOFF.md` there. If it exists, read it in full.
3. Summarize in plain language:
   - **Where we left off:** the current state from the last session.
   - **Pending:** what's left, with context.
   - **Suggested next step:** where to continue today.
4. **PRIMERA VEZ — visita guiada.** Si no hay `HANDOFF.md` **y** la memoria tiene pocos recuerdos
   (solo el del idioma, o ninguno), esta persona acaba de instalar Cortex Edge. **No le preguntes
   "¿en qué trabajamos?" y ya** — todavía no sabe qué tiene entre manos. Hazle el recorrido:

   **a) Demuestra primero, explica después.** Abre confirmando que la memoria funcionó:

   > 🌱 **Bienvenido de vuelta.** Antes de nada, fíjate en esto: **recordé que prefieres el
   > español** sin que me lo dijeras. Eso es la memoria, y ya está andando.

   **b) Muéstrale lo que tiene, con ejemplos reales y diciendo cuándo lo usaría.** Cuatro como
   máximo, en lenguaje simple:

   > **Lo que puedes hacer desde ahora:**
   >
   > • **Que recuerde cosas** — dime *"recuerda que prefiero explicaciones antes del código"* y lo
   >   voy a saber siempre. También con `/cortex-edge:memoria`.
   > • **Cerrar el día sin perder el hilo** — `/cortex-edge:close` guarda dónde quedamos; mañana
   >   `/cortex-edge:start` lo retoma. Es lo que acabas de usar.
   > • **Que te lleve la contra** — si veo un problema en tu plan te lo digo, no te doy la razón
   >   por defecto. No tienes que pedirlo.
   > • **Revisar que todo esté bien** — `/cortex-edge:setup`, por si algún día algo falla.

   **c) Recién ahora, el catálogo.** Ya entendió lo que tiene; ahora sí tiene sentido ofrecer más:

   > **¿Le sumamos capacidades?** Hay un catálogo de skills — depuración rigurosa, redactar
   > documentos, investigación, diseño, video. Los uso solo cuando la tarea lo pide.
   >
   > **1.** Muéstrame el catálogo
   > **2.** Después — empecemos a trabajar 🌱

   Si elige **2**, cierra preguntándole en qué quiere trabajar hoy. Si elige **1**, sigue con
   `/cortex-edge:skills`. **Nunca insistas.**

5. **Si no hay `HANDOFF.md` pero la memoria ya tiene historia** (no es primera vez, simplemente
   nunca cerró con `/cortex-edge:close`): dilo en una línea, recuérdale que `cierra` deja el
   resumen para la próxima, y pregúntale en qué trabaja hoy. Sin recorrido — ya lo conoce.

Don't invent state: if the handoff doesn't mention something, don't assume it. Memory (`MEMORY.md`) already
loaded at startup — this command adds the "where we left off" from the last close. (Español: `/arranca`.)

## Principio de UX

**Ubicación y rumbo, siempre.** Cada mensaje abre diciendo en qué parte del recorrido está la
persona y cierra diciendo qué sigue. Si llega desde `/cortex-edge:setup`, viene del paso 4 — no la
dejes sin saber dónde está parada.

**El contexto va donde está la decisión.** Si preguntas algo, primero da lo necesario para poder
responder — ejemplos concretos, no una pregunta abierta al vacío. Al terminar, di **qué cambió y
cuál es el siguiente paso**, no solo que terminaste.

**Si la mandas a una pantalla que no es tuya** (el explorador de plugins de Claude Code, la web de
un skill), **avísale antes**: qué va a ver, que eso no es Cortex Edge, y qué tiene que hacer ahí.
