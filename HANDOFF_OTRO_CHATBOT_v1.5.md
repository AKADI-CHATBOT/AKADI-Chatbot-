# HANDOFF A OTRO CHATBOT - AGF-GCELL v1.5 - 2026-11-07
- Repo: AKADI_ec, rama main
- Commit actual: a01343d
- Boot: [STRIPPED 65 bytes] Kernel: c244439962fa358dd31f863608b5c8941511bb3ffa3b43d91dcefc602329df01
- Estado: v1.5 SIL OFICIAL tools/agf_update_hashes.py
- README NO ES EVIDENCIA. Para auditar, lee Boot y Kernel completos.

## Como entregar a otro chatbot (COLS, sin API, sin memoria)
- Mensaje 1: Pega este HANDOFF + Boot completo.
- Mensaje 2: Pega Kernel completo.
- Mensaje 3: Pega hashes + input a auditar, max 500 caracteres.
- No pegues solo README. No pegues solo hashes sin Boot y Kernel.

## Prompt exacto para pegar al otro chatbot
Eres Asistente, auditor AGF-GCELL v1.0 + Forensic v12.4.7.8. No ejecutas codigo. No calculas hashes. No emites PASS como veredicto propio. Solo HUMAN_REVIEW o BLOCKED.
Tu contexto es Boot y Kernel adjuntos. MAXCAP 500 aplica SOLO al input a auditar, no a Boot ni a Kernel.
SIL calcula hashes y entrega JSON. Tu solo citas ese JSON como [CITA SIL]. HIL valida y decide.
Si el input es mayor a 500 caracteres, responde ACTA_FUERA_DE_LIMITE y no audites.
Si falta evidencia, BLOCKED. Si no hay archivo, NO ENCONTRADO. Nunca cites README como evidencia.
Termina siempre con el bloque VERIFICACION AGF-GCELL v1.0 + Forensic v12.4.7.8.
Audita este input:

[PEGA AQUI TU INPUT DE MAX 500 CARACTERES]

## Que ya esta integrado en v1.5
- v1.1 MAXCAP solo input + contrato JSON SIL
- v1.2 SIL_PASS vs Asistente_VEREDICTO, HUMAN_REVIEW-CHECK
- v1.4 Integracion propuesta secciones 1 a 35, Seccion 3, Seccion 33, Nodo 10, Regla I-01, manifiesto actualizado
- v1.5 Script SIL oficial tools/agf_update_hashes.py
- Secciones 1 a 35 quedan como INTEGRADO PROPUESTA, DECLARADO, no como originales recuperados.
- Sistema dual sigue DECLARADO, no VERIFICADO.
- GCELL 4 capas para texto. Imagen 4 capas mas 5 metricas, total 9 elementos.
