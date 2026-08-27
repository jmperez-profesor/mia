---
sesion: "02"
bloque: B03
ra: RA3
fecha_prevista: 2026-12-16
duracion: 120 min
ce: [7]
titulo: "Preprocesamiento de texto"
---

# Sesión 02 · Preprocesamiento de texto

## Objetivos de la sesión
- Aplicar las operaciones básicas de normalización de texto: tokenización, minúsculas, eliminación de ruido.
- Diferenciar stemming y lematización, y conocer su impacto en la representación.
- Identificar categorías gramaticales (POS) y entidades nombradas (NER) básicas.
- Relacionar el preprocesamiento con la calidad de cualquier modelo de PLN (CE7: aplicaciones y limitaciones).

## Contenidos
- Tokenización, normalización y limpieza (ruido, URLs, menciones, signos).
- Stopwords y por qué pueden ser perjudiciales o útiles según la tarea.
- Stemming vs. lematización.
- Etiquetado gramatical (POS tagging) y reconocimiento de entidades (NER).
- Nota de implementación: spaCy ofrece pipeline integrado; requiere `python -m spacy download es_core_news_sm`.

## Temporalización (120 min)
- **Apertura / activación (10 min):** reto «cuenta las palabras de este tweet» para evidenciar la necesidad de limpieza.
- **Desarrollo (80 min):** explicación de cada paso sobre textos cortos; demostración de lematización y NER (spaCy si está disponible, si no, versión con regex/reglas); cuadro comparativo stemming/lematización.
- **Cierre y evaluación (30 min):** ejercicio de clasificar tokens por categoría; entrega y revisión de criterios del miniproyecto.

## Práctica guiada (con solución)
Pipeline de preprocesamiento reproducible sin red: limpieza con expresiones regulares, tokenización, eliminación de stopwords y lematización simple mediante un diccionario (`stem`/regla mínima) para textos cortos. Se incluye un bloque opcional con spaCy comentado para quien tenga el modelo instalado.

```python
import re

texto = "Apple presentó el iPhone en 2007. Apple es una empresa de tecnología con sede en Cupertino."

# 1) Limpieza: quitamos puntuacion y pasamos a minusculas
limpio = re.sub(r"[^a-záéíóúñüA-Z0-9\s]", " ", texto.lower())

# 2) Tokenizacion simple
tokens = limpio.split()
print("Tokens:", tokens)

# 3) Stopwords minimas (sin descargas)
stopwords = {"el", "la", "los", "las", "en", "es", "una", "con", "de", "y", "se", "su", "sus"}
tokens_filtrados = [t for t in tokens if t not in stopwords]

# 4) Lematizacion aproximada con regla muy simple (ejemplo didactico)
def lematiza(t):
    reglas = {"presentó": "presentar", "empresa": "empresa", "tecnología": "tecnología"}
    return reglas.get(t, t)

lemmas = [lematiza(t) for t in tokens_filtrados]
print("Tras filtrar y lematizar:", lemmas)

# 5) NER muy basica por diccionario (sin modelo)
entidades = {"apple": "ORG", "iphone": "PRODUCT", "cupertino": "LOC"}
for t in lemmas:
    if t in entidades:
        print(f"Entidad detectada: {t} -> {entidades[t]}")
```

Resultado: se detectan `apple → ORG`, `iphone → PRODUCT` y `cupertino → LOC`, y el texto queda reducido a tokens significativos. Esto muestra cómo el preprocesamiento mejora la señal para tareas posteriores.

## Práctica propuesta (miniproyecto)
**Miniproyecto:** «Limpieza de un corpus de reseñas». Partiendo de 10–20 reseñas sintéticas embebidas, el alumnado construye una función `preprocesar(texto)` reutilizable que aplique limpieza, tokenización, filtrado de stopwords y lematización básica, y reporta cuántos tokens útiles quedan respecto al total.

**Entregables:**
- Notebook `sesion02_miniproyecto.ipynb` con la función y su aplicación al corpus.
- Tabla resumen: tokens crudos vs. tokens útiles por documento.

**Criterios de evaluación:**
- La función `preprocesar` es modular y reutilizable (CE7: aplica PLN a un corpus real).
- Se justifica la eliminación o conservación de stopwords.
- Se identifica al menos una entidad o categoría relevante.

**Notebook:** [Abrir/Descargar miniproyecto](sesion02_miniproyecto.ipynb)

## Evaluación (criterios CE)
- CE7: el alumno explica cómo el preprocesamiento afecta al resultado de un modelo y cita una limitación (p. ej. pérdida de negación al quitar stopwords).
- Se entrega la función funcional y reproducible.

## Atención a la diversidad
- Avanzado: integrar spaCy real (`es_core_news_sm`) y comparar lematización propia vs. spaCy.
- Refuerzo: proporcionar la plantilla de la función con huecos numerados.

## Observaciones
- Si se usa spaCy, recordar: `pip install spacy && python -m spacy download es_core_news_sm`.
- La lematización por diccionario es didáctica; en producción se prefiere un modelo.
