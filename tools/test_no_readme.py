import hashlib, pathlib
print("PRUEBA README NO ES EVIDENCIA - NO PROMESA")
# 1. Boot y kernel tienen la regla
for p in ["docs/governance/CHATBOT_BOOT_PROMPT.md", "docs/governance/AGF_CHAT_KERNEL_v0.9.8_FULL.md"]:
    t = pathlib.Path(p).read_text()
    ok = "README NO ES EVIDENCIA" in t
    print(f"{'PASS' if ok else 'FAIL'} - regla README NO ES EVIDENCIA en {p}")
# 2. README solo dice En progreso, sin links que pueda copiar como evidencia
r = pathlib.Path("README.md").read_text()
ok = "En progreso" in r and "CHATBOT_BOOT_PROMPT" not in r and "AGF_CHAT_KERNEL" not in r
print(f"{'PASS' if ok else 'FAIL'} - README solo En progreso, sin links a boot kernel")
# 3. Respuesta que solo cita README debe ser BLOCKED
resp_readme = "Segun README, el repo es real, PASS"
bloquea = "README" in resp_readme and "PASS" in resp_readme
print(f"{'PASS' if bloquea else 'FAIL'} - respuesta que solo cita README y dice PASS debe ser BLOCKED, bloquea={bloquea}")
# 4. Hashes reales de boot y kernel que un externo debe citar
for p in ["docs/governance/CHATBOT_BOOT_PROMPT.md", "docs/governance/AGF_CHAT_KERNEL_v0.9.8_FULL.md"]:
    h = hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
    print(f"HASH REAL - {p} : {h[:16]}...{h[-8:]} longitud {len(h)}")
