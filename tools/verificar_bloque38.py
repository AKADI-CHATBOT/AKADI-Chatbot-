import pathlib, sys
p = pathlib.Path("docs/governance/AGF_CHAT_KERNEL_v0.9.8_FULL.md")
t = p.read_text().replace("\xa0", " ")
checks = []
def chk(n, c):
    checks.append((n, c))
    print(("PASS - " if c else "BLOCKED - ") + n)
    return c
chk("38 Fail-Closed DECLARADO", "Fail-Closed DECLARADO" in t or "Fail" in t and "DECLARADO, no verificado" in t)
chk("38 Texto que PIDE determinismo", "Texto que PIDE determinismo" in t)
chk("38 Sesgo 09", "Sesgo 09" in t)
chk("38 Calibracion INFERENCIA", "INFERENCIA, no EVIDENCIA" in t)
chk("38 Gap real", "Secciones 1 a 35 NO ENCONTRADO" in t)
chk("38 Frase exacta con GCELL", "PROTOCOLO AGF-GCELL ACEPTADO --- 4 CAPAS GCELL ACTIVAS" in t)
chk("38 Regla PhD", "Regla ingeniero PhD Bloque 38" in t)
chk("38 NO queda 4 CAPAS ACTIVAS sin GCELL", "4 CAPAS ACTIVAS" not in t.replace("4 CAPAS GCELL ACTIVAS", ""))
chk("38 NO dice Gap ninguno", "Gap declarado: [ninguno]" not in t and "Gap" not in t or "Gap declarado" in t)
chk("38 Wrapper existe", pathlib.Path("tools/verificar_boot_motor.py").exists())
ok = all(c for _, c in checks)
print("BLOQUE 38 CUMPLIDO" if ok else "BLOQUE 38 NO CUMPLIDO - BLOCKED")
sys.exit(0 if ok else 1)
