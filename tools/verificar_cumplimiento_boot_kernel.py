import sys, pathlib, hashlib
print("VERIFICAR CUMPLIMIENTO BOOT Y KERNEL - NO PROMESA")
# Requisitos que debe tener la respuesta del chatbot
req = ["MAXCAP 500", "GCELL 4", "4 capas mas 5 metricas", "README NO ES EVIDENCIA", "NO ENCONTRADO", "BLOCKED"]
# Hashes reales que debe citar
boot_h = hashlib.sha256(pathlib.Path("docs/governance/CHATBOT_BOOT_PROMPT.md").read_bytes()).hexdigest()
kernel_h = hashlib.sha256(pathlib.Path("docs/governance/AGF_CHAT_KERNEL_v0.9.8_FULL.md").read_bytes()).hexdigest()
print(f"Hash boot real: {boot_h[:16]}...{boot_h[-8:]}")
print(f"Hash kernel real: {kernel_h[:16]}...{kernel_h[-8:]}")
if len(sys.argv) < 2:
    print("Uso: python3 tools/verificar_cumplimiento_boot_kernel.py <archivo_respuesta_chatbot.txt>")
    print("Si no hay archivo, no se puede verificar cumplimiento -> BLOCKED")
    sys.exit(1)
resp = pathlib.Path(sys.argv[1]).read_text(errors="ignore")
faltan = []
for r in req:
    if r not in resp:
        faltan.append(r)
if boot_h[:16] not in resp:
    faltan.append("hash boot")
if kernel_h[:16] not in resp:
    faltan.append("hash kernel")
if faltan:
    print(f"BLOCKED - falta cumplimiento: {', '.join(faltan)}")
else:
    print("PASS-CHECK - cumple boot y kernel, tiene todos los requisitos y hashes")
