---
sesion: "04"
bloque: B01
ra: RA1
fecha_prevista: 2026-10-21
duracion: 120 min
ce: [4]
titulo: "Representación del conocimiento"
---

# Sesión 04 · Representación del conocimiento

## Objetivos de la sesión
- Explicar por qué la representación del conocimiento es clave en los sistemas de IA.
- Usar grafos de conocimiento para modelar relaciones empresariales.
- Implementar consultas sobre el grafo y razonar con la información representada.

## Contenidos
- Esquemas de representación: lógica, reglas, marcos (frames), grafos/ontologías.
- Grafos de conocimiento: nodos, aristas y relaciones etiquetadas.
- Consultas y razonamiento sobre el grafo (caminos, adyacencia, agregación).

## Temporalización (120 min)
- **Apertura / activación (10 min):** "¿cómo sabe una IA quién manda en tu empresa?" → necesidad de representar relaciones.
- **Desarrollo (80 min):** esquemas de representación; se resuelve la práctica guiada (grafo de empresa); alumnos arrancan su notebook.
- **Cierre y evaluación (30 min):** muestra de consultas en pizarra; rúbrica de la visualización.

## Práctica guiada (con solución)
Modelamos una empresa como grafo dirigido y resolvemos tres consultas.

```python
import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
empleados = [f"E{i}" for i in range(1, 7)]
departamentos = ["D1", "D2", "D3"]
G.add_nodes_from(empleados + departamentos)

relaciones = [
    ("E1", "D1", "pertenece_a"), ("E2", "D1", "pertenece_a"),
    ("E3", "D2", "pertenece_a"), ("E4", "D2", "pertenece_a"),
    ("E5", "D3", "pertenece_a"), ("E6", "D3", "pertenece_a"),
    ("E2", "E1", "reporta_a"), ("E4", "E3", "reporta_a"),
    ("E6", "E5", "reporta_a"), ("E1", "D1", "gestiona"),
    ("E3", "D2", "gestiona"), ("E5", "D3", "gestiona"),
]
for a, b, r in relaciones:
    G.add_edge(a, b, relation=r)

def quien_reporta_a(G, nodo):
    return [u for u, v, d in G.in_edges(nodo, data=True) if d["relation"] == "reporta_a"]

def departamento_mayor(G):
    conteo = {}
    for u, v, d in G.edges(data=True):
        if d["relation"] == "pertenece_a":
            conteo[v] = conteo.get(v, 0) + 1
    return max(conteo, key=conteo.get)

def camino_mando(G, a, b):
    try:
        return nx.shortest_path(G, a, b,
               weight=lambda u, v, d: 0 if d["relation"] == "reporta_a" else 1)
    except nx.NetworkXNoPath:
        return None

print("Reportan a E1:", quien_reporta_a(G, "E1"))
print("Departamento mayor:", departamento_mayor(G))
print("Camino E2->E1->D1:", camino_mando(G, "E2", "D1"))

pos = nx.spring_layout(G, seed=1)
nx.draw(G, pos, with_labels=True, node_color="#cfe3f2", node_size=900)
nx.draw_networkx_edge_labels(G, pos,
    edge_labels={(u, v): d["relation"] for u, v, d in G.edges(data=True)})
plt.title("Grafo de conocimiento de la empresa"); plt.show()
```

**Resultado:** `quien_reporta_a("E1")` devuelve `['E2']`; el departamento mayor se identifica por conteo; el camino de mando `E2→E1→D1` se resuelve siguiendo `reporta_a`.

## Práctica propuesta (miniproyecto)
**Miniproyecto:** modelar el organigrama y las relaciones de una empresa ficticia como grafo de conocimiento e implementar tres consultas (quién reporta a X, departamento mayor, camino de mando).

**Entregables:** grafo construido, funciones de consulta y visualización.

**Criterios de evaluación:** elige esquemas de representación adecuados; razona sobre la información.

**Notebook:** [Abrir/Descargar miniproyecto](sesion04_miniproyecto.ipynb)

## Evaluación (criterios CE)
- CE4: el alumno selecciona un esquema de representación y lo usa para razonar.

## Atención a la diversidad
- Refuerzo: plantilla de aristas ya rellena para completar solo las funciones.
- Ampliación: añadir relación `colabora_con` y consulta de caminos indirectos.

## Observaciones
- Requiere `networkx`; verificar que esté en `requirements.txt` del entorno.
