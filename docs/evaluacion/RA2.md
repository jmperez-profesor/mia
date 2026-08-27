# RA2 · Modelos de resolución de problemas — Banco de pruebas y rúbrica

**Resultado de aprendizaje:** Utiliza modelos de sistemas de Inteligencia Artificial implementando sistemas de resolución de problemas.
**Criterio de evaluación (CE6).**

## 1. Prueba tipo test (10 ítems)

1. En búsqueda no informada, BFS garantiza:
   a) Mínimo coste · b) **Mínimo número de pasos (si coste uniforme)** ✅ · c) Óptimo siempre · d) Menos memoria
2. A* es óptimo si la heurística es:
   a) Cualquiera · b) **Admisible (no sobreestima)** ✅ · c) Muy grande · d) Negativa
3. La función de evaluación de A* es:
   a) f = g − h · b) **f = g + h** ✅ · c) f = h · d) f = g
4. El recocido simulado puede:
   a) Solo subir · b) **Aceptar empeoramientos con cierta probabilidad** ✅ · c) Garantizar óptimo global · d) No usarse en IA
5. Un algoritmo genético usa:
   a) Solo reglas · b) **Selección, cruce y mutación** ✅ · c) Una sola solución · d) Grafo
6. En CSP, la propagación de restricciones sirve para:
   a) Generar más variables · b) **Podar el espacio de búsqueda** ✅ · c) Ignorar restricciones · d) Nada
7. STRIPS representa planes con:
   a) Redes neuronales · b) **Estados, acciones (precondiciones/efectos)** ✅ · c) Solo heurísticas · d) Árboles
8. El backtracking en CSP:
   a) Prueba todo sin poda · b) **Asigna y retrocede ante conflictos** ✅ · c) No retrocede · d) Solo aleatorio
9. Un motor de inferencia encadena reglas mediante:
   a) Conexiones wifi · b) **Encadenamiento hacia delante/atrás** ✅ · c) Sumas · d) Grafos
10. Para un problema de rutas con costes, la mejor opción suele ser:
    a) BFS ciego · b) **A* con heurística de distancia** ✅ · c) Fuerza bruta · d) Un GA siempre

## 2. Prueba de desarrollo (3 ejercicios)

**D1.** Implementa (en pseudocódigo o Python) A* para un grafo y demuestra que con heurística admisible encuentra la ruta de mínimo coste.
*Criterios:* estructura A* (2 p); heurística admisible (2 p); demostración/argumento de optimalidad (1 p).

**D2.** Diseña un CSP para un problema de horarios (variables, dominios, restricciones) y explica cómo resolverlo.
*Criterios:* modelado correcto (3 p); estrategia de resolución (backtracking/propagación) (2 p).

**D3.** Explica un algoritmo genético aplicado a un problema de optimización y justifica sus parámetros.
*Criterios:* codificación y operadores (2 p); criterio de parada y fondo (2 p); interpretación de resultudados (1 p).

## 3. Rúbrica de RA2 (escala 1–10, entera)

| Dimensión | 1–4 | 5–6 | 7–8 | 9–10 |
|-----------|-----|-----|-----|------|
| Búsqueda (A*, no informada) | Errores graves | Implementa BFS/A* básico | A* con heurística correcta | Analiza optimalidad/eficiencia |
| Búsqueda local / GA | No aplica | Aplica un método | Parámetros adecuados | Justifica convergencia |
| CSP / restricciones | Confunde | Modela y resuelve simple | Usa poda/propagación | Problema complejo resuelto |
| Planificación (STRIPS) | No representa | Representa estados/acciones | Plan correcto | Plan óptimo/eficiente |
| Motores de reglas | No infiere | Reglas simples | Encadenamiento correcto | Sistema robusto |

**Conversión a nota:** media de dimensiones (entera). Mínimo para superar el RA = 5.
