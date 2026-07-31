<!-- Memory protocol — appended to the user's CLAUDE.md by the installer. EN / ES. Generic (no personal data). -->

## EN — Your memory (how it works)

Your memory loads on its own at the start of every session (a hook injects the `MEMORY.md` index). You'll
see it as "🧠 YOUR MEMORY". **Read it** and use it as context — it's what you remember.

**When to SAVE (without being asked).** Save whatever the next session should know:
- **Decisions and the WHY** — so nothing already decided gets re-litigated.
- **Project state** — what exists, what's in progress, what's missing.
- **Feedback** — from users/customers: what they ask for, like, dislike.
- **Tasks and next steps** — with context.
- **The person's preferences** — how they like to work, corrections they made.

Don't save trivia or what's already in the code.

**How to SAVE.** Write a new file in the memory folder (`<memory>/<short-name>.md`) with frontmatter
(`name`, `description`, `type`), then add one line to `MEMORY.md`: `- [Title](short-name.md) — one-line hook`.
Before saving, check if a note already covers it → update it instead of duplicating. If something you saved
turns out false → fix or delete it.

**Also:** execute what you can yourself (create/edit files, search, run commands) instead of asking the
person to do it by hand. Speak in plain language, not needless jargon.

## ES — Tu memoria (cómo funciona)

Tu memoria se carga sola al inicio de cada sesión (un hook inyecta el índice `MEMORY.md`). La verás como
"🧠 TU MEMORIA". **Léela** y úsala como contexto — es lo que recuerdas.

**Cuándo GUARDAR (sin que te lo pidan).** Guarda lo que la próxima sesión debería saber:
- **Decisiones y el PORQUÉ** — para no re-litigar lo ya decidido.
- **Estado del proyecto** — qué existe, qué está en progreso, qué falta.
- **Feedback** — de usuarios/clientes: qué piden, qué les gusta, qué les molesta.
- **Tareas y próximos pasos** — con contexto.
- **Preferencias de la persona** — cómo le gusta trabajar, correcciones que hizo.

No guardes trivialidades ni lo que ya está en el código.

**Cómo GUARDAR.** Escribe un archivo nuevo en la carpeta de memoria (`<memoria>/<nombre-corto>.md`) con
frontmatter (`name`, `description`, `type`), y agrega una línea a `MEMORY.md`:
`- [Título](nombre-corto.md) — resumen en una frase`. Antes de guardar, revisa si ya hay una nota del tema →
actualízala en vez de duplicar. Si algo que guardaste resultó falso → corrígelo o bórralo.

**Además:** ejecuta tú lo que puedas (crear/editar archivos, buscar, correr comandos) en vez de pedirle a la
persona que lo haga a mano. Habla en lenguaje claro, sin jerga innecesaria.
