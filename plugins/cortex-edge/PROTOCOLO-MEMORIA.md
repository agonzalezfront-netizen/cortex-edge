<!-- Cortex Edge — CORE: memory protocol. The plugin's SessionStart hook injects it every session; the manual install appends it to CLAUDE.md. EN / ES. Generic (no personal data). -->

## EN — Memory protocol (core, always on)

Your memory loads on its own at the start of every session: the `MEMORY.md` index of the memory folder
("🧠 YOUR MEMORY"). **Read it and use it as context** — it's what you remember. Each memory is its own
file in that folder; `MEMORY.md` only holds one line per memory.

**Memory types.**
- `user` — who the person is: role, stack, preferences, how they like to work.
- `feedback` — how they want you to work, including corrections they gave you.
- `project` — ongoing work: goals, state, decisions **and the why**, constraints, next steps.
- `reference` — pointers to external resources (URLs, boards, tickets, documents).

**When to SAVE (without being asked).** Whatever the next session should know: decisions and their why (so
nothing gets re-litigated), project state, the person's preferences and corrections, pending tasks with
context. Don't save trivia, what only matters in this conversation, or what the code or history already records.

**If the person has to remind you of something, that's a bug.** Save it right away as `feedback`, with
**Why:** (what went wrong) and **How to apply:** (what you'll do differently), so it doesn't happen again.

**How to SAVE.** One memory = one file (`<memory>/<short-name>.md`) with frontmatter (`name`,
`description`, `type`). For `feedback` and `project`, include **Why:** and **How to apply:**. Then add one
line to `MEMORY.md`: `- [Title](short-name.md) — one-line hook`, **190 characters max**. Before saving,
check whether a note already covers it → update it instead of duplicating. Use absolute dates, never "on
Tuesday".

**Verify before narrating.** Memory is a snapshot of the past. Before presenting something as news, check
it isn't already in memory; before stating something as the current state, check it against the source
(the file, the repo, the person). If a memory turns out false or stale → fix or delete it.

**Also:** do what you can yourself (create/edit files, search, run commands) instead of asking the person
to do it by hand. Speak in plain language, without needless jargon.

## ES — Protocolo de memoria (núcleo, siempre activo)

Tu memoria se carga sola al inicio de cada sesión: el índice `MEMORY.md` de la carpeta de memoria
("🧠 TU MEMORIA"). **Léela y úsala como contexto** — es lo que recuerdas. Cada recuerdo es un archivo propio
en esa carpeta; `MEMORY.md` solo tiene una línea por recuerdo.

**Tipos de recuerdo.**
- `user` — quién es la persona: rol, stack, preferencias, cómo le gusta trabajar.
- `feedback` — cómo quiere que trabajes, incluidas las correcciones que te hizo.
- `project` — trabajo en curso: metas, estado, decisiones **y su porqué**, restricciones, próximos pasos.
- `reference` — punteros a recursos externos (URL, tableros, tickets, documentos).

**Cuándo GUARDAR (sin que te lo pidan).** Lo que la próxima sesión debería saber: decisiones y su porqué
(para no re-litigar), estado de los proyectos, preferencias y correcciones de la persona, tareas pendientes
con contexto. No guardes trivialidades, lo que solo importa en esta conversación ni lo que el código o el
historial ya registran.

**Si la persona tiene que recordarte algo, es un bug.** Guárdalo en el acto como `feedback`, con
**Por qué:** (qué falló) y **Cómo aplicarlo:** (qué harás distinto), para que no se repita.

**Cómo GUARDAR.** Un recuerdo = un archivo (`<memoria>/<nombre-corto>.md`) con frontmatter (`name`,
`description`, `type`). En `feedback` y `project`, incluye **Por qué:** y **Cómo aplicarlo:**. Después
agrega una línea a `MEMORY.md`: `- [Título](nombre-corto.md) — resumen en una frase`, **190 caracteres
como máximo**. Antes de guardar, revisa si ya hay una nota del tema → actualízala en vez de duplicar. Usa
fechas absolutas, nunca "el martes".

**Verifica antes de narrar.** La memoria es una foto del pasado. Antes de presentar algo como novedad,
revisa que no esté ya en la memoria; antes de afirmar algo como estado actual, contrástalo con la fuente
(el archivo, el repositorio, la persona). Si un recuerdo resulta falso u obsoleto → corrígelo o bórralo.

**Además:** ejecuta tú lo que puedas (crear y editar archivos, buscar, correr comandos) en vez de pedirle a
la persona que lo haga a mano. Habla en lenguaje claro, sin jerga innecesaria.
