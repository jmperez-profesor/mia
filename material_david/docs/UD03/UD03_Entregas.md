# UD03 · Entregas

<!-- AUTO:notebooks inicio -->
!!! important "5 entregas en el RA3"
    Cada una se corrige con **su rúbrica**, que puedes leer antes de empezar en la propia
    tarea de Moodle. El **peso** de cada entrega está en el libro de calificaciones de
    Moodle, no aquí. La [práctica de la unidad](UD03_ActividadesGuiadas.md) no se
    entrega ni puntúa.

| Actividad | Qué es | Descargar | Abrir en Colab |
|---|---|---|---|
| [`N08` · Del texto al vector](notebooks/UD03_N08_del_texto_al_vector.ipynb) | Clasificador de reseñas desde cero · del texto al vector | [![Descargar](https://img.shields.io/badge/Descargar-.ipynb-blue?logo=jupyter)](https://raw.githubusercontent.com/martinezpenya/ModelosIA/main/docs/UD03/notebooks/UD03_N08_del_texto_al_vector.ipynb){:target="_blank"} | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/martinezpenya/ModelosIA/blob/main/docs/UD03/notebooks/UD03_N08_del_texto_al_vector.ipynb){:target="_blank"} |
| [`N09` · Clasificador de preguntas](notebooks/UD03_N09_clasificador_preguntas.ipynb) | Clasificador de preguntas entrenado y medido | [![Descargar](https://img.shields.io/badge/Descargar-.ipynb-blue?logo=jupyter)](https://raw.githubusercontent.com/martinezpenya/ModelosIA/main/docs/UD03/notebooks/UD03_N09_clasificador_preguntas.ipynb){:target="_blank"} | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/martinezpenya/ModelosIA/blob/main/docs/UD03/notebooks/UD03_N09_clasificador_preguntas.ipynb){:target="_blank"} |
| [`N10` · Análisis de sentimientos en IMDb con DistilBERT](notebooks/UD03_N10_sentimiento_imdb.ipynb) | Análisis de sentimiento en reseñas de cine | [![Descargar](https://img.shields.io/badge/Descargar-.ipynb-blue?logo=jupyter)](https://raw.githubusercontent.com/martinezpenya/ModelosIA/main/docs/UD03/notebooks/UD03_N10_sentimiento_imdb.ipynb){:target="_blank"} | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/martinezpenya/ModelosIA/blob/main/docs/UD03/notebooks/UD03_N10_sentimiento_imdb.ipynb){:target="_blank"} |
| [`N11` · Prototipo de asistente virtual](notebooks/UD03_N11_asistente_virtual.ipynb) | Sistema completo · asistente virtual por voz | [![Descargar](https://img.shields.io/badge/Descargar-.ipynb-blue?logo=jupyter)](https://raw.githubusercontent.com/martinezpenya/ModelosIA/main/docs/UD03/notebooks/UD03_N11_asistente_virtual.ipynb){:target="_blank"} | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/martinezpenya/ModelosIA/blob/main/docs/UD03/notebooks/UD03_N11_asistente_virtual.ipynb){:target="_blank"} |
| [`N12` · Un sistema de PLN de punta a punta](notebooks/UD03_N12_sistema_pln.ipynb) | Sistema completo · extractor de entidades con spaCy | [![Descargar](https://img.shields.io/badge/Descargar-.ipynb-blue?logo=jupyter)](https://raw.githubusercontent.com/martinezpenya/ModelosIA/main/docs/UD03/notebooks/UD03_N12_sistema_pln.ipynb){:target="_blank"} | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/martinezpenya/ModelosIA/blob/main/docs/UD03/notebooks/UD03_N12_sistema_pln.ipynb){:target="_blank"} |

## `N08` · Del texto al vector

Construir un clasificador que determine si una reseña es positiva o negativa, con un conjunto de datos anotado por vosotros y `scikit-learn`.

**Se entrega**: el notebook con el clasificador entrenado y evaluado, y las decisiones de anotación justificadas.

## `N09` · Clasificador de preguntas

Repite el proceso de `N02` —de la bolsa de palabras a un clasificador entrenado— sobre un conjunto de **preguntas**, en vez de noticias.

**Se entrega**: el notebook con el clasificador entrenado y evaluado, **y una sección de conclusiones** que responda: ¿qué decisiones de anotación tomaría un lingüista con este conjunto de preguntas? ¿Qué perfiles harían falta si el proyecto creciera? ¿Qué formación necesitarías tú para mejorar este sistema?

## `N10` · Análisis de sentimientos en IMDb con DistilBERT

*Transfer learning*: parte del DistilBERT de `N03` —afinado para tuits— y adáptalo a reseñas de IMDb, un dominio distinto.

**Se entrega**: el notebook con el modelo afinado y evaluado sobre las reseñas.

## `N11` · Prototipo de asistente virtual

Encadena tres modelos —voz a texto, traducción y texto a voz— en **una sola función** que reciba un audio y devuelva otro.

| Recurso | Enlace |
|---|---|
| Audio de prueba | [`OpenTheDoor.wav`](notebooks/OpenTheDoor.wav) |

**Se entrega**: el notebook con la función conjunta funcionando de punta a punta, **y una sección final** que responda: ¿qué papel tendría un lingüista revisando las transcripciones y traducciones de este asistente? ¿Qué formación necesitaría el equipo si el asistente tuviera que funcionar en varios idiomas?

## `N12` · Un sistema de PLN de punta a punta

Construir un **extractor de entidades** (NER) para textos de un dominio concreto con `spaCy`, siguiendo la metodología del CE g: tarea → datos → herramienta → implementar → evaluar → documentar.

**Se entrega**: el notebook con el extractor funcionando y evaluado, y la documentación de cada paso.
<!-- AUTO:notebooks fin -->

---
[Volver a la UD03](UD03_ES.md) · [Notebooks guiados](UD03_ActividadesGuiadas.md) · Talleres: [N08](notebooks/UD03_N08_del_texto_al_vector.ipynb) · [N12](notebooks/UD03_N12_sistema_pln.ipynb)
