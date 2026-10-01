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
| `/cortex-edge:rigor` | Evidencia antes de "listo": revisión requisito por requisito y lista honesta de lo no verificado |
| `/cortex-edge:tokens` | Mira dónde se van tus tokens: por día, modelo, qué despertó al modelo y sesión |
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

**Qué se carga solo, en cada sesión:** la postura crítica (con *honestidad sobre lo no verificado* y
*pensar vs. ejecutar*), el protocolo de memoria (qué guardar y cómo), tu índice de memoria y, en cada
mensaje, la fecha y la hora local, para que "hoy" o "la próxima semana" se calculen bien. El hook de
memoria avisa cuando el índice se está volviendo demasiado largo para cargarse completo.

**Un vigía de la sesión** habla solo cuando hay motivo: si pasan 20 mensajes sin que se guarde nada en
la memoria, le recuerda a Claude guardar lo importante ahora en vez de esperar al cierre; y cuando el
contexto de la sesión pasa el tope (ver *Sesiones largas* más abajo), avisa que conviene hacer el
traspaso en el próximo cierre natural.

Todo es opcional, con `cortex-edge.json` en tu carpeta de memoria: `{"reloj": false}` apaga el reloj,
`{"idioma": "es"}` carga el núcleo solo en español, `{"recordatorio_guardado": 30}` o `false` ajusta el
recordatorio de guardado, `{"tope_contexto": 150000}` o `false` ajusta el tope de contexto.

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
nueva. **Cierra y vuelve a abrir Claude Code** después de instalar o actualizar: `/reload-plugins`
no garantiza que se apliquen los hooks nuevos, y el propio CLI avisa *"restart required"*. Después
corre `/cortex-edge:setup`: ejecuta los hooks y comprueba que el núcleo de verdad se carga.

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

La instalación manual trae el núcleo y los comandos de continuidad; el vigía de la sesión, `rigor` y
`tokens` vienen solo con el plugin.
</details>

---

> 📋 **[Ver qué cambió en cada versión → CHANGELOG.md](CHANGELOG.md)**

## Dos tipos de skills (que no se confundan)

| | Cuáles son | ¿Hay que instalarlas? |
|---|---|---|
| 🌱 **Nativas de Cortex Edge** | `arranca` · `cierra` · `start` · `close` · `memoria` · `setup` · `skills` · `obsidian` · `rigor` · `tokens` | **No.** Vienen dentro del plugin. Al instalarlo ya las tienes, y se actualizan con él |
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
  no está atada a ninguna feature. Trae además dos reglas de trabajo: **honestidad sobre lo no
  verificado** (nada de "listo" sin evidencia) y **pensar vs. ejecutar** (abajo).

## Sesiones largas: pensar vs. ejecutar, y el tope de contexto

Medido sobre uso real, no supuesto: cuando la salida ronda el 1 % de los tokens, el gasto no es
razonar — es un contexto grande **releído en cada mensaje**, más despertares automáticos que lo
vuelven a releer. Un modelo más barato es la palanca chica; un contexto más chico es la grande.

- **Pensar vs. ejecutar.** La sesión principal es para pensar: decidir, juzgar, verificar. Lo
  repetitivo y mecánico que tiene un **juez objetivo** (un test, un script, un verificador) va a otro
  lado, en este orden: script determinista (cero tokens) > subagente Haiku > Sonnet > Opus > Fable. Sin
  juez objetivo, no se delega.
- **Tope de contexto.** Cuando una sesión viva pasa de **500 mil tokens de contexto**, no se corta la
  tarea en curso: en el próximo cierre natural se cierra con `/cortex-edge:cierra` (handoff con el
  estado vigente) y se sigue en una sesión nueva con `/cortex-edge:arranca`. **Nunca esperes la
  compactación automática**: resume a ciegas lo que un handoff elige con criterio. Con una ventana de
  contexto de 200 mil, baja el tope.
- **Arranque liviano.** Si corres chequeos al empezar, ponlos en un solo script que imprima un
  veredicto por línea (`OK` · `AVISO` · `FALLA`): Claude lee veredictos, no bitácoras.
- **Mídelo.** `/cortex-edge:tokens` lee tus transcripts locales (incluidos los subagentes) y te dice
  dónde se fueron los tokens. Solo números: nunca muestra el contenido de los mensajes ni envía nada.

## Lo que viene: memoria que se ordena (anticipo de la 1.18)

Una memoria grande crece en islas: notas que nadie enlaza, adjuntos que nadie encuentra. Esta es una
memoria real de unas 4.500 notas, antes y durante el orden, tal como la muestra el grafo de Obsidian:

| Antes (30-09-2026): islas y notas sueltas | Durante (01-10-2026): coloreado por tema, islas conectándose |
|---|---|
| ![Grafo de la memoria antes de ordenarla](https://raw.githubusercontent.com/agonzalezfront-netizen/cortex-edge/master/plugins/cortex-edge/docs/grafo-antes-2026-09-30.png) | ![Grafo de la memoria durante el orden](https://raw.githubusercontent.com/agonzalezfront-netizen/cortex-edge/master/plugins/cortex-edge/docs/grafo-durante-2026-10-01.png) |

**Después**, medido con los datos del propio Obsidian: **4.466 notas, 0 huérfanas, 4.155 de 4.156
adjuntos enlazados**. El método detrás se está preparando para la versión 1.18.

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
| **Python 3** en tu PATH | Los hooks (memoria, postura crítica, fecha y hora, vigía de la sesión) y `tokens` son scripts de Python | No cargan y no te avisan — los comandos siguen funcionando |
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

## Licencia / License

**ES:** Publicado bajo la licencia [PolyForm Noncommercial 1.0.0](https://polyformproject.org/licenses/noncommercial/1.0.0): puedes usar, copiar, modificar y compartir este software para cualquier fin **no comercial**. El uso comercial requiere una licencia aparte del autor.

**EN:** Licensed under the [PolyForm Noncommercial License 1.0.0](https://polyformproject.org/licenses/noncommercial/1.0.0): you may use, copy, modify and share this software for any **non-commercial** purpose. Commercial use requires a separate license from the author.

Copyright © 2026 Alberto González.
