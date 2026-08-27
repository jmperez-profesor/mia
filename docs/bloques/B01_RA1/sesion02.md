---
sesion: "02"
bloque: B01
ra: RA1
fecha_prevista: 2026-10-07
duracion: 120 min
ce: [4]
titulo: "Agentes y entornos"
---

# Sesión 02 · Agentes y entornos

## Objetivos de la sesión
- Explicar el concepto de agente racional y su ciclo percepción→decisión→acción.
- Describir las propiedades de un entorno (observable, determinista, episódico, estático, discreto).
- Implementar una simulación simple de un agente y medir su performance.

## Contenidos
- Agente: lo que percibe, lo que actúa y la función que los une.
- Entornos: propiedades (PEAS: Performance, Environment, Actuators, Sensors).
- Medida de performance y diferencia entre agente reactivo y deliberativo (introducción).

## Temporalización (120 min)
- **Apertura / activación (10 min):** analogía del termostato vs el conductor; se presenta PEAS.
- **Desarrollo (80 min):** tipos de entorno con ejemplos; se resuelve la práctica guiada (agente de limpieza); los alumnos arrancan su notebook.
- **Cierre y evaluación (30 min):** comparativa en pizarra de agente aleatorio vs heurístico; rúbrica de la simulación.

## Práctica guiada (con solución)
Simulamos un vacuum agent en rejilla 5×5 y comparamos un agente aleatorio con uno heurístico.

```python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

np.random.seed(7)
N = 5
PASOS = 50

def simular(agente_fn, semilla=0):
    rng = np.random.default_rng(semilla)
    mundo = rng.choice([0, 1], size=(N, N))          # 1 = sucia
    pos = [0, 0]
    historia = []
    for _ in range(PASOS):
        f, c = pos
        if agente_fn == "heur":
            if mundo[f, c] == 1:
                mundo[f, c] = 0
            else:
                vecinas = [(f-1,c),(f+1,c),(f,c-1),(f,c+1)]
                vecinas = [(v[0]%N, v[1]%N) for v in vecinas]
                sucias = [v for v in vecinas if mundo[v] == 1]
                dest = sucias[0] if sucias else vecinas[rng.integers(0,4)]
                pos = list(dest)
        else:  # aleatorio
            if mundo[f, c] == 1 and rng.random() < 0.5:
                mundo[f, c] = 0
            else:
                pos = [rng.integers(0, N), rng.integers(0, N)]
        historia.append(100 * (1 - mundo.sum() / (N*N)))
    return historia

h_heur = simular("heur", 1)
h_rand = simular("rand", 1)

plt.plot(h_heur, label="Heurístico")
plt.plot(h_rand, label="Aleatorio")
plt.xlabel("Paso"); plt.ylabel("% limpio"); plt.legend()
plt.title("Performance del agente de limpieza"); plt.show()

# Media de 10 simulaciones
def media(agente_fn):
    return np.mean([simular(agente_fn, s)[-1] for s in range(10)])
print(pd.DataFrame({"agente":["Heurístico","Aleatorio"],
                    "limpio_final_medio_%":[round(media("heur"),1), round(media("rand"),1)]}))
```

**Resultado:** la curva heurística alcanza ~100% de limpieza rápidamente, mientras la aleatoria se estanca en valores bajos; la tabla confirma la superioridad de la estrategia informada.

## Práctica propuesta (miniproyecto)
**Miniproyecto:** implementar y comparar un agente de limpieza aleatorio frente a uno heurístico en una rejilla 5×5, midiendo la mejora de performance.

**Entregables:** código de simulación, gráfica de mejora y tabla comparativa de 10 simulaciones.

**Criterios de evaluación:** describe el ciclo percepto-acción; relaciona el entorno con la estrategia del agente.

**Notebook:** [Abrir/Descargar miniproyecto](sesion02_miniproyecto.ipynb)

## Evaluación (criterios CE)
- CE4: el alumno describe componentes del agente y justifica la estrategia según el entorno.

## Atención a la diversidad
- Refuerzo: depurar la simulación paso a paso con una rejilla 2×2.
- Ampliación: añadir obstáculos (celdas bloqueadas) y medir su impacto.

## Observaciones
- La solución completa está en la práctica guiada; el notebook trae solo TODOs.
