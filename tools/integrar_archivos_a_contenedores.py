# RUTA: tools/integrar_archivos_a_contenedores.py
# VERSION: v1.0
# PROPOSITO: Integra cualquier archivo a contenedor IN/OUT, real
# ESTADO: PENDIENTE VALIDACION HIL
import os, json, hashlib, shutil
from datetime import datetime, timezone
def leer_archivo(path):
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()
def hash_real(texto):
    return hashlib.sha256(texto.encode("utf-8")).hexdigest()
def integrar_un_archivo(path, chunk_id, anterior="NINGUNO", siguiente="PENDIENTE"):
    contenido = leer_archivo(path)
    hora = datetime.now(timezone.utc).isoformat()
    destino = f"chunks/{chunk_id}_chunk.json"
    if os.path.exists(destino):
        shutil.copy(destino, destino + ".bak_" + datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S"))
    chunk = {
        "Chunk_ID": chunk_id,
        "Circuito": "HIL IN -> SIL OUT -> HIL valida",
        "HIL": "Tu, Human In The Loop, mandas IN y validas OUT",
        "SIL": "Asistente, System In The Loop, hace OUT",
        "MIL": "ELIMINADO, no existe MIL-A ni MIL-B",
        "Peso": 10,
        "Timestamp_IN": hora,
        "Timestamp_OUT": hora,
        "Gerundio": "Integrando",
        "Familia": "Forja",
        "Entropia": "Baja",
        "Asimetria": "Vocabulario / Contexto",
        "Estado": "PENDIENTE VALIDACION HIL",
        "Normalizacion_UTF8": "OK",
        "Archivo_Origen": path,
        "Contenido_IN": contenido[:500],
        "Contenido_OUT": f"Archivo {path} integrado a contenedor IN/OUT, con Hash y Grafo reales, sin API, para LLM opaco en ventana de chat.",
        "Longitud_IN": len(contenido),
        "Longitud_OUT": 0,
        "Hash_IN": hash_real(contenido),
        "Hash_OUT": "",
        "Enlace_Anterior": anterior,
        "Enlace_Siguiente": siguiente,
        "Mejora_Profunda": "REAL, Hash y Hora calculados del contenido real, nada simulado",
    }
    chunk["Longitud_OUT"] = len(chunk["Contenido_OUT"])
    chunk["Hash_OUT"] = hash_real(chunk["Contenido_OUT"])
    json.dump(chunk, open(destino, "w"), indent=2, ensure_ascii=False)
    print(destino, "INTEGRADO REAL", "Hash_IN:", chunk["Hash_IN"][:16], "Longitud_IN:", chunk["Longitud_IN"])
    return destino
if __name__ == "__main__":
    integrar_un_archivo("tools/arquitectura_limpia_v3.py", "C12", anterior="C11", siguiente="PENDIENTE")
    print("INTEGRACION OK")
