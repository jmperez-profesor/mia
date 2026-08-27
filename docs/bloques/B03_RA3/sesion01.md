---
sesion: "01"
bloque: B03
ra: RA3
fecha_prevista: 2026-12-14
duracion: 120 min
ce: [7]
titulo: "Introducción al PLN"
---

# Sesión 01 · Introducción al PLN

## Objetivos de la sesión
- Comprender qué es el Procesamiento de Lenguaje Natural (PLN) y su papel dentro de la IA.
- Identificar los niveles de análisis del lenguaje (fonológico, morfológico, sintáctico, semántico y pragmático).
- Reconocer las aplicaciones reales del PLN y sus principales retos (ambigüedad, polisemia, variación).
- Situar el PLN dentro del alcance del RA3: relacionar la técnica con su aplicación y sus limitaciones.

## Contenidos
- Definición de PLN y su relación con lingüística computacional y aprendizaje automático.
- El «pipeline» básico: desde el texto en bruto hasta una representación útil.
- Niveles de procesamiento del lenguaje y ejemplos intuitivos.
- Aplicaciones: búsqueda, traducción, asistentes, análisis de sentimiento, resumen.
- Limitaciones y sesgos del lenguaje natural.

## Temporalización (120 min)
- **Apertura / activación (10 min):** lluvia de ideas sobre «qué puede hacer una máquina con texto» y dilema de la ambigüedad («Banco»).
- **Desarrollo (80 min):** exposición de niveles y pipeline; demostración en vivo de un contador de palabras y nube de términos sobre un texto corto; debate guiado de aplicaciones y riesgos.
- **Cierre y evaluación (30 min):** cuestionario rápido de discriminación de niveles; planteamiento del miniproyecto de la sesión y revisión de criterios de evaluación.

## Práctica guiada (con solución)
Construimos un primer análisis exploratorio de un texto corto embebido en el código: limpieza mínima, tokenización por expresión regular (sin dependencias de red) y cálculo de frecuencias para detectar palabras clave.

```python
import re
from collections import Counter

texto = (
    "El procesamiento de lenguaje natural permite a las maquinas entender el lenguaje. "
    "El lenguaje natural es ambiguo y rico en matices. "
    "Las maquinas aprenden patrones del lenguaje a partir de ejemplos."
)

# Tokenizacion basica sin red: minusculas + solo alfabeticos
tokens = re.findall(r"[a-záéíóúñü]+", texto.lower())
print("Numero de tokens:", len(tokens))

# Stopwords minimas embebidas (sin descargas)
stopwords = {"el", "las", "la", "de", "a", "y", "en", "por", "sus", "se", "es", "del", "que"}
palabras = [t for t in tokens if t not in stopwords]

frecuencias = Counter(palabras)
print("Top 5 palabras clave:")
for palabra, freq in frecuencias.most_common(5):
    print(f"  {palabra}: {freq}")

# Detectamos si el texto habla de 'lenguaje' y 'maquinas'
temas = {"lenguaje", "maquinas", "natural", "procesamiento"}
presentes = temas.intersection(palabras)
print("Temas detectados:", sorted(presentes))
```

Salida esperada (el orden de `Temas detectados` puede variar): el texto produce 22 tokens, destaca «lenguaje» (3), «maquinas» (2) y «natural» (2), y se confirma la presencia de los temas `lenguaje`, `maquinas`, `natural` y `procesamiento`. Esto ilustra el núcleo del PLN: reducir texto a unidades y patrones manejables.

## Práctica propuesta (miniproyecto)
**Miniproyecto:** «Radiografía de un corpus propio». El alumnado selecciona un corpus pequeño y propio (p. ej. 10–20 reseñas de productos, titulares o mensajes) y elabora un informe exploratorio: número de documentos, vocabulario, 10 términos más frecuentes y tres observaciones sobre ambigüedad o ruido en los datos.

**Entregables:**
- Notebook `sesion01_miniproyecto.ipynb` con el corpus embebido y el análisis.
- Comentario breve (markdown) interpretando los resultados.

**Criterios de evaluación:**
- El corpus es propio y acotado (CE7: relaciona PLN con aplicación real).
- El análisis es reproducible y los resultados se interpretan.
- Se identifica al menos una limitación del texto en bruto.

**Notebook:** [Abrir/Descargar miniproyecto](sesion01_miniproyecto.ipynb)

## Evaluación (criterios CE)
- CE7: el alumno explica qué es el PLN y lo vincula con una aplicación concreta y una limitación.
- El cuestionario de cierre distingue correctamente los niveles de análisis.

## Atención a la diversidad
- Alumnado avanzado: ampliar el corpus y añadir visualización de frecuencias (matplotlib).
- Alumnado con dificultades: plantilla de corpus ya preparada y lista de pasos numerada.

## Observaciones
- No se requieren descargas de modelos para esta sesión: la tokenización se hace con expresiones regulares.
- El miniproyecto sienta la base de datos para las sesiones posteriores (B03-R02 a B03-R08).
