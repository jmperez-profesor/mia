---
sesion: "05"
bloque: B02
ra: RA2
fecha_prevista: 2026-11-18
duracion: 120 min
ce: [6]
titulo: "Algoritmos genéticos II"
---

# Sesión 05 · Algoritmos genéticos II

## Objetivos de la sesión
- Profundizar en los GA: **elitismo**, parámetros y análisis de **convergencia**.
- Adaptar los operadores a representaciones por **permutación** (problema del viajante, TSP).
- Comparar la solución GA con una heurística golosa (vecino más cercano).

## Contenidos
- Elitismo: preservar los `e` mejores para no perder aptitud.
- Cruce OX (order crossover) y mutación por intercambio para permutaciones.
- Tensión exploración/exploitación según `pm` y tamaño de población.
- Comparación frente a la solución golosa del vecino más cercano.

## Temporalización (120 min)
- **Apertura / activación (10 min):** retomar la mochila y plantear "¿y si el orden importa?" → TSP.
- **Desarrollo (80 min):** diseño de la matriz de distancias; codificación de `distancia_total`, `cruce_ox`, `mutacion_swap` y bucle con elitismo; trazado de la ruta y la convergencia; comparación con goloso.
- **Cierre y evaluación (30 min):** debate sobre convergencia y parámetros; entrega del miniproyecto; rúbrica.

## Práctica guiada (con solución)
El individuo es una permutación de clientes; la aptitud es la inversa de la distancia total del recorrido cerrado.

```python
import numpy as np
import matplotlib.pyplot as plt
import random

rng = np.random.default_rng(5)
m = 14
coords = rng.random((m, 2)) * 100
D = np.linalg.norm(coords[:, None, :] - coords[None, :, :], axis=2)

def distancia_total(ruta):
    return sum(D[ruta[i], ruta[(i + 1) % len(ruta)]] for i in range(len(ruta)))

def cruce_ox(a, b):
    i, j = sorted(random.sample(range(m), 2))
    hijo = [None] * m
    hijo[i:j + 1] = a[i:j + 1]
    pos = (j + 1) % m
    for g in b:
        if g not in hijo:
            hijo[pos] = g; pos = (pos + 1) % m
    return hijo

def mutacion_swap(ind, pm=0.1):
    ind = ind[:]
    if random.random() < pm:
        x, y = random.sample(range(m), 2)
        ind[x], ind[y] = ind[y], ind[x]
    return ind

# Goloso: vecino más cercano desde el cliente 0
goloso = [0]
while len(goloso) < m:
    ult = goloso[-1]
    nxt = min((k for k in range(m) if k not in goloso), key=lambda k: D[ult, k])
    goloso.append(nxt)
print("Goloso distancia:", round(distancia_total(goloso), 2))

TAM, GEN, ELITE = 80, 120, 2
pobl = [rng.permutation(m).tolist() for _ in range(TAM)]
mejor_h = []
for _ in range(GEN):
    puntuados = sorted(pobl, key=distancia_total)
    elite = puntuados[:ELITE]
    nueva = elite[:]
    while len(nueva) < TAM:
        h1, h2 = random.choice(puntuados[:TAM // 2]), random.choice(puntuados[:TAM // 2])
        c1, c2 = cruce_ox(h1, h2), cruce_ox(h2, h1)
        nueva += [mutacion_swap(c1), mutacion_swap(c2)]
    pobl = nueva[:TAM]
    mejor_h.append(min(distancia_total(i) for i in pobl))

print("GA distancia:", round(mejor_h[-1], 2))
plt.plot(mejor_h); plt.xlabel("generación"); plt.ylabel("mejor distancia"); plt.show()
# El GA con elitismo mejoró o igualó al goloso y evitó perder la mejor solución hallada.
```

## Práctica propuesta (miniproyecto)
**Miniproyecto:** resuelve el TSP con GA (elitismo, cruce OX, mutación swap) y compara con la heurística golosa.  
**Entregables:** `distancia_total`, `cruce_ox`, `mutacion_swap`, bucle con elitismo y gráfico de la ruta.  
**Criterios de evaluación:** adaptación de operadores a permutaciones y análisis de la convergencia.  
**Notebook:** [Abrir/Descargar miniproyecto](sesion05_miniproyecto.ipynb)

## Evaluación (criterios CE)
- CE6: aplica GA a un problema de permutaciones e integra elitismo y análisis de convergencia.

## Atención a la diversidad
- Refuerzo: `m=10`, `TAM=40`, `GEN=60`.
- Ampliación: estudiar la sensibilidad variando `pm` (0.05, 0.2, 0.5).

## Observaciones
- El cruce OX preserva la viabilidad de la permutación (sin repetir clientes), a diferencia del cruce de un punto.
