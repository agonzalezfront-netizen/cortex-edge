# 🌱 Cortex Edge

> 🇪🇸 **[Léelo en español → README.es.md](README.es.md)**

**Modular toolkit that turns Claude Code into a refined "second brain" — one optional feature at a time.**

Start with memory. Add capabilities as you need them. Every feature is self-contained, explains what it
does, and declares what it depends on. Nothing is forced; you install only what helps your work.

---

## Core (always, not optional)

Every Cortex Edge install ships a **core** that does not depend on any feature:

- **Memory** (`cortex-memory`) — persistent memory between sessions. This is what makes Claude
  "remember" what came before instead of starting from zero every time.
- **Critical stance** (`core/POSTURA-CRITICA.md`) — Cortex is a rigorous partner, not a yes-man: it
  questions ideas, flags gaps and proposes better alternatives. This applies to every idea, plan or
  decision — it is not tied to any feature.

## Catalog (optional features)

| Feature | What it does | Depends on | Status |
|---|---|---|---|
| `cortex-start-close` | `/start` and `/close` — pick up where you left off, and close leaving a handoff | core (memory) | ✅ ready |
| `cortex-skills` | discover and install skills from a curated catalog | core | ✅ ready |

## Install — two commands ⚡

Inside Claude Code, run:

```
/plugin marketplace add agonzalezfront-netizen/cortex-edge
/plugin install cortex-edge@cortex-edge
```

That's it. Nothing to download, nothing to unzip, no paths to edit, no prompt to explain.
The memory hook installs itself and creates its folder on first run.

Then use it:

| Command | What it does |
|---|---|
| `/cortex-edge:start` · `/cortex-edge:arranca` | Pick up where you left off last session |
| `/cortex-edge:close` · `/cortex-edge:cierra` | Close the session saving memory + a handoff |
| `/cortex-edge:memoria` | Save something to persistent memory |
| `/cortex-edge:skills` | Browse the catalog and install the skills that fit your work |

**Where your memory lives:** `~/.claude/cortex-memory/` by default — created automatically.
Prefer it inside your Obsidian vault (or anywhere else)? Set the `CORTEX_MEMORY_PATH`
environment variable to that path and the hook will use it instead.

<details>
<summary>Manual install (no plugin system)</summary>

Prefer to install by hand, or want just one piece? Download a zip and let your Claude install it:

1. **Core only** → [`dist/cortex-edge-core.zip`](dist/cortex-edge-core.zip) — memory + critical stance.
2. **A single feature** → [`dist/cortex-start-close.zip`](dist/cortex-start-close.zip),
   [`dist/cortex-skills.zip`](dist/cortex-skills.zip) — each **requires the core**.
3. **Full** → [`dist/cortex-edge-full.zip`](dist/cortex-edge-full.zip).

Unzip it, open Claude Code inside the folder, and say *"run the install prompt inside"*.
</details>

---

## Feature model

Each feature is a folder under `features/` with the same shape:

```
features/<feature-name>/
  FEATURE.md          → info card: what it is, what it's for, how it helps, dependencies
  install/
    PROMPT-INSTALL.md → the prompt your Claude runs to self-install it
    ...               → the files the feature ships (commands, hooks, etc.)
```

## Transparency of dependencies

A feature's `FEATURE.md` **must** state its dependencies up front, in plain language:

- **Requires another feature** — e.g. *"needs `cortex-memory` installed first"*.
- **Requires an external account/MCP** — e.g. *"needs a connected Notion account"*.
- **Requires nothing** — say so.

It always explains **what it is**, **what it's for**, **how it helps** and **how it improves your
workflow**.

## Languages

Every user-facing text ships in **English and Spanish**. Commands ship language aliases where it helps
(e.g. `/start` = `/arranca`, `/close` = `/cierra`).

---

*🌱 Cortex Edge grows one refined feature at a time.*
