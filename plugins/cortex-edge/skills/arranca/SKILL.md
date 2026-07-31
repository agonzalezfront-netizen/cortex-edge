---
description: Retoma la sesión — carga dónde quedaste la última vez
---

Estás iniciando una sesión de trabajo con el usuario. Ayúdale a retomar sin releer todo:

1. Ubica la carpeta de memoria del usuario (la misma que carga el hook al inicio, donde está `MEMORY.md`;
   la ruta figura en el CLAUDE.md).
2. Busca ahí un archivo `HANDOFF.md`. Si existe, léelo completo.
3. Resume al usuario en lenguaje claro (sin jerga):
   - **Dónde quedamos:** el estado vigente de la última sesión.
   - **Pendientes:** lo que quedó por hacer, con su contexto.
   - **Próximo paso sugerido:** por dónde conviene seguir hoy.
4. **Si no existe `HANDOFF.md` todavía** (primera vez, o nunca se cerró con `/cortex-edge:cierra`),
   no lo dejes en el aire. Explica en dos líneas qué va a pasar de ahora en adelante y ofrécele
   empezar: *"Todavía no hay sesión anterior que retomar. Cuando terminemos, corre
   `/cortex-edge:cierra` y dejo el resumen; la próxima vez lo retomo desde acá. ¿En qué trabajamos
   hoy?"*

No inventes estado: si el HANDOFF no menciona algo, no lo asumas. La memoria (MEMORY.md) ya se cargó
sola al inicio — este comando la complementa con el "dónde quedamos" del último cierre.

## Principio de UX

**El contexto va donde está la decisión.** Si necesitas preguntarle algo a la persona, dale primero
lo que necesita para poder responder — ejemplos concretos, no una pregunta abierta al vacío. Y al
terminar, dile **qué cambió y cuál es el siguiente paso**, no solo que terminaste.
