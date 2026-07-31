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
4. **If there is no `HANDOFF.md` yet** (first run, or the session was never closed with
   `/cortex-edge:close`), don't leave them hanging. Explain in two lines what will happen from now
   on and offer to start: *"No previous session to pick up yet. When we're done, run
   `/cortex-edge:close` and I'll leave the summary — next time I'll resume from there. What are we
   working on today?"*

Don't invent state: if the handoff doesn't mention something, don't assume it. Memory (`MEMORY.md`) already
loaded at startup — this command adds the "where we left off" from the last close. (Español: `/arranca`.)

## Principio de UX

**El contexto va donde está la decisión.** Si necesitas preguntarle algo a la persona, dale primero
lo que necesita para poder responder — ejemplos concretos, no una pregunta abierta al vacío. Y al
terminar, dile **qué cambió y cuál es el siguiente paso**, no solo que terminaste.
