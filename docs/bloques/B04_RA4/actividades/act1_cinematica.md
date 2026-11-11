# Actividad 1 · Cinemática de un manipulador (CE 4a, 4b)

**Trabajo autónomo TA1 (2 h)** · Todo se hace **con código en el cuaderno** [sesion19_sistemas_robotizados.ipynb](../sesion19_sistemas_robotizados.ipynb) (no hace falta papel).

## Objetivo

Recopilar los problemas del **modelado y control cinemático** de un manipulador (CE 4a) y resolverlos **con Python/NumPy** (CE 4b).

## Ejercicios (en el cuaderno)

En `sesion19_sistemas_robotizados.ipynb`, usando `fk_2r`, `ik_2r` y `alcanzable` (ya definidas en el cuaderno):

1. **FK de un brazo plano 2R.** Con `l₁ = 150 mm`, `l₂ = 120 mm`, calcula `(x, y)` y el **radio** para `(0°, 0°)`, `(90°, 0°)`, `(0°, 90°)` y `(45°, 45°)`. ¿Alguna postura queda **fuera** del alcance de 320 mm del DOBOT?
2. **IK del brazo 2R.** Para el punto `(200, 100)`, calcula las **dos soluciones** (codo arriba / codo abajo) y **compruébalas** con `fk_2r`.
3. **Espacio de trabajo.** ¿Cuánto vale el alcance máximo (`l₁ + l₂`)? ¿Y el radio mínimo (`|l₁ − l₂|`)? Compruébalo con `alcanzable` (un punto dentro, otro fuera, otro en el hueco central).

## Entregables

- Cuaderno **`sesion19_sistemas_robotizados.ipynb`** **ejecutado**, con los tres ejercicios y una **conclusión de 3–4 líneas**: *¿qué problemas de cinemática has encontrado y cómo se resuelven?* (CE 4a + 4b).

## Criterios de evaluación (rúbrica RA4)

- **4a:** resuelve FK/IK e identifica múltiples soluciones y singularidades.
- **4b:** implementa y valida las funciones con NumPy; justifica la solución.

<!-- SOLUCIONES (solo docente): [ver soluciones](act1_cinematica_soluciones.md) -->
