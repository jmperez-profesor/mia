# UD02 · Ejercicios de autoevaluación

!!! note "Cómo se corrigen"
    Resuélvelos en tu cuaderno o en un documento Markdown (buen momento para practicar el
    [Taller 1](UD02_T03_Markdown_ES.md)). Las soluciones no se publican: se corrigen y comentan en
    clase.

## A. Sistema de resolución de problemas (RA2-a)

1. Define **espacio de estados** y pon un ejemplo distinto a los de la teoría (p. ej. un ascensor,
   una partida de ajedrez, un cajero automático).
2. Enumera los **cinco requisitos** de un sistema de resolución de problemas y aplícalos al
   problema de las jarras 8-5-3.
3. Para el problema de las **8 reinas**: ¿cuántos arreglos hay sin restricciones?, ¿cuántas
   soluciones válidas existen?
4. Explica con tus palabras la diferencia entre **búsqueda en anchura** y **búsqueda en
   profundidad** (estructura de datos, completitud, optimalidad, memoria).
5. ¿Por qué **DFS no es completa** en espacios infinitos? Pon un ejemplo de problema donde se
   atascaría.
6. ¿Qué es una **heurística**? Explica cómo usa A* la función `f(n) = g(n) + h(n)`.
7. En el 8-puzzle, propón dos heurísticas admisibles y explica por qué no sobreestiman.
8. Resuelve a mano el problema de las **jarras 8-5-3** desde `[8,0,0]` hasta `[4,4,0]` indicando
   los pasos y el contenido de cada jarra.
9. ¿En qué se diferencia **A\*** de **Dijkstra**? ¿Y de la búsqueda **Greedy** (solo `h`)?
10. Dado el árbol de estados con costes: estado inicial S → A (coste 2), S → B (coste 5),
    A → G (coste 3), B → G (coste 1), calcula el camino que encuentra BFS, DFS y A* (h(G)=0).

## B. Clasificación de modelos de IA (RA2-b)

11. Completa la tabla con el tipo de modelo:

| Sistema | Paradigma | Base (conocimiento/datos) |
|---|---|---|
| Termostato con reglas | | |
| Clasificador de spam con ML | | |
| Sistema experto médico | | |
| Red neuronal para imágenes | | |

12. Diferencia **descriptivo**, **predictivo** y **prescriptivo** con un ejemplo de comercio
    electrónico para cada uno.
13. ¿Por qué «todo ML es IA, pero no toda IA es ML»? Pon dos ejemplos de IA que no sea ML.
14. Clasifica por paradigma de aprendizaje: (a) agrupar clientes sin etiquetas, (b) predecir
    abandono de un cliente, (c) un agente que aprende a jugar, (d) detectar anomalías en una red.
15. ¿Qué ventaja aporta un modelo **basado en conocimiento** frente a uno **basado en datos**?
    ¿Y la desventaja principal?

## C. Automatización de tareas (RA2-c)

16. Diferencia **RPA** de **IA** con un ejemplo concreto de cada uno.
17. Explica qué es la **automatización inteligente** y qué papel juegan la IA, el BPM y el RPA.
18. Ordena de más simple a más avanzado los **cinco tipos de agente software** y pon un ejemplo de
    cada uno.
19. Indica si cada tarea es candidata a RPA o a IA/ML y por qué:
    - Copiar datos de un Excel a un ERP cada mañana.
    - Clasificar correos de incidencias por urgencia.
    - Extraer la fecha y el importe de facturas escaneadas.
20. ¿Qué son las **tareas cognitivas** que automatiza la IA? Pon tres ejemplos, incluido al menos
    uno de reconocimiento de voz.

## D. Lógica difusa (RA2-d)

21. Diferencia **lógica booleana** y **lógica difusa**. ¿Qué es la **vaguedad** y en qué se
    distingue de la **incertidumbre**?
22. ¿Qué es una **función de pertenencia**? Dibuja (o describe) una triangular y una trapezoidal y
    di qué grado de pertenencia asignan a un valor dado.
23. Dadas dos funciones con µ_A(x)=0,8 y µ_B(x)=0,3, calcula con las operaciones de Zadeh:
    AND (min), OR (max) y NOT (1−x) para ambos.
24. Explica las **4 fases** de un sistema de inferencia difuso (fuzzificar, reglas, agregar,
    defuzzificar) y los métodos de defuzzificación más comunes.
25. Diferencia **Mamdani** de **Sugeno/TSK** y di cuál implementa `scikit-fuzzy`.
26. ¿Cuántas curvas se recomiendan por variable lingüística y por qué es importante el solape?
27. Escribe el código `scikit-fuzzy` de un controlador de **velocidad del ventilador** según la
    temperatura: antecedentes `temperatura` (0-40) con términos fresca/templada/caliente y
    consecuente `velocidad` (0-100) con baja/media/alta; tres reglas y simulación con 30 ºC.
28. Propón un caso real de razonamiento impreciso distinto a los de la teoría (por ejemplo, en
    control de tráfico o en apoyo al diagnóstico) y describe qué entradas y salidas tendría.

## E. Sistemas basados en reglas (RA2-e)

29. Describe el **ciclo reconocer-actuar** (match, resolve, act) con tus palabras.
30. ¿Qué es el **algoritmo RETE** y por qué mejora el rendimiento de un motor de reglas?
31. Diferencia **encadenamiento hacia delante** y **hacia atrás**; indica cuál usa `experta` y cuál
    usaba MYCIN.
32. ¿Qué es el **salience** y para qué sirve en la resolución de conflictos?
33. Explica por qué `experta` falla en Python 3.10+ y cuáles son las **dos soluciones** posibles.
34. Escribe un sistema `experta` que determine si una **incidencia es urgente**: si `impacto=alto`
    o `usuarios>50`, declara `critica=True` y muestra el mensaje.
35. Un sistema de recomendación basado en reglas y un sistema de recomendación basado en ML
    resuelven el mismo problema. ¿Qué pierdes y qué ganas si usas reglas en vez de ML?

## F. Adecuación del modelo (RA2-f)

36. Enumera los **cinco criterios** para elegir modelo y aplica cada uno a: predecir el fraude de
    tarjetas en tiempo real.
37. ¿Qué significa «empezar simple» y por qué el teorema **No Free Lunch** lo apoya?
38. Dado un problema de datos tabulares con 10.000 filas, ¿qué familia de modelos recomendarías
    primero y por qué?
39. Justifica si usarías reglas, ML o ambos en: (a) filtro de spam, (b) control de un semáforo,
    (c) diagnóstico de una avería con procedimiento escrito, (d) recomendación de películas.
40. Diseña un **flujo de decisión** (diagrama) para elegir entre reglas, lógica difusa, árbol de
    decisión y red neuronal.
41. Aplica los cinco criterios de adecuación del modelo (§9 de la teoría) al caso de un bot de
    Robocode: ¿qué modelo usarías para decidir el disparo, y por qué?

---
[Volver a la UD02](UD02_ES.md) · [Talleres](notebooks/UD02_N01_control_difuso.ipynb)
