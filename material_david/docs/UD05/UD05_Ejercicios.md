# UD05 · Ejercicios de autoevaluación

!!! note "Cómo se trabajan"
    Resuélvelos en tu cuaderno o en un documento Markdown. **No se publican las soluciones**: se
    corrigen y comentan en clase. Los cinco entregables (`N15`-`N14`) son la evaluación práctica de
    la unidad y se describen en las [entregas](UD05_Entregas.md).

## A. Del conocimiento a la arquitectura (RA5-a)

1. Sitúa en la jerarquía **DIKW** estos cuatro enunciados: «37 ºC», «la temperatura corporal es
   37 ºC», «si supera 37 ºC hay fiebre» y «si hay fiebre, toma paracetamol».
2. Define qué es un **sistema experto** y en qué se diferencia de un programa tradicional.
3. Enumera los **componentes** de un sistema experto y la función de cada uno.
4. Explica el **ciclo reconocer-actuar** (match, resolve, act) con tus palabras.
5. Diferencia **encadenamiento hacia delante** y **hacia atrás**. Pon un ejemplo de problema para
   cada uno.
6. Enuncia **Modus Ponens** y **Modus Tollens** y relaciona cada uno con un tipo de encadenamiento.
7. ¿Qué son los **factores de certeza** y por qué los introdujo MYCIN?
8. ¿Por qué la **explicación** es una ventaja clave de los sistemas expertos frente al ML?
9. Dado el ejemplo de la teoría (fiebre CF 0,6 + rigidez CF 0,4), explica cómo se acumula la
   evidencia y qué diferencia hay frente a una regla binaria.

## B. Representación del conocimiento (RA5-a/b)

10. Completa la tabla con la representación del conocimiento:

    | Representación | Estructura base | Inferencia típica |
    |---|---|---|
    | Pares atributo-valor | | |
    | Reglas de producción | | |
    | Representaciones jerárquicas | | |
    | Marcos (frames) | | |
    | Lógica formal | | |
    | Redes semánticas | | |
    | Ontologías | | |

11. Escribe el mismo hecho («si llueve, coge el paraguas») en tres representaciones distintas de
    la tabla anterior.
12. ¿Cuándo conviene usar **reglas** y cuándo una **ontología**?
13. ¿Qué es el *bottleneck* de la adquisición de conocimiento y cómo afecta al desarrollo de un
    sistema experto?
14. Enumera dos sistemas expertos históricos con sus datos (reglas y precisión).

## C. Simular comportamientos con `experta` (RA5-b)

15. ¿Por qué `experta` falla en Python 3.10+ y cuál es la solución que usamos en este módulo?
16. Escribe el código de un sistema `experta` que clasifique una incidencia como crítica si
    `impacto=alto` o `usuarios>50`.
17. Escribe el código de un sistema de **clasificación de animales** (guepardo) como el de la
    teoría.
18. Explica qué hacen `engine.reset()` y `engine.run()`.
19. Propón un ámbito distinto a los vistos en clase (p. ej. hipoteca, semáforo, cultivo) y describe
    3 reglas de su sistema experto.
20. De los siete notebooks de la unidad (§6.1 de la teoría), elige dos de dominios distintos y
    explica en qué se parece su arquitectura y en qué difiere el conocimiento que codifican.

## D. Sistemas híbridos reglas/datos (RA5-b)

21. Diferencia los dos enfoques híbridos de la teoría: deducir reglas de los datos frente a mejorar
    reglas propias con aprendizaje automático.
22. ¿Qué hace **Human-Learn** que no hace un sistema experto puro?
23. ¿Qué ventaja tiene **FIGS** frente a un árbol de decisión grande, en términos de
    interpretabilidad?
24. En `UD05_N04_reglas_desde_datos_titanic.ipynb`, ¿quién escribe las reglas: el experto o el algoritmo? Justifica con lo
    que hace `FIGSClassifier`.
25. Propón un caso donde usarías **skope-rules** en vez de escribir las reglas a mano.

## E. Lógica difusa (RA5-b/d)

26. Explica la diferencia entre lógica proposicional y lógica difusa con el ejemplo de «hace frío».
27. Define **variable lingüística**, **valor lingüístico** y **función de pertenencia**, con un
    ejemplo de cada una.
28. Describe los tres pasos del funcionamiento de un sistema de razonamiento impreciso
    (fuzzificación, evaluación de reglas, desfuzzificación).
29. Con el ejemplo de las propinas: si el servicio es 9,8 y la comida 6,5, ¿por qué la propina
    resultante (19,24 €) está en la banda alta y no en la media?
30. ¿Qué tipo de función de pertenencia usarías para representar un ciclo (p. ej. la hora del día)
    y por qué las triangulares no sirven ahí?

## F. Variación de características y dinámica (RA5-c)

31. Diferencia **sensibilidad** y **robustez** de un sistema experto.
32. ¿Qué ocurre si se añaden demasiadas condiciones al antecedente de una regla crítica? ¿Y si se
    simplifica en exceso?
33. Explica el problema de la **histéresis** en un sistema de ventilación con sensor de CO y la
    solución.
34. ¿Cómo afecta **subir el umbral de certeza** de un diagnóstico a los falsos positivos y a las
    alertas tempranas?
35. ¿Qué le ocurre a la dinámica del sistema si los sensores aportan ruido? ¿Cómo lo mitigarías?

## G. Estrategias de control (RA5-d)

36. Explica qué es la **salience** y por qué se usa para reglas de emergencia.
37. ¿Qué es el **control de meta** (metarrazonamiento)? Relaciónalo con el nivel de «sabiduría» de
    la jerarquía DIKW.
38. Define las **especificaciones de respuesta** de un sistema de control: precisión, tiempo de
    asentamiento, sobreimpulso y estabilidad.
39. Resuelve el ejemplo guiado: para controlar una sala a 21 ºC con error ±0,5 ºC y sobreimpulso
    máximo 1 ºC, ¿qué controlador elegirías (PID sintonizado, experto o difuso) y por qué?

## H. Controladores inteligentes (RA5-e)

40. Describe el **lazo de control** (SP, error, controlador, actuador, planta, PV) y la fórmula del
    PID.
41. ¿Qué limitaciones tiene el PID frente a sistemas no lineales o con retraso?
42. Enumera los **cuatro tipos** de controladores inteligentes y la ventaja de cada uno sobre el
    PID.
43. Con los datos de la teoría: ¿qué mejora aportó el control difuso frente al PID en el control
    térmico (asentamiento y sobreimpulso)?
44. Explica cómo un **sistema experto puede actuar como controlador** (directo y supervisor) y qué
    ventaja aporta la explicación.
45. ¿Qué es el **MPC** (control predictivo) y por qué es proactivo?

## I. Aplicaciones y tendencias (contenidos RA5)

46. Enumera **cuatro sectores** donde se aplican sistemas expertos y un uso en cada uno.
47. ¿Qué es un **BRMS** y qué herramienta es la más conocida (Drools)?
48. ¿Qué son los **sistemas neuro-simbólicos** y qué relación tienen con los sistemas híbridos del
    bloque D?
49. ¿Qué es la **IA explicable (XAI)** y qué relación tiene con MYCIN y con el RGPD?
50. Explica el uso de **reglas como guardarraíl** del ML con un ejemplo (p. ej. LLM acotado).

## J. Caso práctico

51. Elige uno de los cinco entregables (`N15`-`N14`) y, antes de programarlo, redacta en una tabla:
    qué representación de conocimiento usarás, si es puro/híbrido/difuso, y qué especificación de
    respuesta tendría si actuara como controlador.

---
[Volver a la UD05](UD05_ES.md) · [Notebook 10](notebooks/UD05_N10_simular_sistema_experto.ipynb) · [Notebook 5](notebooks/UD05_N05_logica_difusa_propinas.ipynb) · [Notebook 8](notebooks/UD05_N08_controlador_experto.ipynb)
