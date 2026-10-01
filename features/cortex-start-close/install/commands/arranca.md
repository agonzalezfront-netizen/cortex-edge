---
description: Retoma la sesión — carga dónde quedaste la última vez
---
<!-- Generated from the plugin (plugins/cortex-edge/skills/arranca/SKILL.md); do not edit by hand. / Generado desde el plugin (plugins/cortex-edge/skills/arranca/SKILL.md); no editar a mano. -->

Estás iniciando una sesión de trabajo con el usuario. Ayúdale a retomar sin releer todo:

1. Ubica la carpeta de memoria del usuario: la misma que carga el hook al inicio, donde está `MEMORY.md`.
   Su ruta aparece en el contexto cargado al inicio ("Carpeta de memoria"); si no, es
   `$CORTEX_MEMORY_PATH` o, por defecto, `~/.claude/cortex-memory/`.
2. Busca ahí un archivo `HANDOFF.md`. Si existe, léelo completo, empezando por el bloque **Estado
   vigente al cierre** (qué · por qué · dónde · qué falta · primer paso).
3. **Contrasta antes de narrar.** El handoff es una foto del cierre; desde entonces pueden haber
   cambiado cosas. Comprueba lo barato de comprobar (que los archivos o la carpeta de "Dónde" existan,
   el estado del repositorio si lo hay) y marca lo que no pudiste comprobar como *"según el handoff,
   sin verificar"*. Lo que el handoff dejó en ⚠️ sigue sin verificar hasta que alguien lo compruebe.
4. Resume al usuario en lenguaje claro (sin jerga):
   - **Dónde quedamos:** el estado vigente de la última sesión.
   - **Pendientes:** lo que quedó por hacer, con su contexto, incluido lo que quedó sin verificar.
   - **Próximo paso sugerido:** por dónde conviene seguir hoy (el "primer paso" del handoff, salvo
     que lo que comprobaste diga otra cosa).
5. **¿Ya le mostraste qué puede hacer?** La señal NO es cuánta memoria tiene — alguien puede llevar
   semanas guardando cosas sin que nadie le haya explicado nunca los comandos. La señal es un
   recuerdo marcador: busca en la carpeta de memoria un archivo `cortex-edge-recorrido.md`.

   **Si NO existe** → todavía no vio el recorrido. Dos casos:

   - **Memoria vacía o casi** (recién instaló): hazle el recorrido completo del punto 6, sin preguntar.
   - **Ya tiene recuerdos** (venía usándolo sin que nadie le explicara): **ofrécelo, no lo impongas**.

     > Por cierto, veo que ya vienes usándome pero creo que nunca te mostré todo lo que puedes
     > hacer. ¿Te lo cuento en 30 segundos?
     >
     > **1.** Dale  ·  **2.** Ahora no, vamos al trabajo

   **En cuanto termines el recorrido** (o si dice que no), **guarda el marcador**: un archivo
   `cortex-edge-recorrido.md` de tipo `reference` diciendo que ya se le presentó, con la fecha.
   Así no se lo repites nunca más. Formato en `/memoria`.

   **Si el marcador existe** → salta al punto 7. No repitas la presentación.

6. **El recorrido.** Nombra solo comandos que existan en esta instalación (míralo antes).

   **a) Demuestra primero, explica después.** Si hay algún recuerdo suyo, úsalo como prueba viva:

   > 🌱 **Bienvenido de vuelta.** Fíjate: **recordé que prefieres el español** sin que me lo
   > dijeras. Eso es la memoria, y ya está andando.

   **b) Muéstrale lo que tiene, con ejemplos reales y cuándo lo usaría.** Cuatro como máximo:

   > **Lo que puedes hacer desde ahora:**
   >
   > • **Que recuerde cosas** — dime *"recuerda que prefiero explicaciones antes del código"* y lo
   >   voy a saber siempre. También con `/memoria`.
   > • **Cerrar el día sin perder el hilo** — `/cierra` guarda dónde quedamos; mañana
   >   `/arranca` lo retoma. Es lo que acabas de usar.
   > • **Que te lleve la contra** — si veo un problema en tu plan te lo digo, no te doy la razón
   >   por defecto. No tienes que pedirlo.
   > • **Revisar que todo esté bien** — `/setup`, por si algún día algo falla.

   **c) Cuéntale dónde vive su memoria, y la opción de Obsidian.** En dos líneas:

   > Todo esto se guarda como **archivos de texto** en una carpeta tuya — nada encerrado en una
   > base de datos, puedes abrirlos con el Bloc de notas. Y si quieres **verlos como notas**
   > (buscarlos, enlazarlos, leerlos desde el teléfono), puedo conectarlos con **Obsidian**, que es
   > gratis y opcional: `/obsidian` y lo dejo andando. Funciona igual con o sin él.

   **d) Recién ahora, el catálogo.**

   > **¿Le sumamos capacidades?** Hay un catálogo de skills — depuración rigurosa, redactar
   > documentos, investigación, diseño, video. Los uso solo cuando la tarea lo pide.
   >
   > **1.** Muéstrame el catálogo  ·  **2.** Después — empecemos a trabajar 🌱

   Si elige **2**, pregúntale en qué quiere trabajar. Si elige **1**, sigue con
   `/skills`. **Nunca insistas.**

7. **Si no hay `HANDOFF.md`** pero ya conoce el producto: dilo en una línea, recuérdale que
   `/cierra` deja el resumen para la próxima, y pregúntale en qué trabaja hoy.

No inventes estado: si el HANDOFF no menciona algo, no lo asumas. La memoria (MEMORY.md) ya se cargó
sola al inicio — este comando la complementa con el "dónde quedamos" del último cierre. (En inglés:
`/start`.)

## Arranque liviano: un script, un informe corto

Si la persona tiene chequeos que corre al empezar (tests, servicios, el estado de algo), no los corras
como diez comandos sueltos que vuelcan bitácoras en el contexto: cada línea que entra se relee en
**todos** los mensajes siguientes. La práctica que rinde es **un solo script** que corre todos los
chequeos y devuelve un informe compacto, una línea por chequeo con su veredicto (`OK` · `AVISO` ·
`FALLA` y, si falla, el porqué en una frase). Tú lees veredictos, no bitácoras, y abres el detalle solo
de lo que falló. Si ves que la persona repite el mismo ritual de arranque a mano, ofrécele armar ese
script.

**Sesión nueva tras un handoff es lo normal**, no una pérdida: el handoff es el puente. Una sesión que
ya arrastra un contexto enorme cuesta más en cada mensaje que una nueva que lee el handoff.

## Principio de UX

**Ubicación y rumbo, siempre.** Cada mensaje abre diciendo en qué parte del recorrido está la
persona y cierra diciendo qué sigue. Si llega desde `/setup`, viene del paso 4 — no la
dejes sin saber dónde está parada.

**El contexto va donde está la decisión.** Si preguntas algo, primero da lo necesario para poder
responder — ejemplos concretos, no una pregunta abierta al vacío. Al terminar, di **qué cambió y
cuál es el siguiente paso**, no solo que terminaste.

**Si la mandas a una pantalla que no es tuya** (el explorador de plugins de Claude Code, la web de
un skill), **avísale antes**: qué va a ver, que eso no es Cortex Edge, y qué tiene que hacer ahí.
