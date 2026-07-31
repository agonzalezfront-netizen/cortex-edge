---
description: Check that Cortex Edge has everything it needs, explain what got activated, and offer to install what's missing. Use right after installing the plugin, when memory doesn't seem to load, or when the user asks "does this work?", "revisa la instalación", "check my setup", "por qué no recuerda nada".
---

# Setup — verificar, explicar y dejar andando / check, explain, get going

Comprueba que Cortex Edge pueda funcionar, **explica qué queda activo** y **dice qué sigue**.
Check that Cortex Edge can work, **explain what's now active**, and **say what comes next**.

> **Por qué existe:** el hook de memoria es un script de Python. Si el usuario no tiene Python, el
> hook no corre — **y por lo tanto tampoco puede avisar que falta Python**. Sin esta verificación,
> la persona instala, ve los comandos funcionar, y la memoria nunca carga sin explicación.

## Principio de UX que manda en todo este skill

**El contexto va donde está la decisión.** Nunca mandes a la persona a leer el README, la
documentación ni otro comando antes de que pueda decidir o entender. Todo lo que necesita saber
va en el mismo mensaje, en lenguaje simple. Si tiene que irse a otro lado, el mensaje está mal
escrito.

## 0. Primero: el idioma

**Antes que nada, pregunta en qué idioma quiere que lo guíes.** Es lo primero que ve una persona
recién instalada, así que va corto y en ambos idiomas a la vez:

> 🌱 **Cortex Edge** — ¿en qué idioma prefieres que te guíe? / Which language should I guide you in?
>
> **1.** Español  ·  **2.** English

Desde su respuesta, **todo lo que sigue va en ese idioma**: la verificación, las preguntas, los
mensajes de error y el cierre. No mezcles.

**Si ya sabes el idioma** porque la persona te viene escribiendo en él, **no preguntes**: úsalo y
sigue. La pregunta es para el arranque en frío, no para interrogar a alguien que ya te habló.

**Y guarda la elección como recuerdo** (el formato está en `/cortex-edge:memoria`): un archivo
`prefiere-idioma-<es|en>.md` de tipo `user`, con el índice `MEMORY.md` actualizado. Dos motivos:

1. **Persiste** — en las próximas sesiones el hook lo carga y no hay que volver a preguntar.
2. **Demuestra el producto en el primer minuto** — cuando llegues al paso 2 puedes decírselo:
   *"Ya guardé tu primer recuerdo: que prefieres español. En tu próxima sesión lo voy a saber sin
   preguntarte."* Eso explica para qué sirve todo esto mejor que cualquier párrafo.

## 1. Verifica, en silencio

Sin narrar cada paso:

| Qué | Cómo | Para qué sirve |
|---|---|---|
| **Python 3** | `python --version` (y `python3 --version` si falla) | El hook que carga tu memoria al iniciar cada sesión |
| **git** | `git --version` | Que el plugin se actualice solo cuando salga una versión nueva |
| **Carpeta de memoria** | ¿existe `$CORTEX_MEMORY_PATH` o `~/.claude/cortex-memory/`? | Donde viven tus recuerdos |

## 2. Si está todo — confirma, explica y orienta

**No basta con decir "todo listo".** La persona acaba de instalar algo y necesita saber qué cambió
y qué hacer ahora. Tres bloques cortos, sin relleno:

1. **Qué encontraste** — una línea con las versiones.
2. **Qué queda activo** — en lenguaje simple, no técnico. Que entienda qué gana.
3. **Qué sigue** — **una** acción concreta para probarlo ahora mismo.

Ejemplo del tono y la longitud:

> ✅ **Listo.** Tienes Python 3.13 y git 2.55, así que todo funciona.
>
> **Qué queda activo desde ahora:**
> • **Memoria** — lo que guardes se carga solo al empezar cada sesión, en `~/.claude/cortex-memory/`
> • **Postura crítica** — te voy a cuestionar cuando vea un problema, no a darte la razón siempre
> • **Continuidad** — `/cortex-edge:cierra` deja un resumen y `/cortex-edge:arranca` lo retoma
>
> **Ya tienes tu primer recuerdo guardado:** que prefieres el español. En tu próxima sesión lo voy a
> saber sin preguntarte — eso es exactamente lo que hace la memoria.
>
> **Pruébalo con algo tuyo:** dime cómo prefieres que trabaje o en qué proyecto andas, y lo guardo
> con `/cortex-edge:memoria`. La próxima vez arrancamos desde ahí.

Adapta el texto a lo que de verdad encontraste; no lo copies literal. Si la carpeta de memoria ya
tenía recuerdos, dilo (*"ya tienes 4 recuerdos guardados"*) en vez de tratarlo como instalación nueva.

## 3. Si falta algo — todo el contexto en la misma pregunta

**Nunca instales sin permiso, y nunca pidas permiso a ciegas.** La persona debe poder decidir con lo
que ve, sin abrir nada más. En un solo mensaje:

1. **Qué falta** y **para qué sirve**, sin jerga.
2. **Qué dejará de funcionar** — honesto: el resto del plugin sirve igual, solo se pierde la memoria.
3. **Qué harías exactamente**: el comando a la vista, cuánto demora, y qué **no** toca de su sistema.

Ejemplo:

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

**Comando según sistema:** Windows `winget install Python.Python.3.12` · macOS `brew install python`
· Linux `sudo apt install python3` (o el gestor de su distribución). Si no hay gestor disponible,
**no improvises**: dale el enlace oficial (python.org/downloads) y ofrece volver a verificar después.

### Si dice que sí
Instala, **vuelve a verificar** que quedó disponible, y **cierra con el mismo bloque del punto 2**
(qué quedó activo + qué sigue) — acaba de completar la instalación, ahora sí necesita el onboarding.
Si la instalación falla, dilo claro y ofrece el camino manual; no lo dejes creyendo que quedó listo.

### Si dice que no
Respeta la respuesta y cierra con calidez, sin insistir ni repetir el argumento:

> Sin problema. El resto de Cortex Edge funciona igual — solo la memoria entre sesiones queda en
> pausa. Si algún día cambias de opinión, corre `/cortex-edge:setup` y lo dejamos andando en un
> minuto. ¡Gracias por probarlo! 🌱

Deja la puerta abierta. Que quede con ganas de volver, no con la sensación de haber fallado un examen.

## Criterio / Judgment

- **No pidas permiso para lo que no hace falta.** Si Python ya está, ni lo menciones.
- **Una sola pregunta.** Si faltan dos cosas, agrúpalas; no interrogues.
- **Nunca instales software del sistema en silencio**, aunque tengas permisos.
- **Breve no es seco.** Confirmar en una línea y desaparecer deja a la persona sin saber qué hacer:
  el objetivo es que termine sabiendo qué gana y cuál es su siguiente paso.
