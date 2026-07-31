<!-- Cortex Edge — bilingual README (EN / ES) -->

# 🌱 Cortex Edge

**Modular toolkit that turns Claude Code into a refined "second brain" — one optional feature at a time.**
Start with memory. Add capabilities as you need them. Every feature is self-contained, explains what it
does, and declares what it depends on. Nothing is forced; you install only what helps your work.

**Kit modular que convierte a Claude Code en un "segundo cerebro" refinado — una feature opcional a la
vez.** Empiezas con memoria. Agregas capacidades cuando las necesitas. Cada feature es autocontenida,
explica qué hace y declara de qué depende. Nada se impone; instalas solo lo que te ayuda.

---

## Feature model / Modelo de features

Each feature is a folder under `features/` with the same shape:

```
features/<feature-name>/
  FEATURE.md          → info card: what it is, what it's for, how it helps, dependencies (EN + ES)
  install/
    PROMPT-INSTALL.md → the prompt the user's Claude runs to self-install it (EN + ES)
    ...               → the files the feature ships (commands, hooks, etc.)
```

**To install a feature / Para instalar una feature:** open Claude Code in the feature folder and say
*"run PROMPT-INSTALL.md"* / *"ejecuta PROMPT-INSTALL.md"*. Claude installs it and confirms.

## Transparency of dependencies / Transparencia de dependencias

A feature's `FEATURE.md` **must** state its dependencies up front, in plain language:
- **Requires another feature** — e.g. *"needs `cortex-memory` installed first"*.
- **Requires an external account/MCP** — e.g. *"needs a connected Notion account"*.
- **Requires nothing** — say so.

La `FEATURE.md` de cada feature **debe** declarar sus dependencias por adelantado, en lenguaje simple:
si necesita otra feature, si necesita una cuenta/MCP externa, o si no necesita nada. Siempre se explica
**qué es**, **para qué sirve**, **en qué ayuda** y **cómo mejora el proceso de trabajo**.

## Languages / Idiomas
Every user-facing text ships in **EN and ES**. Commands ship language aliases where it helps
(e.g. `/start` = `/arranca`, `/close` = `/cierra`).

---

## Core (always, not optional) / Núcleo (siempre, no opcional)

Every Cortex Edge install ships a **core** that does not depend on any feature:
- **Memory** (`cortex-memory`) — persistent memory between sessions.
- **Critical stance** (`core/POSTURA-CRITICA.md`) — Cortex is a rigorous partner, not a yes-man; it
  questions ideas, flags gaps and proposes better, always. This is general (every idea/plan/decision), not
  tied to any feature.

Todo Cortex Edge trae un **núcleo** que no depende de ninguna feature: **memoria** (continuidad entre
sesiones) + **postura crítica** (`core/POSTURA-CRITICA.md`) — Cortex es un compañero riguroso, no un
sí-señor; cuestiona, señala gaps y propone mejor, siempre. Es general, no atada a ninguna feature.

## Catalog (optional features) / Catálogo (features opcionales)

| Feature | EN | ES | Depends on / Depende de | Status |
|---|---|---|---|---|
| `cortex-start-close` | `/start` + `/close` continuity | `/arranca` + `/cierra` continuidad | core (memory) | ✅ |
| `cortex-skills` | discover + install skills | descubrir + instalar skills | — | 🚧 next / próxima |

## Downloads — three ways / Descargas — tres formas

1. **Core only / Solo el núcleo** → `dist/cortex-edge-core.zip` — memory + critical stance. Standalone.
   Memoria + postura crítica. Funciona solo.
2. **A single feature / Una feature suelta** → `dist/cortex-start-close.zip`, `dist/cortex-skills.zip` —
   each **requires the core** (its installer checks and tells you). Cada una **requiere el núcleo** (su
   instalador lo verifica y te avisa).
3. **Full / Completo** → `dist/cortex-edge-full.zip` — core + all features. Run `INSTALAR.md`.
   Núcleo + todas las features. Ejecuta `INSTALAR.md`.

To install any of them: unzip, open Claude Code in the folder, say "run the install prompt inside".
Para instalar cualquiera: descomprime, abre Claude Code en la carpeta, di "ejecuta el prompt de instalación".

*🌱 Cortex Edge grows one refined feature at a time. / Cortex Edge crece una feature refinada a la vez.*
