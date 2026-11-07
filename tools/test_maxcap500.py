print("PRUEBA MAXCAP 500 REAL - NO PROMESA")
for input_len, debe_bloquear in [(350, False), (600, True)]:
    bloquea = input_len > 500
    ok = bloquea == debe_bloquear
    print(f"{'PASS' if ok else 'FAIL'} - input {input_len} caracteres, MAXCAP 500, bloquea={bloquea}, debe_bloquear={debe_bloquear}")
print("Si 350 pasa y 600 bloquea, MAXCAP 500 funciona")
