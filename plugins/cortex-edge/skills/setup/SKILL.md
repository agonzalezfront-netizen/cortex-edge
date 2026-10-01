---
description: 'Guided setup for Cortex Edge — walks the person step by step: language, requirements check, installing what''s missing, and what to do next. Use right after installing the plugin, when memory doesn''t seem to load, or when the user asks "does this work?", "revisa la instalación", "check my setup", "por qué no recuerda nada".'
---

# Setup — instalación guiada / guided setup

Lleva a la persona **de la mano** por la puesta en marcha. Nunca debe preguntarse dónde está ni
qué viene después.
Walk the person **by the hand** through setup. They should never wonder where they are or what
comes next.

> **Por qué existe:** los hooks del núcleo (memoria, postura crítica, fecha y hora) son scripts de
> Python. Si el usuario no tiene Python, no corren — **y por lo tanto tampoco puede avisar que falta Python**. Sin esta verificación,
> la persona instala, ve los comandos funcionar, y la memoria nunca carga sin explicación.

---

## Las dos reglas que mandan en todo este skill

**1. Ubicación y rumbo, siempre.** Cada mensaje que le envíes abre diciendo **en qué paso está** y
cierra diciendo **qué sigue**. Sin eso, la persona queda a ciegas y abandona.

```
🌱 Cortex Edge · Paso 2 de 4 — Requisitos
   [ ... el contenido del paso ... ]
   → Sigue: dejar tu memoria activa
```

**2. El contexto va donde está la decisión.** Nunca la mandes a leer el README, la documentación ni
otro comando antes de que pueda decidir o entender. Todo lo necesario va en el mismo mensaje, en
lenguaje simple. Si tiene que irse a otro lado, el mensaje está mal escrito.

**El recorrido completo es de 4 pasos.** Anúncialo al empezar para que sepa cuánto falta:
`1 Idioma · 2 Requisitos · 3 Listo · 4 Potenciarlo`. Si hay que instalar algo, ese trabajo va
**dentro** del paso 2 — no cambies la numeración a mitad de camino.

---

## Paso 1 de 4 — Idioma

Lo primero, corto y en ambos idiomas:

> 🌱 **Cortex Edge · Paso 1 de 4 — Idioma**
> *(el recorrido completo: idioma → requisitos → listo → potenciarlo)*
>
> ¿En qué idioma prefieres que te guíe? / Which language should I guide you in?
>
> **1.** Español  ·  **2.** English
>
> → Sigue: reviso que tengas todo lo necesario

Desde su respuesta, **todo va en ese idioma**: verificaciones, preguntas, errores y cierre.

**Si ya sabes el idioma** porque viene escribiéndote en él, **no preguntes**: úsalo, dilo en media
línea (*"sigo en español"*) y pasa al paso 2. La pregunta es para el arranque en frío.

**Guarda la elección como recuerdo** (formato en `/cortex-edge:memoria`): archivo
`prefiere-idioma-<es|en>.md`, tipo `user`, con `MEMORY.md` actualizado. Persiste **y** te sirve para
demostrar el producto en el paso 3.

## Paso 2 de 4 — Requisitos

Verifica sin narrar cada comando:

| Qué | Cómo | Para qué sirve |
|---|---|---|
| **Python 3** | `python --version` (y `python3 --version` si falla) | Los hooks que cargan tu memoria, la postura crítica y la fecha en cada sesión |
| **git** | `git --version` | Que el plugin se actualice solo cuando salga una versión nueva |
| **Carpeta de memoria** | ¿existe `$CORTEX_MEMORY_PATH` o `~/.claude/cortex-memory/`? | Donde viven tus recuerdos |
| **Versión instalada** | `claude plugin list` (o `claude plugin details cortex-edge`) | Saber si estás al día |

**Sobre la versión — di siempre cuál tiene, y si hay una más nueva, ofrécele actualizar.** Una
persona no tiene forma de saber que existe una versión mejor: es tarea tuya avisarle. Para
comparar, refresca el catálogo (`claude plugin marketplace update cortex-edge`) y mira si el
origen trae una superior a la instalada.

Si está desactualizado, díselo con el mismo criterio de siempre — qué gana, y preguntando:

> Tienes **Cortex Edge 1.3.0** y ya existe la **1.9.1**. Las versiones nuevas mejoraron sobre todo
> la guía de instalación y el catálogo de skills. ¿La actualizo? Son unos segundos.

**Si acepta**: actualiza con `claude plugin update cortex-edge@cortex-edge` — y si el plugin está
instalado con **alcance de proyecto**, agrega `--scope project`, porque si no falla. Después
**hay que reiniciar Claude Code** (cerrar y volver a abrir): los plugins y sus hooks se cargan al
arrancar la sesión, y `/reload-plugins` no garantiza que se apliquen los hooks nuevos. Díselo así,
sin suavizarlo. **Si dice que no**, sigue normal con la que tiene.

### Verificación real: ¿el núcleo llega de verdad?

Que el archivo del hook exista **no prueba nada**: el hook puede fallar en silencio (Python que no
es el del PATH, carpeta sin permisos, un error de sintaxis) y la persona nunca se entera. Corre los
hooks tal como los corre Claude Code y **mira lo que devuelven**:

```bash
python "${CLAUDE_PLUGIN_ROOT}/hooks/cargar-nucleo.py" < /dev/null
python "${CLAUDE_PLUGIN_ROOT}/hooks/cargar-memoria.py" < /dev/null
python "${CLAUDE_PLUGIN_ROOT}/hooks/reloj.py" < /dev/null
echo '{"session_id": "setup-check"}' | python "${CLAUDE_PLUGIN_ROOT}/hooks/vigia-sesion.py"; echo "exit $?"
```

(En PowerShell, en vez de `< /dev/null` usa `'' | python "…"`. Si `python` no existe pero
`python3` sí, pruébalo con `python3` y anótalo como problema: el hook usa `python`.)

| Hook | Salida correcta |
|---|---|
| `cargar-nucleo.py` | JSON con `hookSpecificOutput.additionalContext` que contiene **"Postura crítica"** o **"Critical stance"**, y **"Protocolo de memoria"** o **"Memory protocol"** |
| `cargar-memoria.py` | JSON cuyo `additionalContext` contiene **"TU MEMORIA"** o **"YOUR MEMORY"** |
| `reloj.py` | JSON con la fecha de hoy — o vacío si la persona apagó el reloj (ver abajo) |
| `vigia-sesion.py` | `exit 0`, normalmente **sin salida**: solo habla cuando toca recordar guardar o la sesión pasó el tope de contexto. Vacío aquí es lo correcto |

- **Si las cuatro salen bien** → la verificación pasó. Recuerda qué pasó, para el paso 3.
- **Si alguna sale vacía o con error** → **no digas que está listo**. Muestra el error en una
  línea, explica qué deja de funcionar (sin núcleo: no te va a cuestionar ni a guardar recuerdos
  por su cuenta; sin memoria: cada sesión empieza en blanco) y resuélvelo dentro de este paso.
- **Si el índice trae el aviso ⚠️ de tamaño** → díselo y ofrece consolidarlo ahora.

**Nota honesta sobre esta sesión:** los hooks corren **al iniciar** una sesión. Si el plugin se
instaló o actualizó con esta conversación ya abierta, el núcleo **todavía no está en esta
sesión** aunque la verificación pase. Dilo así; el paso 4 la lleva a una sesión nueva.

**Si está todo** → dilo en una línea con las versiones, anuncia qué sigue, y pasa al paso 3.

**Si falta algo** → resuélvelo aquí, sin cambiar de paso. Ver más abajo.

### Configuración opcional (`cortex-edge.json`)

En la carpeta de memoria puede existir un archivo `cortex-edge.json`. Si no existe, todo usa sus
valores por defecto. Menciónalo solo si la persona pregunta o si le molesta algo de esto:

```json
{ "reloj": false, "idioma": "es", "recordatorio_guardado": 20, "tope_contexto": 500000 }
```

- **`reloj`** — por defecto, en cada mensaje se agrega una línea con el día, la fecha y la hora
  local, para que "hoy", "mañana" o "hace una semana" se calculen bien. `false` lo apaga.
- **`idioma`** — `"es"` o `"en"`: el núcleo se carga solo en ese idioma (ocupa la mitad). Si no
  está, se usa el recuerdo `prefiere-idioma-*.md` que guardas en el paso 1; sin ninguno, van ambos.
- **`recordatorio_guardado`** — cada cuántos mensajes, si no se guardó nada en la memoria, se recuerda
  guardar lo importante sin esperar al cierre (por defecto 20). `false` lo apaga.
- **`tope_contexto`** — cuando el contexto de la sesión pasa de este número de tokens (por defecto
  500 000), se avisa que en el próximo cierre natural conviene cerrar con handoff y seguir en una sesión
  nueva. Con modelos de ventana de 200 000 conviene bajarlo (p. ej. 150 000). `false` lo apaga.

## Paso 3 de 4 — Listo: qué queda activo

**No basta con "todo listo".** La persona acaba de instalar algo: necesita saber qué cambió y qué
puede hacer con eso. Ejemplo de tono y largo:

> 🌱 **Cortex Edge · Paso 3 de 4 — Listo**
>
> ✅ Tienes Python 3.13 y git 2.55, y probé los hooks: el núcleo y tu memoria cargan bien.
>
> **Qué se activa desde tu próxima sesión:**
> • **Memoria** — lo que guardemos se carga solo al empezar cada sesión, en `~/.claude/cortex-memory/`
> • **Postura crítica** — te voy a cuestionar cuando vea un problema, no a darte la razón siempre
> • **Fecha y hora** — sé qué día y qué hora es en cada mensaje (se puede apagar)
> • **Vigía de la sesión** — te recuerdo guardar lo importante y aviso cuando la sesión crece tanto
>   que conviene seguir en una nueva
> • **Continuidad** — `/cortex-edge:cierra` deja un resumen y `/cortex-edge:arranca` lo retoma
>
> **Ya tienes tu primer recuerdo guardado:** que prefieres el español. En tu próxima sesión lo voy a
> saber sin preguntarte — eso es exactamente lo que hace la memoria.
>
> → Sigue: te muestro cómo potenciarlo (último paso)

**Solo afirma lo que verificaste.** La lista de "qué se activa" sale de la verificación real del
paso 2, no de lo que el plugin promete. Si un hook no pasó, no lo pongas en la lista: di qué quedó
pendiente y por qué. Nunca digas que la postura "queda activa" sin haber visto la salida del hook.

Adapta a lo que de verdad encontraste. Si la carpeta ya tenía recuerdos, dilo (*"ya tienes 4
recuerdos guardados"*) en vez de tratarlo como instalación nueva.

## Paso 4 de 4 — Potenciarlo (y cierre)

Felicita, ofrece el catálogo, y **deja siempre la salida a la vista**:

> 🌱 **Cortex Edge · Paso 4 de 4 — Potenciarlo**
>
> 🎉 **Ya está, terminaste.** De aquí en adelante voy a recordar lo que guardemos, te voy a
> cuestionar cuando vea un problema, y cada sesión va a empezar donde terminó la anterior.
>
> **Tu siguiente paso, y vale la pena hacerlo ahora:**
>
> **Cierra Claude Code, vuelve a abrirlo**, y en la sesión nueva escribe **`/cortex-edge:arranca`**.
>
> ¿Por qué reiniciar? Porque la memoria y la postura se cargan **al arrancar**. En la sesión que
> tenemos abierta todavía no están activas. En la próxima voy a recordar tu idioma sin que me lo
> digas — y ahí te hago un recorrido por todo lo que puedes hacer.

**No ofrezcas el catálogo de skills acá.** Esa invitación va en el recorrido de `arranca`, cuando
la persona ya vio funcionar lo básico. Ofrecerle instalar cosas antes de que entienda lo que tiene
es apilar sin cimientos.

Si insiste en verlo ahora, muéstraselo igual — pero la ruta recomendada es la de arriba.

**Ojo con lo que felicitas:** mira qué comandos `/cortex-edge:*` tienes disponibles antes de
afirmar. Con el plugin viene todo; con la instalación manual puede haber solo el núcleo.

**Nunca insistas** ni repitas la invitación en sesiones siguientes.

---

## Si falta algo (dentro del paso 2)

**Nunca instales sin permiso, y nunca pidas permiso a ciegas.** La persona debe poder decidir con
lo que ve. En un solo mensaje, sin salir del paso 2:

> 🌱 **Cortex Edge · Paso 2 de 4 — Requisitos**
>
> Para recordar tus conversaciones y cargar su forma de trabajar, Cortex Edge usa unos pequeños
> programas que corren al abrir cada sesión, y necesitan **Python 3**. No lo tienes instalado.
>
> **Sin Python:** los comandos siguen funcionando, pero cada sesión empieza en blanco — no voy a
> recordar nada de la anterior, y la postura crítica y la fecha no se cargan solas.
>
> **Si lo instalo:** ejecuto `winget install Python.Python.3.12`. Toma un par de minutos, es el
> instalador oficial, y no modifica nada más de tu sistema ni de tu Claude Code.
>
> ¿Lo instalo?
>
> → Si aceptas: lo instalo, verifico y seguimos al paso 3

**Comando según sistema:** Windows `winget install Python.Python.3.12` · macOS `brew install python`
· Linux `sudo apt install python3` (o el gestor de su distribución). Si no hay gestor disponible,
**no improvises**: dale el enlace oficial (python.org/downloads) y ofrece volver a verificar después.

**Si dice que sí** → instala, **vuelve a verificar**, y sigue al paso 3 normalmente. Si la
instalación falla, dilo claro y ofrece el camino manual; no lo dejes creyendo que quedó listo.

**Si dice que no** → respeta la respuesta y cierra con calidez, sin insistir:

> Sin problema. Los comandos de Cortex Edge funcionan igual; la memoria entre sesiones y la postura
> crítica automática quedan en pausa. Si algún día cambias de opinión, corre `/cortex-edge:setup` y lo dejamos andando en un
> minuto. ¡Gracias por probarlo! 🌱

Deja la puerta abierta. Que quede con ganas de volver, no con la sensación de haber fallado un examen.

## Criterio / Judgment

- **No pidas permiso para lo que no hace falta.** Si Python ya está, ni lo menciones.
- **Una sola pregunta.** Si faltan dos cosas, agrúpalas; no interrogues.
- **Nunca instales software del sistema en silencio**, aunque tengas permisos.
- **Breve no es seco.** Confirmar en una línea y desaparecer deja a la persona sin saber qué hacer.
- **Si algo la manda a una pantalla que no es tuya** (por ejemplo el explorador de plugins de
  Claude Code), **avísale antes**: qué va a ver, que no es de Cortex Edge, y qué tiene que hacer ahí.
