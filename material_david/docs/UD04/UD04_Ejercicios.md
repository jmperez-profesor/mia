# UD04 · Ejercicios de autoevaluación

!!! note "Cómo se trabajan"
    Resuélvelos en tu cuaderno o en un documento Markdown. No se entregan por separado: son la
    preparación de la **prueba escrita del RA4** y de los talleres ([Notebook 4](notebooks/UD04_N04_cinematica_manipulador.ipynb) · [Notebook 11](notebooks/UD04_N11_diseno_sistema_robotizado.ipynb)). Los
    entregables evaluables son los [seis notebooks](UD04_Entregas.md).

## A. Métodos y aplicaciones de la robótica (RA4-a)

1. Define qué es un **robot** y en qué se diferencia de una máquina automática simple.
2. Clasifica los robots por tipo (manipulador, móvil con ruedas, con patas, aéreo o submarino,
   cobot) y pon un ejemplo real de cada uno.
3. Según la IFR (*World Robotics* 2025): ¿cuántos robots industriales se instalaron en 2024? ¿Cuál
   es el país líder en densidad y cuál en volumen de mercado?
4. ¿Qué posición ocupa **España** en el mercado europeo y qué sector la impulsa?
5. Explica el ciclo **percibir → procesar → actuar** con el ejemplo de un brazo que coge una pieza
   de un transportador.
6. Pon un ejemplo real con cifras de un robot de cada fabricante (KUKA, FANUC, Universal Robots,
   Amazon Robotics), indicando carga útil y alcance.
7. La unidad dice que un manipulador de una tonelada y un brazo de asistencia en silla de ruedas se
   diferencian en más que el tamaño. Explica en qué, y por qué payload y seguridad son criterios
   que a menudo se oponen.

## B. Sensores y actuadores (RA4-a)

8. Diferencia sensor **pasivo** y **activo**, con un ejemplo de cada uno. ¿Qué dos inconvenientes
   tienen los activos?
9. Clasifica estos sensores según **qué miden** (entorno, ubicación o configuración interna): lidar,
   encoder de eje, GPS, giroscopio, sensor de par, baliza wifi, cámara de tiempo de vuelo.
10. Compara **lidar**, **cámara de tiempo de vuelo** y **radar** en alcance, precisión y condiciones
    en las que cada uno gana.
11. ¿Por qué el **GPS** no sirve dentro de un almacén? ¿Qué se usa en su lugar?
12. Explica por qué la **odometría** solo es precisa en distancias cortas, y qué se combina con ella
    para corregirla.
13. Un manipulador de una tonelada tiene que enroscar una bombilla sin romperla. ¿Qué sensores lo
    hacen posible y por qué la **frecuencia de medida** es la clave?
14. Diferencia actuador **eléctrico**, **hidráulico** y **neumático**, e indica para qué se usa cada
    uno.
15. La Shadow Dexterous Hand tiene **20 actuadores** y la mayoría de la industria usa pinzas de dos
    dedos con uno. Explica el compromiso, y por qué «más grados de libertad» no es automáticamente
    mejor.

## C. Qué problema resuelve la robótica (RA4-a)

16. Justifica por qué el entorno de un robot es **no determinista**, **parcialmente observable** y
    **multiagente**, con un ejemplo de cada propiedad.
17. Explica el ejemplo del pasillo estrecho: ¿en qué colaboran el robot y la persona y en qué
    compiten? ¿Qué le pasa a un robot «demasiado educado»?
18. ¿Por qué se dice que la **función de recompensa** de un robot asistencial está en el usuario y
    no en el robot? ¿Qué problema práctico crea eso?
19. Describe la jerarquía **planificación de tareas → planificación de movimiento → control** con un
    ejemplo propio, indicando qué decide cada nivel.
20. La unidad avisa de que partir el problema en niveles **renuncia a algo**. Explica con un ejemplo
    cómo la acción podría ayudar a la percepción si no estuvieran separadas.

## D. Modelado y control cinemático (RA4-a)

21. Define **grado de libertad** y explica por qué hacen falta **≥ 6** para posición y orientación
    libres en 3D.
22. Diferencia articulación de **revolución** y **prismática**, e indica cuál es su variable.
23. Explica la diferencia entre **espacio articular** y **espacio cartesiano**.
24. ¿Qué son los **parámetros de Denavit-Hartenberg** y para qué sirven? Enumera los cuatro.
25. Dado un brazo plano 2R con `l₁ = l₂ = 1` m y `θ₁ = θ₂ = 45°`, calcula la posición del efector con
    las fórmulas de cinemática directa (cos 45° ≈ 0,707).
26. La cinemática directa tiene **una única solución** y la inversa puede tener **16**. Explica a qué
    se debe esa asimetría.
27. ¿Qué es una **singularidad**? Nombra tres tipos frecuentes en robots de 6 ejes.
28. ¿Por qué en una singularidad de muñeca las velocidades articulares tienden a infinito, y qué se
    ve en la célula cuando ocurre?
29. Explica el **desacoplamiento cinemático** (muñeca esférica) y cómo simplifica la IK.
30. Diferencia **control de posición**, **resolved-rate** y **control de impedancia**, con un ejemplo
    de uso de cada uno.
31. Ordena de menos a más los controladores **P**, **PD**, **PID** y **par calculado**, diciendo qué
    aporta cada término nuevo.
32. ¿Por qué los robots industriales usan servomotores con encoder y no motores paso a paso en lazo
    abierto?
33. Diferencia `jtraj` y `ctraj`, y di cuál usarías para mover una herramienta de corte en línea
    recta.

## E. Problemas y soluciones (RA4-b)

34. Diferencia **precisión** y **repetibilidad** (ISO 9283). ¿Por qué la precisión es crítica en
    programación offline y no tanto con *teach pendant*?
35. ¿Qué es la **calibración** de un robot y en qué orden de magnitud puede mejorar la precisión?
36. Explica la **redundancia cinemática**: cuándo aparecen infinitas soluciones y qué se hace en el
    espacio nulo del jacobiano.
37. Para ensamblar una pieza de 1,5 kg con pinza de 0,5 kg a 700 mm con ±0,1 mm, ¿elegirías un UR5e
    (5 kg / 850 mm) o un KUKA KR AGILUS (6 kg / 726 mm)? Justifica con los cuatro pasos del ejemplo
    guiado.
38. Si el *layout* de una célula obliga a cruzar una singularidad, la unidad recomienda cambiar el
    *layout* antes que el controlador. Explica por qué.

## F. Espacio de configuración y planificación (RA4-b)

39. Explica qué es el **espacio de configuración** y cuántas dimensiones tiene para: un brazo de
    6 ejes, un robot móvil en un plano, y un brazo de 7 ejes.
40. Enuncia formalmente el problema de planificación de movimiento (los cinco elementos) y explica
    por qué se llama «el problema de la mudanza del piano».
41. Compara **grafo de visibilidad** y **diagrama de Voronoi**: qué optimiza cada uno y en qué se
    paga esa elección.
42. ¿Por qué la **descomposición celular** deja de ser viable al aumentar las dimensiones, y qué se
    usa en su lugar para un brazo de 6 ejes?
43. Explica la diferencia entre un **plan** y una **política**, e indica cuál de los dos son las
    leyes de control del §6.4.
44. La robótica real planifica en cinemática y luego convierte el plan en política. Nombra las **dos
    suboptimalidades** que introduce eso y di qué técnica ataca ambas a la vez.
45. Un robot lleva una taza de café llena. ¿Cómo se expresa eso en el problema de planificación?

## G. Percepción (RA4-b)

46. Ordena por dificultad los problemas de **localización**, **mapeo** y **SLAM**, explicando qué se
    conoce en cada uno.
47. ¿Por qué SLAM parece un problema circular imposible, y cómo lo rompe el enfoque probabilístico?
48. Describe las **tres fases** de la localización de Monte Carlo con filtro de partículas. ¿Qué
    representa el robot en la fase intermedia que no podría representar si eligiera una sola
    respuesta?
49. La unidad dice que quedarse con «el estado más probable» es un atajo que a veces se rompe.
    Explica en qué situación concreta falla y por qué es peligroso.
50. Explica el ejemplo de entrar de la calle a una habitación con fluorescentes: qué cambia en las
    medidas y por qué un robot que no se readapte «creerá que ha cambiado de mundo».

## H. Aprendizaje en robótica (RA4-b)

51. ¿Por qué el aprendizaje por refuerzo funciona en simulación y falla en un robot real? Da las
    **dos** razones.
52. Explica el problema **sim-to-real** y por qué los sistemas prácticos incorporan conocimiento
    previo del robot y de la tarea.

## I. Técnicas de programación de robots (RA4-c)

53. Completa la tabla con la técnica de programación adecuada:

    | Situación | Técnica |
    |---|---|
    | Operario sin conocimientos de programación configura una trayectoria básica | |
    | Célula industrial monomarca de alta cadencia | |
    | Programar una geometría compleja sin parar la producción | |
    | Robot móvil con navegación y sensores, en investigación | |
    | Cobot que se guía tirando del brazo con la mano | |

54. Explica qué es el **teach pendant** y por qué su principal desventaja es parar la producción.
55. ¿Qué son **RAPID**, **KRL** y **URScript**? ¿Cuál se parece más a Python y cómo se envía al
    robot desde un cliente Python?
56. ¿Qué es **ROS 2** y qué elementos lo componen? ¿Para qué tipo de robots se usa?
57. ¿Por qué los cobots permiten el **guiado manual**? ¿Qué mecanismo lo hace posible?
58. Un cobot lleva un cuchillo en la pinza. ¿Es una **aplicación colaborativa**? Justifica con la
    ISO 10218:2025.
59. Para los cuatro entregables que resuelven la navegación con cámara (`N06`, `N07`, `N09`, `N10`),
    rellena una tabla con: qué escribes tú, qué decide el programa, cuántos datos necesita y si
    puedes explicar por qué el robot actuó como actuó.
60. De esas cuatro técnicas, ¿cuál elegirías para una máquina que tiene que pasar una auditoría de
    seguridad, y cuál para una que tiene que resolver un problema que nadie sabe describir con
    reglas? Justifica las dos.

## J. Humanos y robots (RA4-c, RA4-d)

61. ¿Por qué modelar a una persona como un **obstáculo móvil** no funciona? ¿Qué se gana al
    modelarla como un agente con objetivos?
62. Explica por qué el planteamiento como juego lleva al «¿qué crees que creo que crees?» y qué
    consecuencia tiene que las personas seamos **subóptimas** de forma predecible.
63. Describe la descomposición **predicción → acción** en la coordinación con personas.
64. Relaciona el problema de «aprender lo que la persona quiere» con el *specification gaming* de la
    UD06. ¿Por qué es más grave con un brazo de una tonelada?

## K. Diseño e implementación (RA4-d)

65. Enumera los cinco criterios de selección de un manipulador y una pregunta guía para cada uno.
66. Explica por qué el **payload** debe incluir la herramienta y los cables, y qué son los momentos
    de inercia de la herramienta.
67. Un robot admite 10 kg en la brida pero no 6 kg en el extremo de una herramienta larga. Explica
    la aparente contradicción.
68. Diferencia sensores **propioceptivos** y **exteroceptivos**, con dos ejemplos de cada uno.
69. ¿Qué permite la **visión** en una célula que no permiten las posiciones fijas?
70. Describe el **ciclo de vida** de un proyecto robótico en sus seis pasos.
71. ¿Qué papel juegan el **PLC** y los protocolos **OPC UA / MQTT** en una célula de Industria 4.0?
    ¿Por qué el bus del PLC tiene que ser determinista?
72. ¿Qué es un **gemelo digital** y cómo se relaciona con el mantenimiento predictivo?
73. Relaciona cada norma con lo que regula: ISO 12100, ISO 10218-1/-2, ISO/TS 15066, ISO 10218:2025,
    ISO 9283.
74. ¿Qué **dos** cosas cambia la ISO 10218:2025 respecto a la situación anterior?
75. La norma obliga a auditorías de **ciberseguridad industrial** de la célula. Explica por qué un
    robot conectado a la red de planta es una superficie de ataque, enlazando con la UD06.

## L. Simulación con Python (RA4-a, RA4-b)

76. Escribe el código con `roboticstoolbox-python` para cargar el robot **Panda**, calcular su
    cinemática directa y su inversa.
77. ¿Qué diferencia hay entre `fkine`, `ikine_LM` y `jacob0`?
78. Propón una forma de detectar si una configuración está **cerca** de una singularidad (pista:
    rango o número de condición del jacobiano).
79. Escribe con `aitk.robots` el código mínimo para crear un mundo con una imagen de fondo, colocar
    un robot con cámara y ejecutar 30 segundos de simulación con tu controlador.
80. Compara los dos simuladores de la unidad: para qué sirve cada uno y por qué no se puede usar el
    mismo para las dos cosas.

!!! note "Soluciones"
    Las soluciones no se publican: se corrigen y comentan en clase.

---
[Volver a la UD04](UD04_ES.md) · [Notebook 4](notebooks/UD04_N04_cinematica_manipulador.ipynb) · [Notebook 11](notebooks/UD04_N11_diseno_sistema_robotizado.ipynb) · [Entregables](UD04_Entregas.md)
