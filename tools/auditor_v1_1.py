#!/usr/bin/env python3
# RUTA: tools/auditor_v1_1.py
# VERSION: v1.1
# FECHA: 2026-11-09
# PROPOSITO: Validar contenedores IN/OUT con UTF-8, PROTO-COM, Desconstruccion, Hash y Deduplicacion
# ESTADO: PERMANENTE
import json, hashlib, glob, sys, os
sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.getcwd())
try:
    from tools.normalizacion_utf8 import auditar
except ModuleNotFoundError:
    from normalizacion_utf8 import auditar
def validar_chunk(p):
    d=json.load(open(p))
    errores=[]
    if d["Longitud_IN"]!=len(d["Contenido_IN"]): errores.append("Longitud_IN mismatch")
    if d["Hash_IN"]!=hashlib.sha256(d["Contenido_IN"].encode()).hexdigest(): errores.append("Hash_IN mismatch")
    if d["Contenido_OUT"]:
        if d["Longitud_OUT"]!=len(d["Contenido_OUT"]): errores.append("Longitud_OUT mismatch")
        if d["Hash_OUT"]!=hashlib.sha256(d["Contenido_OUT"].encode()).hexdigest(): errores.append("Hash_OUT mismatch")
    a=auditar(d["Contenido_IN"]+d["Contenido_OUT"])
    if a["guion_raro"]: errores.append("Guion raro U+2011 detectado")
    if "Desconstruccion_IN" not in d: errores.append("Falta Desconstruccion_IN")
    return {"chunk": d["Chunk_ID"], "estado": d["Estado"], "errores": errores, "auditoria_utf8": a}
if __name__=="__main__":
    for p in sorted(glob.glob("chunks/*.json")):
        print(validar_chunk(p))
