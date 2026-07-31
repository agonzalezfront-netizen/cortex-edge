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

**Ubicación y rumbo, siempre.** Cada mensaje abre diciendo en qué parte del recorrido está la
persona y cierra diciendo qué sigue. Si llega desde `/cortex-edge:setup`, viene del paso 4 — no la
dejes sin saber dónde está parada.

**El contexto va donde está la decisión.** Si preguntas algo, primero da lo necesario para poder
responder — ejemplos concretos, no una pregunta abierta al vacío. Al terminar, di **qué cambió y
cuál es el siguiente paso**, no solo que terminaste.

**Si la mandas a una pantalla que no es tuya** (el explorador de plugins de Claude Code, la web de
un skill), **avísale antes**: qué va a ver, que eso no es Cortex Edge, y qué tiene que hacer ahí.
