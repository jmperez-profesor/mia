---
sesion: "10"
bloque: B02
ra: RA2
fecha_prevista: 2026-12-09
duracion: 120 min
ce: [6]
titulo: "Miniproyecto RA2"
---

# Sesión 10 · Miniproyecto RA2

## Objetivos de la sesión
- Integrar varias técnicas del bloque B02 en un **proyecto cerrado** y realista.
- Justificar la elección de cada modelo de resolución de problemas.
- Entregar y defender una solución funcional y documentada.

## Contenidos
- Combinación de **búsqueda informada** (A*, S02) y **algoritmo genético** (S05).
- Descomposición: distancias reales entre puntos (sobre grid) + orden óptimo de visita.
- Ingeniería del problema: representación, función objetivo, visualización y memoria.

## Temporalización (120 min)
- **Apertura / activación (10 min):** presentación del reto "ruta de reparto en ciudad con obras" y descomposición en dos subproblemas.
- **Desarrollo (80 min):** sesión de trabajo del miniproyecto; el docente rota para tutorizar; los grupos construyen la matriz de distancias con A* y el GA sobre permutaciones; generan el gráfico y redactan la memoria.
- **Cierre y evaluación (30 min):** demostración de resultados por grupo; coevaluación con rúbrica; cierre del bloque B02.

## Práctica guiada (con solución)
Subproblema 1: distancia real entre puntos con A* sobre el grid. Subproblema 2: GA sobre el orden de visita minimizando la distancia total (ruta cerrada al almacén).

```python
import numpy as np
import matplotlib.pyplot as plt
import heapq, random

rng = np.random.default_rng(2026)
N = 20
grid = rng.choice([0, 1], size=(N, N), p=[0.85, 0.15])
puntos = [(0, 0)] + [tuple(rng.integers(0, N, size=2).tolist()) for _ in range(7)]
for p in puntos: grid[p] = 0

def asegura_camino(grid, a, b):
    r, c = a
    while r != b[0]:
        grid[r, c] = 0
        r += 1 if b[0] > r else -1
    while c != b[1]:
        grid[r, c] = 0
        c += 1 if b[1] > c else -1
    grid[b] = 0

for i in range(1, len(puntos)):
    asegura_camino(grid, puntos[0], puntos[i])

def astar(a, b):
    open_ = [(0, 0, a)]; g = {a: 0}; prev = {a: None}
    while open_:
        _, gs, s = heapq.heappop(open_)
        if s == b: break
        for d in ((1,0),(-1,0),(0,1),(0,-1)):
            ns = (s[0]+d[0], s[1]+d[1])
            if 0 <= ns[0] < N and 0 <= ns[1] < N and grid[ns] == 0:
                ng = gs + 1
                if ns not in g or ng < g[ns]:
                    g[ns] = ng; prev[ns] = s
                    heapq.heappush(open_, (ng, ng, ns))
    if b not in g: return float('inf')
    return g[b]

k = len(puntos)
D = np.zeros((k, k))
for i in range(k):
    for j in range(i + 1, k):
        d = astar(puntos[i], puntos[j])
        D[i, j] = D[j, i] = d

def recorrido(ruta):
    return sum(D[ruta[i], ruta[(i + 1) % len(ruta)]] for i in range(len(ruta)))

TAM, GEN, ELITE = 80, 150, 2
pobl = [rng.permutation(range(1, k)).tolist() for _ in range(TAM)]
mejor_h = []
for _ in range(GEN):
    pob = sorted(pobl, key=recorrido)
    elite = pob[:ELITE]
    nueva = elite[:]
    while len(nueva) < TAM:
        a, b = random.choice(pob[:TAM // 2]), random.choice(pob[:TAM // 2])
        i, j = sorted(random.sample(range(k - 1), 2))
        h1 = a[:i] + b[i:j + 1] + a[j + 1:]
        nueva.append(h1)
    pobl = nueva[:TAM]
    mejor_h.append(min(recorrido(r) for r in pobl))

mejor = min(pobl, key=recorrido)
print("Mejor recorrido (índices):", [0] + mejor)
print("Distancia total A*:", recorrido([0] + mejor))
plt.plot(mejor_h); plt.xlabel("generación"); plt.ylabel("distancia total"); plt.show()
# A* aporta las distancias reales sobre el grid; el GA halla el orden de visita que las minimiza.
```

## Práctica propuesta (miniproyecto)
**Miniproyecto:** optimiza la ruta de reparto de una furgoneta combinando A* (distancias reales entre `k` puntos sobre un grid con obstáculos) y un GA (orden de visita que minimiza la distancia total). Entrega además una memoria (≤ 150 palabras) que justifique la combinación de métodos.  
**Entregables:** matriz de distancias A*, GA sobre permutaciones, gráfico de la ruta sobre el grid y memoria.  
**Criterios de evaluación:** integración de modelos, justificación de la elección y solución funcional y documentada.  
**Notebook:** [Abrir/Descargar miniproyecto](sesion10_miniproyecto.ipynb)

## Evaluación (criterios CE)
- CE6: integra modelos de resolución de problemas, justifica su elección y entrega una solución funcional documentada.

## Atención a la diversidad
- Refuerzo: `k=4` puntos y `N=12`; entregar el esqueleto del GA.
- Ampliación: comparar el GA contra la solución golosa de vecino más cercano sobre las distancias A*.

## Observaciones
- Es el cierre del bloque: cada grupo defiende su diseño; se evalúa también la calidad de la memoria y la explicación técnica.
