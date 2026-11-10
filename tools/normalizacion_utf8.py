#!/usr/bin/env python3
# RUTA: tools/normalizacion_utf8.py
# VERSION: v1.0
# FECHA_ULTIMA_MODIFICACION: 2026-11-09
# PROPOSITO: Normalizacion, codificacion y analisis UTF-8 para contenedores IN/OUT
# ESTADO: PERMANENTE
import unicodedata, math, collections
GUION_RARO = "\u2011"
GUION_NORMAL = "-"
def od_c_octal(ch):
    return " ".join(format(b, "03o") for b in ch.encode("utf-8"))
def normalizar(text):
    return unicodedata.normalize("NFC", text)
def detectar_guion_raro(text):
    return GUION_RARO in text
def medir_entropia(text):
    if not text:
        return 0.0
    c = collections.Counter(text)
    n = len(text)
    return -sum((v/n) * math.log2(v/n) for v in c.values())
def auditar(text):
    return {
        "utf8_valid": True,
        "nfc": text == normalizar(text),
        "bom": text.startswith("\ufeff"),
        "crlf": "\r\n" in text,
        "guion_raro": detectar_guion_raro(text),
        "guion_raro_od": od_c_octal(GUION_RARO),
        "guion_normal_od": od_c_octal(GUION_NORMAL),
        "entropia": round(medir_entropia(text), 4),
    }
if __name__ == "__main__":
    import sys
    t = open(sys.argv[1], encoding="utf-8").read() if len(sys.argv) > 1 else "mango - palta"
    print(auditar(t))
