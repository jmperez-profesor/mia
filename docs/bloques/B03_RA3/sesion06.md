---
sesion: "06"
bloque: B03
ra: RA3
fecha_prevista: 2027-01-18
duracion: 120 min
ce: [7]
titulo: "Clasificación de texto y sentimiento"
---

# Sesión 06 · Clasificación de texto y sentimiento

## Objetivos de la sesión
- Aplicar la clasificación de texto supervisada: vectorizar y entrenar un clasificador.
- Implementar un análisis de sentimiento (positivo/negativo) con datos sintéticos.
- Interpretar las métricas básicas (precisión, matriz de confusión).
- Relacionar la clasificación con aplicaciones reales y sus sesgos (CE7).

## Contenidos
- Pipeline de clasificación: TF-IDF → modelo (regresión logística / Naive Bayes).
- Análisis de sentimiento como caso particular de clasificación.
- Conjuntos de entrenamiento/prueba y métricas de evaluación.
- Limitación: dependencia del corpus de entrenamiento y lenguaje sarcástico/ambiguio.

## Temporalización (120 min)
- **Apertura / activación (10 min):** clasificar a mano 5 reseñas para discutir reglas vs. aprendizaje automático.
- **Desarrollo (80 min):** construcción de un corpus etiquetado sintético; entrenamiento con `TfidfVectorizer` + `LogisticRegression`; evaluación con `classification_report`; mini-demostración opcional de spaCy para sentimiento (comentada).
- **Cierre y evaluación (30 min):** interpretación de errores; planteamiento del miniproyecto.

## Práctica guiada (con solución)
Creamos un corpus sintético de reseñas etiquetadas y entrenamos un clasificador de sentimiento con `sklearn`. Sin red.

```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

textos = [
    "el producto es excelente y funciona muy bien", "muy buena calidad, lo recomiendo",
    "funciona perfecto, estoy encantado", "genial, supero mis expectativas",
    "es horrible, no funciona nada", "pésimo, me arrepiento de la compra",
    "terrible experiencia, no lo compres", "defraudante, calidad muy mala",
]
etiquetas = ["positivo", "positivo", "positivo", "positivo",
             "negativo", "negativo", "negativo", "negativo"]

X_train, X_test, y_train, y_test = train_test_split(
    textos, etiquetas, test_size=0.5, random_state=42, stratify=etiquetas)

vec = TfidfVectorizer()
Xtr = vec.fit_transform(X_train)
Xte = vec.transform(X_test)

clf = LogisticRegression()
clf.fit(Xtr, y_train)

pred = clf.predict(Xte)
print(classification_report(y_test, pred, digits=3))

# Prediccion sobre nuevos ejemplos
nuevos = ["el servicio es bueno y rapido", "no me gusto, muy malo"]
print("Predicciones:", clf.predict(vec.transform(nuevos)))
```

Interpretación: con un corpus pequeño y claro el clasificador alcanza buena separación; las palabras «excelente/buena/perfecto» pesan hacia positivo y «horrible/pésimo/mala» hacia negativo. Muestra cómo el PLN resuelve una tarea real de negocio (gestión de reseñas).

## Práctica propuesta (miniproyecto)
**Miniproyecto:** «Clasificador de tickets de soporte». El alumnado crea un corpus sintético de 20–30 tickets etiquetados por categoría (facturación, técnico, cuenta) y entrena un clasificador, evaluándolo y analizando un caso mal clasificado.

**Entregables:**
- Notebook `sesion06_miniproyecto.ipynb` con el pipeline y la evaluación.
- Informe breve del caso mal clasificado y posible mejora.

**Criterios de evaluación:**
- El clasificador se entrena y evalúa correctamente (CE7: aplica PLN a una tarea real).
- Se interpretan las métricas y al menos un error.
- Se propone una mejora fundamentada.

**Notebook:** [Abrir/Descargar miniproyecto](sesion06_miniproyecto.ipynb)

## Evaluación (criterios CE)
- CE7: el alumno explica la clasificación de texto y la vincula con una aplicación (gestión de incidencias, moderación) y una limitación (sesgo del corpus).
- El notebook entrena y evalúa reproduciblemente.

## Atención a la diversidad
- Avanzado: probar Naive Bayes y comparar con regresión logística.
- Refuerzo: corpus de 16 tickets ya etiquetados y métricas facilitadas.

## Observaciones
- `sklearn` no requiere red. Para spaCy en producción: `python -m spacy download es_core_news_sm`.
- Corpus pequeño ⇒ métricas con varianza alta; útil para discutir sobreajuste.
