---
sesion: "05"
bloque: B03
ra: RA3
fecha_prevista: 2027-01-13
duracion: 120 min
ce: [7]
titulo: "Modelos de lenguaje y transformers"
---

# Sesión 05 · Modelos de lenguaje y transformers

## Objetivos de la sesión
- Entender qué es un modelo de lenguaje (LM) y la noción de probabilidad de una secuencia.
- Conocer los modelos n-grama como base y sus limitaciones (esparcidad, contexto fijo).
- Introducir el mecanismo de atención y la arquitectura transformer de forma conceptual.
- Relacionar transformers con las aplicaciones actuales (CE7: aplicaciones y limitaciones).

## Contenidos
- Modelo de lenguaje: P(palabra | contexto) y generación.
- N-gramas: unigramas, bigramas, trigramas; suavizado intuitivo.
- De RNN/LSTM a transformers: necesidad de contexto más amplio y paralelización.
- Atención: «ponderar qué partes del contexto importan». Visión cualitativa, no matemática.
- Limitaciones: coste, necesidad de datos y riesgo de reproducir sesgos.

## Temporalización (120 min)
- **Apertura / activación (10 min):** completar frases para discutir qué palabra es más probable y por qué.
- **Desarrollo (80 min):** cálculo manual de probabilidades de bigramas sobre un corpus corto; implementación de un LM n-grama sencillo en Python; esquema visual del mecanismo de atención.
- **Cierre y evaluación (30 min):** mapa conceptual transformer (entrada → atención → salida); planteamiento del miniproyecto.

## Práctica guiada (con solución)
Construimos un modelo de lenguaje basado en bigramas con un corpus sintético y generamos texto prediciendo la palabra más probable. Todo sin red.

```python
from collections import defaultdict, Counter

# Corpus sintetico: frases de un dominio (clima)
oraciones = [
    "hace sol y calor",
    "hace viento y frio",
    "llueve y hace frio",
    "hace sol y viento",
    "nieva y hace mucho frio",
]

# Construimos conteo de bigramas (palabra_anterior -> {palabra_siguiente: conteo})
bigramas = defaultdict(Counter)
for oracion in oraciones:
    palabras = oracion.split()
    for a, b in zip(palabras, palabras[1:]):
        bigramas[a][b] += 1

def predecir(anterior):
    siguientes = bigramas[anterior]
    if not siguientes:
        return None
    return siguientes.most_common(1)[0][0]

# Generamos a partir de 'hace'
actual = "hace"
generado = [actual]
for _ in range(4):
    sig = predecir(actual)
    if sig is None:
        break
    generado.append(sig)
    actual = sig

print("Texto generado:", " ".join(generado))
```

Interpretación: el modelo aprende que tras `hace` suelen aparecer condiciones climáticas (`sol`, `viento`, `frio`…) y tras `frio` a menudo aparece `y` o termina. Ilustra el LM n-grama: predice basándose solo en el contexto inmediato, de ahí su limitación con dependencias largas (que los transformers resuelven vía atención).

## Práctica propuesta (miniproyecto)
**Miniproyecto:** «Mi primer modelo de lenguaje». El alumnado diseña un corpus sintético de 15–25 oraciones sobre un tema libre, entrena un LM n-grama (unigrama o bigrama) y genera 5 textos, analizando coherencia y limitaciones.

**Entregables:**
- Notebook `sesion05_miniproyecto.ipynb` con el entrenamiento y la generación.
- Comentario comparando n-grama con la idea de transformer.

**Criterios de evaluación:**
- El LM se entrena sobre corpus propio (CE7: aplica PLN a una tarea real).
- La generación es funcional y se analiza críticamente.
- Se explica la limitación del contexto fijo de los n-gramas.

**Notebook:** [Abrir/Descargar miniproyecto](sesion05_miniproyecto.ipynb)

## Evaluación (criterios CE)
- CE7: el alumno explica el concepto de modelo de lenguaje y lo vincula con una aplicación (autocompletado, traducción) y una limitación (contexto fijo de n-gramas vs. atención).
- El notebook genera texto reproducible.

## Atención a la diversidad
- Avanzado: implementar trigramas y medir efecto en la coherencia.
- Refuerzo: corpus de 10 oraciones y generación de 2 textos facilitada.

## Observaciones
- No se requiere red ni modelos pesados; el ejemplo es didáctico y ligero.
- La transición a transformers se hace a nivel conceptual; no se entrena un transformer real en esta sesión.
