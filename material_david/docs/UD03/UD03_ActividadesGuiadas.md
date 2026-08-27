# UD03 · Notebooks guiados

<!-- AUTO:notebooks inicio -->
!!! info "Práctica: se hace, no se entrega"
    7 actividades que se trabajan **en clase**, con el profesor. **No se
    entregas ni puntúas**: preparas las [entregas de la unidad](UD03_Entregas.md) y la prueba escrita del RA3.

| Actividad | Qué es | Descargar | Abrir en Colab |
|---|---|---|---|
| [`N01` · Introducción al procesamiento del lenguaje natural](notebooks/UD03_N01_introduccion_pln.ipynb) | Introducción · el pipeline de PLN de punta a punta | [![Descargar](https://img.shields.io/badge/Descargar-.ipynb-blue?logo=jupyter)](https://raw.githubusercontent.com/martinezpenya/ModelosIA/main/docs/UD03/notebooks/UD03_N01_introduccion_pln.ipynb){:target="_blank"} | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/martinezpenya/ModelosIA/blob/main/docs/UD03/notebooks/UD03_N01_introduccion_pln.ipynb){:target="_blank"} |
| [`N02` · Clasificador de noticias](notebooks/UD03_N02_clasificacion_texto_torch.ipynb) | Clasificación de texto con PyTorch | [![Descargar](https://img.shields.io/badge/Descargar-.ipynb-blue?logo=jupyter)](https://raw.githubusercontent.com/martinezpenya/ModelosIA/main/docs/UD03/notebooks/UD03_N02_clasificacion_texto_torch.ipynb){:target="_blank"} | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/martinezpenya/ModelosIA/blob/main/docs/UD03/notebooks/UD03_N02_clasificacion_texto_torch.ipynb){:target="_blank"} |
| [`N03` · Modelos de lenguaje, DistilBERT](notebooks/UD03_N03_modelos_lenguaje_distilbert.ipynb) | Modelos de lenguaje · DistilBERT | [![Descargar](https://img.shields.io/badge/Descargar-.ipynb-blue?logo=jupyter)](https://raw.githubusercontent.com/martinezpenya/ModelosIA/main/docs/UD03/notebooks/UD03_N03_modelos_lenguaje_distilbert.ipynb){:target="_blank"} | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/martinezpenya/ModelosIA/blob/main/docs/UD03/notebooks/UD03_N03_modelos_lenguaje_distilbert.ipynb){:target="_blank"} |
| [`N04` · Primeros pasos con spaCy](notebooks/UD03_N04_spacy_primeros_pasos.ipynb) | Primeros pasos con spaCy | [![Descargar](https://img.shields.io/badge/Descargar-.ipynb-blue?logo=jupyter)](https://raw.githubusercontent.com/martinezpenya/ModelosIA/main/docs/UD03/notebooks/UD03_N04_spacy_primeros_pasos.ipynb){:target="_blank"} | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/martinezpenya/ModelosIA/blob/main/docs/UD03/notebooks/UD03_N04_spacy_primeros_pasos.ipynb){:target="_blank"} |
| [`N05` · Ampliación: clasificador de géneros musicales](notebooks/UD03_N05_ampliacion_generos_musicales.ipynb) | Ampliación · clasificador de géneros musicales | [![Descargar](https://img.shields.io/badge/Descargar-.ipynb-blue?logo=jupyter)](https://raw.githubusercontent.com/martinezpenya/ModelosIA/main/docs/UD03/notebooks/UD03_N05_ampliacion_generos_musicales.ipynb){:target="_blank"} | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/martinezpenya/ModelosIA/blob/main/docs/UD03/notebooks/UD03_N05_ampliacion_generos_musicales.ipynb){:target="_blank"} |
| [`N06` · Representación de texto](notebooks/UD03_N06_representacion_texto.ipynb) | Práctica · representación de texto por dos caminos | [![Descargar](https://img.shields.io/badge/Descargar-.ipynb-blue?logo=jupyter)](https://raw.githubusercontent.com/martinezpenya/ModelosIA/main/docs/UD03/notebooks/UD03_N06_representacion_texto.ipynb){:target="_blank"} | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/martinezpenya/ModelosIA/blob/main/docs/UD03/notebooks/UD03_N06_representacion_texto.ipynb){:target="_blank"} |
| [`N07` · NLTK y Python](notebooks/UD03_N07_nltk_python.ipynb) | Práctica · etiquetado con NLTK y `cess_esp` | [![Descargar](https://img.shields.io/badge/Descargar-.ipynb-blue?logo=jupyter)](https://raw.githubusercontent.com/martinezpenya/ModelosIA/main/docs/UD03/notebooks/UD03_N07_nltk_python.ipynb){:target="_blank"} | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/martinezpenya/ModelosIA/blob/main/docs/UD03/notebooks/UD03_N07_nltk_python.ipynb){:target="_blank"} |

## `N01` · Introducción al procesamiento del lenguaje natural

Los fundamentos con `nltk` y TextBlob: tokenizar, quitar *stopwords*, etiquetar categorías gramaticales, extraer frases nominales y construir representaciones bolsa de palabras, tf-idf y *word embeddings*. !!! caution "`gensim` no instala en Python 3.14" La celda de *Word2Vec* usa `gensim`, que **todavía no publica rueda para Python 3.14** (su última versión, 4.4.0, llega hasta 3.13). En el contenedor de la unidad no pasa nada —lleva Python 3.12—, pero si trabajas con un intérprete más nuevo, esa celda concreta fallará al instalar. El resto del notebook no depende de `gensim`.

## `N02` · Clasificador de noticias

Construye un clasificador de texto **desde cero**: de la bolsa de palabras a los *word embeddings*, con un modelo de PyTorch entrenado y evaluado. Es el notebook que `N09` repite sobre datos propios.

## `N03` · Modelos de lenguaje, DistilBERT

*Transfer learning* de manual: parte de un **DistilBERT** preentrenado y lo afina para análisis de sentimiento con una base de datos de tuits. `N10` repite el proceso sobre reseñas de cine.

## `N04` · Primeros pasos con spaCy

El *pipeline* de spaCy de una sola pasada: tokenización, POS, dependencias y entidades, sobre texto en español.

## `N05` · Ampliación: clasificador de géneros musicales

Un sistema de PLN aplicado a **audio**: clasificar el género de una canción combinando `librosa` y `transformers`. Es el notebook más largo del módulo (240 celdas) y **no cuenta horas de la unidad**: queda como material de ampliación para quien quiera ir más allá de `N11`.

## `N06` · Representación de texto

Tokenizar, quitar *stopwords* y construir una bolsa de palabras y un vector tf-idf, resuelto **con NLTK y con TextBlob** — el mismo ejercicio, dos librerías.

**Qué tienes que tener al terminar**: los cuatro ejercicios resueltos por **uno** de los dos caminos —tú eliges— y una comparación breve con el otro. **No se entrega**: es práctica.

## `N07` · NLTK y Python

Procesa el corpus español anotado `cess_esp`: separa entrenamiento y prueba, reduce el conjunto de etiquetas morfosintácticas de 289 a un conjunto manejable, y valida con validación cruzada.

**Qué tienes que tener al terminar**: los seis apartados resueltos. **No se entrega**: es práctica.
<!-- AUTO:notebooks fin -->

---
[Volver a la UD03](UD03_ES.md) · [Entregas](UD03_Entregas.md)
