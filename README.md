# 🌱 Cortex Edge

> 🇪🇸 **[Léelo en español → README.es.md](README.es.md)**

**A collaborator that remembers you, challenges you, and picks up where you left off.**

Not a note repository, not a reminders assistant: it's what comes out of putting memory, judgment and
continuity on top of the tool you already use. Start with memory and add capabilities as you need them —
every feature explains what it does and what it depends on. Nothing is forced.

---

## Install

There are **two ways**, and it's worth knowing which one fits you before you start:

| | How | Best for |
|---|---|---|
| ⚡ **As a plugin** *(recommended)* | Two commands inside Claude Code | Almost everyone |
| 📦 **Manually from this repo** | Download a zip and your Claude installs it | If you want just one piece, or prefer to review every file first |

### ⚡ As a plugin

Inside Claude Code, run:

```
/plugin marketplace add agonzalezfront-netizen/cortex-edge
/plugin install cortex-edge@cortex-edge
```

Nothing to download, no paths to edit, no prompt to explain. The memory hook installs itself and
creates its folder on first run. And **updates reach you automatically** when a new version ships.

Then use it:

| Command | What it does |
|---|---|
| `/cortex-edge:start` · `/cortex-edge:arranca` | Pick up where you left off last session |
| `/cortex-edge:close` · `/cortex-edge:cierra` | Close the session saving memory + a handoff |
| `/cortex-edge:memoria` | Save something to persistent memory |
| `/cortex-edge:skills` | Browse the catalog and install the skills that fit your work |
| `/cortex-edge:obsidian` | Connect your memory to Obsidian to browse it as notes (optional) |
| `/cortex-edge:setup` | Check everything is ready and offer to install what's missing |

> **If `/reload-plugins` reports `0 skills`, nothing is wrong.** That counter only looks at
> `commands/` directories, and Cortex Edge's commands live in `skills/` (the recommended layout
> for new plugins). To confirm they're there, type `/cortex-edge:` and they should show up — or
> just run `/cortex-edge:setup`.

**Recommended first step:** run `/cortex-edge:setup`. It asks which language you'd like to be guided
in, checks you have what's needed and, if something is missing, explains what it's for and asks
before installing anything.

**Where your memory lives:** `~/.claude/cortex-memory/` by default — created automatically.
Prefer it inside your Obsidian vault (or anywhere else)? Set the `CORTEX_MEMORY_PATH`
environment variable to that path and the hook will use it instead.

<details>
<summary>🔄 How to update to a new version</summary>

**Simplest: just ask your Claude.** Inside Claude Code, type:

> *update the cortex-edge plugin*

It runs the commands, **figures out on its own which scope you installed it with** (user or
project) and applies it. This is the recommended path — you don't need to know anything below.

**To check which version you have:**

```bash
claude plugin list                    # all of them, with version, scope and status
claude plugin details cortex-edge     # details for one
```

(`/cortex-edge:setup` tells you too, and warns you if a newer version exists.)

**By hand, from your terminal**, if you prefer:

```bash
claude plugin marketplace update cortex-edge
claude plugin update cortex-edge@cortex-edge
```

⚠️ **If you installed it with project scope**, the second command fails unless you say so:

```bash
claude plugin update cortex-edge@cortex-edge --scope project
```

**Now the important part: applying the new version.** Claude Code loads plugins **when the session
starts**, so your open conversation keeps the old version even though the new one is already on
disk. Try `/reload-plugins` first; if `/cortex-edge:setup` still shows the older version, **close and
reopen Claude Code** — the CLI itself warns *"restart required"*, and on a version change it is
usually right.

To know which one is actually loaded, ask your Claude: *"which cortex-edge version is loaded in this
session?"*

**If you use `/plugin` inside Claude Code**, it opens **Claude Code's plugin browser** — a list of
hundreds of plugins from everywhere. **That is not Cortex Edge or our catalog**: it's Claude Code's
own manager, the same for any plugin. Go to the **Installed** tab, find `cortex-edge`, update there.

Claude Code also updates plugins in the background, so it reaches you eventually anyway.
</details>

<details>
<summary>📦 Manually from this repo — expand</summary>

Prefer to install by hand, or want just one piece? Download a zip and let your Claude install it:

1. **Core only** → [`dist/cortex-edge-core.zip`](dist/cortex-edge-core.zip) — memory + critical stance.
2. **A single feature** → [`dist/cortex-start-close.zip`](dist/cortex-start-close.zip),
   [`dist/cortex-skills.zip`](dist/cortex-skills.zip) — each **requires the core**.
3. **Full** → [`dist/cortex-edge-full.zip`](dist/cortex-edge-full.zip).

Unzip it, open Claude Code inside the folder, and say *"run the install prompt inside"*.
</details>

---

> 📋 **[See what changed in each version → CHANGELOG.md](CHANGELOG.md)**

## Two kinds of skills (don't mix them up)

| | Which ones | Do you install them? |
|---|---|---|
| 🌱 **Cortex Edge's own** | `arranca` · `cierra` · `memoria` · `setup` · `skills` · `start` · `close` | **No.** They ship inside the plugin. Installing it gives you all of them, and they update with it |
| 🧰 **From the catalog** | superpowers, document writing, research, design, video… | **Yes, and they're optional.** Written by third parties. `/cortex-edge:skills` helps you pick and install only the ones that fit you |

**Why the difference matters:** the built-in ones *are* Cortex Edge and depend on nothing else. The
catalog ones are recommendations — some need an external account or MCP server, and each card says
so before you install anything. If you install none, Cortex Edge works just as well.

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

---

## Requirements

Stated up front, because this project asks every feature to declare its dependencies — the project
itself owes you the same:

| Needs | Why | Without it |
|---|---|---|
| **Claude Code** | Cortex Edge is an extension of it, not a separate app | Nothing works |
| **Python 3** on your PATH | The memory hook is a Python script | Memory silently won't load — the rest still works |
| **git** | How the plugin marketplace fetches and updates | Use the manual zip install instead |

Your memory is plain Markdown files in a folder. Nothing is locked in a database or a proprietary
format — you can read, edit, back up or walk away with them at any time.

## Built on other people's work

Cortex Edge is a thin layer. Almost everything that makes it useful was built by others, and it's
worth being explicit about that:

- **[Claude Code](https://code.claude.com) and its plugin, skill and hook system** (Anthropic) — the
  entire foundation. Cortex Edge only arranges pieces that Claude Code already provides.
- **Community skills** — the catalog in `/cortex-edge:skills` mostly recommends **skills written by
  other people**. We didn't build them; we help you find and install the ones that fit your work.
- **The MCP ecosystem** — every connector skill (Notion, Slack, Drive…) depends on an MCP server
  maintained by someone else.
- **[Obsidian](https://obsidian.md)** — optional, but a natural home: point `CORTEX_MEMORY_PATH` at a
  folder in your vault and your memory becomes notes you can browse, link and search like any other.
- **Markdown and git** — the boring, durable formats that make all of the above portable.

**What Cortex Edge actually adds:** persistence between sessions, a stance that doesn't just agree
with you, continuity when you stop and come back, and curation of what to install. Cortex Edge doesn't invent a new tool — it makes the
one you already use remember you and have judgment of its own.

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
