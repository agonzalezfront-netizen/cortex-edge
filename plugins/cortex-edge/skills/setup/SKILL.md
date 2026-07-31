---
description: 'Guided setup for Cortex Edge — walks the person step by step: language, requirements check, installing what''s missing, and what to do next. Use right after installing the plugin, when memory doesn''t seem to load, or when the user asks "does this work?", "revisa la instalación", "check my setup", "por qué no recuerda nada".'
---

# Setup — instalación guiada / guided setup

Lleva a la persona **de la mano** por la puesta en marcha. Nunca debe preguntarse dónde está ni
qué viene después.
Walk the person **by the hand** through setup. They should never wonder where they are or what
comes next.

> **Por qué existe:** el hook de memoria es un script de Python. Si el usuario no tiene Python, el
> hook no corre — **y por lo tanto tampoco puede avisar que falta Python**. Sin esta verificación,
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
| **Python 3** | `python --version` (y `python3 --version` si falla) | El hook que carga tu memoria al iniciar cada sesión |
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
`/reload-plugins` aplica sin reiniciar. **Si dice que no**, sigue normal con la que tiene.

**Si está todo** → dilo en una línea con las versiones, anuncia qué sigue, y pasa al paso 3.

**Si falta algo** → resuélvelo aquí, sin cambiar de paso. Ver más abajo.

## Paso 3 de 4 — Listo: qué queda activo

**No basta con "todo listo".** La persona acaba de instalar algo: necesita saber qué cambió y qué
puede hacer con eso. Ejemplo de tono y largo:

> 🌱 **Cortex Edge · Paso 3 de 4 — Listo**
>
> ✅ Tienes Python 3.13 y git 2.55. Todo funciona.
>
> **Qué queda activo desde ahora:**
> • **Memoria** — lo que guardemos se carga solo al empezar cada sesión, en `~/.claude/cortex-memory/`
> • **Postura crítica** — te voy a cuestionar cuando vea un problema, no a darte la razón siempre
> • **Continuidad** — `/cortex-edge:cierra` deja un resumen y `/cortex-edge:arranca` lo retoma
>
> **Ya tienes tu primer recuerdo guardado:** que prefieres el español. En tu próxima sesión lo voy a
> saber sin preguntarte — eso es exactamente lo que hace la memoria.
>
> → Sigue: te muestro cómo potenciarlo (último paso)

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
> **Cierra esta conversación y abre una nueva**, y ahí escribe **`/cortex-edge:arranca`**.
>
> ¿Por qué una sesión nueva? Porque la memoria se carga **al arrancar**. En la que estamos ahora
> todavía no está activa. En la próxima voy a recordar tu idioma sin que me lo digas — y ahí te
> hago un recorrido por todo lo que puedes hacer.

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
> Para recordar tus conversaciones, Cortex Edge usa un pequeño programa que corre al abrir cada
> sesión, y ese programa necesita **Python 3**. No lo tienes instalado.
>
> **Sin Python:** el resto funciona igual (los comandos, la postura crítica), pero cada sesión
> empieza en blanco — no voy a recordar nada de la anterior.
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

> Sin problema. El resto de Cortex Edge funciona igual — solo la memoria entre sesiones queda en
> pausa. Si algún día cambias de opinión, corre `/cortex-edge:setup` y lo dejamos andando en un
> minuto. ¡Gracias por probarlo! 🌱

Deja la puerta abierta. Que quede con ganas de volver, no con la sensación de haber fallado un examen.

## Criterio / Judgment

- **No pidas permiso para lo que no hace falta.** Si Python ya está, ni lo menciones.
- **Una sola pregunta.** Si faltan dos cosas, agrúpalas; no interrogues.
- **Nunca instales software del sistema en silencio**, aunque tengas permisos.
- **Breve no es seco.** Confirmar en una línea y desaparecer deja a la persona sin saber qué hacer.
- **Si algo la manda a una pantalla que no es tuya** (por ejemplo el explorador de plugins de
  Claude Code), **avísale antes**: qué va a ver, que no es de Cortex Edge, y qué tiene que hacer ahí.
