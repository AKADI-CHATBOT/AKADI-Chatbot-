import os, sys, subprocess
print("VERIFICAR ANTES DE CAMBIAR")
for ruta in ["docs/governance/CHATBOT_BOOT_PROMPT.md", "docs/governance/REGLA_RAIZ.md", "docs/governance/REGLAS_GENERALES_INALTERABLES.md", "tools/verificar_boot_motor.py"]:
    if not os.path.exists(ruta):
        print(f"BLOCKED - NO ENCONTRADO: {ruta}")
        sys.exit(1)
    print(f"OK - existe: {ruta}")
res = subprocess.run([sys.executable, "tools/verificar_boot_motor.py", "termux_sealed/actas/ACTA_20261106T213419_f891fee2.json"], capture_output=True, text=True)
print(res.stdout.strip())
if res.returncode != 0:
    print("BLOCKED - acta real no pasa validador")
    sys.exit(1)
print("VERIFICADO - se realiza, no se pregunta")
