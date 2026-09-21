# RA4 · Análisis de sistemas robotizados — Banco de pruebas y rúbrica

**Resultado de aprendizaje:** Analiza sistemas robotizados, evaluando opciones de diseño e implementación.
**Criterios de evaluación:** RA4-a (modelado y control cinemático), RA4-b (soluciones a los problemas), RA4-c (técnicas de programación), RA4-d (diseño e implementación).

## 1. Prueba tipo test (10 ítems)

1. Un robot es, en esencia:
   a) Un programa de escritorio · b) **Un agente encarnado que percibe, procesa y actúa sobre el mundo físico** ✅ · c) Una base de datos · d) Una red neuronal

2. Los sensores **propioceptivos** informan de:
   a) El entorno · b) La ubicación global · c) **El estado interno del propio robot (encoders, giroscopio, fuerza)** ✅ · d) La red

3. Un manipulador necesita al menos **6 grados de libertad** para:
   a) Moverse en línea recta · b) **Colocar el efector en cualquier posición y orientación en 3D** ✅ · c) Levantar 10 kg · d) Nada especial

4. La **cinemática directa** (FK):
   a) Tiene múltiples soluciones · b) **Tiene solución única y se resuelve con matrices DH** ✅ · c) Es imposible · d) Solo vale para móviles

5. La **cinemática inversa** de un 6R general puede tener hasta:
   a) 1 solución · b) 2 soluciones · c) **16 soluciones** ✅ · d) Infinitas siempre

6. Una **singularidad** cinemática se produce cuando:
   a) El robot se apaga · b) **El jacobiano pierde rango y la velocidad articular tiende a infinito** ✅ · c) Falta batería · d) El efector es grande

7. Un robot **repetible** pero **impreciso**:
   a) No existe · b) **Vuelve siempre al mismo punto, que no es el programado** ✅ · c) Nunca acierta · d) No necesita calibración

8. Para planificar movimiento con muchas dimensiones se usa:
   a) Grafo de visibilidad · b) **Muestreo (RRT/PRM)** ✅ · c) Diagrama de Voronoi · d) Fuerza bruta

9. El **filtro de partículas (MCL)** representa la posición del robot como:
   a) Un número exacto · b) **Una distribución de probabilidad (nube de hipótesis)** ✅ · c) Un mapa · d) Una regla

10. La **ISO 10218:2025** establece que «colaborativo» es una propiedad de:
    a) El brazo aislado · b) **La aplicación completa (robot + herramienta + entorno + tarea)** ✅ · c) El PLC · d) El software ROS 2

## 2. Prueba de desarrollo (3 ejercicios)

**D1.** Resuelve la cinemática directa de un brazo plano 3R con eslabones `l₁=l₂=l₃=1` para `[0,0,0]` y `[90°,0,0]`, y explica por qué la inversa es más difícil.
*Criterios:* fórmulas/resultados correctos (2 p); distinción FK/IK (2 p); mención de múltiples soluciones/singularidades (1 p).

**D2.** Dado un robot de 6 ejes que debe coger una pieza de 1,5 kg con una pinza de 0,5 kg a 700 mm con repetibilidad ±0,1 mm, selecciona un modelo y justifica los criterios (payload, alcance, repetibilidad, seguridad).
*Criterios:* cálculo de payload con herramienta (2 p); criterios comparados (2 p); decisión de seguridad (ISO 10218:2025) (1 p).

**D3.** Explica la diferencia entre planificar y controlar, y entre un plan y una política, con un ejemplo de navegación.
*Criterios:* distinción plan/control (2 p); ejemplo coherente (2 p); relación con control óptimo o seguimiento (1 p).

## 3. Rúbrica de RA4 (escala 1–10, entera)

| Dimensión | 1–4 (Insuf.) | 5–6 (Medio) | 7–8 (Notable) | 9–10 (Excelente) |
|-----------|--------------|-------------|---------------|------------------|
| Hardware y aplicaciones | No distingue tipos | Nombra tipos y sensores | Relaciona sensor con tarea | Argumenta con datos de mercado (IFR) |
| Cinemática (FK/IK) | No la resuelve | Resuelve FK | Resuelve FK e IK | Analiza singularidades y redundancia |
| Planificación y percepción | No las explica | Describe métodos | Elige el método adecuado | Integra percepción y planificación |
| Programación de robots | No la conoce | Nombra técnicas | Compara técnicas con criterio | Justifica elección con el caso real |
| Diseño e implementación | Sin criterios | Aplica payload/alcance | Verifica singularidades y seguridad | Diseña la célula completa (IIoT, ISO) |

**Conversión a nota:** media de las dimensiones (entera). Mínimo para superar el RA = 5.
