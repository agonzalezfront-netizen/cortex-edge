---
description: Cierra la sesión — guarda lo importante, apaga lo que quedó corriendo y deja un handoff con el estado vigente
---
<!-- Generated from the plugin (plugins/cortex-edge/skills/cierra/SKILL.md); do not edit by hand. / Generado desde el plugin (plugins/cortex-edge/skills/cierra/SKILL.md); no editar a mano. -->

Estás cerrando la sesión de trabajo con el usuario. Haz esto antes de terminar:

**1. Guarda en memoria lo que la próxima sesión debería saber.**
Repasa lo que pasó en esta sesión (decisiones, avances, cosas que cambiaron) y guárdalo siguiendo el
protocolo de memoria cargado al inicio: decisiones **y su porqué**, estado de los proyectos, feedback y
correcciones de la persona, tareas pendientes, preferencias. Actualiza notas existentes en vez de
duplicar. No guardes conversación trivial ni lo que ya está en el código.

**2. Cada lección, a `feedback`.** Si durante la sesión la persona tuvo que recordarte o corregirte algo,
o un error tuyo costó una vuelta, guárdalo como `feedback` con **Por qué:** (qué falló) y **Cómo
aplicarlo:** (qué harás distinto). Si puede repetirse, anota también qué **guarda** lo evitaría sin
depender de acordarse (un test, un chequeo en un script) y ofrécela.

**3. Apaga lo que esta sesión dejó corriendo.** Procesos en segundo plano, monitores, tareas
programadas o en bucle, servidores de desarrollo, observadores de archivos: si los lanzaste **tú en esta
sesión** y ya no hacen falta, detenlos. Cada uno que sigue vivo puede despertar al modelo y gastar
tokens después de cerrada la sesión. **No toques** lo que ya existía antes de la sesión ni los servicios
del sistema. Si algo debe quedar corriendo a propósito, dilo en el handoff con su porqué.

**4. Escribe o actualiza `HANDOFF.md`** en la carpeta de memoria (junto a `MEMORY.md`). Abre con el
bloque de **estado vigente**: es lo primero que leerá la próxima sesión.

```markdown
# HANDOFF — <fecha y hora de hoy>

## Estado vigente al cierre
- **Qué:** <en qué se estaba trabajando, en una o dos frases>
- **Por qué:** <para qué; la decisión o el objetivo detrás>
- **Dónde:** <archivos, carpeta, rama, URL: lo necesario para encontrarlo sin buscar>
- **Qué falta:** <lo que queda para darlo por terminado>
- **Primer paso:** <la primera acción concreta para la próxima sesión>

## Verificado y sin verificar
- ✅ <lo que se comprobó, con qué: test, comando, archivo>
- ⚠️ <lo que NO se comprobó y por qué>

## Pendientes
- <lo que falta, con contexto suficiente para retomarlo>

## Quedó corriendo (si aplica)
- <proceso o tarea que sigue vivo a propósito, y por qué>
```

Sobrescribe el HANDOFF anterior (siempre refleja el estado más reciente). **Honestidad:** nada va en
✅ sin evidencia; lo que no verificaste va en ⚠️, aunque creas que funciona.

**5. Si la sesión ya es grande, este cierre es el traspaso.** Si apareció el aviso 📏 de tope de
contexto (o la sesión lleva muchas horas y vueltas), dilo: la siguiente tarea conviene empezarla en
una **sesión nueva** con `/arranca`, que lee este handoff. No esperes la compactación
automática: resume a ciegas lo que este handoff elige con criterio.

**6. Confirma al usuario** en pocas líneas: qué guardaste en memoria, qué apagaste, qué quedó sin
verificar, y que el handoff quedó listo. (En inglés: `/close`.)

## Principio de UX

**Ubicación y rumbo, siempre.** Cada mensaje abre diciendo en qué parte del recorrido está la
persona y cierra diciendo qué sigue. Si llega desde `/setup`, viene del paso 4 — no la
dejes sin saber dónde está parada.

**El contexto va donde está la decisión.** Si preguntas algo, primero da lo necesario para poder
responder — ejemplos concretos, no una pregunta abierta al vacío. Al terminar, di **qué cambió y
cuál es el siguiente paso**, no solo que terminaste.

**Si la mandas a una pantalla que no es tuya** (el explorador de plugins de Claude Code, la web de
un skill), **avísale antes**: qué va a ver, que eso no es Cortex Edge, y qué tiene que hacer ahí.
