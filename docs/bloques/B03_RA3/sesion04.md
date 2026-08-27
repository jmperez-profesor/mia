---
sesion: "04"
bloque: B03
ra: RA3
fecha_prevista: 2027-01-11
duracion: 120 min
ce: [7]
titulo: "Word embeddings"
---

# Sesión 04 · Word embeddings

## Objetivos de la sesión
- Comprender qué es un word embedding y cómo representa el significado como vector denso.
- Distinguir los embeddings de la bolsa de palabras y de TF-IDF (contexto vs. frecuencia).
- Entrenar un modelo Word2Vec sobre un corpus sintético y explorar relaciones semánticas.
- Relacionar los embeddings con aplicaciones reales y sus sesgos (CE7).

## Contenidos
- De palabras discretas a vectores continuos: la hipótesis distributiva («una palabra se conoce por su contexto»).
- Modelos Word2Vec: Skip-gram y CBOW (concepto, no matemáticas profundas).
- Similitud de coseno entre palabras y analogías simples.
- Limitaciones: sesgos en los embeddings y palabras fuera de vocabulario (OOV).

## Temporalización (120 min)
- **Apertura / activación (10 min):** analogía «rey − hombre + mujer ≈ reina» para intuir el espacio vectorial.
- **Desarrollo (80 min):** entrenamiento de Word2Vec con `gensim` sobre frases sintéticas; consulta de palabras más similares; visualización 2D con PCA de un subconjunto de vectores.
- **Cierre y evaluación (30 min):** debate sobre sesgos (¿aprende estereotipos del corpus?); planteamiento del miniproyecto.

## Práctica guiada (con solución)
Entrenamos Word2Vec con `gensim` sobre un corpus sintético pequeño (frases de cocina y tecnología) y consultamos similitudes. Funciona sin red porque el corpus es propio.

```python
from gensim.models import Word2Vec
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Corpus sintetico embebido (oraciones tokenizadas)
oraciones = [
    ["cocinar", "arroz", "con", "olla"],
    ["hervir", "agua", "en", "olla"],
    ["freir", "patatas", "con", "aceite"],
    ["programar", "modelo", "con", "python"],
    ["entrenar", "modelo", "con", "datos"],
    ["cocinar", "arroz", "con", "aceite"],
    ["hervir", "arroz", "en", "olla"],
    ["programar", "datos", "con", "python"],
]

modelo = Word2Vec(sentences=oraciones, vector_size=20, window=2, min_count=1, epochs=200, seed=42)

# Palabras mas similares a 'olla'
print("Similares a 'olla':")
for palabra, score in modelo.wv.most_similar("olla", topn=3):
    print(f"  {palabra}: {score:.3f}")

# Visualizacion 2D de un subconjunto
terminos = ["olla", "arroz", "aceite", "python", "datos", "modelo"]
vectores = [modelo.wv[t] for t in terminos]
reducido = PCA(n_components=2).fit_transform(vectores)

plt.figure(figsize=(5, 4))
for nombre, (x, y) in zip(terminos, reducido):
    plt.scatter(x, y)
    plt.annotate(nombre, (x, y))
plt.title("Embeddings (PCA 2D)")
plt.tight_layout()
plt.show()
```

Interpretación: `olla` debería agruparse con términos de cocción (`arroz`, `hervir`), mientras `python`/`datos` forman el cluster de programación, mostrando que el modelo captura relaciones semánticas del contexto.

## Práctica propuesta (miniproyecto)
**Miniproyecto:** «Embeddings de un dominio». El alumnado construye un corpus sintético de 30–50 oraciones sobre un dominio elegido (videojuegos, deporte o museos) y entrena Word2Vec, reportando 3 relaciones semánticas interesantes y 1 posible sesgo.

**Entregables:**
- Notebook `sesion04_miniproyecto.ipynb` con el entrenamiento y las consultas.
- Comentario markdown con las relaciones y el sesgo detectado.

**Criterios de evaluación:**
- El modelo se entrena sobre corpus propio (CE7: aplica PLN a un dominio real).
- Se interpretan relaciones semánticas coherentes.
- Se identifica una limitación (sesgo u OOV).

**Notebook:** [Abrir/Descargar miniproyecto](sesion04_miniproyecto.ipynb)

## Evaluación (criterios CE)
- CE7: el alumno explica qué es un embedding y lo vincula con una aplicación (búsqueda, traducción) y una limitación (sesgos).
- El notebook entrena y consulta el modelo correctamente.

## Atención a la diversidad
- Avanzado: comparar `vector_size` y `window` y comentar efecto en similitudes.
- Refuerzo: corpus de 20 oraciones ya elaborado y consultas facilitadas.

## Observaciones
- `gensim` y `sklearn` no requieren red para esta práctica.
- Con corpus muy pequeño los vectores son ruidosos; sirve como demostración didáctica.
