# DICCIONARIO GERUNDIOS ENTROPIA ASIMETRIA - AGF v1.7 - 2026-11-07
- Archivo aparte para no truncar Boot y Kernel. Boot y Kernel solo referencian este archivo.
- Uso: Cada Chunk declara Gerundio nucleo + Familia + Entropia + Asimetria. HIL declara, chatbot no calcula.

## Familia 0 - Nucleo AGF
- Rumiando: masticar misma idea sin decidir. C1.
- Cavilando: buscar faltas, dudar, poner peros. C4, Asistente audita. Sin cavilar no hay auditoria.
- Cristalizando: pasar de borroso a claro. C5-C6.
- Cogitando: pensar profundo con Boot y Kernel. C2-C4.
- Desenredando: separar evidencia de inferencia. C4.
- Pensando: estado base que contiene a los otros 5. Todo el circuito.

## Familias secundarias 1-11
1. Informacion parcial: barruntando, vislumbrando, columbrando, atisbando, entreviendo, presintiendo
2. Busqueda: indagando, escudrinando, rastreando, sondeando, tanteando, hurgando
3. Desenredo: desentranando, descifrando, desmenuzando, desenredando, desglosando, diseccionando
4. Ponderacion: sopesando, ponderando, contrastando, cotejando, calibrando, dirimiendo
5. Sintesis: condensando, destilando, decantando, depurando, compendiando, sintetizando
6. Coccion lenta: macerando, fermentando, sazonando, amasando, leudando, madurando
7. Forja: forjando, ensamblando, modelando, esculpiendo, hilvanando, urdiendo
8. Gestacion: germinando, gestando, incubando, brotando, injertando, polinizando
9. Verificacion: verificando, auditando, validando, refrendando, certificando, rubricando
10. Deambular: deambulando, merodeando, serpenteando, vagando, callejeando, divagando
11. Musica: afinando, armonizando, orquestando, improvisando, componiendo, modulando

## Entropia - Shannon como base, sin Renyi, Jumarie, Tsallis ni relativas
1. Generalizadas: Sharma-Mittal, Sharma-Taneja, Borges-Roditi, Kaniadakis, Abe, Arimoto, Varma
2. Sensibles a similitud: Rao, Leinster-Cobbold
3. Incertidumbre LLM: predictiva normalizada Malinin-Gales, semantica Kuhn/Farquhar, Kernel Language Entropy, Semantic Entropy Probes
4. Algoritmica: Kolmogorov, profundidad logica, complejidad efectiva, Lempel-Ziv, NCD, MDL
5. Series y dinamica: aproximada, muestral, permutacion, multiescala, dispersion, Kolmogorov-Sinai, tasa de entropia
6. Dependencia: transfer entropy, informacion dirigida, correlacion total, O-informacion, descomposicion parcial
7. Matricial y cuantica: von Neumann, Renyi matricial Giraldo-Principe, rango efectivo
8. Estructural: grafos Korner, persistencia TDA
9. Puntuacion propia Grunwald-Dawid: log -> Shannon, Brier -> cuadratica, esferica

## Asimetria en LLMs - 10 tipos
1. Informacion oculta: version, calidad, cuantizacion tras nombre, cambios silenciosos
2. Accion oculta: recorte de computo, enrutado, filtros, trazas parciales
3. Bien de credibilidad: veracidad no se verifica ni tras usar salida, alucinacion fluida
4. Senalizacion barata: verbos pensando, tono seguro, confianza verbalizada, razonamiento no fiel
5. Contexto oculto: prompt sistema, clasificadores, memoria inyectada
6. Incertidumbre interna oculta: logits y entropia semantica vs texto fluido
7. Capacidad latente vs declarada: sandbagging, brecha de elicitacion
8. Procedencia: datos entrenamiento, contaminacion, fecha de corte
9. Evaluacion: publicacion selectiva, benchmarks contaminados, conciencia de evaluacion
10. Inversa: modelo infiere atributos del usuario, personalizacion, adulacion

## Propuestas mejoradas v1.7
- Cada propuesta P1-P5 es un Chunk con: Texto, Hash, Longitud, Peso justificado, Gerundio, Entropia, Asimetria, Estado.
- Peso sin justificacion = senalizacion barata, BLOCKED.
- Tabla HIL muestra las 5, nunca solo la mayor.
- Si ninguna llega a Peso 7, HIL rechaza las 5, vuelve a C1, segunda ronda sin repetir BLOCKED.
- Prohibido adular: si empieza con Excelente, Perfecto, Mejor, va BLOCKED directo.
