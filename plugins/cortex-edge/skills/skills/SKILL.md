---
description: Browse a curated catalog of skills and install the ones that fit the user's work. Use when the user asks what skills exist, wants to add capabilities, says "instala skills", "qué skills hay", "what skills can I add", or asks for a tool Claude doesn't have yet.
---

# Skills — catálogo e instalación / catalog and install

Ayuda a la persona a **elegir e instalar skills** para su Claude Code, y deja activada la capa de
comportamiento para que después no tenga que nombrarlos.

Help the user **choose and install skills**, then turn on the behavior layer so they never have to
name a skill again.

## Cómo trabajar esto / How to work

**Aclara la diferencia antes de mostrar nada.** Mucha gente confunde las dos cosas:

> Ojo, son dos cosas distintas: las **7 skills de Cortex Edge** (`arranca`, `cierra`, `memoria`,
> `setup`, `skills`, `start`, `close`) ya las tienes — vienen dentro del plugin. Lo que te muestro
> acá es un **catálogo de skills de terceros**, opcionales, para darle capacidades extra.

**0. Antes de nada, mira qué ya tiene instalado.** Recomendarle instalar algo que ya usa te
desacredita al instante. Revisa en silencio:

- `claude plugin list` — plugins instalados y de qué marketplace vienen
- `~/.claude/skills/` — sus skills personales
- `.claude/skills/` del proyecto en el que está, si existe

Con eso: **marca lo que ya tiene como “ya lo tienes ✓” y no lo ofrezcas**. Si ya tiene varios de un
grupo, tómalo como señal de por dónde va su interés y empieza por ahí. Y si te pide instalar algo
que ya está, dilo derecho — *"ese ya lo tienes andando"* — en vez de reinstalarlo.

**1. Pregunta primero en qué trabaja.** No listes los cinco grupos de golpe — es ruido. Pregunta a qué
se dedica o qué le gustaría que su Claude hiciera mejor, y **abre solo el grupo que calza**:

| Si la persona… | Abre (uso interno) |
|---|---|
| programa, construye software, arregla bugs | `catalog/01-producto-dev.md` |
| escribe informes, propuestas, presentaciones, planillas | `catalog/02-documentos.md` |
| investiga, analiza datos | `catalog/03-investigacion-datos.md` |
| hace diseño, video, imágenes, o quiere crear sus propios skills | `catalog/04-multimedia-meta.md` |
| quiere conectar Notion, Slack, Drive… | `catalog/05-conectores.md` |

🚫 **Esos nombres de archivo son internos: la persona NUNCA debe verlos.** Son índices que tú lees
para saber qué recomendar. Lo que le muestras a ella son **los skills que hay adentro**, con su
nombre real (superpowers, docx, pdf…) y en lenguaje simple. Mostrarle `01-producto-dev.md` es como
darle el número de estante en vez del libro.

Cada ficha del catálogo dice: **qué es · para qué es bueno · cuándo Cortex lo toma solo · cuándo NO ·
de qué depende**. Traduce eso a lenguaje simple, sin jerga.

**2. Explica antes de instalar, y pregunta.** Nunca instales sin confirmar. Di para qué sirve y qué
cambia en su día a día. Si un skill necesita una cuenta externa o un MCP, **dilo antes**, no después.

**Siempre deja una salida a la vista.** En cada paso donde la persona elige, la última opción es
irse sin instalar nada — y sin que parezca un error. Por ejemplo:

> **1.** Instalar [skill]
> **2.** Ver otro grupo
> **3.** Lo dejo para después 🌱

Si elige irse, cierra corto y cálido, recordándole el comando para volver:
*"Dale. Cuando quieras, `/cortex-edge:skills` y seguimos donde quedamos."* **Nada de insistir.**

**3. Instala lo elegido.** Los skills de la comunidad se instalan por su propio mecanismo (marketplace
de plugins, repo, o copiando a `~/.claude/skills/`). Sigue las instrucciones del skill que corresponda
y **verifica que quedó disponible** antes de decir que está listo.

**4. Activa la capa de comportamiento — este es el paso que hace la diferencia.**
Lee `COMPORTAMIENTO.md` (está junto a este archivo) y **agrega su contenido al `CLAUDE.md` del
usuario** si aún no está. Eso es lo que hace que Claude tome los skills por su cuenta, en vez de
esperar a que se los nombren. Confírmale en una línea que quedó activo.

## Criterio / Judgment

- **Pocos y buenos.** Instalar diez skills que no usa es peor que dos que sí. Recomienda por su trabajo
  real, no por completitud.
- **Si pide el skill equivocado, dilo.** Propón el que de verdad calza y explica por qué — la persona
  siempre puede insistir, pero primero merece saber cuál es el camino ideal.
- **Sin uso performativo.** Un skill que no aporta valor está tan mal como ignorar uno que sí.

## Principio de UX

**Ubicación y rumbo, siempre.** Cada mensaje abre diciendo en qué parte del recorrido está la
persona y cierra diciendo qué sigue. Si llega desde `/cortex-edge:setup`, viene del paso 4 — no la
dejes sin saber dónde está parada.

**El contexto va donde está la decisión.** Si preguntas algo, primero da lo necesario para poder
responder — ejemplos concretos, no una pregunta abierta al vacío. Al terminar, di **qué cambió y
cuál es el siguiente paso**, no solo que terminaste.

**Si la mandas a una pantalla que no es tuya** (el explorador de plugins de Claude Code, la web de
un skill), **avísale antes**: qué va a ver, que eso no es Cortex Edge, y qué tiene que hacer ahí.
