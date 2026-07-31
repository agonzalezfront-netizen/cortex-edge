# 🌱 Install Cortex Edge / Instalar Cortex Edge

**How it's used / Cómo se usa:** unzip on the desktop, open Claude Code in this folder, and say
*"run INSTALAR.md"* / descomprime en el escritorio, abre Claude Code en esta carpeta y di
*"ejecuta INSTALAR.md"*.

---

**EN.** Hi Claude. You're installing Cortex Edge for this person. Do the **core** first (always), then offer
the optional features. Reply in the person's language. Be honest — only claim something is installed once it
really is.

**ES.** Hola Claude. Vas a instalar Cortex Edge para esta persona. Primero el **núcleo** (siempre), después
ofreces las features opcionales. Responde en su idioma. Sé honesto — solo digas que algo quedó instalado
cuando de verdad lo esté.

## ♻️ Idempotent install / Instalación idempotente (READ FIRST / LEE ESTO PRIMERO)
This package may be installed **over a previous (partial) install** — the person may already have memory,
`/arranca /cierra`, or some skills. **Before installing each piece, check if it's already there:**
- If it's already present and unchanged → **skip it**, don't reinstall.
- If it's an older version → **update it in place**.
- **Never duplicate** in `CLAUDE.md`: if a block (critical stance, memory protocol, commands note) is already
  there, do **not** append a second copy — leave it or replace it.
Install **only what's missing**, and at the end report what was already present vs. what you added.

Este paquete puede instalarse **sobre una instalación previa (parcial)** — la persona quizá ya tiene memoria,
`/arranca /cierra`, o algunos skills. **Antes de instalar cada pieza, verifica si ya está:** si está igual →
**sáltala**; si es una versión vieja → **actualízala**; **nunca dupliques** en el `CLAUDE.md` (si un bloque ya
está, no agregues una segunda copia). Instala **solo lo que falta** y al final reporta qué ya estaba vs. qué agregaste.

## Step 1 — Core / Núcleo (always / siempre)

1. **Memory / Memoria.** Check there's a memory folder with `MEMORY.md`. If it exists, good — skip. If not,
   install it from this package: run `core/cortex-memory/install/PROMPT-INSTALL.md`.
   Verifica que exista la carpeta de memoria con `MEMORY.md`. Si existe, bien — sáltalo. Si no, instálala
   desde este paquete: ejecuta `core/cortex-memory/install/PROMPT-INSTALL.md`.
2. **Critical stance / Postura crítica.** Append the content of `core/POSTURA-CRITICA.md` (the person's
   language section) to their `CLAUDE.md` (`C:\Users\<USER>\.claude\CLAUDE.md`). This is **not optional** —
   it's how Cortex behaves with everything. Agrega `core/POSTURA-CRITICA.md` (sección del idioma) al
   `CLAUDE.md`. **No es opcional** — es cómo se comporta Cortex con todo.

## Step 2 — Optional features / Features opcionales

Read `README.md` and each `features/*/FEATURE.md`. Present the available features to the person in plain
language (what each is, what for, dependencies) and ask which to install:
Lee `README.md` y cada `features/*/FEATURE.md`. Presenta las features en lenguaje simple (qué es, para qué,
dependencias) y pregunta cuáles instalar:

- **cortex-start-close** — `/start`+`/close` continuity → run `features/cortex-start-close/install/PROMPT-INSTALL.md`.
- **cortex-skills** — skill catalog + behavior layer → run `features/cortex-skills/install/PROMPT-INSTALL.md`.

For each feature the person picks, follow its own `install/PROMPT-INSTALL.md`. Respect declared dependencies
(a feature that needs another, or an external account, says so).
Para cada feature elegida, sigue su propio `install/PROMPT-INSTALL.md`. Respeta las dependencias declaradas.

## Done / Al terminar
Summarize honestly: core installed (memory ✓, critical stance ✓), which features are active, and anything
that needs an account or couldn't be installed from here.
Resume con honestidad: núcleo instalado (memoria ✓, postura crítica ✓), qué features quedaron activas, y lo
que necesita una cuenta o no se pudo instalar desde acá.
