# Changelog

Qué cambió en cada versión, en lenguaje simple. / What changed in each version, in plain language.

Casi todo lo de la 1.3 en adelante salió de **mirar a una persona real instalarlo** — no de
planificación. Los hallazgos están marcados con 👤.
Almost everything from 1.3 on came from **watching a real person install it**, not from planning.
Those findings are marked 👤.

---

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
