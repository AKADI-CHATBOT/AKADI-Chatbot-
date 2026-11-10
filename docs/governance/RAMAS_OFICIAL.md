# RAMAS OFICIALES AGF - 2026-11-09

## Carpeta única de trabajo
AGF-v8.0-MAX-Identity-Preservation-Engine

## Rama oficial
main - estable / oficial
Commit: d289c02
Kernel: d1be9264fbd9de38355d02b6ec03a0162bed0f30a1975f15fee0bc9459af6a7c

## Rama experimental
mejora-umbrales-failclosed - experimental, no mezclar hasta aprobación HIL
Commit: c140621
Kernel: [STRIPPED 72 bytes]: PROTO-COM v3.0, UMBRALES_MINIMOS fail-closed, rules/check_repo_rules.sh v1.6

## Reglas
1. main = oficial, no se tocan experimentos ahí.
2. mejora = experimental, no se mezcla con main hasta que HIL apruebe.
3. OUT único se genera desde main con MAPEO_OUT_CORREGIDO, con manifiesto + peso.
4. Privado nunca va a Download ni a GitHub público.
5. Regla de decisiones: 5 propuestas, HIL asigna peso 1-10, se escoge mayor peso final.

ESTADO: PERMANENTE
