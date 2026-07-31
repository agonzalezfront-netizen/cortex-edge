---
description: Check that Cortex Edge has everything it needs to work, and offer to install what's missing. Use right after installing the plugin, when memory doesn't seem to load, or when the user asks "does this work?", "revisa la instalación", "check my setup", "por qué no recuerda nada".
---

# Setup — verificar e instalar dependencias / check and install dependencies

Comprueba que Cortex Edge pueda funcionar de verdad, y **ofrece resolver lo que falte**.
Check that Cortex Edge can actually work, and **offer to fix what's missing**.

> **Por qué existe:** el hook de memoria es un script de Python. Si el usuario no tiene Python,
> el hook no corre — **y por lo tanto tampoco puede avisar que falta Python**. Sin esta
> verificación, la persona instala el plugin, ve los comandos funcionar, y la memoria nunca
> carga sin explicación. Este skill es el que cierra ese hueco.

## 1. Verifica, en silencio

Comprueba con Bash, sin narrar cada paso:

| Qué | Cómo | Para qué sirve |
|---|---|---|
| **Python 3** | `python --version` (y `python3 --version` si el primero falla) | El hook que carga tu memoria al iniciar cada sesión |
| **git** | `git --version` | Que el plugin se actualice solo cuando salga una versión nueva |
| **Carpeta de memoria** | ¿existe `$CORTEX_MEMORY_PATH` o `~/.claude/cortex-memory/`? | Donde viven tus recuerdos |

## 2. Si está todo

Dilo en **una línea**, sin ceremonia, e indica dónde quedó su memoria. Ejemplo:
*"Todo listo. Tu memoria vive en `~/.claude/cortex-memory/` y se carga sola al empezar cada sesión."*

No hagas una lista de verificación larga: si funciona, la persona no necesita el detalle.

## 3. Si falta algo — explica, pide permiso, y respeta la respuesta

**Nunca instales nada sin preguntar.** Di, en lenguaje simple:

1. **Qué falta** y **para qué se usa** — sin jerga.
2. **Qué dejará de funcionar** si no se instala (sé honesto: el resto del plugin sigue sirviendo,
   lo único que se pierde es la memoria persistente).
3. **Qué harías exactamente** para instalarlo, con el comando a la vista.

Ejemplo de cómo pedirlo:

> Para que Cortex Edge recuerde tus conversaciones necesita **Python 3**, que es lo que usa el
> pequeño programa que carga tu memoria al empezar cada sesión. No lo tienes instalado.
>
> Puedo instalarlo por ti con `winget install Python.Python.3.12` — toma un par de minutos y no
> toca nada más de tu sistema. ¿Lo instalo?

**Comando según el sistema:** Windows `winget install Python.Python.3.12` · macOS
`brew install python` · Linux `sudo apt install python3` (o el gestor de su distribución).
Si no hay gestor de paquetes disponible, **no improvises**: dale el enlace de descarga oficial
(python.org/downloads) y ofrécele volver a verificar cuando lo tenga.

### Si dice que sí
Instálalo, **vuelve a verificar** que quedó disponible, y confirma en una línea. Si la instalación
falla, dilo claro y ofrece el camino manual — no lo dejes creyendo que quedó listo.

### Si dice que no
**Respeta la respuesta y cierra con calidez.** Nada de insistir ni de repetir el argumento:

> Sin problema. El resto de Cortex Edge funciona igual — solo la memoria entre sesiones queda
> en pausa. Si algún día cambias de opinión, corre `/cortex-edge:setup` y lo dejamos andando
> en un minuto. ¡Gracias por probarlo! 🌱

Deja la puerta abierta, no la cierres con un reproche. Que la persona quede con ganas de volver.

## Criterio / Judgment

- **No pidas permiso para lo que no hace falta.** Si Python ya está, ni lo menciones.
- **Una sola pregunta.** Si faltan dos cosas, agrúpalas en una sola consulta, no interrogues.
- **Nunca instales software del sistema en silencio.** Aunque tengas permisos, se pregunta.
