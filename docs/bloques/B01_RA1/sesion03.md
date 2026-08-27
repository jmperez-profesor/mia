---
sesion: "03"
bloque: B01
ra: RA1
fecha_prevista: 2026-10-19
duracion: 120 min
ce: [4]
titulo: "Arquitecturas de agentes"
---

# Sesión 03 · Arquitecturas de agentes

## Objetivos de la sesión
- Distinguir arquitecturas de agente: reflejo simple, basada en modelo y orientada a objetivos.
- Identificar qué componentes (estado, modelo del mundo, objetivo) aporta cada una.
- Relacionar la arquitectura elegida con la eficiencia operativa en logística.

## Contenidos
- Arquitectura de reflejo simple (tabla condición→acción).
- Arquitectura basada en modelo (mantiene estado interno del mundo).
- Arquitectura orientada a objetivos (busca secuencias que cumplan un objetivo).
- Trade-off: simplicidad vs calidad de la solución.

## Temporalización (120 min)
- **Apertura / activación (10 min):** retomar el agente de limpieza y preguntar "¿y si no ve toda la habitación?" → necesidad de modelo.
- **Desarrollo (80 min):** tres arquitecturas con esquemas; se resuelve la práctica guiada (ruteo logístico); alumnos arrancan su notebook.
- **Cierre y evaluación (30 min):** gráfica comparativa de costes; rúbrica de la justificación.

## Práctica guiada (con solución)
Comparamos tres arquitecturas de agente en un problema de reparto (grafo de 8 nodos).

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(13)
NODOS = 8
distancias = np.random.randint(5, 50, size=(NODOS, NODOS))
np.fill_diagonal(distancias, 0)
distancias = (distancias + distancias.T) // 2
pedidos = [1, 3, 4, 6, 2, 7, 0, 5]

def ruta_reflejo(pedidos, dist):
    return [0] + pedidos + [0]

def ruta_modelo(pedidos, dist):
    actual, ruta, pend = 0, [0], set(pedidos)
    while pend:
        sig = min(pend, key=lambda n: dist[actual, n])
        ruta.append(sig); pend.discard(sig); actual = sig
    return ruta + [0]

def ruta_objetivo(pedidos, dist):
    # como modelo pero optimiza también el regreso al almacen (nodo 0)
    actual, ruta, pend = 0, [0], set(pedidos)
    while pend:
        sig = min(pend, key=lambda n: dist[actual, n] + dist[n, 0])
        ruta.append(sig); pend.discard(sig); actual = sig
    return ruta + [0]

def coste(ruta, dist):
    return sum(dist[ruta[i], ruta[i+1]] for i in range(len(ruta)-1))

res = {a: np.mean([coste(g(pedidos, distancias), distancias) for _ in range(20)])
       for a, g in [("Reflejo", ruta_reflejo), ("Modelo", ruta_modelo),
                    ("Objetivo", ruta_objetivo)]}
print(pd.DataFrame({"arquitectura": list(res), "coste_medio": [round(v,1) for v in res.values()]}))
plt.bar(list(res), list(res.values()), color="#4a8f3c")
plt.ylabel("Coste medio de ruta"); plt.title("Arquitecturas de agente en logística")
plt.show()
```

**Resultado:** la arquitectura de reflejo da el mayor coste (orden fijo); modelo y objetivo lo reducen, siendo objetivo la más eficiente al considerar el regreso.

## Práctica propuesta (miniproyecto)
**Miniproyecto:** implementar y comparar tres arquitecturas de agente (reflejo, modelo, objetivo) sobre un grafo logístico sintético, midiendo coste de ruta.

**Entregables:** implementación de las tres arquitecturas, gráfica de barras de coste medio y justificación escrita.

**Criterios de evaluación:** distingue componentes de cada arquitectura; argumenta arquitectura→eficiencia.

**Notebook:** [Abrir/Descargar miniproyecto](sesion03_miniproyecto.ipynb)

## Evaluación (criterios CE)
- CE4: el alumno describe estado/modelo/objetivo y argumenta la mejora de eficiencia.

## Atención a la diversidad
- Refuerzo: dibujar la ruta a mano sobre el grafo para un solo pedido.
- Ampliación: añadir una cuarta arquitectura basada en utilidad (penalizar tiempo).

## Observaciones
- Sustituir `np.random.randint` por `rng` en el notebook del alumno si se prefiere reproducibilidad estricta.
