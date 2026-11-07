import json, sys, os
if len(sys.argv) < 2:
    print("BLOCKED - NO ENCONTRADO - falta ruta del audit o acta")
    sys.exit(1)
ruta = sys.argv[1]
if not os.path.exists(ruta):
    print(f"BLOCKED - NO ENCONTRADO - no existe: {ruta}")
    sys.exit(1)
try:
    with open(ruta) as f:
        data = json.load(f)
except Exception as e:
    print(f"BLOCKED - audit no es JSON valido: {e}")
    sys.exit(1)
# Buscar todos los valores que parecen hash, en cualquier nivel
encontrados = []
def buscar(obj):
    if isinstance(obj, dict):
        for k, v in obj.items():
            if "sha256" in k.lower() and isinstance(v, str):
                encontrados.append((k, v))
            else:
                buscar(v)
    elif isinstance(obj, list):
        for v in obj:
            buscar(v)
buscar(data)
if len(encontrados) == 0:
    print(f"BLOCKED - NO SE ENCONTRO NINGUN HASH en {ruta}")
    sys.exit(1)
for k, h in encontrados:
    if len(h) != 64:
        print(f"BLOCKED - hash en {k} no es completo de 64: {h}")
        sys.exit(1)
    if h in ["abc123", "def456"]:
        print(f"BLOCKED - hash de test, no real en {k}: {h}")
        sys.exit(1)
print(f"PASS-CHECK - {ruta} tiene {len(encontrados)} hashes completos y no es test")
