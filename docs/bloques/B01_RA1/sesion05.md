---
sesion: "05"
bloque: B01
ra: RA1
fecha_prevista: 2026-10-26
duracion: 120 min
ce: [4]
titulo: "Sistemas basados en conocimiento en la empresa"
---

# Sesión 05 · Sistemas basados en conocimiento en la empresa

## Objetivos de la sesión
- Explicar qué es un sistema basado en conocimiento (SBC) y sus componentes (base de conocimiento, motor de inferencia).
- Diseñar reglas IF–THEN para un caso empresarial (triaje de incidencias TI).
- Cuantificar cómo un SBC mejora la eficiencia operativa (menos escalado manual).

## Contenidos
- Componentes de un SBC: base de hechos, base de reglas, motor de inferencia.
- Encadenamiento hacia delante (forward chaining) y hacia atrás.
- Aplicación empresarial: help-desk, diagnóstico, cumplimiento.

## Temporalización (120 min)
- **Apertura / activación (10 min):** "¿quién resuelve tu incidencia de TI?" → automatización de triaje.
- **Desarrollo (80 min):** ciclo de un SBC; se resuelve la práctica guiada (triaje con forward chaining); alumnos arrancan su notebook.
- **Cierre y evaluación (30 min):** gráfica de reparto por nivel; rúbrica de coherencia de reglas.

## Práctica guiada (con solución)
Implementamos un motor de inferencia por forward chaining para triaje de incidencias.

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(21)
incidencias = pd.DataFrame({
    "id": range(1, 21),
    "error_login":       np.random.randint(0, 2, 20),
    "lentitud":          np.random.randint(0, 2, 20),
    "software_terceros": np.random.randint(0, 2, 20),
    "datos_criticos":    np.random.randint(0, 2, 20),
    "afecta_varios":     np.random.randint(0, 2, 20),
})

reglas = [
    ("auto_reset", {"error_login": 1}),
    ("nivel_1",    {"lentitud": 1, "software_terceros": 0}),
    ("nivel_2",    {"software_terceros": 1}),
    ("nivel_3",    {"datos_criticos": 1, "afecta_varios": 1}),
]

def inferir(fila, reglas):
    conc = []
    for conclusion, cond in reglas:
        if all(fila[k] == v for k, v in cond.items()):
            conc.append(conclusion)
    # prioridad: nivel_3 > nivel_2 > nivel_1 > auto_reset
    for c in ["nivel_3", "nivel_2", "nivel_1", "auto_reset"]:
        if c in conc:
            return c
    return "sin_clasificar"

incidencias["nivel"] = incidencias.apply(lambda r: inferir(r, reglas), axis=1)
print(incidencias["nivel"].value_counts())
auto = (incidencias["nivel"] == "auto_reset").mean() * 100
print(f"Tasa de auto-resolución: {auto:.1f}%")

incidencias["nivel"].value_counts().plot(kind="bar", color="#b5651d")
plt.ylabel("Nº incidencias"); plt.title("Reparto por nivel de soporte")
plt.show()
```

**Resultado:** se obtiene el reparto de incidencias por nivel y la tasa de auto-resolución; el gráfico evidencia cuántas incidencias resuelve automáticamente el SBC.

## Práctica propuesta (miniproyecto)
**Miniproyecto:** construir un sistema experto de triaje de incidencias TI mediante forward chaining sobre 20 incidencias sintéticas y calcular tasa de auto-resolución.

**Entregables:** base de reglas + motor, evaluación sobre el conjunto y gráfica de reparto por nivel.

**Criterios de evaluación:** identifica cómo un SBC mejora la eficiencia; aplica reglas coherentes.

**Notebook:** [Abrir/Descargar miniproyecto](sesion05_miniproyecto.ipynb)

## Evaluación (criterios CE)
- CE4: el alumno diseña reglas y explica el impacto operativo del SBC.

## Atención a la diversidad
- Refuerzo: ejemplo de una regla resuelta a mano antes de programar.
- Ampliación: añadir encadenamiento hacia atrás para una consulta concreta.

## Observaciones
- Cuidar que las reglas no se solapen de forma ambigua; documentar prioridad.
