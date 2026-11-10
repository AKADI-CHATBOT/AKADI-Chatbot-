// RUTA: tools/normalizacion_utf8.c
// VERSION: v1.0
// FECHA: 2026-11-09
// PROPOSITO: Normalizacion, codificacion y analisis UTF-8 para contenedores IN/OUT - version C con GCC
// ESTADO: PERMANENTE
#include <stdio.h>
#include <string.h>
#include <math.h>
void od_c_octal(const unsigned char *s) {
  for (int i=0; s[i]; i++) printf("%03o ", s[i]);
  printf("\n");
}
int detectar_guion_raro(const unsigned char *s) {
  for (int i=0; s[i] && s[i+1] && s[i+2]; i++) {
    if (s[i]==0xE2 && s[i+1]==0x80 && s[i+2]==0x91) return 1;
  }
  return 0;
}
double medir_entropia(const unsigned char *s) {
  int freq[256]={0}; int n=0;
  for (int i=0; s[i]; i++) { freq[s[i]]++; n++; }
  if (n==0) return 0;
  double e=0;
  for (int i=0;i<256;i++) if (freq[i]) { double p=(double)freq[i]/n; e-=p*log2(p); }
  return e;
}
int main() {
  const unsigned char *a=(unsigned char*)"mango - palta";
  const unsigned char *b=(unsigned char*)"mango \xE2\x80\x91 palta";
  printf("Normal: guion_raro=%d entropia=%.4f od=", detectar_guion_raro(a), medir_entropia(a)); od_c_octal((unsigned char*)"-");
  printf("Raro: guion_raro=%d entropia=%.4f od=", detectar_guion_raro(b), medir_entropia(b)); od_c_octal((unsigned char*)"\xE2\x80\x91");
  printf("Test A: %d\nTest B: %d\n", detectar_guion_raro(a), detectar_guion_raro(b));
  return 0;
}
