<!-- Info card — EN / ES. cortex-memory is the base of the core. -->

# 🧠 cortex-memory (core)

### EN
**What it is.** Persistent memory: your Claude reads a memory index at the start of every session and saves
what matters as you go — so it stops forgetting between sessions.
**What it's for.** So decisions, your project's state and your preferences survive. You don't re-explain
your context every time.
**How it helps.** The memory lives inside your own notes (e.g. Obsidian), so *you* see it too. A
SessionStart hook injects the index automatically; you'll see a "🧠 YOUR MEMORY" block at the start.
**Depends on.** Nothing — this is the base everything else builds on.
**Ships.** SessionStart hook, memory protocol (added to your `CLAUDE.md`), and a seed memory folder.

### ES
**Qué es.** Memoria persistente: tu Claude lee un índice de memoria al inicio de cada sesión y guarda lo
importante sobre la marcha — así deja de olvidar entre sesiones.
**Para qué sirve.** Para que las decisiones, el estado de tu proyecto y tus preferencias sobrevivan. No
re-explicas tu contexto cada vez.
**En qué ayuda.** La memoria vive dentro de tus propias notas (ej. Obsidian), así *tú* también la ves. Un
hook SessionStart inyecta el índice solo; verás un bloque "🧠 TU MEMORIA" al comienzo.
**Depende de.** Nada — es la base sobre la que se construye todo lo demás.
**Incluye.** Hook SessionStart, protocolo de memoria (se agrega a tu `CLAUDE.md`) y una carpeta de memoria
semilla.
