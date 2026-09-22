# Actividad 1 · Cinemática de un manipulador (CE 4a, 4b)

**Trabajo autónomo TA1 (2 h)** · Ficha de problemas + cuaderno Colab [UD04_cinematica.ipynb](../colab/UD04_cinematica.ipynb)

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

## Parte B · Con Python (Colab)

En `UD04_cinematica.ipynb`:

1. Implementa `fk_2r(theta1, theta2, l1, l2)` y comprueba la parte A.
2. Implementa `ik_2r(x, y, l1, l2)` que devuelva **las dos soluciones**.
3. Dibuja con matplotlib el **espacio de trabajo** (nube de puntos para muchos ángulos) y marca el alcance de 320 mm.
4. **Extra:** simula una singularidad (brazo totalmente estirado `θ₂ = 0`) y comenta qué le pasa a la IK.

## Entregables

- Ficha de la parte A (a mano, escaneada o en Markdown).
- Cuaderno `UD04_cinematica.ipynb` **ejecutado**, con las gráficas y una conclusión de 3 líneas: *¿qué problemas de cinemática has encontrado y cómo se resuelven?* (CE 4a + 4b).

## Criterios de evaluación (rúbrica RA4)

- **4a:** resuelve FK/IK e identifica múltiples soluciones y singularidades.
- **4b:** implementa y valida las funciones con NumPy; justifica la solución.
