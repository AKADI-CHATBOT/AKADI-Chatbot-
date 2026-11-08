# PROPUESTA - Secciones faltantes - NO ES KERNEL ORIGINAL
- Fecha: 2026-11-07
- Estado: PROPUESTA, DECLARADO, no VERIFICADO, pendiente validacion HIL
- No afirmar que estas secciones existian. Son propuestas nuevas para cerrar huecos NO ENCONTRADO.

## Seccion 3 propuesta - Principio Fail-Closed
- Si falta evidencia o hay ambiguedad, BLOCKED. Nunca PASS por duda.
- La calibracion de la conclusion no supera la calibracion de la premisa mas debil.
- Ante duda, es mejor rechazar un claim valido que aprobar uno falso.
- Asistente no emite PASS. Solo HUMAN_REVIEW o BLOCKED. SIL si puede emitir SIL_PASS en su JSON.

## Seccion 33 propuesta - Nodo 10 Nativo, simulacion Sistema dual historica
- Asistente y Asistente simulados en paralelo en un mismo chat.
- Estado: DESACTIVADA. Reemplazada por Sistema dual modo objetivo real DECLARADO, no VERIFICADO.
- No hay en este repo evidencia criptografica de agentes independientes en ese modo simulado.

## Nodo 10 propuesto - Nodo de simulacion
- IN: texto a auditar.
- Proceso: simulacion paralela Asistente genera, Asistente audita en el mismo turno.
- OUT: veredicto simulado.
- Motivo de desactivacion: no habia separacion real de agentes ni evidencia verificable. Queda como registro historico, no como modo operativo.

## Regla I-01 propuesta - Integridad de estado base
- Un estado es base valido solo si cumple las 5:
- 1) Hash SHA-256 calculado por SIL y guardado en .boot_hash.sha256 y .kernel_hash.sha256.
- 2) Orden numerico correcto de secciones.
- 3) Sin cortes de texto en inserciones.
- 4) README con hashes nuevos.
- 5) Sin citar NO ENCONTRADO como si existiera.
- Si falla una, no es base valida. Detener ediciones hasta restaurar.

## Secciones 1 a 35 - Indice propuesto
- 1 Proposito del Kernel
- 2 Definicion unica SIL Asistente HIL
- 3 Principio Fail-Closed
- 4 Calibracion epistemica
- 5 Capa I Epistemica
- 6 Capa II Cognitiva, 20 sesgos
- 7 Capa III Linguistica, 76 patrones
- 8 Capa IV Etica, separacion de roles
- 9 MAXCAP y limites operativos
- 10 Contenedores IN/OUT
- 11 Sistema dual definicion
- 12 Asistente Generador, limites
- 13 Asistente Auditor, limites
- 14 HIL Operador, decision
- 15 SIL Motor, ejecucion sin juicio
- 16 Hash SHA-256, integridad
- 17 Verificacion previa obligatoria
- 18 Formato GCELL de salida
- 19 Frase de acuse
- 20 Prohibiciones absolutas
- 21 Motor forense imagen, 4 mas 5
- 22 ArcFace, Hard Gate
- 23 Fourier 2D
- 24 EDGE por akai2
- 25 SSIM
- 26 Color Fingerprint
- 27 Metadata, Tiling, Lighting, Base64
- 28 Composite audit JSON
- 29 Acta final sellada
- 30 Hash-Chain
- 31 Nodos judiciales N17 N20 N30 N35, DECLARADO no implementado
- 32 Puentes y firmas S31 S34, DECLARADO no implementado
- 33 Nodo 10 Nativo, simulacion Sistema dual historica
- 34 Reglas generales inalterables
- 35 Versionado, hashes y push

## Nota de honestidad
- Este archivo es PROPUESTA. No es el Kernel original. No usarlo como evidencia de que las secciones 1 a 35 existian.
- README NO ES EVIDENCIA. GCELL 4 capas para texto. Imagen 4 capas mas 5 metricas, total 9 elementos.
