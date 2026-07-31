# 🌱 Cortex Edge

> 🇬🇧 **[Read it in English → README.md](README.md)**

**Kit modular que convierte a Claude Code en un "segundo cerebro" refinado — una feature opcional a la vez.**

Empiezas con memoria. Agregas capacidades cuando las necesitas. Cada feature es autocontenida, explica
qué hace y declara de qué depende. Nada se impone; instalas solo lo que te ayuda.

---

## Instalación

Hay **dos formas**, y conviene que sepas cuál te sirve antes de empezar:

| | Cómo | Ideal para |
|---|---|---|
| ⚡ **Como plugin** *(recomendado)* | Dos comandos dentro de Claude Code | Casi todo el mundo |
| 📦 **Manual desde este repo** | Bajas un zip y tu Claude lo instala | Si quieres solo una pieza, o prefieres revisar cada archivo antes |

### ⚡ Como plugin

Dentro de Claude Code, ejecuta:

```
/plugin marketplace add agonzalezfront-netizen/cortex-edge
/plugin install cortex-edge@cortex-edge
```

Nada que descargar, ninguna ruta que editar, ningún prompt que explicar. El hook de memoria se
instala solo y crea su carpeta la primera vez. Y **te llegan las actualizaciones automáticamente**
cuando publico una versión nueva.

Después lo usas así:

| Comando | Qué hace |
|---|---|
| `/cortex-edge:arranca` · `/cortex-edge:start` | Retoma donde quedaste la última sesión |
| `/cortex-edge:cierra` · `/cortex-edge:close` | Cierra la sesión guardando memoria + handoff |
| `/cortex-edge:memoria` | Guarda algo en la memoria persistente |
| `/cortex-edge:skills` | Explora el catálogo e instala los skills que te sirvan |

**Dónde vive tu memoria:** en `~/.claude/cortex-memory/` por defecto — se crea sola.
¿La prefieres dentro de tu Obsidian (o donde sea)? Define la variable de entorno
`CORTEX_MEMORY_PATH` con esa ruta y el hook la usará en su lugar.

<details>
<summary>📦 Manual desde este repo — desplegar</summary>

¿Prefieres instalarlo a mano, o quieres solo una pieza? Baja un zip y deja que tu Claude lo instale:

1. **Solo el núcleo** → [`dist/cortex-edge-core.zip`](dist/cortex-edge-core.zip) — memoria + postura crítica.
2. **Una feature suelta** → [`dist/cortex-start-close.zip`](dist/cortex-start-close.zip),
   [`dist/cortex-skills.zip`](dist/cortex-skills.zip) — cada una **requiere el núcleo**.
3. **Completo** → [`dist/cortex-edge-full.zip`](dist/cortex-edge-full.zip).

Descomprime, abre Claude Code dentro de la carpeta y di *"ejecuta el prompt de instalación"*.
</details>

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
| `cortex-skills` | descubrir e instalar skills desde un catálogo curado | núcleo | ✅ lista |

---

## Requisitos

Declarados por adelantado, porque este proyecto le exige a cada feature que declare sus dependencias
— el proyecto mismo te debe lo mismo:

| Necesita | Para qué | Si no lo tienes |
|---|---|---|
| **Claude Code** | Cortex Edge es una extensión suya, no una app aparte | No funciona nada |
| **Python 3** en tu PATH | El hook de memoria es un script de Python | La memoria no carga y no te avisa — el resto sigue funcionando |
| **git** | Es como el marketplace baja y actualiza el plugin | Usa la instalación manual por zip |

Tu memoria son archivos Markdown en una carpeta. Nada queda encerrado en una base de datos ni en un
formato propietario — puedes leerlos, editarlos, respaldarlos o irte con ellos cuando quieras.

## Se apoya en el trabajo de otros

Cortex Edge es una capa delgada. Casi todo lo que lo hace útil lo construyó otra gente, y corresponde
decirlo claro:

- **[Claude Code](https://code.claude.com) y su sistema de plugins, skills y hooks** (Anthropic) — toda
  la base. Cortex Edge solo ordena piezas que Claude Code ya ofrece.
- **Skills de la comunidad** — el catálogo de `/cortex-edge:skills` recomienda en su mayoría **skills
  escritos por otras personas**. No los hicimos nosotros; te ayudamos a encontrar e instalar los que
  calzan con tu trabajo.
- **El ecosistema MCP** — cada skill de conectores (Notion, Slack, Drive…) depende de un servidor MCP
  que mantiene alguien más.
- **[Obsidian](https://obsidian.md)** — opcional, pero le calza natural: apunta `CORTEX_MEMORY_PATH` a
  una carpeta de tu vault y tu memoria pasa a ser notas que puedes navegar, enlazar y buscar como
  cualquier otra.
- **Markdown y git** — los formatos aburridos y duraderos que hacen que todo lo anterior sea portable.

**Lo que Cortex Edge sí aporta:** persistencia entre sesiones, una postura que no te da la razón por
defecto, continuidad cuando paras y vuelves, y criterio sobre qué instalar. No es un segundo cerebro
por sí solo — es lo que convierte un conjunto de muy buenas herramientas en una que se acuerda de ti.

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
