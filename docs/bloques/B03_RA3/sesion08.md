---
sesion: "08"
bloque: B03
ra: RA3
fecha_prevista: 2027-01-25
duracion: 120 min
ce: [7]
titulo: "Miniproyecto RA3"
---

# Sesión 08 · Miniproyecto RA3

## Objetivos de la sesión
- Integrar los conocimientos del bloque B03 en un pipeline completo de PLN.
- Aplicar preprocesamiento, representación, clasificación o embeddings a un corpus propio.
- Evaluar el resultado y reflexionar sobre aplicaciones y limitaciones (CE7).
- Elaborar la entrega final del bloque con criterios de calidad profesional.

## Contenidos
- Repaso del pipeline: texto en bruto → preprocesado → representación → modelo → evaluación.
- Elección de la tarea (clasificación de sentimiento, buscador o embeddings de dominio).
- Buenas prácticas de entrega: reproducibilidad, interpretación y ética.
- Cierre del RA3: mapa de aplicaciones y limitaciones del PLN.

## Temporalización (120 min)
- **Apertura / activación (10 min):** revisión de los entregables de sesiones previas y selección del reto final.
- **Desarrollo (80 min):** trabajo en el notebook integrador; el docente rota dando soporte; checklist de calidad (corpus propio, código reproducible, métricas, reflexión ética).
- **Cierre y evaluación (30 min):** demostración rápida de 2–3 proyectos; rúbrica de evaluación CE7; cierre del bloque.

## Práctica guiada (con solución)
Ejemplo de pipeline integrador completo (corpus sintético de reseñas) que une preprocesado, TF-IDF, clasificación y evaluación en un solo script ejecutable sin red.

```python
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# 1) Corpus sintetico embebido (texto en bruto)
bruto = [
    "El movil es fantastico y la bateria dura mucho",
    "Pesimo telefono, se calienta y la bateria falla",
    "Muy buen equipo, camara excelente y rapido",
    "Horrible, se bloquea y el servicio es malo",
    "Me encanta, funciona perfecto y es ligero",
    "Defraudante, lento y con muchos errores",
]
etiquetas = ["positivo", "negativo", "positivo", "negativo", "positivo", "negativo"]

# 2) Preprocesado minimo (limpieza sin red)
stop = {"es", "y", "el", "la", "con", "se", "de", "muy", "es", "un", "una"}
def limpiar(t):
    t = re.sub(r"[^a-záéíóúñü\s]", " ", t.lower())
    return " ".join(p for p in t.split() if p not in stop)

textos = [limpiar(t) for t in bruto]

# 3) Representacion + 4) Modelo
X_train, X_test, y_train, y_test = train_test_split(
    textos, etiquetas, test_size=0.5, random_state=42, stratify=etiquetas)

vec = TfidfVectorizer()
clf = LogisticRegression()
clf.fit(vec.fit_transform(X_train), y_train)

# 5) Evaluacion
pred = clf.predict(vec.transform(X_test))
print(classification_report(y_test, pred, digits=3))

# 6) Reflexion: limitaciones (corpus pequeño, sin negacion explícita, sesgo de léxico)
print("Limitaciones: corpus muy reducido y sesgado al léxico de opiniones cortas.")
```

Interpretación: el pipeline completo demuestra que un problema real de PLN se resuelve combinando las piezas del bloque. El informe de métricas y la reflexión final cubren el CE7 (aplicación + limitaciones).

## Práctica propuesta (miniproyecto)
**Miniproyecto:** «Proyecto integrador RA3». El alumnado elige UNA de estas opciones y entrega un notebook completo y reproducible:
1. Clasificador de sentimiento de un corpus propio (≥20 ejemplos).
2. Buscador semántico TF-IDF sobre un corpus propio (≥10 documentos).
3. Embeddings de dominio (Word2Vec) sobre un corpus propio (≥30 oraciones).

**Entregables:**
- Notebook `sesion08_miniproyecto.ipynb` con el pipeline elegido.
- Sección markdown de «Aplicación y limitaciones» (reflexión CE7).

**Criterios de evaluación:**
- El corpus es propio y el notebook reproducible (CE7).
- Se aplica correctamente al menos una técnica del bloque (preprocesado/representación/modelo).
- Se evalúa el resultado y se reflexiona sobre aplicaciones y limitaciones del PLN.

**Notebook:** [Abrir/Descargar miniproyecto](sesion08_miniproyecto.ipynb)

## Evaluación (criterios CE)
- CE7: el alumno relaciona el PLN con una aplicación concreta y expone sus limitaciones de forma fundamentada.
- Rúbrica: corpus propio (25%), código reproducible (25%), evaluación (25%), reflexión ética/aplicaciones (25%).

## Atención a la diversidad
- Avanzado: combinar dos técnicas (p. ej. embeddings + clasificador).
- Refuerzo: plantilla de notebook con secciones numeradas y corpus de apoyo.

## Observaciones
- Esta sesión es de síntesis y entrega; el docente actúa como tutoría rotatoria.
- No se requieren descargas de modelos: todo el corpus es sintético/embebido salvo que el alumno elija spaCy (opcional).
