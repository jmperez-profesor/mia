---
sesion: "07"
bloque: B03
ra: RA3
fecha_prevista: 2027-01-20
duracion: 120 min
ce: [7]
titulo: "Generación y LLMs"
---

# Sesión 07 · Generación y LLMs

## Objetivos de la sesión
- Distinguir generación de texto por reglas, n-gramas y modelos de lenguaje grandes (LLM).
- Conocer el concepto de «prompt» y las estrategias básicas de prompting.
- Identificar alucinaciones, sesgos y limitaciones de los LLM.
- Relacionar los LLM con aplicaciones reales y su gobernanza (CE7).

## Contenidos
- De la generación estadística (n-gramas) a los LLM basados en transformers.
- Prompting: instrucción, contexto, ejemplos (few-shot) y papel del sistema.
- Alucinaciones: por qué un LLM «inventa» y cómo mitigarlo (verificación, fuentes).
- Limitaciones: coste, privacidad, sesgos y dependencia de los datos de entrenamiento.

## Temporalización (120 min)
- **Apertura / activación (10 min):** comparar una respuesta generada por n-grama frente a una esperada de LLM sobre la misma pregunta.
- **Desarrollo (80 min):** repaso de generación n-grama ya vista; conceptualización de LLM y atención a escala; taller de prompting con plantillas; debate de alucinaciones mediante ejemplos ficticios.
- **Cierre y evaluación (30 min):** rúbrica de un buen prompt; planteamiento del miniproyecto final.

## Práctica guiada (con solución)
Reutilizamos un LM n-grama para generar texto (sin red) y, a continuación, mostramos cómo estructurar un prompt para un LLM externo. La parte de LLM queda como plantilla comentada (requiere API/red), manteniendo la sesión ejecutable offline.

```python
import random
from collections import defaultdict, Counter

# Corpus sintetico de respuestas de soporte (estilo n-grama)
oraciones = [
    "reinicie el router para solucionar la conexion",
    "compruebe su contraseña e intente de nuevo",
    "actualice la aplicacion desde la tienda",
    "contacte con soporte si el error persiste",
    "verifique su conexion antes de continuar",
]

modelo = defaultdict(Counter)
for o in oraciones:
    palabras = o.split()
    for a, b in zip(palabras, palabras[1:]):
        modelo[a][b] += 1

def generar(inicio="verifique", pasos=6):
    actual = inicio
    out = [actual]
    for _ in range(pasos):
        siguientes = modelo[actual]
        if not siguientes:
            break
        actual = random.choice(list(siguientes))
        out.append(actual)
    return " ".join(out)

random.seed(1)
print("Respuesta generada (n-grama):", generar())

# --- Prompt para LLM (requiere red/API; no se ejecuta en esta sesion) ---
prompt_plantilla = """
Eres un asistente de soporte técnico para una empresa de telecomunicaciones.
Responde en español, en menos de 50 palabras y citando pasos concretos.
Pregunta del cliente: "{pregunta}"
"""
print("\nEjemplo de prompt (no ejecutado):")
print(prompt_plantilla.format(pregunta="No tengo internet desde ayer"))
```

Interpretación: el n-grama produce respuestas plausibles pero repetitivas y sin verdadera comprensión; el prompt bien diseñado (rol + restricciones + contexto) es lo que permite a un LLM dar respuestas útiles. Se evidencia la diferencia entre «generar texto» y «entender».

## Práctica propuesta (miniproyecto)
**Miniproyecto:** «Diseño de prompts para un caso de uso». El alumnado elige un caso (atención al cliente, resumen, clasificación) y diseña 3 variantes de prompt (básico, con contexto, few-shot), discutiendo cuál es más robusta y qué alucinaciones podrían aparecer.

**Entregables:**
- Notebook `sesion07_miniproyecto.ipynb` con las plantillas de prompt y un análisis escrito.
- Tabla comparativa de las 3 variantes y riesgos identificados.

**Criterios de evaluación:**
- Los prompts son coherentes y aplicables (CE7: aplica PLN/LLM a una tarea real).
- Se identifican alucinaciones y limitaciones.
- Se propone una estrategia de mitigación.

**Notebook:** [Abrir/Descargar miniproyecto](sesion07_miniproyecto.ipynb)

## Evaluación (criterios CE)
- CE7: el alumno explica qué es un LLM y lo vincula con una aplicación y con limitaciones (alucinaciones, sesgos, privacidad).
- El análisis de prompts es crítico y fundamentado.

## Atención a la diversidad
- Avanzado: añadir evaluación automática de los prompts con un modelo disponible.
- Refuerzo: plantilla de prompt ya estructurada con huecos numerados.

## Observaciones
- La parte de LLM es conceptual/plantilla; no se conecta a APIs para mantener la sesión ejecutable sin red.
- Recomendar buenas prácticas de privacidad: no enviar datos personales a servicios externos.
