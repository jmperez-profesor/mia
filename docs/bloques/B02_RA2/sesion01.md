---
sesion: "01"
bloque: B02
ra: RA2
fecha_prevista: 2026-11-04
duracion: 120 min
ce: [6]
titulo: "Espacios de estados y búsqueda no informada"
---

# Sesión 01 · Espacios de estados y búsqueda no informada

## Objetivos de la sesión
- Definir formalmente un problema de búsqueda: estado, estado inicial, objetivo, acciones (operadores) y coste de camino.
- Distinguir el **espacio de estados** (grafo de configuraciones) del árbol de búsqueda generado por un algoritmo.
- Implementar y comparar dos estrategias de **búsqueda no informada**: BFS (anchura) y DFS (profundidad).

## Contenidos
- Componentes de un problema de búsqueda (Russell & Norvig, cap. 3).
- Grafo de estados vs. árbol de búsqueda; riesgo de estados repetidos.
- BFS: completo y óptimo en pasos; DFS: menor memoria, no óptimo.
- Estrategia de exploración (cola FIFO vs. pila LIFO) y control de visitados.

## Temporalización (120 min)
- **Apertura / activación (10 min):** rompehielos con el "laberinto del aula": un voluntario da pasos ciegos; se discute qué información haría falta para no errar. Se introduce la terminología (estado, acción, objetivo).
- **Desarrollo (80 min):** exposición de los componentes del problema de búsqueda; dibujo en pizarra del grafo de estados y del árbol BFS/DFS; codificación en vivo de `vecinos`, `bfs` y `dfs` sobre una cuadrícula; ejecución y conteo de nodos explorados.
- **Cierre y evaluación (30 min):** puesta en común de resultados de la práctica guiada; rúbrica de autoevaluación; entrega del miniproyecto como tarea.

## Práctica guiada (con solución)
Modelamos una ciudad como una cuadrícula `N×N` donde `1` es obstáculo. BFS garantiza la ruta con **menos pasos** porque explora por niveles; DFS puede dar una ruta más larga pero explora menos nodos en entornos ramificados.

```python
import numpy as np
import matplotlib.pyplot as plt
from collections import deque

rng = np.random.default_rng(42)
N = 12
grid = rng.choice([0, 1], size=(N, N), p=[0.82, 0.18])  # 1 = obstáculo
start, goal = (0, 0), (N - 1, N - 1)
grid[start] = 0
grid[goal] = 0

def asegura_camino(grid, start, goal):
    # Garantiza conectividad borrando obstáculos en la ruta en L start->goal.
    r, c = start
    while r != goal[0]:
        grid[r, c] = 0
        r += 1 if goal[0] > r else -1
    while c != goal[1]:
        grid[r, c] = 0
        c += 1 if goal[1] > c else -1
    grid[goal] = 0

asegura_camino(grid, start, goal)

def vecinos(s):
    for d in ((1,0),(-1,0),(0,1),(0,-1)):
        ns = (s[0]+d[0], s[1]+d[1])
        if 0 <= ns[0] < N and 0 <= ns[1] < N and grid[ns] == 0:
            yield ns

def bfs(start, goal):
    q = deque([start]); prev = {start: None}; explorados = 0
    while q:
        s = q.popleft(); explorados += 1
        if s == goal: break
        for ns in vecinos(s):
            if ns not in prev:
                prev[ns] = s; q.append(ns)
    if goal not in prev: return None, explorados
    path = []; s = goal
    while s is not None: path.append(s); s = prev[s]
    return path[::-1], explorados

def dfs(start, goal):
    stack = [start]; prev = {start: None}; explorados = 0
    while stack:
        s = stack.pop(); explorados += 1
        if s == goal: break
        for ns in vecinos(s):
            if ns not in prev:
                prev[ns] = s; stack.append(ns)
    if goal not in prev: return None, explorados
    path = []; s = goal
    while s is not None: path.append(s); s = prev[s]
    return path[::-1], explorados

ruta_bfs, exp_bfs = bfs(start, goal)
ruta_dfs, exp_dfs = dfs(start, goal)
print("BFS  -> pasos:", len(ruta_bfs)-1, "| nodos explorados:", exp_bfs)
print("DFS  -> pasos:", len(ruta_dfs)-1, "| nodos explorados:", exp_dfs)
# Resultado típico: BFS encuentra la ruta más corta (menos pasos);
# DFS explora muchos menos nodos pero la ruta suele ser más larga.
```

## Práctica propuesta (miniproyecto)
**Miniproyecto:** implementa BFS y DFS en una cuadrícula ciudad con obstáculos sintéticos, dibuja las rutas y compara el número de nodos explorados.  
**Entregables:** funciones `bfs`/`dfs`, gráfico Matplotlib de la ruta y una celda de conclusión comparativa.  
**Criterios de evaluación:** correcta definición de operadores, control de estados visitados, interpretación de la diferencia BFS/DFS.  
**Notebook:** [Abrir/Descargar miniproyecto](sesion01_miniproyecto.ipynb)

## Evaluación (criterios CE)
- CE6: identifica el espacio de estados y aplica un algoritmo de búsqueda no informada correcto y terminante.

## Atención a la diversidad
- Refuerzo: entregar la cuadrícula pequeña (6×6) y la plantilla de `vecinos` ya escrita.
- Ampliación: añadir movimientos en diagonal y medir el efecto en BFS/DFS.

## Observaciones
- No confundir "menos nodos explorados" (eficiencia) con "ruta óptima" (calidad): DFS gana en memoria pero no en optimalidad de pasos.
