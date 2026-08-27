---
sesion: "03"
bloque: B02
ra: RA2
fecha_prevista: 2026-11-11
duracion: 120 min
ce: [6]
titulo: "Búsqueda local"
---

# Sesión 03 · Búsqueda local

## Objetivos de la sesión
- Entender la **búsqueda local**: optimizar una función objetivo moviéndose en el vecindario del estado actual, sin memoria de recorrido.
- Implementar **escalada** (hill climbing) y **recocido simulado** (simulated annealing).
- Valorar el papel de la temperatura/ruido para escapar de óptimos locales.

## Contenidos
- Espacio de estados como permutaciones; función objetivo a minimizar.
- Hill climbing: convergencia rápida pero sensible a óptimos locales.
- Recocido simulado: probabilidad de aceptar empeoramientos `exp(-Δ/T)`; enfriamiento.
- Trayectoria de coste como diagnóstico de convergencia.

## Temporalización (120 min)
- **Apertura / activación (10 min):** metáfora del senderista en niebla que solo ve el siguiente paso; se motiva la búsqueda local.
- **Desarrollo (80 min):** formulación del problema de asignación (flujo×distancia); codificación de `coste`, `escalada` y `recocido`; trazado de la curva de convergencia.
- **Cierre y evaluación (30 min):** comparativa hill climbing vs recocido; rúbrica; entrega del miniproyecto.

## Práctica guiada (con solución)
Problema de diseño de planta: minimizar `Σ flujo(i,j)·distancia(local(i),local(j))` permutando locales.

```python
import numpy as np
import matplotlib.pyplot as plt
import random, math

rng = np.random.default_rng(3)
n = 8
flujo = rng.integers(0, 10, size=(n, n)); flujo = flujo + flujo.T
distancia = rng.integers(1, 10, size=(n, n)); distancia = (distancia + distancia.T) / 2

def coste(p):
    return sum(flujo[i, j] * distancia[p[i], p[j]] for i in range(n) for j in range(n))

def vecino(p):
    a, b = random.sample(range(n), 2)
    q = p[:]; q[a], q[b] = q[b], q[a]
    return q

def escalada(iters=3000):
    s = list(range(n)); random.shuffle(s); c = coste(s); traza = [c]
    for _ in range(iters):
        q = vecino(s); cq = coste(q)
        if cq < c: s, c = q, cq
        traza.append(c)
    return s, c, traza

def recocido(T0=50.0, Tf=0.1, alpha=0.97, iters=6000):
    s = list(range(n)); random.shuffle(s); c = coste(s); traza = [c]; T = T0
    for _ in range(iters):
        q = vecino(s); cq = coste(q); delta = cq - c
        if delta < 0 or random.random() < math.exp(-delta / T):
            s, c = q, cq
        T = max(Tf, T * alpha); traza.append(c)
    return s, c, traza

mejor_esc, c_esc, traza_esc = escalada()
mejor_rec, c_rec, traza_rec = recocido()
print("Hill climbing ->", c_esc)
print("Recocido     ->", c_rec)
plt.plot(traza_esc, label="hill climbing")
plt.plot(traza_rec, label="recocido simulado")
plt.xlabel("iteración"); plt.ylabel("coste"); plt.legend(); plt.show()
# El recocido suele hallar menor coste al escapar de óptimos locales mediante el ruido térmico.
```

## Práctica propuesta (miniproyecto)
**Miniproyecto:** resuelve la asignación de departamentos a locales con hill climbing y recocido simulado; compara las curvas de convergencia.  
**Entregables:** funciones de búsqueda local, gráfico de traza y conclusión sobre óptimos locales.  
**Criterios de evaluación:** formulación correcta de la función objetivo y uso adecuado del esquema de enfriamiento.  
**Notebook:** [Abrir/Descargar miniproyecto](sesion03_miniproyecto.ipynb)

## Evaluación (criterios CE)
- CE6: formula el problema como optimización y aplica métodos de búsqueda local.

## Atención a la diversidad
- Refuerzo: `n=5` y pocas iteraciones para visualizar fácilmente.
- Ampliación: comparar distintas leyes de enfriamiento (lineal vs geométrica).

## Observaciones
- El hill climbing puro se queda atrapado en óptimos locales; el recocido lo compensa a costa de más cómputo.
