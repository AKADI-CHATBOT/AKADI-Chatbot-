# HANDOFF OTRO CHATBOT v1.6
# FECHA: 2026-11-09
# RAMA: mejora-umbrales-failclosed
# COMMIT BASE: 158dd32 - Cerrar C4 auditor v1.1
# ESTADO: PRIVADO - USO INTERNO - SIN PRECIO NI LICENCIA COMERCIAL

## PROTOCOLO 3+1 MENSAJES
1. HANDOFF + Boot completo
2. Kernel completo + MAPEO_KERNEL_AGF.txt
3. Hashes + Input <=500 chars + C1-C5
4. PROTO-COM + modulos + auditor v1.1

## CADENA C1-C5 APROBADO
- C1 CIR-001 APROBADO - 5 propuestas claridad boot prompt - Longitud_IN 125
- C2 CIR-002 APROBADO - modulo normalizacion UTF-8 Python - Longitud_IN 126
- C3 CIR-003 APROBADO - modulo normalizacion UTF-8 C con GCC - Longitud_IN 129
- C4 CIR-004 APROBADO - auditor v1.1 integra Python, C y PROTO-COM - Longitud_IN 125
- C5 CIR-005 APROBADO - HANDOFF v1.6 con C1-C4 y estado comercial privado - Longitud_IN 146

## MODULOS
- tools/normalizacion_utf8.py v1.0 - NFC, BOM, CRLF, guion raro U+2011 od 342 200 221 vs 055, entropia Shannon
- tools/normalizacion_utf8.c v1.0 - GCC, mismo test, entropia por bytes
- tools/auditor_v1_1.py v1.1 - valida Hash, Longitud, Desconstruccion, guion raro, deduplicacion

## PROTO-COM v3.0
- docs/governance/PROTO-COM/diccionario.json - mango, pedo, aguacate-palta
- docs/governance/PROTO-COM/formato-instruccion.md - 5 datos obligatorios
- docs/governance/PROTO-COM/reglas.md - 10 reglas, 5 lenguaje + 5 instrucciones
- docs/governance/RAMAS_OFICIAL.md - main oficial, mejora experimental, peso sugerido = peso final automatico

## ESTADO COMERCIAL
- Valor comercial: NO DECLARADO OFICIALMENTE
- Estado: PRIVADO / USO INTERNO
- Precio: NO HAY
- Licencia comercial: NO HAY
- Venta / distribucion publica: NO AUTORIZADA
- Uso comercial: requiere autorizacion explicita HIL/AKADI por escrito
- Autorizacion ejecucion: PENDIENTE VALIDACION OPERADOR (HIL)

## NO ENTREGAR
- PAQUETE_COMPLETO*.md, .env, termux_sealed/, *.jpg/png/webp con rostros, *.onnx, *.tflite, .git/filter-repo/, *_ARCHIVO_*, PRIVADO_ARCHIVO
