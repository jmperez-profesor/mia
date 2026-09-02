---
sesion: "08"
bloque: B01
ra: RA1
fecha_prevista: 2026-11-09
duracion: 120 min
ce: [4]
titulo: "Evaluación crítica y Miniproyecto RA1"
---

# Sesión 08 · Evaluación crítica y Miniproyecto RA1

> **Cierre de B01** — integramos todo y miramos con lupa lo que falta: riesgos, ética y cómo se evalúa. Adaptado de `material_david/docs/UD01/UD01_ES.md` §§7–10, 14–15 (beneficios/riesgos, AI Act, puntos clave, FAQ, evaluación) + `artint/docs/ia/modelos/machine.md` (R y mejora continua) + `artint/docs/llm/benchmarks.md` para evaluación de generative.

## Objetivos de la sesión

Al finalizar, serás capaz de (RA1 — CE RA1-a/b/c/d):

- **Sintetizar** B01: de principios y clasificaciones a técnicas, interacciones y KPIs.
- **Evaluar críticamente** un sistema RA1 (sesgos, explicabilidad, drift, privacidad, AI Act/RGPD).
- **Defender** con datos el antes/después y preparar el **miniproyecto integrador RA1** evaluable (40 % actividades / 60 % prueba, ≥5 por RA).

## Contenidos

### 1. Lo que te llevas de B01 — en 6 frases

| Idea fuerza | En una línea |
|---|---|
| Sistema inteligente | Percibe → razona → actúa; autonomía, adaptación, decisión |
| Tres lentes | Débil/fuerte (tarea) · convencional/computacional (escuela) · Russell/Hintze (capacidades) |
| Jerarquía | **IA > ML > DL > GenAI** |
| Aprendizaje | Supervisado (clasif./regresión), no supervisado (clustering), refuerzo, semi/auto |
| Vida real | Compras, buscadores, asistentes, traducción, coches, ciberseguridad |
| Interacción | Chatbot/voz/visión/agente → eficiencia si baja coste/tiempo/error medido con KPI |

Glosario y FAQ completos en `UD01_ES.md` §9–10 — úsalos como chuleta para el miniproyecto.

### 2. Beneficios, riesgos y marco — el triángulo responsable

| Beneficios (para el KPI) | Riesgos (si lo haces mal) | Marco |
|---|---|---|
| Automatiza lo repetitivo, más info de datos, menos error, 24×7, menos riesgo físico | Sesgos en datos, modelos robados/alterados, *model drift*, privacidad | **AI Act 2024/1689** por riesgo (prohibidas 02/02/2025, sanciones 02/08/2025, general 02/08/2026; sistémico si >10²⁵ FLOPS) + **RGPD** (minimización) |

Principios de **IA responsable**: explicabilidad, equidad, robustez, rendición de cuentas. Todo se profundiza en UD06; aquí basta con *nombrarlo y evaluarlo*.

!!! warning "Sesgo que se cuela"
    Si entrenas con datos con sesgo de género, el modelo lo **amplifica**. No es un bug menor, es un riesgo operativo y legal.

### 3. FAQ exprés — lo que más pregunta el alumnado

- **¿Todo con datos es ML?** No. Reglas y búsqueda heurística son IA sin ML.
- **¿IA débil vs. fuerte?** Toda la actual es débil; la fuerte es teórica.
- **¿Clasificación vs. regresión?** Categoría vs. número continuo.
- **¿DL cuándo?** Con muchos datos y tarea compleja (imagen/audio/texto); si no, árbol/KNN explicable gana.
- **¿El chatbot *entiende*?** Procesa estadísticamente y genera plausible; verifica siempre.
- **¿Sustituirá empleos?** Automatiza *tareas*, no profesiones enteras.
- **¿Predictiva vs. generativa?** Una estima, otra crea.

### 4. Cómo se evalúa RA1 — sin sorpresas

| Peso | Instrumento | Qué mira |
|---|---|---|
| **40 %** actividades | 4 talleres (media) + miniproyecto S08 | Rúbrica por tarea |
| **60 %** prueba | Test + desarrollo en Moodle | Contenido §§3–7 |

**Normativa:** se superan **todos los RA** (Orden 8/2025 art. 5.1); el centro exige **≥5 en cada RA**. Recuperación: repetir caso con datos distintos + autoevaluación.

## Práctica guiada (con solución) — en vivo

Integramos B01 en un **clasificador de tipos de sistema** y dejamos el informe crítico semi-hecho para que veas el nivel esperado.

```python
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Catálogo sintético (usa los atributos de S01)
df = pd.DataFrame({
    "usa_reglas":[1,0,1,0,1,0,1,0,1,0,1,0,1,0,1],
    "usa_ml":[0,1,0,1,0,1,0,1,0,1,0,1,0,1,0],
    "autonomo":[0,0,1,1,0,1,0,1,1,0,0,1,1,0,1],
    "simbolico":[1,0,1,0,1,0,1,0,1,0,1,0,1,0,1],
})
df["tipo"] = ["Reglas" if r else "ML" for r in df["usa_reglas"]==1]
# Pequeño truco: híbrido cuando ambos están a 1 (no ocurre aquí por construcción)

X_train, X_test, y_train, y_test = train_test_split(df.drop(columns="tipo"), df["tipo"], test_size=0.3, random_state=0, stratify=df["tipo"])
clf = DecisionTreeClassifier(max_depth=3, random_state=0).fit(X_train, y_train)
print("Accuracy:", round(accuracy_score(y_test, clf.predict(X_test)), 3))
print(export_text(clf, feature_names=list(df.columns[:-1])))

# Informe crítico — plantilla que el alumnado amplía
informe = """
**Riesgos:** sesgo en datos de entrenamiento (ej. sobrerrepresentación de casos de devolución), drift si cambia el catálogo, explicabilidad limitada en autónomos.
**Mitigaciones:** validación con test no visto, log de decisiones, revisión humana en casos de baja confianza, minimización RGPD y registro AI Act según riesgo.
**KPI:** FCR/AHT antes/después con números ficticios pero plausibles.
"""
print(informe)
```

**Salida esperada:** `Accuracy 1.0` en este toy (trivial), árbol `usa_reglas ≤0.5 → ML else Reglas`, e informe con 5 viñetas mínimas.

## Práctica propuesta (miniproyecto) — entregable RA1

**Capstone B01 (individual):** caracteriza **15 sistemas sintéticos** (los de arriba + 5 que inventes con `ganancia_pct` y `arquitectura` reactiva/deliberativa), entrena el **árbol**, exporta `caracterizacion_sistemas.csv` y redacta un **informe crítico** (300–400 palabras) que incluya: *sesgo, explicabilidad, drift, privacidad/RGPD y AI Act, supervisión humana e impacto laboral*, con **un KPI antes/después** inventado pero creíble (ej. tienda 200 reclamaciones 8 min/15 % error → 2.8 min/<5 %).

**Entregables en `sesion08_miniproyecto.ipynb`:**

1. CSV + `accuracy` + texto del árbol.
2. Informe crítico en Markdown (5 viñetas + 1 tabla KPI).

**Rúbrica (resumen):** caracteriza con criterios explícitos (tipo+escuela+Hintze+KPI) · clasifica coherentemente · crítica fundamentada (no genérica).

**Notebook:** [Abrir/Descargar miniproyecto](sesion08_miniproyecto.ipynb)

## Materiales / recursos

- **Apuntes base:** `material_david/docs/UD01/UD01_ES.md` §§7–10, 14; `artint/docs/ia/modelos/machine.md`.
- **Normativa:** AI Act 2024/1689 + RGPD (ver `UD01_ES.md` §7).
- **Glosario/FAQ:** §§9–10 de UD01.

## Evaluación (criterios CE)

- **CE RA1 (4):** integra principios, campos, técnicas e interacciones y emite juicio crítico con KPI.

## Atención a la diversidad

- **Refuerzo:** informe con huecos (`Riesgo: ___ → Mitigación: ___`).
- **Ampliación:** añade métrica de equidad (p. ej. paridad de error por grupo) al informe.

## Observaciones

- Sesión de cierre: deja 30 min para **coevaluación** rápida con rúbrica. El miniproyecto S08 es la **evidencia principal de RA1** para el 40 %.
- Si el grupo va justo, el árbol puede quedar como demo y el informe como tarea para casa (entrega en Aules).
