---
description: Retoma la sesión — carga dónde quedaste la última vez
---

Estás iniciando una sesión de trabajo con el usuario. Ayúdale a retomar sin releer todo:

1. Ubica la carpeta de memoria del usuario (la misma que carga el hook al inicio, donde está `MEMORY.md`;
   la ruta figura en el CLAUDE.md).
2. Busca ahí un archivo `HANDOFF.md`. Si existe, léelo completo.
3. Resume al usuario en lenguaje claro (sin jerga):
   - **Dónde quedamos:** el estado vigente de la última sesión.
   - **Pendientes:** lo que quedó por hacer, con su contexto.
   - **Próximo paso sugerido:** por dónde conviene seguir hoy.
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
   > • **Cerrar el día sin perder el hilo** — `/cortex-edge:cierra` guarda dónde quedamos; mañana
   >   `/cortex-edge:arranca` lo retoma. Es lo que acabas de usar.
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
   nunca cerró con `/cortex-edge:cierra`): dilo en una línea, recuérdale que `cierra` deja el
   resumen para la próxima, y pregúntale en qué trabaja hoy. Sin recorrido — ya lo conoce.

No inventes estado: si el HANDOFF no menciona algo, no lo asumas. La memoria (MEMORY.md) ya se cargó
sola al inicio — este comando la complementa con el "dónde quedamos" del último cierre.

## Principio de UX

**Ubicación y rumbo, siempre.** Cada mensaje abre diciendo en qué parte del recorrido está la
persona y cierra diciendo qué sigue. Si llega desde `/cortex-edge:setup`, viene del paso 4 — no la
dejes sin saber dónde está parada.

**El contexto va donde está la decisión.** Si preguntas algo, primero da lo necesario para poder
responder — ejemplos concretos, no una pregunta abierta al vacío. Al terminar, di **qué cambió y
cuál es el siguiente paso**, no solo que terminaste.

**Si la mandas a una pantalla que no es tuya** (el explorador de plugins de Claude Code, la web de
un skill), **avísale antes**: qué va a ver, que eso no es Cortex Edge, y qué tiene que hacer ahí.
