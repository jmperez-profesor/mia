---
sesion: "01"
bloque: B01
ra: RA1
fecha_prevista: 2026-10-05
duracion: 120 min
ce: [4]
titulo: "Introducción a la IA y tipos de sistemas"
---

# Sesión 01 · Introducción a la IA y tipos de sistemas

## Objetivos de la sesión
- Definir qué es un sistema de Inteligencia Artificial y su ciclo percepción→razonamiento→acción.
- Distinguir las grandes tipologías de sistemas de IA (simbólica, basada en reglas, aprendizaje automático, híbrida, autónoma).
- Relacionar cada tipo con un caso de aplicación en la empresa.

## Contenidos
- Concepto de IA y de sistema inteligente (principios fundamentales).
- Clasificaciones: IA débil vs fuerte; Russell & Norvig (sistemas que piensan/actúan como humanos/racionales); Hintze (reactivos, con memoria, basados en objetivos, basados en utilidad).
- Tipos de sistemas: reglas, aprendizaje automático, simbólico, híbrido, autónomo.
- Campos de aplicación y vínculo con la eficiencia operativa.

## Temporalización (120 min)
- **Apertura / activación (10 min):** debate "¿es inteligente tu lavadora?" para contrastar automatización vs inteligencia; se introduce el diagrama percepción→razonamiento→acción.
- **Desarrollo (80 min):** exposición de tipologías con ejemplos reales (spam, recomendadores, planificadores, visión); cuadro comparativo en pizarra; se presenta el miniproyecto S1 y se resuelve la práctica guiada en vivo.
- **Cierre y evaluación (30 min):** los alumnos arrancan su notebook; rúbrica rápida de la clasificación; recogida de dudas.

## Práctica guiada (con solución)
Clasificamos una tabla sintética de 12 sistemas según sus atributos. La solución completa:

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)

sistemas = pd.DataFrame({
    "nombre": [
        "FiltroSpam-EX", "DiagnosticoMed-RB", "RecomendadorShop-ML",
        "ChatbotHR-ML", "PlanificadorRutas-SYM", "DeteccionCobre-ML",
        "ReglasCredito-RB", "VisionRobot-SYM", "AsistenteVoz-ML",
        "OptimizadorRed-SYM", "ClasificadorDocs-ML", "ExpertoLegal-RB",
    ],
    "usa_reglas":     [0,1,0,0,1,0,1,1,0,1,0,1],
    "usa_ml":         [1,0,1,1,0,1,0,0,1,0,1,0],
    "es_simbolico":   [0,1,0,0,1,0,1,1,0,1,0,1],
    "requiere_datos": [1,0,1,1,0,1,0,0,1,0,1,0],
    "autonomo":       [0,0,0,0,1,1,0,1,1,1,0,0],
})

def clasificar_tipo(f):
    if f["usa_reglas"] and f["es_simbolico"]:
        base = "IA simbólica / basada en reglas"
    elif f["usa_ml"] and f["requiere_datos"]:
        base = "Aprendizaje automático"
    elif (f["usa_reglas"] or f["es_simbolico"]) and (f["usa_ml"] or f["requiere_datos"]):
        base = "Híbrido"
    else:
        base = "Otro"
    return base + (" (autónomo)" if f["autonomo"] else "")

sistemas["tipo"] = sistemas.apply(clasificar_tipo, axis=1)
print(sistemas[["nombre", "tipo"]])

conteo = sistemas["tipo"].value_counts()
plt.figure(figsize=(8, 4))
plt.bar(conteo.index, conteo.values, color="#3f7cac")
plt.xticks(rotation=30, ha="right")
plt.ylabel("Nº de sistemas")
plt.title("Reparto de sistemas por tipología")
plt.tight_layout()
plt.show()

sistemas.to_csv("sistemas_clasificados.csv", index=False)
```

**Resultado:** se obtienen 12 sistemas etiquetados (p. ej. `PlanificadorRutas-SYM` → *IA simbólica / basada en reglas (autónomo)*) y un gráfico de barras con el reparto. El CSV queda listo como entregable.

## Práctica propuesta (miniproyecto)
**Miniproyecto:** caracterizar y clasificar 12 sistemas de IA ficticios a partir de sus atributos binarios, produciendo la visualización del reparto y justificando la tipología de 3 de ellos.

**Entregables:** `sistemas_clasificados.csv`, gráfico de barras por tipo, párrafo justificando 3 sistemas.

**Criterios de evaluación:** identifica principios y tipología de sistemas inteligentes; la clasificación es coherente con los atributos.

**Notebook:** [Abrir/Descargar miniproyecto](sesion01_miniproyecto.ipynb)

## Evaluación (criterios CE)
- CE4: el alumno distingue tipos de sistemas y justifica la clasificación con criterios explícitos.

## Atención a la diversidad
- Refuerzo: plantilla de tabla con ejemplos resueltos del mundo real.
- Ampliación: añadir una dimensión propia (p. ej. "explicable") y re-clasificar.

## Observaciones
- El notebook es punto de partida: la solución completa ya se trabajó en la práctica guiada.
