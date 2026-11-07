import subprocess, sys, json, os
print("PRUEBA COGNITIVA REAL - NO PROMESA")
pasados = 0
totales = 0
def probar(nombre, debe_pasar, ruta):
    global pasados, totales
    totales += 1
    res = subprocess.run([sys.executable, "tools/verificar_boot_motor.py", ruta], capture_output=True, text=True)
    paso = (res.returncode == 0) == debe_pasar
    print(f"{'PASS' if paso else 'FAIL'} - {nombre}: {res.stdout.strip()}")
    if paso:
        pasados += 1
# 1. Debe aceptar acta real con hash completo
probar("1 acepta acta real", True, "termux_sealed/actas/ACTA_20261106T213419_f891fee2.json")
# 2. Debe rechazar acta test con abc123
probar("2 rechaza acta test", False, "termux_sealed/actas_test/ACTA_20261106T185544_672ca6d5.json")
# 3. Debe rechazar composite con hash recortado
probar("3 rechaza composite hash recortado", False, "termux_sealed/composite_audit.json")
# 4. Debe rechazar archivo que no existe
probar("4 rechaza archivo no existe", False, "termux_sealed/actas/ACTA_NO_EXISTE.json")
# 5. Debe verificar que boot exige motor
totales += 1
with open("docs/governance/CHATBOT_BOOT_PROMPT.md") as f:
    txt = f.read()
if "BOOT EXIGE MOTOR" in txt and "hash completo de 64" in txt:
    print("PASS - 5 boot exige motor con hash completo")
    pasados += 1
else:
    print("FAIL - 5 boot no exige motor")
# 6. Debe verificar que reglas generales estan en boot y kernel
totales += 1
with open("docs/governance/AGF_CHAT_KERNEL_v0.9.8_FULL.md") as f:
    ktxt = f.read()
if "REGLAS GENERALES INALTERABLES" in txt and "REGLAS GENERALES INALTERABLES" in ktxt:
    print("PASS - 6 reglas generales en boot y kernel")
    pasados += 1
else:
    print("FAIL - 6 reglas generales faltan")
print(f"RESULTADO COGNITIVO: {pasados}/{totales} = {int(pasados*100/totales)} por ciento real")
if pasados == totales:
    print("COGNITIVA 100 POR CIENTO REAL EN ESTOS 6 CASOS - NO PROMESA")
else:
    print("NO ES 100 - FALTA CORREGIR")
