# Soluciones · Actividad 1 · Cinemática de un manipulador

> **Solo para el docente.** No compartir con el alumnado antes de la corrección.

## Parte A · A mano

### 1. Cinemática directa (FK)

Fórmulas (brazo 2R, `l₁ = 150 mm`, `l₂ = 120 mm`):

$$x = l_1\cos\theta_1 + l_2\cos(\theta_1+\theta_2) \qquad y = l_1\sin\theta_1 + l_2\sin(\theta_1+\theta_2)$$

| (θ₁, θ₂) | x (mm) | y (mm) | Punto | Radio r | ¿> 320 mm? |
|---|---|---|---|---|---|
| (0°, 0°) | 150·1 + 120·1 = **270** | 0 + 0 = **0** | (270, 0) | 270 | No |
| (90°, 0°) | 150·0 + 120·0 = **0** | 150·1 + 120·1 = **270** | (0, 270) | 270 | No |
| (0°, 90°) | 150·1 + 120·0 = **150** | 0 + 120·1 = **120** | (150, 120) | 192,1 | No |
| (45°, 45°) | 150·0,707 + 120·0 = **106,07** | 150·0,707 + 120·1 = **226,07** | (106,1; 226,1) | 249,7 | No |

**Ninguno queda fuera.** El radio máximo es 270 mm (todos por debajo) y el DOBOT llega a 320 mm.

### 2. Cinemática inversa (IK) para (200, 100)

Es alcanzable: r = √(200²+100²) = **223,6 mm**, dentro del anillo [30, 270].

$$c_2 = \frac{x^2+y^2-l_1^2-l_2^2}{2l_1l_2} = \frac{50000-22500-14400}{36000} = \frac{13100}{36000} = 0{,}3639$$

$$\theta_2 = \pm\arccos(0{,}3639) = \pm 68{,}7°$$

$$\theta_1 = \operatorname{atan2}(y,x) - \operatorname{atan2}\big(l_2\sin\theta_2,\; l_1+l_2\cos\theta_2\big)$$

| Solución | θ₁ | θ₂ | Comprobación FK |
|---|---|---|---|
| **Codo abajo** | **−3,4°** | **+68,7°** | → (200, 100) ✓ |
| **Codo arriba** | **+56,6°** | **−68,7°** | → (200, 100) ✓ |

### 3. Espacio de trabajo

- **Alcance máximo = `l₁ + l₂ = 270 mm`.** Con el brazo **totalmente estirado** (θ₂ = 0), la punta queda a la máxima distancia de la base; cualquier otro θ₂ «dobla» el brazo y acorta esa distancia.
- **Radio mínimo = `|l₁ − l₂| = 30 mm`.** Con el brazo **totalmente plegado** (θ₂ = 180°), los dos eslabones se oponen y la punta queda a `l₁ − l₂ = 30 mm`; no puede acercarse más a la base.
- El espacio de trabajo es un **anillo** (corona circular) entre **30 mm y 270 mm**.

## Parte B · Prueba el código (Colab)

Resultados esperados al ejecutar `sesion19_sistemas_robotizados.ipynb`:

1. **FK:** `fk_2r(0°, 0°)` → `(270.0, 0.0)`; `fk_2r(90°, 0°)` → `(0.0, 270.0)`. Coinciden con la parte A.
2. **IK:** `ik_2r(200, 100)` devuelve las dos soluciones (codo abajo ≈ (−3,4°; 68,7°), codo arriba ≈ (56,6°; −68,7°)), y `fk_2r(*solución)` devuelve (200, 100) en ambas.
3. **Espacio de trabajo:** la nube de puntos dibuja el **anillo** entre 30 y 270 mm, dentro de la circunferencia roja de 320 mm.
4. **Extra (singularidad):** para `(269.9, 0)`, `ik_2r` da **θ₂ ≈ 3,1°** (casi 0 → brazo estirado). Al acercarse a `l₁+l₂`, θ₂ → 0 y la IK se vuelve muy **sensible**.

## Conclusión de ejemplo (3–4 líneas)

*La FK tiene solución única (de ángulos a posición, sumando tramos); la IK, en cambio, tiene dos soluciones (codo arriba/abajo) y a veces ninguna (fuera del anillo). La singularidad aparece con el brazo estirado (θ₂ ≈ 0), donde el movimiento se vuelve muy sensible. Por eso hay que comprobar el alcance antes de programar un punto.*
