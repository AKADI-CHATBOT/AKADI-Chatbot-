#!/usr/bin/env bash
# RUTA: rules/check_repo_rules.sh
# VERSIÓN: 1.6
# FECHA_ULTIMA_MODIFICACIÓN: 2026‑11‑08
# PROPÓSITO: Validar reglas básicas del repositorio AGF‑v8.0‑MAX
# ARCHIVOS_LECTURA: todos archivos .sh raíz / tools / tmp_edicion + backups carpeta
# ARCHIVOS_MODIFICACIÓN: ninguno
# ESTADO: PERMANENTE

REPO_ROOT="$(pwd)"
TMP_DIR="${REPO_ROOT}/tmp_edicion"
BACKUP_DIR="${REPO_ROOT}/docs/governance/BACKUPS"
echo "============================================="
echo "VALIDADOR DE REGLAS DEL REPOSITORIO ‑ v1.6"
echo "============================================="

# 1
echo -e "\n=== 1. Comprobación: Scripts .sh definitivos en tmp_edicion ==="
DEF_INIT_TMP=""
while IFS= read -r f; do
  if ! grep -qE '#.*ESTADO:[[:space:]]*TEMPORAL|#.*FECHA_LIMITE_REVISIÓN' "$f" 2>/dev/null; then
    DEF_INIT_TMP+="$f"$'\n'
  fi
done < <(find "${TMP_DIR}" -maxdepth 2 -type f -iname "*.sh" 2>/dev/null || true)
if [[ -n "${DEF_INIT_TMP}" ]]; then
  echo "🔴 INCUMPLIMIENTO: Script sin marca TEMPORAL detectado en tmp_edicion:"
  echo "${DEF_INIT_TMP}"
else
  echo "✅ Cumplido: No hay scripts definitivos sin marca en tmp_edicion"
fi

# 2
echo -e "\n=== 2. Comprobación: Cabecera obligatoria scripts permanentes ==="
MISSING_HEADER=""
while IFS= read -r f; do
  [[ -z "$f" ]] && continue
  MISS=""
  grep -q '# RUTA:' "$f" || MISS="${MISS}RUTA "
  grep -q '# VERSIÓN:' "$f" || MISS="${MISS}VERSIÓN "
  grep -q '# FECHA_ULTIMA_MODIFICACIÓN:' "$f" || MISS="${MISS}FECHA "
  grep -q '# PROPÓSITO:' "$f" || MISS="${MISS}PROPÓSITO "
  grep -q '# ESTADO:[[:space:]]*PERMANENTE' "$f" || MISS="${MISS}ESTADO "
  if [[ -n "${MISS}" ]]; then
    MISSING_HEADER+="$f → Faltan campos: ${MISS}"$'\n'
  fi
done < <(find . -type f \( -path "./tools/*.sh" -o -maxdepth 1 -iname "*.sh" \) ! -path "./tmp_edicion/*" 2>/dev/null || true)
if [[ -n "${MISSING_HEADER}" ]]; then
  echo "🔴 INCUMPLIMIENTO: Scripts permanentes con cabecera incompleta:"
  echo "${MISSING_HEADER}"
else
  echo "✅ Cumplido: Todos scripts permanentes tienen cabecera mínima"
fi

# 3
echo -e "\n=== 3. Comprobación: Scripts temporales vencidos ==="
HOY=$(date +%Y‑%m‑%d)
EXPIRED=""
while IFS= read -r f; do
  [[ -z "$f" ]] && continue
  LIM=$(grep -oE '#.*FECHA_LIMITE_REVISIÓN:[[:space:]]*[0‑9]{4}‑[0‑9]{2}‑[0‑9]{2}' "$f" 2>/dev/null | grep -oE '[0‑9]{4}‑[0‑9]{2}‑[0‑9]{2}' || true)
  if [[ -n "${LIM}" && "${LIM}" < "${HOY}" ]]; then
    EXPIRED+="$f (límite: ${LIM})"$'\n'
  fi
done < <(find "${TMP_DIR}" -type f -iname "*.sh" 2>/dev/null || true)
if [[ -n "${EXPIRED}" ]]; then
  echo "⚠️ ADVERTENCIA: Scripts temporales vencidos detectados:"
  echo "${EXPIRED}"
else
  echo "✅ Cumplido: Sin scripts temporales vencidos"
fi

# 4
echo -e "\n=== 4. Comprobación: Líneas rm ‑f sin validación de ruta ==="
RM_RISK=""
while IFS= read -r f; do
  [[ -z "$f" ]] && continue
  while IFS= read -r linea; do
    [[ -z "$linea" ]] && continue
    echo "$linea" | grep -qE '^[[:space:]]*#' && continue
    if echo "$linea" | grep -qE 'rm[[:space:]]+(-[[:alpha:]]*f|‑‑force)'; then
      if ! echo "$linea" | grep -qi 'tmp_edicion'; then
        RM_RISK+="$f → $linea"$'\n'
      fi
    fi
  done < <(grep -nE 'rm[[:space:]]+(-[[:alpha:]]*f|‑‑force)' "$f" 2>/dev/null || true)
done < <(find . -type f -iname "*.sh" 2>/dev/null || true)
if [[ -n "${RM_RISK}" ]]; then
  echo "🔴 RIESGO DETECTADO: rm ‑f fuera de tmp_edicion o sin validación:"
  echo "${RM_RISK}"
else
  echo "✅ Cumplido: No se detectó rm ‑f riesgoso"
fi

# 5
echo -e "\n=== 5. Comprobación: Carpeta docs/governance/BACKUPS existe ==="
if [[ -d "${BACKUP_DIR}" ]]; then
  echo "✅ Cumplido: Carpeta BACKUPS encontrada → ${BACKUP_DIR}"
else
  echo "🔴 INCUMPLIMIENTO: Carpeta BACKUPS NO existe"
  echo "👉 Comando para crearla: mkdir -p ${BACKUP_DIR}"
fi

# 6 Actualizada: Cuenta backups válidos
echo -e "\n=== 6. Comprobación: Formato nombres archivos backup ==="
VALID_BACKUPS=0
BAD_NAME=""
while IFS= read -r archivo; do
  nombre=$(basename "${archivo}")
  if echo "${nombre}" | grep -qE '^BACKUP_[0‑9]{4}‑[0‑9]{2}‑[0‑9]{2}_[0‑9]{2}‑[0‑9]{2}‑[0‑9]{2}\.md$'; then
    ((VALID_BACKUPS++))
  else
    BAD_NAME+="${archivo}"$'\n'
  fi
done < <(find "${BACKUP_DIR}" -maxdepth 1 -type f -iname "*.md" 2>/dev/null || true)

if [[ -z "${BAD_NAME}" ]]; then
  echo "✅ Cumplido: ${VALID_BACKUPS} backup(s) válido(s) detectado(s)"
else
  echo "🔴 INCUMPLIMIENTO: Archivos backup con nombre no estandarizado:"
  echo "${BAD_NAME}"
  echo "👉 Ejemplo nombre válido: BACKUP_2026‑11‑08_17‑49‑00.md"
fi

echo -e "\n=== FIN VALIDACIÓN v1.6 ==="
