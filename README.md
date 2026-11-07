# AKADI — AGF-GCELL
En progreso.
Work in progress.

README NO ES EVIDENCIA. Para auditar, lee boot y kernel completos y cumple lo que dicen. Si citas README como fuente, es BLOCKED.

## Lo que si paso de verdad en pruebas locales
- Prueba cognitiva: 6 de 6, 100 por ciento real en esos 6 casos. Acepta acta real, rechaza acta test, rechaza composite con hash recortado, rechaza archivo no existe, boot exige motor con hash completo, reglas generales en boot y kernel.
- Prueba MAXCAP 500: 350 pasa, 600 bloquea.
- Prueba README NO ES EVIDENCIA: boot y kernel tienen la regla, README solo En progreso, respuesta que solo cita README queda BLOCKED.
- Prueba cumplimiento: respuesta que cumple con hashes y requisitos da PASS-CHECK, respuesta que no cumple da BLOCKED.
- Acta real que pasa validador: termux_sealed/actas/ACTA_20261106T213419_f891fee2.json, con 2 hashes completos de 64.
- Acta test: NO ENCONTRADO en termux_sealed/actas/ACTA_20261106T185544_672ca6d5.json, por eso queda BLOCKED por NO ENCONTRADO. No se afirma que tenga hashes abc123 ni que este marcada TEST dentro, porque el archivo no existe para verificarlo.

## Reglas reales
- GCELL: 4 capas para texto, Epistemica, Cognitiva, Linguistica, Etica.
- Imagen: 4 capas mas 5 metricas, total 9 elementos, no 9 capas separadas.
- MAXCAP: 500 caracteres.
- Motor: tools/agf_full_9_layers.py, audit JSON requerido, hash completo de 64.

## Hashes para verificar que leiste boot y kernel
- Boot: 34fa8b77ff6e67771a3e5a998d859069409cc0a8094b5e908458bfe597ebdea4
- Kernel: 75396906f60bbc80d7e432891ca60b113ee8cee827ffe94095afd80f9d0c3906

No es sistema verificado completo. Es trabajo en progreso con pruebas locales medidas.
