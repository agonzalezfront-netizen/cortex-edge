# Changelog

Qué cambió en cada versión, en lenguaje simple. / What changed in each version, in plain language.

Casi todo lo de la 1.3 en adelante salió de **mirar a una persona real instalarlo** — no de
planificación. Los hallazgos están marcados con 👤.
Almost everything from 1.3 on came from **watching a real person install it**, not from planning.
Those findings are marked 👤.

---

## 1.17.0 — 2026-10-01 · continuidad y rigor / continuity and rigor
- **El handoff abre con el estado vigente.** `cierra` deja arriba un bloque fijo (qué · por qué ·
  dónde · qué falta · primer paso) y una sección **verificado / sin verificar**: nada va como hecho sin
  evidencia. `arranca` lee ese bloque primero y **lo contrasta con la fuente** antes de contarlo como
  estado actual; lo que no pudo comprobar lo dice ("según el handoff, sin verificar").
- **Cerrar apaga lo que quedó corriendo.** Procesos en segundo plano, monitores, tareas programadas o
  en bucle que la sesión lanzó: si ya no hacen falta, se detienen (cada uno puede despertar al modelo y
  gastar tokens después del cierre). Lo que ya existía antes no se toca.
- **Cada lección, a `feedback`.** Si hubo que corregir o recordarle algo a Claude, o un error costó
  una vuelta, se guarda con **Por qué** y **Cómo aplicarlo**, y si puede repetirse se ofrece una guarda
  que no dependa de acordarse (un test, un chequeo).
- **Vigía de la sesión** (hook nuevo, `vigia-sesion.py`). Habla solo con motivo: si pasan 20 mensajes
  sin guardar nada en la memoria, recuerda guardar lo importante **ahora**, no al cierre; y si el
  contexto de la sesión pasa el **tope de 500 mil tokens**, avisa que en el próximo cierre natural
  conviene cerrar con handoff y seguir en una sesión nueva. Nunca esperar la compactación automática.
  Ambos se ajustan o se apagan en `cortex-edge.json` (`recordatorio_guardado`, `tope_contexto`).
- **Dos reglas nuevas en la postura del núcleo:** *honestidad sobre lo no verificado* (decir "listo"
  solo con evidencia) y *pensar vs. ejecutar* (la sesión principal piensa, decide y verifica; lo
  mecánico con juez objetivo va a un script o a un subagente con modelo menor, en este orden: script
  determinista > Haiku > Sonnet > Opus > Fable).
- **Nuevo `/cortex-edge:tokens`** — dónde se van tus tokens, medido desde tus transcripts locales (los
  de subagentes incluidos): por día, modelo, qué despertó al modelo y sesión, con el contexto que se
  relee en cada mensaje. Solo números; nunca muestra el contenido de los mensajes ni envía nada.
- **Nuevo `/cortex-edge:rigor`** — evidencia antes de "listo": matriz requisito → evidencia,
  inventario completo de lo anómalo, lo medido separado de lo supuesto.
- **Arranque liviano**, documentado en `arranca`: los chequeos de inicio van en un solo script que
  devuelve un veredicto por línea (OK · AVISO · FALLA); Claude lee veredictos, no bitácoras.
- La vía manual (`features/`) ahora se **genera desde el plugin** al publicar: ya no puede quedar
  atrasada respecto de `arranca`, `cierra`, `start` y `close`.

**Anticipo de la 1.18 — memoria que se ordena.** Una memoria grande crece en islas. Esta es una real,
de unas 4.500 notas, en el grafo de Obsidian:

| Antes (30-09) | Durante (01-10) |
|---|---|
| ![Antes: islas y notas sueltas](https://raw.githubusercontent.com/agonzalezfront-netizen/cortex-edge/master/plugins/cortex-edge/docs/grafo-antes-2026-09-30.png) | ![Durante: coloreado por tema, islas conectándose](https://raw.githubusercontent.com/agonzalezfront-netizen/cortex-edge/master/plugins/cortex-edge/docs/grafo-durante-2026-10-01.png) |

**Después**, medido con los datos del propio Obsidian: **4.466 notas, 0 huérfanas, 4.155 de 4.156
adjuntos enlazados**. El método se está preparando para la 1.18.

*In English:* the handoff now opens with a fixed current-state block plus verified / not-verified
lists, and `start` checks it against the source before narrating it; closing stops what the session
left running; every lesson becomes `feedback`; a new session watcher reminds Claude to save memory
and flags sessions over a 500k-token context ceiling (hand over at the next natural stopping point,
never wait for automatic compaction); the core stance adds *honesty about what isn't verified* and
*think vs. execute*; new `/cortex-edge:tokens` and `/cortex-edge:rigor`. Preview of 1.18: memory that
tidies itself (graph before and during above).

## 1.16.0 — 2026-09-30 · el núcleo funciona de verdad / the core really works
- **La postura crítica y el protocolo de memoria ahora llegan al modelo en la instalación por
  plugin.** Antes el hook solo inyectaba `MEMORY.md`: la postura y el protocolo (qué guardar,
  tipos `user`/`feedback`/`project`/`reference`, verificar antes de dar algo por novedad, "si te
  tienen que recordar algo, es un bug") solo existían en la instalación manual. Un nuevo hook,
  `cargar-nucleo.py`, los lee de `POSTURA-CRITICA.md` y `PROTOCOLO-MEMORIA.md` (una sola fuente)
  y los carga al inicio de cada sesión, en el idioma de la persona si se conoce.
- **Control de tamaño del índice.** Claude Code corta lo que inyecta cada hook a 10 000 caracteres,
  y desde adentro un índice truncado no se nota. El hook de memoria avisa al pasar de ~8 000
  caracteres, marca las líneas de más de 190, y si aun así no cabe corta por líneas completas y
  **dice** cuántas quedaron fuera. La regla de 190 caracteres queda documentada en `memoria`.
- **Fecha y hora en cada mensaje** (hook `UserPromptSubmit`): día de la semana, fecha ISO, hora y
  zona. Activo por defecto; se apaga con `{"reloj": false}` en `cortex-edge.json`, dentro de la
  carpeta de memoria.
- **`setup` ya no promete lo que no verificó.** Corre los hooks y revisa que la salida contenga la
  postura y la memoria antes de decir que algo quedó activo. Y corrige un error: tras instalar o
  actualizar **hay que reiniciar Claude Code**; `/reload-plugins` no basta para los hooks.
- `start` y `close` quedan enteramente en inglés; `arranca` y `cierra`, en español.
- Licencia coherente en todo el paquete: PolyForm Noncommercial 1.0.0 (manifiesto y ambos READMEs).
- Tests de los hooks (`hooks/test_hooks.py`).

## 1.15.0
- **Prueba de manejo al instalar skills.** La primera vez que instalas algo del catálogo, se te
  ofrece probarlo ahí mismo con **un caso concreto de lo tuyo** — no una explicación. Puedes hacer
  un recorrido por todos o probar uno solo, y al final se cierra con lo que más ahorra tiempo:
  **no hace falta llamar a los skills con comandos**, basta con decir lo que necesitas.

## 1.14.0
- **Nuevo `/cortex-edge:obsidian`** — conecta tu carpeta de memoria con Obsidian para verla como
  notas: buscar, enlazar, ver el mapa, leerla desde el teléfono. Si no lo tienes, se ofrece a
  instalarlo; migra tus recuerdos **copiando, nunca moviendo**, verifica que llegaron completos y
  deja la carpeta original de respaldo. **Obsidian sigue siendo opcional**: la memoria funciona
  igual sin él.
- El recorrido de la primera sesión ahora cuenta dónde viven tus recuerdos y menciona esta opción.

## 1.13.0
- 👤 **El recorrido ya no se decide por cuánta memoria tienes.** Antes se usaba "tiene pocos
  recuerdos" como señal de "es nuevo", y alguien que llevaba semanas usándolo sin que nadie le
  explicara los comandos nunca lo veía. Ahora se guarda un marcador: si nunca se te presentó, se
  te ofrece — y si ya lo viste, no se repite nunca más.

## 1.12.1
- 👤 El CHANGELOG se quedaba atrás respecto a la versión publicada. Ahora `publicar.py` **no deja
  publicar** si la versión del manifiesto no está documentada acá.

## 1.12.0
- 👤 **Visita guiada en la primera sesión.** El onboarding ya no termina al instalar: `setup` te
  invita a abrir una sesión nueva y ahí `/cortex-edge:arranca` detecta que es tu primera vez, te
  demuestra la memoria funcionando (recuerda tu idioma), te muestra qué puedes hacer con ejemplos
  reales, y **recién entonces** te ofrece el catálogo.
- `setup` ya no ofrece el catálogo: apilar capacidades antes de entender lo que tienes es construir
  sin cimientos.

## 1.11.3
- Se agrega este CHANGELOG, enlazado desde ambos READMEs.

## 1.11.2
- 👤 El catálogo ahora dice **qué skills** hay en cada grupo (superpowers, docx, dataviz…), no solo
  la categoría. Antes había que abrir los cinco grupos para saber qué contenían.

## 1.11.1
- 👤 Los nombres de archivo internos del catálogo ya no se muestran a la persona.

## 1.11.0
- 👤 **Distinción explícita** entre las 7 skills propias de Cortex Edge (vienen dentro del plugin,
  no se instalan aparte) y las del catálogo (de terceros, opcionales). Causaba confusión real.

## 1.10.1
- 👤 **Corregido un error de documentación**: tras actualizar de versión **hay que reiniciar Claude
  Code**; `/reload-plugins` no siempre basta. El CLI ya lo advertía y lo habíamos minimizado.
- Se explica cómo saber qué versión está *realmente* cargada en la sesión (disco y sesión pueden
  discrepar sin aviso).

## 1.10.0
- `/cortex-edge:setup` ahora **reporta tu versión y te avisa si hay una más nueva**, ofreciendo
  actualizar. Antes no había forma de enterarse de que existía una mejor.

## 1.9.1
- 👤 **Corregidas las instrucciones de actualización**: el comando fallaba si el plugin estaba
  instalado con alcance de proyecto. Ahora se documenta `--scope project`.
- La vía recomendada pasa a ser **pedírselo a tu propio Claude en palabras** — detecta el alcance solo.

## 1.9.0
- El catálogo **verifica qué tienes instalado antes de recomendar**, en vez de ofrecerte algo que
  ya usas.

## 1.8.0
- 👤 **Instalación guiada de 4 pasos.** Cada mensaje dice en qué paso vas y qué sigue. El recorrido
  se anuncia completo al empezar.
- Si el flujo te manda a una pantalla que no es de Cortex Edge, ahora te avisa antes.

## 1.7.1
- 👤 Se aclara que el explorador que abre `/plugin` es **el gestor de Claude Code**, no nuestro
  catálogo — y qué hacer ahí.
- Documentada la actualización desde terminal, sin abrir ventanas.

## 1.7.0
- Cierre celebratorio al terminar, con invitación a potenciarlo y **salida siempre visible**
  ("lo dejo para después"), sin insistir.

## 1.6.0
- `/cortex-edge:setup` **pregunta primero en qué idioma guiarte**, y guarda la elección como tu
  **primer recuerdo** — así ves la memoria funcionando en el primer minuto.

## 1.5.0
- 👤 `/cortex-edge:memoria` ya no pregunta al vacío: explica para qué sirve y da ejemplos concretos
  antes de preguntar. Al guardar, dice **qué cambia**, no solo que guardó.

## 1.4.0
- 👤 El setup deja de ser una línea seca: explica **qué queda activo** y **qué hacer ahora**.

## 1.3.2
- 👤 Se aclara que `0 skills` en `/reload-plugins` **es normal** (ese contador solo mira
  `commands/`). Parecía un error de instalación y no lo era.

## 1.3.0
- Nuevo `/cortex-edge:setup`: verifica Python, git y la carpeta de memoria, y ofrece instalar lo
  que falte **pidiendo permiso**. Cierra un hueco real: si falta Python, el hook de memoria no
  puede avisar que falta Python, porque el hook *es* Python.

## 1.2.0
- **Requisitos declarados** (Claude Code, Python 3, git) y sección de **crédito** a lo que sostiene
  el proyecto: Claude Code, los skills de la comunidad, el ecosistema MCP, Obsidian, Markdown y git.

## 1.1.0
- `/cortex-edge:skills` completo: catálogo curado en 5 grupos con divulgación progresiva.

## 1.0.0
- Primera versión como **plugin nativo de Claude Code**. Instalación en dos comandos.
- Núcleo: memoria persistente entre sesiones + postura crítica.
- Continuidad: `/arranca` y `/cierra` (`/start`, `/close`).
- Hook de memoria **cero configuración**: crea su carpeta sola, o usa `CORTEX_MEMORY_PATH`.
