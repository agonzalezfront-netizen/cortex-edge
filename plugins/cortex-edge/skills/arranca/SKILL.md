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
4. Si no existe `HANDOFF.md` todavía, dilo en una línea y pregúntale en qué quiere trabajar hoy.

No inventes estado: si el HANDOFF no menciona algo, no lo asumas. La memoria (MEMORY.md) ya se cargó
sola al inicio — este comando la complementa con el "dónde quedamos" del último cierre.
