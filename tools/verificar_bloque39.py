import pathlib, hashlib, sys
k = pathlib.Path("docs/governance/AGF_CHAT_KERNEL_v0.9.8_FULL.md")
t = k.read_text().replace("\xa0", " ")
checks = []
def chk(n, c):
    checks.append((n, c))
    print(("PASS - " if c else "BLOCKED - ") + n)
chk("39 I-01 NO DEFINIDA", "Regla I-01 NO DEFINIDA" in t)
chk("39 Ejemplo no es hash real", "EJEMPLO-685fd4b-NO-ES-HASH-REAL" in t or "EJEMPLO" in t)
chk("39 Registro NO ENCONTRADO", "Registro NO ENCONTRADO" in t)
chk("39 Nivel 3 DECLARADO pendiente", "Nivel 3 DECLARADO pendiente" in t or "DECLARADO pendiente" in t)
chk("39 Regla PhD", "Regla ingeniero PhD Bloque 39" in t)
# Hash file coincide con kernel actual
h = pathlib.Path(".kernel_hash.sha256")
real = hashlib.sha256(k.read_bytes()).hexdigest()
chk("39 .kernel_hash.sha256 existe", h.exists())
if h.exists():
    chk("39 .kernel_hash.sha256 coincide con kernel", h.read_text().strip() == real)
else:
    chk("39 .kernel_hash.sha256 coincide con kernel", False)
ok = all(c for _, c in checks)
print("BLOQUE 39 CUMPLIDO" if ok else "BLOQUE 39 NO CUMPLIDO - BLOCKED")
sys.exit(0 if ok else 1)
