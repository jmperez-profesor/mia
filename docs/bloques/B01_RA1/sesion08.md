---
sesion: "08"
bloque: B01
ra: RA1
fecha_prevista: 2026-11-02
duracion: 120 min
ce: [4]
titulo: "Evaluación crítica y Miniproyecto RA1"
---

# Sesión 08 · Evaluación crítica y Miniproyecto RA1

## Objetivos de la sesión
- Integrar todo el bloque B01 caracterizando sistemas de IA de forma integral.
- Entrenar un clasificador que predice el tipo de sistema a partir de sus atributos.
- Emitir una evaluación crítica de riesgos y buenas prácticas.

## Contenidos
- Caracterización integral: tipo, arquitectura, representación y eficiencia.
- Aprendizaje supervisado aplicado a la propia caracterización (árbol de decisión).
- Evaluación crítica: sesgos, explicabilidad, riesgos éticos y operativos.

## Temporalización (120 min)
- **Apertura / activación (10 min):** repaso del bloque y criterios de la rúbrica del miniproyecto.
- **Desarrollo (80 min):** se resuelve la práctica guiada (pipeline + árbol + informe); los alumnos completan su notebook capstone.
- **Cierre y evaluación (30 min):** puesta en común de informes críticos; coevaluación y cierre del RA1.

## Práctica guiada (con solución)
Pipeline de caracterización y clasificador de sistemas de IA.

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

np.random.seed(8)
n = 15
sistemas = pd.DataFrame({
    "nombre": [f"Sistema_{i:02d}" for i in range(1, n + 1)],
    "usa_reglas": np.random.randint(0, 2, n),
    "usa_ml":     np.random.randint(0, 2, n),
    "autonomo":   np.random.randint(0, 2, n),
    "simbolico":  np.random.randint(0, 2, n),
    "ganancia_pct": np.random.uniform(2, 35, n).round(1),
})
sistemas["tipo"] = np.where(sistemas["usa_ml"] == 1, "ML",
                    np.where(sistemas["usa_reglas"] == 1, "Reglas", "Hibrido"))
sistemas["arquitectura"] = np.where(sistemas["autonomo"] == 1, "Deliberativa",
                                     "Reactiva")

X = sistemas[["usa_reglas", "usa_ml", "autonomo", "simbolico"]]
y = sistemas["tipo"]
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.3, random_state=0, stratify=y)
clf = DecisionTreeClassifier(max_depth=3, random_state=0).fit(X_tr, y_tr)
print("Accuracy:", round(accuracy_score(y_te, clf.predict(X_te)), 3))
print(export_text(clf, feature_names=list(X.columns)))

sistemas.to_csv("caracterizacion_sistemas.csv", index=False)
print(sistemas[["nombre", "tipo", "arquitectura", "ganancia_pct"]])
```

**Resultado:** el árbol clasifica el tipo de sistema a partir de sus atributos y se exporta `caracterizacion_sistemas.csv`. El informe crítico (markdown) debe incluir, al menos: (1) riesgo de sesgo en datos de entrenamiento, (2) necesidad de explicabilidad en decisiones autónomas, (3) mantenimiento de la base de conocimiento, (4) supervisión humana y (5) impacto en puestos de trabajo.

## Práctica propuesta (miniproyecto)
**Miniproyecto:** integrar el bloque B01 caracterizando 15 sistemas de IA sintéticos (tipo, arquitectura, ganancia), entrenando un clasificador y redactando un informe crítico de riesgos.

**Entregables:** `caracterizacion_sistemas.csv`, clasificador con reporte de accuracy e informe crítico (3–5 viñetas).

**Criterios de evaluación:** caracteriza integralmente cada sistema; evalúa críticamente impacto y riesgos.

**Notebook:** [Abrir/Descargar miniproyecto](sesion08_miniproyecto.ipynb)

## Evaluación (criterios CE)
- CE4: el alumno caracteriza sistemas de IA y emite juicio crítico fundamentado.

## Atención a la diversidad
- Refuerzo: rúbrica desglosada con ejemplos de nivel "logro" vs "en proceso".
- Ampliación: añadir métrica de equidad al informe crítico.

## Observaciones
- Sesión de cierre de RA1: conviene reservar tiempo para la coevaluación del informe.
