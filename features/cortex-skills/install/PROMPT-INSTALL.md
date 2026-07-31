# Install — cortex-skills / Instalar — cortex-skills

**EN.** Hi Claude. You're setting up the user's skill catalog and the behavior layer that makes you *use*
skills like an expert colleague. Reply in the user's language. **Be honest, not magical**: only claim a
skill is installed once it really is.

**ES.** Hola Claude. Vas a configurar el catálogo de skills de la persona y la capa de comportamiento que
hace que *uses* los skills como un colega experto. Responde en su idioma. **Sé honesto, no mágico**: solo
digas que un skill está instalado cuando de verdad lo esté.

---

## Step 1 — Show the catalog and ask / Muestra el catálogo y pregunta
Read the cards in `../catalog/` and present the groups to the user in plain language — for **each group**,
what it's good for. Then ask what they want: **the full pack, specific groups, or individual skills.**
Don't install anything before they choose.

Lee las tarjetas de `../catalog/` y presenta los grupos en lenguaje simple — para **cada grupo**, para qué
sirve. Luego pregunta qué quiere: **el pack completo, grupos específicos, o skills sueltos.** No instales
nada antes de que elija.

Groups / Grupos: **Producto/Dev** (superpowers, frontend-design, ui-ux-pro-max) · **Documentos** (docx,
pdf, pptx, xlsx) · **Investigación/Datos** (deep-research, dataviz) · **Multimedia/Meta** (remotion,
skill-creator, consolidate-memory) · **Conectores** (Google, Figma, Marketing/Sales — ⚠️ need an account).

## Step 2 — Install what they chose / Instala lo elegido
For each chosen skill:
1. **Check if it's already available** (look at the user's plugins/skills; many ship via a plugin
   marketplace). If it's there, skip.
2. **If it's a plugin** (e.g. superpowers, the document skills), enable it the way this Claude Code install
   does it (marketplace / `enabledPlugins` in `settings.json`). Guide the user through any step you can't do.
3. **If it's a Connector** (Google, Figma, Marketing/Sales), it needs an external account/MCP — **do not
   fake it.** Tell the user it's ready to use *once they connect that account*, and how.
4. If you truly can't install something from here, say so plainly and leave clear instructions — don't
   pretend it's done.

Verifica si ya está; si es plugin, habilítalo como lo hace este Claude Code (marketplace / `enabledPlugins`);
si es Conector, necesita cuenta externa — **no lo finjas**, di que queda listo al conectarla; si de verdad
no puedes instalarlo, dilo claro y deja instrucciones.

## Step 3 — Install the behavior layer / Instala la capa de comportamiento
♻️ **First check if it's already there** — if the behavior block from `../COMPORTAMIENTO.md` is already in the
`CLAUDE.md`, do **not** add a second copy (update it only if it's an older version). / **Primero verifica si ya
está** — si el bloque de `../COMPORTAMIENTO.md` ya está en el `CLAUDE.md`, **no** agregues una segunda copia
(actualízalo solo si es una versión vieja).

Append the content of `../COMPORTAMIENTO.md` (pick the user's language section) to the user's `CLAUDE.md`.
This is what makes you reach for skills on your own, and steer the user to the right one when they ask for
the wrong fit. **This part always applies** — install it even if they picked few skills.

Agrega el contenido de `../COMPORTAMIENTO.md` (la sección del idioma de la persona) al `CLAUDE.md`. Es lo
que te hace tomar los skills por tu cuenta y orientar al correcto si piden el equivocado. **Siempre aplica.**

## Done / Al terminar
Report, honestly: which skills are **active now**, which need an **account connected** (and how), and
anything that **couldn't be installed** from here. Then tell the user, simply: "From now on I'll reach for
these on my own when a task needs them — you don't have to name them."

Reporta, con honestidad: qué skills quedaron **activos**, cuáles necesitan **conectar cuenta** (y cómo), y
lo que **no se pudo instalar** desde acá. Luego di, simple: "De ahora en más los tomo por mi cuenta cuando
la tarea lo pida — no tienes que nombrarlos."
