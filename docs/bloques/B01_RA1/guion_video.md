# B01 · RA1 — Guion de sesión con vídeo (DotCSV)

> **Vídeo:** [¿Qué es el Machine Learning? ¿Y Deep Learning? Un mapa conceptual](https://www.youtube.com/watch?v=KytW151dpqU) · DotCSV · **duración real 7:46**.
> **Uso en clase:** troceado en 3 fragmentos e intercalado con ejercicios de los [apuntes](apuntes.md). A **1,25×** son ~6 min en total; a **1,15×**, ~6:45.

!!! warning "Marcas corregidas"
    El CSV original (`Marca-Fragmento-Quocurre-Etiquetadidctica.csv`) traía las marcas **escaladas ~2,5×** (llegaba a ~19:30). Aquí están **corregidas** con los subtítulos reales del vídeo (7:46).

## Fragmentos reales del vídeo

| Marca | Fragmento | Qué ocurre | Etiqueta didáctica |
|---|---|---|---|
| 00:00–00:35 | Presentación | Plantea la necesidad de un **mapa conceptual**: los términos IA, ML, redes neuronales, big data y deep learning se solapan | FUND-ML |
| 00:35–01:33 | ¿Qué es la IA? | Definir la IA es difícil (no hay definición única de "inteligencia"); idea común: **imitar comportamientos inteligentes** | FUND-ML |
| 01:33–02:43 | IA débil vs. fuerte | Distingue **débil** (una tarea; un robot que solo anda) y **fuerte** (dominios diversos); toda la IA actual es débil | FUND-ML ETICA |
| 02:43–03:26 | Imitación vs. cognición | **Imitar no es comprender**: programar los movimientos de un brazo no le da inteligencia | FUND-ML |
| 03:26–03:58 | Subcampos de la IA | Robótica (movimiento), **NLP** (lenguaje) y **voz** (texto↔voz) | FUND-ML NLP RL-AGENTES |
| 03:58–04:46 | El papel del Machine Learning | El ML aprende de la experiencia y **generaliza**; tres tipos: **supervisado, no supervisado y por refuerzo** | SUPERVISADO NOSUPERVISADO RL-AGENTES |
| 04:46–05:13 | ML dentro de la IA | El ML no es "otra disciplina": es **componente nuclear**. Programar acciones vs. **aprender** a realizarlas | FUND-ML |
| 05:13–05:37 | Técnicas de ML | Repaso: árboles de decisión, regresión, clasificación, clustering… | SUPERVISADO NOSUPERVISADO |
| 05:37–06:23 | Redes neuronales y deep learning | **Aprendizaje jerárquico**: capas concretas (tornillo, rueda) → abstractas (coche, camión); **deep learning** = muchas capas | DEEP-LEARNING |
| 06:23–07:27 | Big Data | La era de la información: **acumular** datos y **analizarlos** (de la captura al conocimiento); el DL como "redes vitaminadas" | FUND-ML Big Data |
| 07:27–07:46 | Cierre y mapa | **IA ⊃ ML ⊃ RN/DL**, con big data como motor | FUND-ML síntesis |

## Guion de la sesión (120 min)

| Min | Momento |
|---|---|
| 0–10 | **Apertura:** gancho *¿es inteligente tu lavadora?* + objetivos y la ficha de 1 minuto → [desarrollo literal](#apertura) |
| 10–14 | **Vídeo · fragmento 1** (00:00–03:26) a 1,25× → presentación, qué es la IA, débil/fuerte, imitación |
| 14–28 | **Ejercicio 1** (apuntes): rellena la ficha de 1 minuto de un sistema conocido + clasifícalo débil/fuerte |
| 28–32 | **Vídeo · fragmento 2** (03:26–05:37) a 1,25× → subcampos, ML, ML dentro de la IA, técnicas |
| 32–50 | **Tu esquema** IA > ML > DL > GenAI (pizarra) + **Ejercicio 2**: clasifica supervisado / no supervisado |
| 50–54 | **Vídeo · fragmento 3** (05:37–07:46) a 1,25× → RN/DL, big data, cierre y mapa |
| 54–60 | **Puesta en común** del mapa conceptual (3 preguntas orales) |
| 60–95 | **Cosa 2 · KPI**: caso de las 1.000 consultas resuelto + esquema *problema → KPI → técnica → antes/después* |
| 95–110 | **Ejercicio 3**: calcula antes/después (código del apunte o a mano) |
| 110–120 | **Cierre:** ficha + 1 riesgo + rúbrica del entregable |

!!! tip "Regla de oro"
    **Nunca dos fragmentos seguidos**: vídeo → ejercicio → vídeo. Y una **pregunta oral** tras cada corte antes de continuar.

---

## Apertura · 0–10 min {#apertura}

### 1. Gancho (0–4 min) — texto literal

**Dices:**

> «Levad la mano quien tenga una lavadora en casa. …Bien. Ahora la pregunta seria: **¿vuestra lavadora es inteligente?**»

*Deja que respondan. Casi todos dirán que sí.*

**Dices:**

> «Perfecto. Entonces **¿qué hace de “inteligente”?**»

*Espera respuestas (“se adapta”, “elige el programa sola”, “es que la compré con Wi-Fi”). Anótalas en una columna de la pizarra.*

**Dices:**

> «Vamos allá con lo que hace: tú metes ropa, agua y detergente, y ella **ejecuta el mismo guion de siempre** —tiempos, giros, temperatura—. Si le echas una manta pesada, **no “piensa” nada nuevo**: sigue exactamente el mismo programa. Esto es **automatización**, no inteligencia.»
>
> «Ahora cambiad una sola cosa: que un **sensor de carga ajuste el agua aprendiendo de los 10.000 lavados anteriores**, sin que nadie haya escrito la regla. ¿Eso ya es inteligencia? **Eso ya es IA.**»

**La frase que cierras en la pizarra y que se queda ahí toda la sesión:**

```text
¿Qué cambió?  No la lavadora: el que DECIDE.

      PERCIBE  ->  RAZONA  ->  ACTÚA
```

> «Durante los próximos 120 minutos vais a ser capaces de hacer eso con **cualquier** sistema, **en un minuto**.»

### 2. Objetivos (4–6 min) — texto literal

**Dices:**

> «Solo dos cosas hoy. **Nada más.**»

Escribe estas dos filas en la pizarra (no las leas del portátil):

| # | Objetivo | Cómo lo compruebo al final |
|---|---|---|
| **1** | **Caracterizar** cualquier sistema IA con la ficha de 1 minuto | Rellenas una ficha completa en el entregable |
| **2** | **Decidir con 1 KPI** si compensa | Calculas antes/después y dices **sí/no + 1 riesgo** |

**Dices:**

> «Lo que no entra hoy —historia, transformers, el AI Act— **queda como lectura de mapa**, no como temario de examen. Si sobra tiempo, **ampliamos por el KPI**, nunca por teoría.»

### 3. Ficha de 1 minuto (6–10 min) — plantilla para la pizarra

Escribe en la pizarra **exactamente esto**:

```text
FICHA DE 1 MINUTO  —  <sistema>

1. ¿Qué PERCIBE?               (datos de entrada)
2. ¿Razona con REGLAS o con DATOS?
3. ¿Qué ACCIÓN produce?        (qué hace al final)
4. Tarea ESTRECHA: ¿cuál?      (solo una; lo que NO hace)
```

**Rellénasela tú en directo, al lado**, con el ejemplo de los apuntes:

| Campo | Chatbot de reclamaciones |
|---|---|
| **Percibe** | El texto del correo y el historial del cliente |
| **Reglas o datos** | **Datos**: clasificador entrenado con reclamaciones etiquetadas |
| **Acción** | Enruta el caso (devolución / cambio / defecto / consulta) |
| **Tarea estrecha** | Clasificar esas 4 categorías. **No** conversa de otra cosa |

**Dices:**

> «Minuto y medio. Coged un papel, el móvil o vuestro Drive, elegid **un sistema que conozcáis de verdad** —el del curro, el del DAW, una tienda de barrio— y rellenad las 4 casillas. Quien acabe, levanta la mano.»
>
> «**No valen frases de folleto.** Si ponéis “us IA”, lo tiramos y lo volvemos a hacer.»

*Pon el temporizador en pantalla (1:30) y circula mientras responden.*

**Errores que corriges en directo al levantar las manos:**

| Lo que escriben | Por qué falla | Cómo lo enderezas |
|---|---|---|
| *«Usa IA»* en la casilla 2 | No dice **cómo** decide | «¿Alguien escribió las reglas o salió de los datos?» |
| Tarea estrecha: *«ayudar a los usuarios»* | No se puede encajar | «Si mañana os piden otra cosa, ¿el sistema la hace? Entonces no es estrecha» |
| Solo 3 casillas | Se olvida la 4 | La 4 es la más importante: **qué NO hace** |
| *«Es inteligente»* en la 3 | Describe, no actúa | «¿Qué **hace**? ¿Responde, recomienda, controla?» |

**Transición (min 10) — dices:**

> «Ahora mirad el primer fragmento: por qué esto de “IA” no está tan claro como parece.»

→ **Vídeo · fragmento 1** (00:00–03:26) · [enlace directo](https://www.youtube.com/watch?v=KytW151dpqU&t=0s)

!!! info "Materiales de estos 10 minutos"
    Pizarra con la ficha escrita antes de que entren · temporizador visible · tus objetivos ya en la pizarra · enlace al fragmento 1 abierto en una pestaña (no lo busques delante de ellos).


## Enlaces para la presentación (embed con `start`/`end`)

Incrustar en Genially / Google Slides / PowerPoint (Web):

```
Fragmento 1:  https://www.youtube.com/embed/KytW151dpqU?start=0&end=206
Fragmento 2:  https://www.youtube.com/embed/KytW151dpqU?start=206&end=337
Fragmento 3:  https://www.youtube.com/embed/KytW151dpqU?start=337&end=466
```

Enlaces para el alumnado (abrir en el minuto exacto):

- [Fragmento 1 (00:00)](https://www.youtube.com/watch?v=KytW151dpqU&t=0s) · [Fragmento 2 (03:26)](https://www.youtube.com/watch?v=KytW151dpqU&t=206s) · [Fragmento 3 (05:37)](https://www.youtube.com/watch?v=KytW151dpqU&t=337s)
