# 🌱 Cortex Edge

> 🇬🇧 **[Read it in English → README.md](README.md)**

**Kit modular que convierte a Claude Code en un "segundo cerebro" refinado — una feature opcional a la vez.**

Empiezas con memoria. Agregas capacidades cuando las necesitas. Cada feature es autocontenida, explica
qué hace y declara de qué depende. Nada se impone; instalas solo lo que te ayuda.

---

## Núcleo (siempre, no opcional)

Toda instalación de Cortex Edge trae un **núcleo** que no depende de ninguna feature:

- **Memoria** (`cortex-memory`) — memoria persistente entre sesiones. Es lo que hace que Claude
  "recuerde" lo de antes en vez de partir de cero cada vez.
- **Postura crítica** (`core/POSTURA-CRITICA.md`) — Cortex es un compañero riguroso, no un sí-señor:
  cuestiona ideas, señala gaps y propone alternativas mejores. Aplica a toda idea, plan o decisión —
  no está atada a ninguna feature.

## Catálogo (features opcionales)

| Feature | Qué hace | Depende de | Estado |
|---|---|---|---|
| `cortex-start-close` | `/arranca` y `/cierra` — retoma donde quedaste, y cierra dejando un handoff | núcleo (memoria) | ✅ lista |
| `cortex-skills` | descubrir e instalar skills | — | 🚧 próxima |

## Descargas — tres formas

1. **Solo el núcleo** → [`dist/cortex-edge-core.zip`](dist/cortex-edge-core.zip) — memoria + postura
   crítica. Funciona solo.
2. **Una feature suelta** → [`dist/cortex-start-close.zip`](dist/cortex-start-close.zip),
   [`dist/cortex-skills.zip`](dist/cortex-skills.zip) — cada una **requiere el núcleo** (su instalador
   lo verifica y te avisa).
3. **Completo** → [`dist/cortex-edge-full.zip`](dist/cortex-edge-full.zip) — núcleo + todas las features.

**Para instalar cualquiera:** descomprime, abre Claude Code dentro de la carpeta y di
*"ejecuta el prompt de instalación"*. Claude lo instala y te confirma.

---

## Modelo de features

Cada feature es una carpeta dentro de `features/` con la misma forma:

```
features/<nombre-feature>/
  FEATURE.md          → ficha: qué es, para qué sirve, en qué ayuda, dependencias
  install/
    PROMPT-INSTALL.md → el prompt que tu Claude ejecuta para autoinstalarla
    ...               → los archivos que trae la feature (comandos, hooks, etc.)
```

## Transparencia de dependencias

La `FEATURE.md` de cada feature **debe** declarar sus dependencias por adelantado, en lenguaje simple:

- **Requiere otra feature** — por ejemplo *"necesita `cortex-memory` instalada primero"*.
- **Requiere una cuenta/MCP externa** — por ejemplo *"necesita una cuenta de Notion conectada"*.
- **No requiere nada** — se dice así.

Siempre se explica **qué es**, **para qué sirve**, **en qué ayuda** y **cómo mejora tu proceso de
trabajo**.

## Idiomas

Todo texto de cara al usuario viene en **inglés y español**. Los comandos traen alias por idioma donde
ayuda (por ejemplo `/start` = `/arranca`, `/close` = `/cierra`).

---

*🌱 Cortex Edge crece una feature refinada a la vez.*
