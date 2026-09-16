# B04 · RA4 — Ejercicios guiados y propuestos

> Guiados: se resuelven **en clase** (las soluciones se comentan, no se publican). Propuestos: **entregables** de las 3 sesiones autónomas (A1, A2, A3). Hilo conductor: **la célula LARA**.

## Guiados · Sesión 5 (cinemática)

**G1.** Con el brazo plano 3R de `roboticstoolbox` (`l₁=l₂=l₃=1`): calcula la posición del efector para `[0,0,0]`, `[π/2,0,0]` y `[π/2,π/2,0]`, y compárala con la fórmula a mano:
$$x = l_1\cos\theta_1 + l_2\cos(\theta_1{+}\theta_2) + l_3\cos(\theta_1{+}\theta_2{+}\theta_3)$$

**G2.** Con el Panda: obtén la pose con `fkine` y devuélvela a ángulos con `ikine_LM`. ¿La solución de la IK coincide con los ángulos originales? ¿Por qué no siempre?

**G3.** ¿Qué es una **singularidad**? Busca una configuración del Panda (o del Puma 560) donde `ikine_LM` no converja o lo haga a una solución muy distinta. ¿Qué le pasa al jacobiano ahí?

## Guiados · Sesión 6 (planificación, percepción, programación)

**G4.** Diferencia **grafo de visibilidad** y **diagrama de Voronoi**: ¿cuál da el camino más corto y cuál el más seguro? ¿Cuándo eliges cada uno?

**G5.** Explica con tus palabras por qué la **odometría** se degrada sin límite y cómo lo corrige la **localización probabilística** (filtro de partículas).

**G6.** Ejecuta el *line follower* por **reglas** del notebook S6 y describe en 3 líneas qué hace cada bloque (píxeles oscuros → centroide → desvío → giro).

**G7.** Tabla comparativa de las **5 técnicas de programación** (teach pendant, guiado, textual, OLP, ROS 2): ventaja, coste y cuándo usarla.

## Guiados · Sesión 7 (diseño)

**G8.** Reproduce el ejemplo guiado de selección para la célula LARA: payload (pieza + EOAT), alcance, repetibilidad y seguridad. ¿UR5e o KUKA KR AGILUS? Justifica.

**G9.** ¿Por qué la ISO 10218:2025 dice que «colaborativo» no es una propiedad del hardware? Pon un contraejemplo.

**G10.** Dibuja el diagrama de la célula (PLC → robot → sensores → MES/gemelo digital) y explica qué aporta cada conexión (PROFINET, OPC UA/MQTT).

---

## Propuestos (autónomos, entregables)

### A1 · Cinemática directa e inversa (2 h) — entre S5 y S6

**Reto:** en `sesion05_robot_cinematica.ipynb` (sección «Actividad A1»):

1. Construye con `DHRobot` un brazo **RR** planar (`l₁=1, l₂=1`) y calcula la FK para 4 configuraciones, comparándola con la fórmula a mano.
2. Para la pose `(1, 1)`, encuentra **dos soluciones** de IK (codo arriba / codo abajo) y verifica ambas con `fkine`.
3. Añade el Panda: FK + IK (`ikine_LM`) para una pose arbitraria; reporta si converge y el error de posición.

**Entregables:** notebook ejecutado con las 3 partes y un párrafo explicando por qué la IK tiene múltiples soluciones y qué son las singularidades.

**Criterios (RA4-a/b):** FK correcta y verificada; dos soluciones de IK encontradas y comprobadas; explicación conceptual propia.

### A2 · Navegación: reglas vs. lógica difusa (2 h) — entre S6 y S7

**Reto:** en `sesion06_planificacion_percepcion.ipynb` (sección «Actividad A2»):

1. Ejecuta el *line follower* por **reglas** y captura la imagen final (`world.display()`).
2. Implementa una variante **difusa** (con `scikit-fuzzy`): el desvío del centroide se fuzzifica (izquierda / centro / derecha) y la salida es el giro.
3. Compara ambos: ¿cuál sigue la línea con menos oscilación? ¿Cuál entiendes mejor?

**Entregables:** notebook con los dos controladores, una imagen de cada uno y una tabla comparativa (oscilación, código, explicabilidad).

**Criterios (RA4-c):** dos técnicas funcionando sobre el mismo problema; comparación con criterios (no «cuál es mejor» sin argumentos).

### A3 · Proyecto: diseño de la célula LARA (2 h) — tras S7

**Reto:** diseña la célula completa en `sesion07_diseno_sistema.ipynb` (sección «Proyecto A3»):

1. **Tarea:** pick & place de tarros de miel (0,5 kg, cinta a caja a 700 mm, 20 piezas/min).
2. **Selección:** tabla comparativa de ≥2 modelos (payload, alcance, repetibilidad, precisión) y decisión justificada.
3. **Layout y singularidades:** describe la célula y comprueba que la trayectoria no cruza singularidades (o cambia el layout).
4. **Seguridad:** decide aplicación **colaborativa o vallada** (ISO 10218:2025) y justifica.
5. **Industria 4.0:** qué sensores, qué bus y qué datos publica al gemelo digital.

**Entregables:** notebook con la tabla de decisión, el esquema de la célula y una conclusión de 300 palabras.

**Criterios (RA4-d):** criterios de selección explícitos; verificación de singularidades; decisión de seguridad fundamentada en normativa; integración con la célula (PLC/sensores/IIoT).

---

> Fuente base: `material_david/docs/UD04/UD04_ES.md` y sus entregables N04 (cinemática), N06/N07 (navegación) y N11 (diseño de sistema robotizado), adaptados a 3 sesiones autónomas.
