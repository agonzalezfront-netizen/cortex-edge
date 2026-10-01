---
description: Close the session — save what matters, stop what was left running and leave a handoff with the current state
---
<!-- Generated from the plugin (plugins/cortex-edge/skills/close/SKILL.md); do not edit by hand. / Generado desde el plugin (plugins/cortex-edge/skills/close/SKILL.md); no editar a mano. -->

You are closing the work session. Do this before finishing:

**1. Save to memory what the next session should know.** Review what happened (decisions, progress,
changes) and save it following the memory protocol loaded at startup: decisions **and the why**,
project state, feedback and corrections from the person, pending tasks, preferences. Update existing
notes instead of duplicating. Don't save trivia or what's already in the code.

**2. Every lesson becomes `feedback`.** If the person had to remind or correct you during the session,
or a mistake of yours cost a round trip, save it as `feedback` with **Why:** (what went wrong) and
**How to apply:** (what you'll do differently). If it can happen again, also note which **guard** would
prevent it without relying on memory (a test, a check in a script) and offer it.

**3. Stop what this session left running.** Background processes, monitors, scheduled or looping
tasks, dev servers, file watchers: if **you started them in this session** and they're no longer
needed, stop them. Each one still alive can wake the model up and spend tokens after the session is
closed. **Don't touch** what existed before the session or system services. If something must stay
running on purpose, say so in the handoff, with the why.

**4. Write or update `HANDOFF.md`** in the memory folder (next to `MEMORY.md`). Open it with the
**current state** block: it's the first thing the next session will read.

```markdown
# HANDOFF — <today's date and time>

## Current state at close
- **What:** <what we were working on, in one or two sentences>
- **Why:** <what for; the decision or goal behind it>
- **Where:** <files, folder, branch, URL: enough to find it without searching>
- **What's left:** <what remains to call it done>
- **First step:** <the first concrete action for the next session>

## Verified and not verified
- ✅ <what was checked, and with what: test, command, file>
- ⚠️ <what was NOT checked, and why>

## Pending
- <what's left, with enough context to resume it>

## Left running (if any)
- <process or task still alive on purpose, and why>
```

Overwrite the previous handoff (it always reflects the most recent state). **Honesty:** nothing goes
under ✅ without evidence; what you didn't verify goes under ⚠️, even if you believe it works.

**5. If the session is already big, this close is the hand-over.** If the 📏 context-ceiling warning
showed up (or the session has run for many hours and turns), say so: the next task is better started
in a **fresh session** with `/start`, which reads this handoff. Don't wait for automatic
compaction: it summarizes blindly what this handoff chooses with judgment.

**6. Confirm to the user** in a few lines: what you saved to memory, what you stopped, what remains
unverified, and that the handoff is ready. (Spanish: `/cierra`.)

## UX principles

**Location and direction, always.** Every message opens by saying where the person is in the flow
and closes by saying what comes next. If they arrive from `/setup`, they're coming from
step 4 — don't leave them unsure where they stand.

**Context goes where the decision is.** If you ask something, first give what they need to answer —
concrete examples, not an open question into the void. When you finish, say **what changed and
what the next step is**, not just that you're done.

**If you send them to a screen that isn't yours** (Claude Code's plugin browser, a skill's website),
**warn them first**: what they'll see, that it isn't Cortex Edge, and what they need to do there.
