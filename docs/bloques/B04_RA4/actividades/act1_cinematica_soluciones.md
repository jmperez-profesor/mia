# Soluciones · Actividad 1 · Cinemática de un manipulador

> **Solo para el docente.** No compartir con el alumnado antes de la corrección.

## Resultados esperados (ejecutando el cuaderno)

El cuaderno `sesion19_sistemas_robotizados.ipynb` trae definidas `fk_2r`, `ik_2r` y `alcanzable`. La actividad pide ejecutar estos tres bloques; estas son las **salidas correctas**.

### 1. FK — cuatro posturas

```python
for (a1, a2) in [(0, 0), (90, 0), (0, 90), (45, 45)]:
    x, y = fk_2r(np.radians(a1), np.radians(a2))
    r = np.hypot(x, y)
    print(f"({a1:2d}°, {a2:2d}°) -> punta ({x:6.1f}, {y:6.1f}) mm, radio {r:5.1f} mm  {'FUERA (>320)' if r > 320 else 'dentro'}")
```

**Salida:**

```
( 0°,  0°) -> punta ( 270.0,    0.0) mm, radio 270.0 mm  dentro
(90°,  0°) -> punta (   0.0,  270.0) mm, radio 270.0 mm  dentro
( 0°, 90°) -> punta ( 150.0,  120.0) mm, radio 192.1 mm  dentro
(45°, 45°) -> punta ( 106.1,  226.1) mm, radio 249.7 mm  dentro
```

**Ninguna queda fuera.** El radio máximo es 270 mm (< 320 mm del DOBOT).

### 2. IK — las dos soluciones de (200, 100)

```python
abajo, arriba = ik_2r(200, 100)
print("codo abajo :", tuple(round(np.degrees(a), 1) for a in abajo))
print("codo arriba:", tuple(round(np.degrees(a), 1) for a in arriba))
print("FK(codo abajo)  =", tuple(round(v, 1) for v in fk_2r(*abajo)))
print("FK(codo arriba) =", tuple(round(v, 1) for v in fk_2r(*arriba)))
```

**Salida:**

```
codo abajo : (-3.4, 68.7)
codo arriba: (56.6, -68.7)
FK(codo abajo)  = (200.0, 100.0)
FK(codo arriba) = (200.0, 100.0)
```

Ambas posturas devuelven el punto `(200, 100)`. ✅

### 3. Espacio de trabajo

```python
print("alcance máximo  (l1+l2):", L1 + L2, "mm")
print("radio mínimo (|l1-l2|):", abs(L1 - L2), "mm")
print("(200, 100) alcanzable:", alcanzable(200, 100))   # dentro del anillo
print("(300, 0)   alcanzable:", alcanzable(300, 0))     # fuera (>270)
print("(10, 0)    alcanzable:", alcanzable(10, 0))      # hueco central (<30)
```

**Salida:**

```
alcance máximo  (l1+l2): 270.0 mm
radio mínimo (|l1-l2|): 30.0 mm
(200, 100) alcanzable: True
(300, 0)   alcanzable: False
(10, 0)    alcanzable: False
```

**Explicación:** el alcance máximo es `l₁ + l₂ = 270 mm` (brazo **estirado**, θ₂ = 0); el radio mínimo es `|l₁ − l₂| = 30 mm` (brazo **plegado**, θ₂ = 180°). El espacio de trabajo es un **anillo** entre 30 y 270 mm.

## Conclusión de ejemplo (3–4 líneas)

*La FK tiene solución única (de ángulos a posición, sumando tramos); la IK, en cambio, tiene dos soluciones (codo arriba/abajo) y a veces ninguna (fuera del anillo o en el hueco central). La singularidad aparece con el brazo estirado (θ₂ ≈ 0), donde el movimiento se vuelve muy sensible. Por eso hay que comprobar el alcance antes de programar un punto.*
