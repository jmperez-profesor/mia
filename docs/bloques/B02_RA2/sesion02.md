---
sesion: "02"
bloque: B02
ra: RA2
fecha_prevista: 2026-11-09
duracion: 120 min
ce: [6]
titulo: "Búsqueda informada: A* y heurísticas"
---

# Sesión 02 · Búsqueda informada: A* y heurísticas

## Objetivos de la sesión
- Comprender qué es una **heurística** y por qué debe ser **admisible** (no sobreestimar el coste real).
- Implementar **A\*** con cola de prioridad y función `f(n)=g(n)+h(n)`.
- Contrastar "ruta de menor número de pasos" (BFS) frente a "ruta de menor coste" (A*).

## Contenidos
- Función de evaluación `f = g + h`; papel de `g` (coste real) y `h` (estimación).
- Admisibilidad y consistencia de la heurística; optimalidad de A* con heurística admisible.
- Distancia de Manhattan como heurística admisible en cuadrícula con movimientos 4-direccionales.
- Terreno con costes variables (asfalto/grava/barro).

## Temporalización (120 min)
- **Apertura / activación (10 min):** recordar BFS y plantear: "¿y si un camino corto pasa por el barro?". Se motiva la necesidad de costes.
- **Desarrollo (80 min):** teoría de heurísticas admisibles; demostración informal de por qué A* no descarta la solución óptima; codificación de `h` (Manhattan), `astar` con `heapq` y comparación con BFS sobre un grid de costes.
- **Cierre y evaluación (30 min):** discusión de por qué Manhattan es admisible aquí; revisión de la práctica; entrega del miniproyecto.

## Práctica guiada (con solución)
El grid ahora tiene coste por celda. A* usa la Manhattan como `h`, que es admisible porque cada paso cuesta al menos 1, así que la heurística nunca sobreestima.

```python
import numpy as np
import matplotlib.pyplot as plt
import heapq

rng = np.random.default_rng(7)
N = 12
coste = rng.integers(1, 6, size=(N, N)).astype(float)  # 1 asfalto .. 5 barro
start, goal = (0, 0), (N - 1, N - 1)
coste[start] = 1.0; coste[goal] = 1.0

def asegura_camino(grid, start, goal):
    r, c = start
    while r != goal[0]:
        grid[r, c] = 0
        r += 1 if goal[0] > r else -1
    while c != goal[1]:
        grid[r, c] = 0
        c += 1 if goal[1] > c else -1
    grid[goal] = 0

asegura_camino(coste, start, goal)

def h(s):
    return abs(s[0]-goal[0]) + abs(s[1]-goal[1])  # Manhattan (admisible)

def vecinos(s):
    for d in ((1,0),(-1,0),(0,1),(0,-1)):
        ns = (s[0]+d[0], s[1]+d[1])
        if 0 <= ns[0] < N and 0 <= ns[1] < N:
            yield ns

def astar(start, goal):
    open_ = [(h(start), 0.0, start)]
    g = {start: 0.0}; prev = {start: None}; explorados = 0
    while open_:
        f, gs, s = heapq.heappop(open_); explorados += 1
        if s == goal: break
        for ns in vecinos(s):
            ng = gs + coste[ns]
            if ns not in g or ng < g[ns]:
                g[ns] = ng; prev[ns] = s
                heapq.heappush(open_, (ng + h(ns), ng, ns))
    if goal not in g: return None, float('inf'), explorados
    path = []; s = goal
    while s is not None: path.append(s); s = prev[s]
    return path[::-1], g[goal], explorados

ruta, c, exp = astar(start, goal)
print("A* coste total:", c, "| pasos:", len(ruta)-1, "| nodos explorados:", exp)
# Frente a BFS (que contaría pasos), A* elige rodear el barro si ahorra coste.
```

## Práctica propuesta (miniproyecto)
**Miniproyecto:** implementa A* con heurística de Manhattan sobre un grid de costes y compara el coste de la ruta con la de BFS.  
**Entregables:** función `astar`, justificación de admisibilidad y gráfico de la ruta óptima.  
**Criterios de evaluación:** uso correcto de `g`/`h`, optimalidad y explicación de la heurística.  
**Notebook:** [Abrir/Descargar miniproyecto](sesion02_miniproyecto.ipynb)

## Evaluación (criterios CE)
- CE6: diseña una heurística admisible y aplica A* para resolver un problema de coste mínimo.

## Atención a la diversidad
- Refuerzo: partir de un grid 8×8 con solo dos niveles de coste.
- Ampliación: probar una heurística no admisible (p.ej. Manhattan × 2) y observar que deja de ser óptimo.

## Observaciones
- La optimalidad de A* depende de la heurística: admisible ⇒ óptimo; consistente ⇒ también eficiente.
