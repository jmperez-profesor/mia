# B04 · RA4 — Ejercicios guiados y propuestos

> 3 sesiones presenciales + 3 autónomas. Los **guiados** se hacen en clase con el profesor (no se entregan); los **propuestos** son las actividades autónomas que **sí se entregan** y se corrigen con rúbrica. Hilo conductor: **Célula-07**. Adaptados de la UD04 de David Martínez Peña (CC BY-NC-SA 4.0).

## Sesión 1 · Robot y cinemática (RA4-a)

### Guiados (en clase)

**G1.** Clasifica por tipo (manipulador, móvil, patas, UAV/AUV, cobot) 6 robots de la Célula-07 y de dos casos reales (KUKA KR AGILUS, Amazon Robotics).

**G2.** Para una tarea de *pick-and-place*, elige sensor (entorno/ubicación/propioceptivo) y actuador (eléctrico/hidráulico/neumático). Justifica.

**G3.** Ejecuta `sesion01_cinematica.ipynb`: calcula la FK de un brazo 3R con `q=[0,0,0]` y `q=[π/2,0,0]`. ¿Dónde está el efector en cada caso?

**G4.** Con el jacobiano del brazo 3R, detecta una configuración cercana a singularidad (codo estirado) y explica por qué la velocidad articular se dispara.

**G5.** Con `roboticstoolbox`, resuelve la IK del Panda para una pose y comprueba el resultado con `fkine`.

### Propuestos (autónomo A1, entregable)

**P1.** Tabla DH de un manipulador 6R + FK con `roboticstoolbox`.

**P2.** IK para 3 poses; indica cuáles tienen **múltiples soluciones**.

**P3.** Jacobiano en 3 configuraciones; localiza una **singularidad**.

**P4.** Informe (5 líneas): configuración recomendada para evitar la singularidad.

## Sesión 2 · Planificación y percepción (RA4-b)

### Guiados (en clase)

**G6.** Dibuja el **espacio de configuración** de un robot móvil 2D con 2 obstáculos y marca el espacio libre.

**G7.** Ejecuta `sesion02_planificacion_percepcion.ipynb`: genera un camino con **RRT** y explica por qué el resultado es irregular.

**G8.** Ejecuta el **filtro de partículas**: ¿cuántas medidas hacen falta para que la estimación converja a 5,0?

**G9.** Con AITK, define un mundo y un robot con cámara; ¿qué devuelve el sensor de cada píxel?

### Propuestos (autónomo A2, entregable)

**P5.** Planificador (RRT o PRM) para el AMR con 3 obstáculos + comparación con **A\*** en rejilla.

**P6.** Navegación con AITK: seguir una línea con **reglas** y luego con **lógica difusa** (o control proporcional).

**P7.** Tabla comparativa: longitud del camino, suavidad y tiempo. Justifica la técnica elegida.

## Sesión 3 · Programación y diseño (RA4-c/d)

### Guiados (en clase)

**G10.** Clasifica 5 formas de programar un robot (teach pendant, guiado manual, textual, OLP, ROS 2) y di cuándo usarías cada una.

**G11.** Ejecuta `sesion03_diseno_programacion.ipynb`: filtra el catálogo por payload (pieza + pinza + cables) y alcance.

**G12.** Compara control por **reglas** vs. **proporcional** sobre la planta simulada; ¿cuál estabiliza antes?

**G13.** Dado un brazo que comparte espacio con personas, decide: aplicación colaborativa (ISO 10218:2025) o vallado. Justifica.

### Propuestos (autónomo A3, proyecto, entregable)

**P8.** Diseña la Célula-07: tarea, selección de robot, seguridad y verificación en simulación.

**P9.** Propón la célula 4.0: PLC, telemetría (OPC UA/MQTT) y un uso del gemelo digital.

**P10.** Memoria de 1 página (tarea → criterios → selección → seguridad → riesgos).

## Autoevaluación (repaso tipo test)

**A1.** ¿Cuántos DoF hacen falta para pose libre en 3D? ¿Por qué?
**A2.** ¿Qué diferencia hay entre precisión y repetibilidad? Pon un ejemplo.
**A3.** ¿Por qué la FK tiene solución única y la IK no?
**A4.** ¿Qué es una singularidad y cómo se evita?
**A5.** ¿Qué método de planificación da el camino más corto? ¿Y el más seguro?
**A6.** Diferencia plan y política.
**A7.** ¿Qué resuelve SLAM y por qué es difícil?
**A8.** ¿Por qué el aprendizaje por refuerzo falla en un robot real?
**A9.** ¿Qué significa que «colaborativo» no es una propiedad del hardware?
**A10.** Enumera los criterios de selección de un robot y el error típico con el payload.
