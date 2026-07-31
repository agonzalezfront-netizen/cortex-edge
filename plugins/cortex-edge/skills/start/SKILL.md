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
4. If there is no `HANDOFF.md` yet, say so in one line and ask what they want to work on today.

Don't invent state: if the handoff doesn't mention something, don't assume it. Memory (`MEMORY.md`) already
loaded at startup — this command adds the "where we left off" from the last close. (Español: `/arranca`.)
