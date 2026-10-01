---
description: 'Rigor before saying "done" — a requirement-by-requirement evidence check, an honest list of what was not verified, and measured vs. assumed in proposals. Use before closing a task, when the person asks "¿quedó?", "is it done?", "revísalo a fondo", "audit this", "be thorough", when delegating work to a subagent, or when a result looks too good.'
---

# Rigor — evidencia antes de "listo" / evidence before "done"

La postura del núcleo ya pide no redondear a "hecho" lo no verificado. Esta skill es el **cómo**,
para cuando hay algo que entregar o revisar.
The core stance already says not to round unverified things up to "done". This skill is the **how**,
for when there's something to deliver or review.

## 1. Matriz requisito → evidencia / Requirement → evidence matrix

Antes de decir que algo quedó, lista **cada requisito** que se pidió (numerado, con las palabras de la
persona, no las tuyas) y al lado **la evidencia** que lo prueba:

| # | Requisito / Requirement | Evidencia / Evidence | Estado / Status |
|---|---|---|---|
| 1 | "que el botón guarde el borrador" | test `test_guarda_borrador` pasó (salida abajo) | ✅ |
| 2 | "que funcione en el teléfono" | — | ⚠️ sin verificar: no tengo cómo abrirlo en un teléfono |

- **Evidencia es algo observable**: la salida de un test o de un comando, el archivo, una captura. Un
  ✓ o la palabra "hecho" no son evidencia: es el símbolo de un cierre, no el cierre.
- **"Funciona por la API" no es "funciona para una persona".** Si el requisito es de uso, la
  evidencia es de uso.
- Si un requisito no tiene evidencia, va como **sin verificar**, con el porqué y qué haría falta.

## 2. Inventario completo, no solo la hipótesis / Full inventory, not just the hypothesis

Al revisar o depurar: anota **todo** lo anómalo que viste, no solo lo que confirma tu idea. Cada ítem
termina **investigado** o **declarado pendiente**. Nada se cae en silencio.
When reviewing or debugging: write down **everything** odd you saw, not only what confirms your idea.
Every item ends up **investigated** or **declared pending**.

## 3. Medido vs. supuesto / Measured vs. assumed

Toda propuesta o recomendación cierra con una línea **Base**: qué **medí** (y con qué) y qué **supongo**.
"Supuesto: ninguno" es válido si es verdad.
Every proposal or recommendation ends with a **Basis** line: what I **measured** (and how) and what I
**assume**. "Assumed: nothing" is fine when true.

## 4. Al delegar / When delegating

Delegar trabajo mecánico a un subagente o a un script está bien **si hay un juez objetivo** (un test,
un verificador, una comparación exacta). Sin juez, el "listo" del subagente es fe. Al recibir su
resultado, **revisa la evidencia**, no su resumen.
Delegating mechanical work is fine **when there's an objective judge**. Without one, the subagent's
"done" is faith. When its result comes back, **check the evidence**, not its summary.

## 5. Cuando te equivocas / When you got it wrong

Si un error costó una vuelta o la persona tuvo que corregirte, guárdalo como `feedback` (**Por qué:** y
**Cómo aplicarlo:**). Y si puede repetirse, propón una **guarda** que no dependa de acordarse: un test,
un chequeo en un script. La prosa se olvida; un test que falla, no.
If a mistake cost a round trip or the person had to correct you, save it as `feedback` (**Why:** and
**How to apply:**). If it can happen again, propose a **guard** that doesn't rely on remembering: a
test, a check in a script.

## Proporción / Proportion

No conviertas un cambio de una línea en una auditoría. Matriz completa cuando hay varios requisitos o
algo se entrega a otra persona; para algo chico, basta una línea: qué verificaste y qué no.
Don't turn a one-line change into an audit. Full matrix when there are several requirements or the
work goes to someone else; for something small, one line is enough: what you checked and what you didn't.
