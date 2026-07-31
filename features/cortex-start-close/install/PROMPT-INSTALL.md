# Install — cortex-start-close / Instalar — cortex-start-close

**EN.** Hi Claude. Install two continuity commands for this user: `/start`+`/close` (EN) and
`/arranca`+`/cierra` (ES). Reply in the user's language.

**ES.** Hola Claude. Instálale a esta persona dos comandos de continuidad: `/start`+`/close` (EN) y
`/arranca`+`/cierra` (ES). Responde en el idioma de la persona.

## Requires / Requiere
Core memory (`cortex-memory`) installed — the handoff lives in the memory folder. If there's no memory
folder with `MEMORY.md`, install memory first / instala memoria primero.

## Steps / Pasos
> ♻️ **Idempotent / Idempotente:** if the commands or the CLAUDE.md note are already there, overwrite the
> files but do **not** add a second copy of the note. Install only what's missing. / Si los comandos o la nota
> del CLAUDE.md ya están, sobrescribe los archivos pero **no** dupliques la nota. Instala solo lo que falte.

1. Create `C:\Users\<USER>\.claude\commands\` if missing / si no existe.
2. Copy the 4 files from `commands/` there: `start.md`, `close.md`, `arranca.md`, `cierra.md`.
3. Confirm the memory folder (with `MEMORY.md`) is reachable — `/close` writes `HANDOFF.md` there and
   `/start` reads it. If you can't find it, ask the user for the path / pregunta la ruta.
4. Add to the end of the user's `CLAUDE.md` / Agrega al final del `CLAUDE.md`:
   ```
   ## Continuity commands / Comandos de continuidad
   - /start (= /arranca): resume where we left off / retomar dónde quedamos.
   - /close (= /cierra): save + write handoff / guardar + dejar handoff.
   ```
5. Test / Prueba: run `/start` — with no handoff yet it should say so and ask what to work on.

## Done / Al terminar
Tell the user, simply: "Now type **/start** when you begin and **/close** when you finish — no session
starts blank." / "Ahora escribe **/arranca** al empezar y **/cierra** al terminar — ninguna sesión arranca
en blanco."
