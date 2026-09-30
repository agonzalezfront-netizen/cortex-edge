---
description: Close the session — save what matters and leave a handoff for next time
---

You are closing the work session. Do this before finishing:

**1. Save to memory what the next session should know.** Review what happened (decisions, progress,
changes) and save it following the memory protocol loaded at startup: decisions **and the why**,
project state, feedback and corrections from the person, pending tasks, preferences. Update existing
notes instead of duplicating. Don't save trivia or what's already in the code. If the person had to
remind you of something during the session, save it as `feedback` with **Why:** and **How to apply:**.

**2. Write or update `HANDOFF.md`** in the memory folder (next to `MEMORY.md`):

```markdown
# HANDOFF — <today's date>

## Where we left off
<what we were working on and why — the real current state at close>

## Pending
- <what's left, with enough context to resume it>

## Next step
<the first concrete action for the next session>
```

Overwrite the previous handoff (it always reflects the most recent state).

**3. Confirm to the user** in one line: what you saved to memory and that the handoff is ready.
(Spanish: `/cortex-edge:cierra`.)

## UX principles

**Location and direction, always.** Every message opens by saying where the person is in the flow
and closes by saying what comes next. If they arrive from `/cortex-edge:setup`, they're coming from
step 4 — don't leave them unsure where they stand.

**Context goes where the decision is.** If you ask something, first give what they need to answer —
concrete examples, not an open question into the void. When you finish, say **what changed and
what the next step is**, not just that you're done.

**If you send them to a screen that isn't yours** (Claude Code's plugin browser, a skill's website),
**warn them first**: what they'll see, that it isn't Cortex Edge, and what they need to do there.
