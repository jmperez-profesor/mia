---
titulo: "S01 · Preguntas frecuentes (RA1)"
---

# S01 · Preguntas frecuentes con respuesta

> **Uso docente.** Preguntas que el alumnado suele plantear en la S01, con la respuesta que doy en clase. Van **colapsadas** (`???`): se abre una y no se pone el pasillo de respuestas delante de la pantalla.
>
> Si me preguntas algo que no está aquí, lo añado.

---

## A. Conceptos de la sesión

??? question "¿Es IA Excel? ¿Y el autocompletar de un formulario? ¿Y el antidesbordes del coche?"
    **No, no y no.** Son **automatización**, no IA: aplican reglas o cálculos que alguien programó y que se cumplen siempre igual.

    **El test que uso en clase:** *¿qué pasa si el comportamiento «aprende» o cambia con los datos sin que nadie reescriba el programa?*
    - Excel con una fórmula → no cambia → no es IA.
    - El **antidesbordes** → detección por sensor + umbral fijo → no es IA (aunque lo parezca y así lo vendan).
    - Un **recuperador de Google** que reordena resultados según lo que la gente pulsa → sí aprende → es IA.

    Ojo: el hecho de que no sea IA **no lo hace malo**. El problema es vender «IA» donde hay una fórmula de Excel.

??? question "¿Un termostato es IA? ¿Y mi lavadora?"
    **Sí, formalmente, y es IA basada en reglas (simbólica):** `si T < 18 → enciende`. Es un caso *elemental* y se incluye en la definición porque **percibe** (termómetro), **razona** (la regla) y **actúa** (enciende).

    **Mi lavadora:** su ciclo es un **programador escrito a mano** (tiempos, giros, temperatura). No razona sobre nada, solo ejecuta. Es automatización; si su sensor de carga ajustase el agua **aprendiendo** de ciclos anteriores, ya sería ML.

    *Diferencia clave:* el termostato **decide** (aplica un criterio a un estado percibido); la lavadora **ejecuta** un guion.

??? question "¿ChatGPT es ML, deep learning o generativa? ¿Es IA fuerte?"
    **Las tres cosas a la vez, en capas anidadas:** es **IA** (todas son IA) → dentro del **ML** → dentro del **deep learning** (redes con muchas capas, la arquitectura *Transformer*) → dentro de la **IA generativa** (crea texto nuevo).

    **No es IA fuerte.** Sigue siendo **débil/estrecha**: es extraordinario con texto, pero si le pides multiplicar 847×139 con el razonamiento, o leer un plano y decirte cuántas piezas hay, falla o se inventa la respuesta. No transfiere lo que sabe de una tarea a otra.

??? question "¿Todo lo que usa datos es machine learning?"
    **No.** La contabilidad usa datos y no es ML. El ML es **aprender de los datos un patrón que nadie escribió**.

    Diferencia en un ejemplo: un **listado de precios** (Excel) → aplica reglas. Un **modelo que predice el precio** de una casa a partir de 200 ventas → ML.

    Y recuerda la jerarquía: **todo ML es IA, pero no toda IA es ML** (hay IA de reglas y búsquedas que no aprende).

??? question "¿Qué diferencia hay entre clasificación, regresión y clustering? ¿Y con detección de anomalías?"
    | Técnica | Devuelve | Ejemplo | ¿Hay etiquetas? |
    |---|---|---|---|
    | **Clasificación** | Una **categoría** (spam / no spam) | Priorizar incidencias | Sí |
    | **Regresión** | Un **valor continuo** (28.400 €) | Prever demanda | Sí |
    | **Clustering** | Un **grupo** inventado (0 / 1) | Segmentar clientes | **No** |
    | **Detección de anomalías** | «Esto **se sale**» | Fraude, avería | No siempre |

    **Truco para no confundirlos:** si la respuesta es **«sí/no» o un nombre** → clasificación. Si es un **número con decimales** → regresión. Si **nadie te dio las respuestas** → clustering.

??? question "¿Por qué un chatbot no es «verdadera» inteligencia?"
    Un LLM **no entiende**: calcula, palabra a palabra, qué texto es estadísticamente más probable. Por eso:

    - Puede **alucinar**: cita un artículo que no existe con toda la naturalidad del mundo.
    - Pasa de una tarea a otra **sin transferir** nada.
    - No tiene objetivos propios ni recuerda (salvo que le des contexto).

    El **test de Turing** (1950) nos haría concluir que *sí* entiende — y ahí está su límite: mide si **engañamos**, no si **comprendemos**. Para eso está el **test de Lovelace** (2001): ¿el sistema crea algo que su propio programador no puede explicar?

??? question "¿La IA débil es peor que la fuerte? ¿Cuándo llega la fuerte?"
    **No es peor: es distinta.** Toda la IA débil que usas hoy resuelve **una** tarea con un rendimiento a veces superior al humano. La **fuerte** (AGI) ni siquiera tiene prototipo: es teórica.

    *Lo que te interesa para el RA1:* **no necesitas AGI para justificar una mejora.** Un clasificador de devoluciones con un −58 % de coste ya es un argumento de negocio completo. El salto a AGI es otro debate (y otras implicaciones éticas).

??? question "¿Cuál es el «único dilema» que decíais en clase: reglas o datos?"
    El dilema se resume en **una pregunta**: *¿puedo escribir todas las reglas del problema en una hoja?*

    | Si… | Entonces… | Ejemplo |
    |---|---|---|
    | **Sí**, las reglas caben | **Reglas** | `si T<18 → enciende`; presupuesto con casillas |
    | **No**, hay más casos de los que puedes enumerar | **Datos (ML)** | spam, fraude, diagnóstico por imagen |

    **El error a evitar:** *empezar por lo que está de moda*. Se empieza por el proceso y su complejidad.

---

## B. La práctica guiada y los ejercicios

??? question "El código me da «Precisión: 1.0». ¿Lo he hecho bien o mal?"
    **Has hecho el código bien** — y el número es correcto. Lo que hay que entender es **por qué no sirve como evidencia**:

    1. El test son solo **45 flores**; una muestra así no te dice nada de fiabilidad.
    2. Iris es un dataset **famoso y fácil**: hasta un modelo tonto acierta.

    **Qué decir en clase:** *«Precisión 1,00 con 45 casos; válido como demo, no como validación»*. Si quieres **material a las bases de datos**, pregunta por los **datos que no se han usado para entrenar** — pero eso ya es sesión de otra cosa.

??? question "¿Para qué sirve separar train y test? ¿Y para qué es ese random_state=42?"
    - **`train_test_split` (train/test):** si evalúas con los mismos datos con los que entrenaste, el modelo **se ha aprendido las respuestas** y el resultado es un espejismo. **Test = examen con preguntas nuevas.**
    - **`random_state=42`:** fija la «suerte» del reparto para que **todos repitáis exactamente el mismo resultado**. Sin él, cada ejecución cambia de reparto y tu 1,00 podría ser 0,93. No es magia: es **reproducibilidad**.
    - **`max_depth=3`:** limita la profundidad del árbol para que **no se memorice** los datos (*overfitting*).

??? question "¿Cuántos datos necesito? ¿Y cuántas etiquetas?"
    Depende de la tarea, pero órdenes de magnitud útiles:

    | Tarea | Mínimo razonable |
    |---|---|
    | Reglas escritas a mano | Ninguno (pero **tú** tienes que saber el dominio) |
    | Clasificación sencilla (tabla) | Cientos de ejemplos por clase |
    | Visión / imagen | Miles por clase |
    | LLM afinado (fine-tuning) | Miles–decenas de miles |

    **Lo que casi siempre es más importante que el volumen:** que los datos estén **limpios, representativos y etiquetados bien**. Diez mil ejemplos mal etiquetados dan peor modelo que mil bien etiquetados.

??? question "El KPI de mi proceso no se puede medir «antes». ¿Qué hago?"
    **Opciones, de mejor a peor:**

    1. **Estimar con datos de proxy:** usa el **AHT** (tiempo medio de gestión) o el **coste por documento** que ya se lleva la empresa — suele existir.
    2. **Piloto acotado:** mide *antes* en **una sucursal / una línea / dos semanas** y compara.
    3. **Benchmark externo:** cifra publicada del sector (con fuente citada) — válido si lo marcas como estimación.

    **No válido:** decir *«antes tardábamos mucho, ahora menos»*. Sin número no hay KPI, y sin KPI **no hay decisión**.

??? question "¿Puedo usar 2 KPIs? ¿Y hacer la media de ambos?"
    **Sí a los 2** (recomendado: uno de **coste** o **tiempo** + uno de **error**). **No a la media**: son unidades distintas (€/día y %), la media es una mezcla sin sentido.

    Cómo se hace bien:

    | KPI | Antes | Después | Variación |
    |---|---|---|---|
    | Coste | 600 €/día | 168 €/día | **−72 %** |
    | Error de clasificación | 15 % | 4 % | **−11 p.p.** |

    *Ojo con «p.p.»:* entre dos **porcentajes** la diferencia es en **puntos porcentuales** (15 % → 4 % = −11 p.p., no −73 %).

??? question "¿Mi sistema es IA según el artículo 3.1 del AI Act? ¿Me pueden suspender por eso?"
    Son **dos preguntas distintas**, y conviene no mezclarlas:

    1. **¿Es un sistema de IA?** (art. 3.1): basado en máquina, distinto nivel de autonomía, **puede adaptarse tras el despliegue** e **infiere** resultados (predicciones, contenido, decisiones). → Un escáner de caja **no**; un recomendador que se reentrena **sí**.
    2. **¿Está prohibido o limitado?** El AI Act clasifica por **riesgo** (prohibido / alto / limitado / mínimo), no por «qué tan IA» sea.

    *Para esta sesión:* basta con aplicar el **art. 3.1 a tus 3 sistemas y justificar los descartes**. La clasificación de riesgos la ves en otra UD.

??? question "¿Cuándo **no** hay que meter IA en un proceso?"
    **No la metas cuando:**

    - Las **reglas caben en una hoja** y son estables (una fórmula basta y es gratis).
    - **No puedes medir** el antes/después → no sabrás si ha funcionado.
    - El **coste de un fallo es enorme** y no hay supervisión humana (diagnóstico sin revisión, decisiones sobre personas).
    - **No tienes datos** ni presupuesto para conseguirlos.
    - El proceso es **el que menos duele**: arregla primero el cuello de botella real.

    La pregunta útil no es *«¿podemos usar IA?»* sino *«¿qué problema resuelve y qué número mejora?»*.

---

## C. Entregas y miniproyecto

??? question "¿La ficha de 1 minuto tiene que ser de una empresa real?"
    **Sí, de algo que exista**: de tu empresa, de LARA, del proyecto de hidrógeno, de la colmena o de un comercio que conozcas. Lo que **no** vale es un ejemplo inventado de internet, porque **no puedes averiguar su KPI** y la práctica pierde el sentido.

    *Alternativa válida si estás bloqueado:* un proceso **tuvo**, de tu centro o de tu familia (el teléfono de una tienda, la matrícula, el pedido de una farmacia), siempre con números creíbles.

??? question "¿El entregable es la ficha o el notebook del miniproyecto?"
    **El entregable es el miniproyecto único de la sesión:** ficha + KPI + decisión. El notebook que está en *Entregas* es donde lo recoges.

    - **Si tu profesor te ha indicado** la tabla de 12 sistemas → resuelve ese (Solución A o B).
    - **En cualquier caso**, el **RA1** se evalúa con la **ficha de 1 sistema real + KPI + decisión**. Si solo entregas lo primero y no hay KPI, falta el 60 % del criterio.

??? question "¿Puedo usar IA (ChatGPT) para hacer los ejercicios?"
    **Sí, si la citas y la verificas.** Lo que **no** vale es pegar la respuesta sin entenderla: la evaluación es **tu criterio**, no el del modelo.

    Recomendación práctica: pide a la IA **varias** soluciones y un **contraargumento**, y tú decides cuál queda. Cita al final: *«Consultado a ChatGPT el …, contrastado con …»*.

??? question "¿Tengo que citar las fuentes? ¿Y la IA?"
    **Sí, y con detalle mínimo:** qué, quién, cuándo y enlace. Una cifra (el 88 % de adopción, el ahorro de un caso) **sin fuente es una opinión**.

    Ejemplo corto: *AI Index Report 2026, Stanford HAI (consultado 2026-10-05).* Si la cifra viene de una IA, se cita **también la pregunta que le hiciste** y la fuente original que enlaza.

??? question "¿Cuál es el error más común en la decisión (3 líneas)?"
    Decidir **«sí» sin riesgo** o con un riesgo genérico (*«riesgo de privacidad»*). Lo que se evalúa es que el riesgo esté **atado a tu proceso** y la mitigación sea **verificable**:

    - ✗ «Podría haber problemas de privacidad.»
    - ✔ «Los correos de reclamación contienen NIF y teléfono (privacidad, RGPD): los anonimizo antes de entrenar y dejo el modelo sin texto original.»

??? question "¿Qué pasa si mi modelo falla en el tiempo? (¿eso es el drift?)"
    Sí. El **drift** es que el mundo cambia y tus datos de entrenamiento se quedan viejos: un clasificador de devoluciones entrenado en mayo falla en diciembre, cuando los motivos de devolución cambian.

    **Mitigación estándar (una línea, siempre igual):** *«Reviso el KPI cada mes; si cae por debajo de X, reentreno con los datos de los últimos 3 meses»*. Poner **frecuencia + umbral + acción** es lo que la hace creíble.

---

## D. Dudas de repaso (respuesta rápida)

??? question "¿Cuántas cosas vimos hoy?"
    **Dos.** (1) **Caracterizar** un sistema con la ficha de 1 minuto: qué percibe, si razona con reglas o datos, qué acción produce y cuál es su tarea estrecha. (2) **Decidir con 1 KPI** antes/después: coste, tiempo o error, y un riesgo.

??? question "¿Se puede ser IA y no ser ML?"
    **Sí**: un sistema experto con reglas `si… entonces…` es IA y **no aprende** de datos. Es precisamente la mitad de la tabla de la sesión.

??? question "¿Qué es un agente de IA y en qué se diferencia de un chatbot?"
    El **chatbot** responde; el **agente** **actúa**: diseña su flujo de trabajo y usa herramientas (buscar, enviar, tramitar) para lograr un objetivo. Responder vs. ejecutar.

??? question "¿Un sistema de IA puede adaptarse tras el despliegue?"
    **Sí, ese es un rasgo distintivo** del art. 3.1 del Reglamento: seguir aprendiendo *después* de ponerlo en marcha. Un programa con reglas fijas **no** se adapta: cambia solo si alguien reescribe el código.

??? question "¿La IA aporta eficiencia solo con eficiencia?"
    En esta sesión, **sí**: el RA1 se sostiene sobre **mejora medible de la eficiencia operativa**. Si el número no mejora, la conclusión es **«no compensa»** — y también es un resultado válido de la práctica.

---

## Ver también

- [Soluciones de prácticas](soluciones_s01.md) — con los códigos y las salidas reales.
- [Apuntes completos (RA1)](apuntes.md) §12–§14 — autoevaluación y glosario.
- [Ejercicios de autoevaluación](ejercicios_s01.md) · [Plan de la sesión](sesion01.md)
- [Guion de sesión con vídeo](guion_video.md)
