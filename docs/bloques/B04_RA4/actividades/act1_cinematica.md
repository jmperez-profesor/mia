# Actividad 1 · Cinemática de un manipulador (CE 4a, 4b)

**Trabajo autónomo TA1 (2 h)** · Ficha de problemas (a mano) + prueba del código en el cuaderno [sesion19_sistemas_robotizados.ipynb](../sesion19_sistemas_robotizados.ipynb)

## Objetivo

Recopilar los problemas del **modelado y control cinemático** de un manipulador (CE 4a) y resolverlos con lápiz y con Python/NumPy (CE 4b).

## Parte A · A mano

1. **FK de un brazo plano 2R.** Con `l₁ = 150 mm`, `l₂ = 120 mm`:
   - Calcula `(x, y)` para `(θ₁, θ₂) = (0°, 0°)`, `(90°, 0°)`, `(0°, 90°)` y `(45°, 45°)`.
   - ¿Alguno queda **fuera** del alcance de 320 mm del DOBOT?
2. **IK del brazo 2R.** Para el punto `(200, 100)`:
   - Encuentra las **dos soluciones** (codo arriba / codo abajo).
   - Comprueba cada una con la fórmula de la FK.
3. **Espacio de trabajo.** ¿Por qué el alcance máximo es `l₁ + l₂`? ¿Qué radio mínimo tiene el espacio de trabajo y por qué?

## Parte B · Prueba el código (Colab)

El cuaderno [sesion19_sistemas_robotizados.ipynb](../sesion19_sistemas_robotizados.ipynb) ya trae implementadas `fk_2r`, `ik_2r` y el dibujo del espacio de trabajo. Tu trabajo es **probarlo**:

1. Ejecuta todas las celdas y comprueba que los resultados de la **parte A** coinciden.
2. Cambia **ángulos** en la FK y **puntos objetivo** en la IK; observa las dos soluciones.
3. Dibuja el **espacio de trabajo** y localiza el anillo de alcance y el límite de 320 mm.
4. **Extra:** prueba la singularidad (punto casi en `l₁ + l₂`) y comenta qué le pasa a la IK.

## Entregables

- Ficha de la parte A (a mano, escaneada o en Markdown).
- Cuaderno **`sesion19_sistemas_robotizados.ipynb`** ejecutado, con las pruebas y una **conclusión de 3–4 líneas**: *¿qué problemas de cinemática has encontrado y cómo se resuelven?* (CE 4a + 4b).

## Criterios de evaluación (rúbrica RA4)

- **4a:** resuelve FK/IK e identifica múltiples soluciones y singularidades.
- **4b:** implementa y valida las funciones con NumPy; justifica la solución.

<!-- SOLUCIONES (solo docente): [ver soluciones](act1_cinematica_soluciones.md) -->
