---
description: Save something to persistent memory so it survives across sessions. Use when the user says "recuerda esto", "guarda esto en memoria", "remember this", or when something important surfaces that would be lost when the session ends (a preference, a decision and its why, an ongoing project, a correction they gave you).
---

# Memoria — guardar / save

Escribe un recuerdo en la carpeta de memoria del usuario, para que sobreviva a esta sesión.
Write a memory to the user's memory folder so it survives this session.

## Dónde / Where

`$CORTEX_MEMORY_PATH` si está definida; si no, `~/.claude/cortex-memory/`.
Es la misma carpeta que el hook `SessionStart` carga al inicio de cada conversación.

## Cómo / How

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
incluido el porqué) · `project` (trabajo en curso, metas, restricciones) · `reference`
(punteros a recursos externos: URLs, tableros, tickets).

## Después de escribir / After writing

Agrega **una línea** al índice `MEMORY.md` de esa carpeta:

```markdown
- [Título corto](archivo.md) — de qué se trata en pocas palabras
```

`MEMORY.md` es solo el índice — nunca pongas ahí el contenido del recuerdo.

## Reglas / Rules

- **Antes de crear, busca.** Si ya existe un archivo que cubre el tema, actualiza ese en vez de
  duplicar. Borra los que resulten estar equivocados.
- **No guardes lo obvio ni lo efímero**: nada que el repositorio o el historial ya registren, ni
  cosas que solo importan en esta conversación.
- **Fechas absolutas.** "El martes" no significa nada dentro de tres semanas: escribe la fecha.
- Confirma al usuario en una línea qué guardaste y dónde.
