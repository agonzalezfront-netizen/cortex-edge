# 🌱 Cortex Edge

> 🇬🇧 **[Read it in English → README.md](README.md)**

**Un colaborador que te recuerda, te cuestiona y retoma donde quedaste.**

No es un repositorio de notas ni un asistente de recordatorios: es lo que resulta de juntar memoria,
criterio y continuidad sobre la herramienta que ya usas. Empiezas con memoria y agregas capacidades
cuando las necesitas — cada feature explica qué hace y de qué depende. Nada se impone.

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
| `/cortex-edge:obsidian` | Conecta tu memoria con Obsidian para verla como notas (opcional) |
| `/cortex-edge:setup` | Verifica que todo esté listo y ofrece instalar lo que falte |

> **Si `/reload-plugins` te dice `0 skills`, está todo bien.** Ese contador solo mira los
> directorios `commands/`, y los comandos de Cortex Edge viven en `skills/` (el formato
> recomendado para plugins nuevos). Para comprobar que están, escribe `/cortex-edge:` y
> deberías verlos aparecer — o simplemente corre `/cortex-edge:setup`.

**Primer paso recomendado:** ejecuta `/cortex-edge:setup`. Te pregunta en qué idioma quieres que te
guíe, comprueba que tengas lo necesario y, si falta algo, te explica para qué sirve y te pregunta
antes de instalar nada.

**Dónde vive tu memoria:** en `~/.claude/cortex-memory/` por defecto — se crea sola.
¿La prefieres dentro de tu Obsidian (o donde sea)? Define la variable de entorno
`CORTEX_MEMORY_PATH` con esa ruta y el hook la usará en su lugar.

<details>
<summary>🔄 Cómo actualizar a una versión nueva</summary>

**Lo más simple: pídeselo a tu Claude.** Dentro de Claude Code, escríbele:

> *actualiza el plugin cortex-edge*

Él corre los comandos, **detecta solo con qué alcance lo tienes instalado** (usuario o proyecto) y
lo deja aplicado. Es la vía recomendada porque no tienes que saber nada de lo de abajo.

**Para saber qué versión tienes:**

```bash
claude plugin list                    # todos, con version, alcance y estado
claude plugin details cortex-edge     # detalle de uno
```

(`/cortex-edge:setup` también te lo dice, y te avisa si hay una version mas nueva.)

**A mano, desde tu terminal**, si prefieres:

```bash
claude plugin marketplace update cortex-edge
claude plugin update cortex-edge@cortex-edge
```

⚠️ **Si lo instalaste con alcance de proyecto**, el segundo comando falla salvo que se lo digas:

```bash
claude plugin update cortex-edge@cortex-edge --scope project
```

**Y ahora lo importante: aplicar la versión nueva.** Claude Code carga los plugins **al arrancar la
sesión**, así que tu conversación abierta sigue con la versión vieja aunque el disco ya tenga la
nueva. Prueba `/reload-plugins` primero; si `/cortex-edge:setup` te sigue mostrando la versión
anterior, **cierra y vuelve a abrir Claude Code** — el propio CLI avisa *"restart required"* y en un
cambio de versión suele tener razón.

Para saber cuál está realmente cargada, pregúntale a tu Claude: *"¿qué versión de cortex-edge tienes
cargada en esta sesión?"*

**Si usas `/plugin` dentro de Claude Code**, se abre el **explorador de plugins de Claude Code** —
una lista con cientos de plugins de todo el mundo. **Eso no es Cortex Edge ni nuestro catálogo**:
es el gestor propio de Claude Code, igual para cualquier plugin. Ve a la pestaña **Installed**,
busca `cortex-edge` y actualízalo ahí.

Claude Code también actualiza plugins solo en segundo plano, así que tarde o temprano te llega.
</details>

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

> 📋 **[Ver qué cambió en cada versión → CHANGELOG.md](CHANGELOG.md)**

## Dos tipos de skills (que no se confundan)

| | Cuáles son | ¿Hay que instalarlas? |
|---|---|---|
| 🌱 **Nativas de Cortex Edge** | `arranca` · `cierra` · `memoria` · `setup` · `skills` · `start` · `close` | **No.** Vienen dentro del plugin. Al instalarlo ya las tienes, y se actualizan con él |
| 🧰 **Del catálogo** | superpowers, redacción de documentos, investigación, diseño, video… | **Sí, y son opcionales.** Están escritas por terceros. `/cortex-edge:skills` te ayuda a elegir e instalar solo las que te sirvan |

**Por qué importa la diferencia:** las nativas son Cortex Edge y no dependen de nada más. Las del
catálogo son recomendaciones — algunas necesitan una cuenta o un servidor MCP externo, y cada ficha
lo dice antes de que instales nada. Si no instalas ninguna, Cortex Edge funciona igual de bien.

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
defecto, continuidad cuando paras y vuelves, y criterio sobre qué instalar. Cortex Edge no inventa una herramienta
nueva — hace que la que ya usas se acuerde de ti y tenga criterio propio.

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
