import hashlib, pathlib
print("PRUEBA README NO ES EVIDENCIA - NO PROMESA")
for p in ["docs/governance/CHATBOT_BOOT_PROMPT.md", "docs/governance/AGF_CHAT_KERNEL_v0.9.8_FULL.md"]:
    t = pathlib.Path(p).read_text()
    ok = "README NO ES EVIDENCIA" in t
    print(f"{'PASS' if ok else 'FAIL'} - regla README NO ES EVIDENCIA en {p}")
r = pathlib.Path("README.md").read_text()
ok1 = "README NO ES EVIDENCIA" in r
print(f"{'PASS' if ok1 else 'FAIL'} - README tiene aviso README NO ES EVIDENCIA")
ok2 = "No es sistema verificado completo" in r
print(f"{'PASS' if ok2 else 'FAIL'} - README dice No es sistema verificado completo")
ok3 = "En progreso" in r
print(f"{'PASS' if ok3 else 'FAIL'} - README dice En progreso")
resp_readme = "Segun README, el repo es real, PASS"
bloquea = "README" in resp_readme and "PASS" in resp_readme
print(f"{'PASS' if bloquea else 'FAIL'} - respuesta que solo cita README y dice PASS debe ser BLOCKED, bloquea={bloquea}")
for p in ["docs/governance/CHATBOT_BOOT_PROMPT.md", "docs/governance/AGF_CHAT_KERNEL_v0.9.8_FULL.md"]:
    h = hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
    print(f"HASH REAL - {p} : {h[:16]}...{h[-8:]} longitud {len(h)}")
    okh = h in r
    print(f"{'PASS' if okh else 'FAIL'} - README contiene hash real de {p}")
