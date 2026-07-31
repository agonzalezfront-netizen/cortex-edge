---
description: 'Connect the memory folder to Obsidian so the person can browse, search and link their memories visually. Use when they ask about Obsidian, want to see or organize their memories, say "quiero ver mis recuerdos", "integrar obsidian", "connect obsidian", or when the guided tour offers it.'
---

# Obsidian — conectar tu memoria / connect your memory

Deja los recuerdos **navegables como notas**, sin cambiar nada de cómo funciona la memoria.
Make memories **browsable as notes**, without changing how memory works.

## Principio de UX

**Ubicación y rumbo, siempre** · **el contexto va donde está la decisión** · si la mandas a una
pantalla que no es tuya, avísale antes qué va a ver.

---

## 1. Explica primero — qué gana y qué NO cambia

**No des por hecho que sabe qué es Obsidian.** En dos líneas, sin jerga:

> Tus recuerdos ya son archivos de texto en una carpeta — eso no va a cambiar. **Obsidian es una
> app gratuita que abre esa carpeta** y te deja verlos como notas: buscarlos, enlazarlos entre sí,
> ver un mapa de cómo se conectan, y leerlos desde el teléfono si quieres.
>
> No es obligatorio y no cambia nada de cómo yo recuerdo: **funciona igual con o sin Obsidian.**
> Es puramente para tu comodidad, para que puedas mirar y ordenar lo que vamos guardando.
>
> **1.** Sí, conectémoslo  ·  **2.** Ahora no 🌱

Si dice que no, cierra corto y sigue. **Nunca insistas.**

## 2. Mira qué tiene antes de proponer nada

- **¿Obsidian instalado?** Windows `winget list Obsidian.Obsidian` · macOS `ls /Applications | grep -i obsidian`
  · Linux según su gestor.
- **¿Ya tiene una vault?** Pregúntale — no la busques revolviendo su disco. Si tiene, va ahí; si no,
  se crea una.
- **¿Dónde vive hoy su memoria?** `$CORTEX_MEMORY_PATH` o `~/.claude/cortex-memory/`, y **cuántos
  recuerdos hay** (los vas a migrar, así que después verificas que estén todos).

## 3. Si no lo tiene instalado — pide permiso, con todo a la vista

> Obsidian no está instalado. Puedo instalarlo con `winget install Obsidian.Obsidian` — es gratuito,
> del sitio oficial, y no toca nada de tu Claude Code ni de tus recuerdos actuales. ¿Lo instalo?

Comandos: Windows `winget install Obsidian.Obsidian` · macOS `brew install --cask obsidian` ·
Linux según distribución. Si no hay gestor, dale **obsidian.md/download** y ofrece continuar cuando
lo tenga. **Si dice que no, para acá** — el resto no tiene sentido sin la app.

## 4. La migración — con red, nunca a lo bruto

**Regla dura: copiar, verificar, y recién entonces cambiar la ruta. Jamás mover primero.**

1. **Decide el destino** con la persona: una carpeta dentro de su vault (por ejemplo
   `<vault>/memoria-cortex/`). Si no tenía vault, créala en la ruta que ella elija.
2. **Copia** todos los `.md` de la carpeta actual al destino. **Copia, no muevas.**
3. **Verifica** que el número de archivos y el `MEMORY.md` estén completos en el destino.
4. **Apunta `CORTEX_MEMORY_PATH` al destino, de forma permanente**:
   - Windows: `setx CORTEX_MEMORY_PATH "<ruta>"` (toma efecto en procesos nuevos)
   - macOS/Linux: agrega el `export` a su `~/.zshrc` o `~/.bashrc`
5. **Avísale que el cambio entra en la próxima sesión**, no en esta: la variable la leen los
   procesos nuevos, y el hook de memoria corre al arrancar.
6. **No borres la carpeta original todavía.** Déjala como respaldo y dile que, cuando confirme en
   la próxima sesión que todo carga bien, puede borrarla — o hazlo tú si te lo pide entonces.

## 5. Ofrece traer más cosas a la vault

Ya que está armada, pregúntale si quiere sumar algo más — **sin proponer nada raro ni tocar nada
sin permiso**:

> Ya tienes la vault andando. Si quieres, también puedo traer acá otras cosas tuyas: notas sueltas,
> documentación de un proyecto, apuntes que tengas en archivos de texto. ¿Hay algo que te sirva
> tener junto a tus recuerdos, o lo dejamos así por ahora?

**Solo copia lo que te indique explícitamente**, y siempre copiando, nunca moviendo.

## 6. Cierra diciendo qué cambió y qué sigue

> ✅ Listo. Tus **N recuerdos** están ahora en `<ruta>` y esa carpeta es una vault de Obsidian.
>
> **Qué cambia:** puedes abrir Obsidian y verlos, buscarlos y enlazarlos. **Qué no cambia:** yo
> sigo recordando igual, y sigo guardando ahí lo nuevo.
>
> → En tu próxima sesión voy a leer desde la carpeta nueva. Si algo no cargara, la carpeta vieja
> sigue intacta como respaldo.

## Criterio

- **Nunca instales software ni cambies variables de entorno en silencio.** Se pregunta.
- **Copiar siempre, mover nunca.** Un recuerdo perdido no se recupera.
- **Si algo falla a mitad**, dilo y deja todo apuntando a la carpeta original, que sigue completa.
- Obsidian **no es requisito** de Cortex Edge y no debe presentarse como tal en ningún momento.
