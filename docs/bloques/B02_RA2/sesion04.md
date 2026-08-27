---
sesion: "04"
bloque: B02
ra: RA2
fecha_prevista: 2026-11-16
duracion: 120 min
ce: [6]
titulo: "Algoritmos genéticos I"
---

# Sesión 04 · Algoritmos genéticos I

## Objetivos de la sesión
- Conocer los componentes de un **algoritmo genético**: representación, fitness, selección, cruce y mutación.
- Codificar una solución binaria para el **problema de la mochila** (knapsack).
- Observar la evolución del mejor fitness por generación.

## Contenidos
- Población, individuo (genotipo) y fitness (aptitud).
- Restricción de capacidad: solución inviable penalizada o descartada.
- Selección por torneo, cruce de un punto y mutación bit-flip.
- Bucle evolutivo: evaluar → seleccionar → cruzar → mutar → reemplazar.

## Temporalización (120 min)
- **Apertura / activación (10 min):** analogía biológica (población, herencia, supervivencia); se presenta el enunciado de la mochila.
- **Desarrollo (80 min):** diseño de la representación binaria y la función fitness con restricción; codificación en vivo de selección/torneo, cruce de un punto y mutación; ejecución y gráfico del mejor fitness.
- **Cierre y evaluación (30 min):** interpretación de la convergencia; entrega del miniproyecto; rúbrica.

## Práctica guiada (con solución)
Cada individuo es una lista de bits; el fitness es el valor total si cabe en la mochila, y 0 si la supera (penalización total que fuerza a descartar inviables).

```python
import numpy as np
import matplotlib.pyplot as plt
import random

rng = np.random.default_rng(11)
n = 25
pesos = rng.integers(1, 12, size=n)
valores = rng.integers(15, 120, size=n)
CAPACIDAD = 90

def fitness(ind):
    p = sum(pesos[i] for i, b in enumerate(ind) if b)
    if p > CAPACIDAD: return 0
    return sum(valores[i] for i, b in enumerate(ind) if b)

def seleccion(pobl, k=3):
    cand = random.sample(pobl, k)
    return max(cand, key=fitness)

def cruce(a, b):
    pt = random.randrange(1, n)
    return a[:pt] + b[pt:], b[:pt] + a[pt:]

def mutacion(ind, pm=0.05):
    return [g ^ 1 if random.random() < pm else g for g in ind]

TAM, GEN = 60, 80
pobl = [rng.integers(0, 2, size=n).tolist() for _ in range(TAM)]
mejor_h = []
for _ in range(GEN):
    nueva = []
    while len(nueva) < TAM:
        h1, h2 = seleccion(pobl), seleccion(pobl)
        c1, c2 = cruce(h1, h2)
        nueva += [mutacion(c1), mutacion(c2)]
    pobl = nueva
    mejor_h.append(max(fitness(i) for i in pobl))

print("Mejor valor:", mejor_h[-1])
plt.plot(mejor_h); plt.xlabel("generación"); plt.ylabel("mejor fitness"); plt.show()
# El GA converge rápido hacia soluciones válidas de alto valor sin sobrepasar la capacidad.
```

## Práctica propuesta (miniproyecto)
**Miniproyecto:** resuelve la mochila con un GA (selección, cruce de un punto, mutación) y verifica que la mejor solución cumple la capacidad.  
**Entregables:** `fitness`, `seleccion`, `cruce`, `mutacion`, bucle evolutivo y gráfico de convergencia.  
**Criterios de evaluación:** representación binaria correcta, tratamiento de la restricción y análisis del fitness.  
**Notebook:** [Abrir/Descargar miniproyecto](sesion04_miniproyecto.ipynb)

## Evaluación (criterios CE)
- CE6: representa la solución, define el fitness con restricción y aplica operadores genéticos.

## Atención a la diversidad
- Refuerzo: `n=12`, `TAM=30`, `GEN=40` para iterar rápido.
- Ampliación: comparar penalización suave (valor − α·exceso) frente a descarte (fitness 0).

## Observaciones
- Una buena práctica es conservar siempre el mejor individuo (elitismo, que retomaremos en S05).
