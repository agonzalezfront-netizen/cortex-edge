---
description: Save something to persistent memory so it survives across sessions. Use when the user says "recuerda esto", "guarda esto en memoria", "remember this", when something important surfaces that would be lost when the session ends (a preference, a decision and its why, an ongoing project, a correction they gave you), or when they invoke it directly to set memory up.
---

# Memoria — guardar / save

Escribe un recuerdo en la carpeta de memoria, para que sobreviva a esta sesión.
Write a memory to the memory folder so it survives this session.

## Principio de UX

**El contexto va donde está la decisión.** Si tienes que preguntarle algo a la persona, dale
primero lo necesario para poder responder. Preguntar "¿qué quieres guardar?" a alguien que
acaba de instalar esto es dejarlo mirando una página en blanco.

## Dónde / Where

`$CORTEX_MEMORY_PATH` si está definida; si no, `~/.claude/cortex-memory/`.
Es la misma carpeta que el hook `SessionStart` carga al inicio de cada conversación.

---

## Caso A — la persona ya dijo qué guardar

Guárdalo directo (formato abajo) y confirma. No preguntes de más.

## Caso B — invocan el comando "en frío", sin nada concreto que guardar

Esto pasa casi siempre justo después de instalar. **No preguntes a secas.** Explica para qué
sirve, da ejemplos concretos que pueda tomar o adaptar, y recién ahí pregunta. Algo así:

> **La memoria sirve para no repetirte.** Lo que guardemos acá lo voy a saber en todas tus
> próximas sesiones, sin que me lo cuentes de nuevo.
>
> Lo que más rinde guardar:
> • **Cómo prefieres que trabaje** — *"explícame antes de escribir código"*, *"sé directo, sin
>   preámbulos"*, *"respóndeme siempre en español"*
> • **Quién eres y a qué te dedicas** — tu rol, tu stack, el tipo de proyectos que haces
> • **En qué andas ahora** — el proyecto activo, su objetivo, qué falta
> • **Una decisión y su porqué** — para que no la volvamos a discutir en tres semanas
>
> ¿Con cuál partimos? Dímelo con tus palabras, yo le doy formato.

Adapta los ejemplos a lo que sepas de la persona por la conversación. Si no sabes nada de ella,
los de arriba sirven tal cual.

---

## Formato del archivo

**Un recuerdo = un archivo.** Nombre en kebab-case, corto y descriptivo
(`prefiere-tests-antes-del-codigo.md`). Dentro:

```markdown
---
name: <slug-en-kebab-case>
description: <una línea: de qué se trata, para decidir si es relevante al recordar>
type: user | feedback | project | reference
---

<El hecho, en pocas líneas. Si es feedback o un proyecto, agrega **Por qué:** y
**Cómo aplicarlo:**. Enlaza recuerdos relacionados con [[nombre-del-otro]].>
```

**Tipos**: `user` (quién es, su rol, sus preferencias) · `feedback` (cómo quiere que trabajes,
incluido el porqué) · `project` (trabajo en curso, metas, restricciones) · `reference` (punteros a
recursos externos: URLs, tableros, tickets).

## Después de escribir

1. Agrega **una línea** al índice `MEMORY.md` de esa carpeta:
   ```markdown
   - [Título corto](archivo.md) — de qué se trata en pocas palabras
   ```
   `MEMORY.md` es solo el índice — nunca pongas ahí el contenido del recuerdo.

2. **Confirma explicando qué cambia**, no solo que guardaste:

   > Guardado. Desde tu próxima sesión voy a saber que prefieres que te explique antes de
   > escribir código, sin que me lo digas. Ya llevas 3 recuerdos.

   Esa segunda frase es la que hace que la persona entienda para qué sirvió. Sin ella, "guardado"
   es un archivo más que no significa nada.

## Reglas

- **Antes de crear, busca.** Si ya existe un archivo que cubre el tema, actualiza ese en vez de
  duplicar. Borra los que resulten estar equivocados.
- **No guardes lo obvio ni lo efímero**: nada que el repositorio o el historial ya registren, ni
  cosas que solo importan en esta conversación.
- **Fechas absolutas.** "El martes" no significa nada dentro de tres semanas: escribe la fecha.
