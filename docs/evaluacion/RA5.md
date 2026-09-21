# RA5 · Sistemas expertos y motores de reglas — Banco de pruebas y rúbrica

**Resultado de aprendizaje:** Aplica sistemas expertos evaluando la influencia de los controladores inteligentes en el comportamiento del sistema.
**Criterios de evaluación:** RA5-a (dinámica y estructuras), RA5-b (representar y simular), RA5-c (variación de características), RA5-d (estrategias de control), RA5-e (controladores inteligentes).

## 1. Prueba tipo test (10 ítems)

1. La jerarquía DIKW ordena, de menor a mayor:
   a) Sabiduría, conocimiento, información, dato · b) **Dato, información, conocimiento, sabiduría** ✅ · c) Dato, conocimiento, información, sabiduría · d) Información, dato, sabiduría, conocimiento

2. El ciclo de inferencia de un motor de reglas es:
   a) Compilar, ejecutar, depurar · b) **Reconocer, resolver, actuar** ✅ · c) Entrenar, validar, probar · d) Cargar, guardar, cerrar

3. El encadenamiento hacia atrás (backward) es típico de:
   a) Control en tiempo real · b) **Diagnóstico guiado por metas** ✅ · c) Planificación de rutas · d) Visión artificial

4. Los factores de certeza los introdujo:
   a) XCON · b) **MYCIN** ✅ · c) Drools · d) DENDRAL

5. `experta` falla en Python 3.10+ porque:
   a) Usa TensorFlow · b) **`collections.Mapping` se eliminó** ✅ · c) No soporta Windows · d) Requiere GPU

6. RETE y PHREAK son:
   a) Lenguajes de programación · b) **Algoritmos de *matching* eficiente de reglas** ✅ · c) Formatos de imagen · d) Tipos de sensor

7. En una tabla de decisión DMN, la *hit policy* `unique` exige:
   a) Que gane la primera fila · b) **Que solo una fila encaje** ✅ · c) Devolver todas las filas · d) Ignorar solapes

8. Un BRMS como Drools sirve para:
   a) Entrenar redes neuronales · b) **Gestionar reglas de negocio separadas del código** ✅ · c) Simular robots · d) Comprimir datos

9. FIGS aplicado a un histórico de decisiones:
   a) Las encripta · b) **Extrae reglas legibles de los datos** ✅ · c) Borra duplicados · d) Genera imágenes

10. Usar reglas como «guardarraíl» de un LLM consiste en:
    a) Entrenar el modelo · b) **Validar y acotar su salida antes de ejecutarla** ✅ · c) Aumentar la temperatura · d) Desactivar el modelo

## 2. Prueba de desarrollo (3 ejercicios)

**D1.** Explica la arquitectura de un sistema experto (base de conocimiento, memoria de trabajo, motor de inferencia y subsistema de explicación) y el ciclo reconocer-resolver-actuar.
*Criterios:* componentes descritos (2 p); ciclo explicado (2 p); papel de la explicación (1 p).

**D2.** Modela una política de decisión (p. ej. aprobación de una transacción) como **tabla DMN** con su *hit policy*, e impleméntala con `rule-engine` o `clipspy`.
*Criterios:* tabla coherente y completa (2 p); hit policy justificada (1 p); implementación correcta (2 p).

**D3.** Diferencia un sistema experto puro, un híbrido reglas/datos y un guardarraíl de LLM. Pon un caso de cada uno y di cuándo usarías cada enfoque.
*Criterios:* tres enfoques diferenciados (2 p); casos plausibles (2 p); criterio de selección (1 p).

## 3. Rúbrica de RA5 (escala 1–10, entera)

| Dimensión | 1–4 (Insuf.) | 5–6 (Medio) | 7–8 (Notable) | 9–10 (Excelente) |
|-----------|--------------|-------------|---------------|------------------|
| Arquitectura y dinámica | Confunde componentes | Describe los componentes | Explica el ciclo completo | Justifica el diseño del motor |
| Representación del conocimiento | No distingue | Usa reglas | Elige representación idónea | Compara y justifica (DMN/reglas/difuso) |
| Motores de reglas | No los identifica | Nombra uno | Compara varios con criterio | Elige con benchmark y cobertura |
| Híbridos y guardarraíles | No los entiende | Describe un caso | Implementa un híbrido | Diseña guardarraíl y lo evalúa |
| Explicabilidad y normativa | La ignora | La menciona | La relaciona con el caso | La integra (XAI, AI Act, auditoría) |

**Conversión a nota:** media de las dimensiones (entera). Mínimo para superar el RA = 5.
