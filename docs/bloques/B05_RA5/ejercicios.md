# B05 · RA5 — Ejercicios de autoevaluación

> Resuélvelos en tu cuaderno o en un documento. **No se publican las soluciones**: se corrigen y comentan en clase. Están organizados por sesión (S9, S11, S14) y adaptados de la UD05 de David Martínez Peña (CC BY-NC-SA 4.0).

## S9 · Sistemas expertos (RA5-a/c)

1. Sitúa en la jerarquía **DIKW** estos cuatro enunciados: «37 ºC», «la temperatura corporal es 37 ºC», «si supera 37 ºC hay fiebre» y «si hay fiebre, toma paracetamol».
2. Define qué es un **sistema experto** y en qué se diferencia de un programa tradicional.
3. Enumera los **componentes** de un sistema experto y la función de cada uno.
4. Explica el **ciclo reconocer-resolver-actuar** (match, resolve, act) con tus palabras.
5. Diferencia **encadenamiento hacia delante** y **hacia atrás**, con un ejemplo de cada uno.
6. Enuncia **Modus Ponens** y **Modus Tollens** y relaciónalos con el encadenamiento.
7. ¿Qué son los **factores de certeza** y por qué los introdujo MYCIN?
8. ¿Por qué la **explicación** es una ventaja clave de los sistemas expertos frente al ML?
9. Completa la tabla de **representación del conocimiento** (estructura, inferencia, ventaja y límite) para: pares atributo-valor, reglas de producción, jerarquías, marcos, lógica formal, redes semánticas y ontologías.
10. Escribe el mismo hecho («si llueve, coge el paraguas») en tres representaciones distintas.
11. ¿Qué es el *bottleneck* de la adquisición de conocimiento y cómo afecta al desarrollo?
12. Explica por qué el micro-motor de la sesión (sin resolución de conflictos) produce dos decisiones contradictorias y cómo se resuelve con `salience`.
13. ¿Por qué `experta` falla en Python 3.10+ y cuál es la solución que usamos?
14. Escribe un sistema `experta` que clasifique una incidencia como crítica si `impacto=alto` o `usuarios>50`.
15. ¿Qué es el algoritmo **RETE** y qué mejora introduce **PHREAK**?
16. ¿Cuándo usarías `clipspy` (CLIPS) en vez de `experta`?
17. Diferencia **sensibilidad** y **robustez**. ¿Qué problema causa un sensor con ruido y umbral justo, y cómo se corrige (histéresis)?

## S11 · Motores de reglas (RA5-b)

18. ¿Qué es el **decision management** y qué permite un **BRMS** que no permite el código disperso?
19. Nombra tres herramientas BRMS y en qué sector se usan.
20. Explica las *hit policies* **First**, **Unique**, **Priority** y **Collect**.
21. ¿Qué es **DMN** y por qué se dice que es el «lenguaje de negocio» de las decisiones?
22. Dada la tabla de decisión de Pagarium (importe, antigüedad, intentos → decisión), escribe qué decisión toma cada caso y detecta huecos o solapes.
23. ¿Qué es el formato **JDM** y qué motor lo usa?
24. ¿Qué diferencia hay entre usar **GoRules ZEN** y **`rule-engine`** (Python)?
25. ¿Qué es el **verificador de cobertura** y qué dos defectos detecta (huecos y solapes)?
26. Con el benchmark de la sesión (if/else ~0,1 µs, ZEN ~54 µs, CLIPS ~96 µs, `experta` ~190 µs), ¿en qué tres casos merece la pena un motor y en cuál no?

## S14 · Híbridos, guardarraíles y neuro-simbólico (RA5-b/d/e)

27. Diferencia los dos enfoques híbridos: **deducir reglas de los datos** frente a **integrar reglas propias con ML**.
28. ¿Qué hace **FIGS** que no hace un árbol de decisión grande, en términos de interpretabilidad?
29. En el ejemplo de FIGS sobre Pagarium, ¿quién escribe las reglas: el experto o el algoritmo? Justifica.
30. ¿Qué es un **guardarraíl** para un agente LLM? Pon un ejemplo con la función `validar_accion_llm`.
31. ¿Qué aportan los **sistemas neuro-simbólicos** (menos alucinaciones, explicabilidad, trazabilidad)? Relaciónalo con los híbridos reglas/datos.
32. ¿Qué es la **IA explicable (XAI)** y qué relación tiene con MYCIN y con el RGPD?
33. Situa el calendario del **AI Act**: prácticas prohibidas, transparencia y obligaciones de alto riesgo. ¿Por qué hay que verificarlo antes de evaluar?
34. En el **proyecto Pagarium**, describe las dos capas (reglas de negocio + guardarraíl) y los tres entregables del informe.

> **Nota:** los bloques de **lógica difusa**, **estrategias de control** y **controladores PID/inteligentes** de la UD05 de David se trabajan en otro bloque del curso.
