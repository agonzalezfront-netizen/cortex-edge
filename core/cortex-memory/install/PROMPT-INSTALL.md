# Install — cortex-memory / Instalar — cortex-memory

**EN.** Hi Claude. Install persistent memory for this person. Reply in their language. Replace `<USER>` with
their Windows user and `<VAULT>` with their notes/Obsidian folder.

**ES.** Hola Claude. Instálale memoria persistente a esta persona. Responde en su idioma. Reemplaza `<USER>`
por su usuario de Windows y `<VAULT>` por su carpeta de notas/Obsidian.

## Steps / Pasos
1. **Memory folder / Carpeta de memoria.** Copy `memoria-semilla/` into the person's notes folder and rename
   it to `memoria` → `C:\Users\<USER>\Obsidian\<VAULT>\memoria\` (with `MEMORY.md` + `ejemplo.md`).
   Copia `memoria-semilla/` dentro de sus notas y renómbrala a `memoria`.
2. **Hook.** Copy `hooks/cargar-memoria.py` to `C:\Users\<USER>\.claude\hooks\cargar-memoria.py` (create the
   folder if missing). Then edit its `MEMORY_DIR` line with the real path from step 1.
   Copia el hook y edita su línea `MEMORY_DIR` con la ruta real del paso 1.
3. **Memory protocol / Protocolo de memoria.** Append `CLAUDE-memoria.md` (the person's language section) to
   `C:\Users\<USER>\.claude\CLAUDE.md` (create it if missing). Fix the memory path mentioned inside.
   Agrega `CLAUDE-memoria.md` (sección del idioma) al `CLAUDE.md`. Corrige la ruta de memoria que aparece adentro.
4. **Activate the hook / Activa el hook.** Add the `SessionStart` block from `settings-snippet.json` to
   `C:\Users\<USER>\.claude\settings.json` (merge into existing `"hooks"` if present, don't replace it).
   Agrega el bloque `SessionStart` de `settings-snippet.json` a `settings.json` (fusiona, no reemplaces).

## Test / Prueba
Restart Claude Code. At the start you should see a "🧠 YOUR MEMORY / TU MEMORIA" block. If it shows, it works.
Reinicia Claude Code. Al inicio deberías ver el bloque "🧠 TU MEMORIA". Si aparece, funciona.

## Notes / Notas
The hook is **fail-silent**: if something breaks it won't crash Claude, it just won't load memory that time.
El hook es **fail-silent**: si algo falla no rompe tu Claude, solo no carga memoria esa vez.
