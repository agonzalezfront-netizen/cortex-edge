---
description: Cierra la sesión — guarda lo importante y deja un handoff para la próxima vez
---

Estás cerrando la sesión de trabajo con el usuario. Haz dos cosas antes de terminar:

**1. Guarda en memoria lo que la próxima sesión debería saber.**
Repasa lo que pasó en esta sesión (decisiones, avances, cosas que cambiaron) y guárdalo siguiendo el
protocolo de tu CLAUDE.md: decisiones de producto **y su porqué**, features y su estado, feedback de
autores/usuarios, tareas pendientes, preferencias del usuario. Actualiza notas existentes en vez de
duplicar. No guardes conversación trivial ni lo que ya está en el código.

**2. Escribe o actualiza `HANDOFF.md`** en la carpeta de memoria (junto a `MEMORY.md`), con este formato:

```markdown
# HANDOFF — <fecha de hoy>

## Dónde quedamos
<en qué se estaba trabajando y por qué — el estado vigente real al cerrar>

## Pendientes
- <lo que falta, con contexto suficiente para retomarlo>

## Próximo paso
<la primera acción concreta para la próxima sesión>
```

Sobrescribe el HANDOFF anterior (siempre refleja el estado más reciente).

**3. Confirma al usuario** en una línea: qué guardaste en memoria y que el handoff quedó listo para la
próxima vez.

## Principio de UX

**El contexto va donde está la decisión.** Si necesitas preguntarle algo a la persona, dale primero
lo que necesita para poder responder — ejemplos concretos, no una pregunta abierta al vacío. Y al
terminar, dile **qué cambió y cuál es el siguiente paso**, no solo que terminaste.
