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
- Boot: ba84b105642cfae1aced79faf881fcff40af0b853e4532c39753f361869474f6
- Kernel: 15a750239a2ec2c37493f20bdfba668b223faaa5a8bd8138f077259a343b23a4

No es sistema verificado completo. Es trabajo en progreso con pruebas locales medidas.
