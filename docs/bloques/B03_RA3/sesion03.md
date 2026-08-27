---
sesion: "03"
bloque: B03
ra: RA3
fecha_prevista: 2026-12-21
duracion: 120 min
ce: [7]
titulo: "Representación de texto"
---

# Sesión 03 · Representación de texto

## Objetivos de la sesión
- Entender por qué el texto debe convertirse en vectores numéricos para ser procesado por modelos.
- Aplicar la bolsa de palabras (Bag of Words) y el esquema TF-IDF.
- Interpretar el significado de los pesos TF-IDF y su utilidad frente al conteo simple.
- Usar la similitud del coseno para comparar documentos (CE7: aplicación real del PLN).

## Contenidos
- Del texto a la matriz: vocabulario y vectorización.
- Bolsa de palabras (BoW) y n-gramas.
- TF-IDF: frecuencia de término y frecuencia inversa en documentos.
- Similitud del coseno como medida de cercanía entre documentos.
- Limitación: BoW y TF-IDF pierden el orden y el contexto.

## Temporalización (120 min)
- **Apertura / activación (10 min):** ejemplo intuitivo de «dos frases, mismo vocabulario, distinto significado» para motivar la necesidad de pesos.
- **Desarrollo (80 min):** construcción manual de una matriz TF-IDF sobre 4 documentos cortos; uso de `sklearn` (`CountVectorizer`, `TfidfVectorizer`); cálculo de similitud del coseno entre documentos.
- **Cierre y evaluación (30 min):** interpretación de qué documentos son más similares y por qué; planteamiento del miniproyecto.

## Práctica guiada (con solución)
Creamos un corpus sintético de 4 documentos y comparamos BoW frente a TF-IDF, además de medir la similitud del coseno entre el documento 0 y el resto.

```python
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

docs = [
    "el gato come pescado en la cocina",
    "el perro come carne en el jardin",
    "el gato duerme en la cocina tranquilo",
    "el coche viaja rapido por la carretera",
]

# Bolsa de palabras (conteo)
bow = CountVectorizer()
X_bow = bow.fit_transform(docs)
print("Vocabulario BoW:", bow.get_feature_names_out())

# TF-IDF
tfidf = TfidfVectorizer()
X_tfidf = tfidf.fit_transform(docs)
print("Vocabulario TF-IDF:", tfidf.get_feature_names_out())

# Similitud del coseno del doc 0 frente a los demas
sims = cosine_similarity(X_tfidf[0], X_tfidf).flatten()
for i, s in enumerate(sims):
    print(f"Similitud(doc0, doc{i}) = {s:.3f}")
```

Interpretación: el documento 0 (`gato/pescado/cocina`) será más similar al documento 2 (`gato/cocina`) que al 1 o 3, reflejando el solapamiento de términos relevantes. TF-IDF da más peso a términos discriminativos y menos a palabras vacías como `el`/`en`.

## Práctica propuesta (miniproyecto)
**Miniproyecto:** «Buscador semántico mini». El alumnado vectoriza un corpus propio de 8–12 documentos cortos con TF-IDF y, dada una consulta de prueba, devuelve los 3 documentos más similares usando la similitud del coseno.

**Entregables:**
- Notebook `sesion03_miniproyecto.ipynb` con la vectorización y la función de búsqueda.
- Listado de los resultados para al menos 2 consultas distintas.

**Criterios de evaluación:**
- El corpus se vectoriza correctamente con TF-IDF (CE7: aplica PLN a una tarea real).
- La búsqueda devuelve resultados coherentes y se explican.
- Se comenta la limitación de perder el orden de las palabras.

**Notebook:** [Abrir/Descargar miniproyecto](sesion03_miniproyecto.ipynb)

## Evaluación (criterios CE)
- CE7: el alumno explica TF-IDF y lo vincula con una aplicación (búsqueda, recomendación) y una limitación (pérdida de contexto).
- El notebook entrega resultados reproducibles.

## Atención a la diversidad
- Avanzado: añadir n-gramas (`ngram_range=(1,2)`) y comparar resultados.
- Refuerzo: corpus de 5 documentos y consulta única facilitada.

## Observaciones
- `sklearn` no requiere red para esta práctica; todo el corpus es sintético/embebido.
- Recordar que TF-IDF necesita al menos 2 documentos para calcular la frecuencia inversa.
