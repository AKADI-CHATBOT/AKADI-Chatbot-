import pathlib, sys
t = pathlib.Path("docs/governance/AGF_CHAT_KERNEL_v0.9.8_FULL.md").read_text().replace("\xa0", " ")
def chk(n, c):
    print(("PASS - " if c else "BLOCKED - ") + n)
    return c
ok = True
ok &= chk("40 9 elementos no 9 capas", "9 elementos (4 capas forenses + 5 metricas)" in t)
ok &= chk("40 ACTA_FINAL salida NO ENCONTRADO script SI existe", "ACTA_FINAL_SELLADA_CLOSED salida NO ENCONTRADO" in t)
ok &= chk("40 MAXCAP pendiente", "Solo MAXCAP 500 verificado" in t)
ok &= chk("40 Regla honestidad archivo verificable", "archivo verificable con ls y hash" in t)
ok &= chk("40 Regla PhD", "Regla ingeniero PhD Bloque 40" in t)
ok &= chk("40 Fecha desactualizada", "Fecha desactualizada" in t)
print("BLOQUE 40 CUMPLIDO" if ok else "BLOQUE 40 NO CUMPLIDO - BLOCKED")
sys.exit(0 if ok else 1)
