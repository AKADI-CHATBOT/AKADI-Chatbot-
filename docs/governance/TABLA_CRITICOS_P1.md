# Tabla concisa – 5 críticos prioritarios (P1)
| # | Descripción crítico | Estado actual | Criterio resuelto | Fecha resolución |
|---|---|---|---|---|
| 1 | API fail‑open: ignora exit‑code motor, usa JSON anterior → HTTP 200 inválido | RESUELTO | Motor exit 0 obligatorio antes de leer JSON; motor caído → 503 y no cargar archivos previos | 2026‑11‑08 |
| 2 | MAXCAP 500 vs 200 desalineado + cálculo longitud incluye nombres archivos | PENDIENTE | Mismo valor en Boot / Kernel / código / tests / README; longitud solo cuenta texto de entrada | 2026‑11‑08 |
| 3 | Motor genera hash 16 caracteres rechazado por validador & Boot | PENDIENTE | Hash generado por motor coincide con regla de longitud definida en Boot y verificador | 2026‑11‑08 |
| 4 | Hash‑chain roto: ledger vs verificador usan fuentes distintas para hash | PENDIENTE | Ledger y verificador calculan hash sobre el mismo contenido del evento y pasan todos los tests de integridad | 2026‑11‑08 |
| 5 | README cita archivo ausente + test cognitivo informa 100 % cuando faltan archivos | PENDIENTE | Quitar referencia a archivo inexistente; test reporta éxito solo cuando todos los casos se ejecutan realmente | 2026‑11‑08 |
