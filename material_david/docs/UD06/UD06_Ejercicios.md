# UD06 · Ejercicios de autoevaluación

!!! note "Cómo se trabajan"
    Resuélvelos en tu cuaderno o en un documento Markdown. **No se publican las soluciones**: se
    corrigen y comentan en clase. Los ejercicios marcados con 🗣️ son material directo para los
    **debates** de la unidad: llévalos preparados.

## A. Riesgos y deontología (RA6-a)

1. Enumera **tres riesgos** de la IA con un caso real y su dato asociado.
2. Explica la **brecha de responsabilidad** en un sistema de IA opaco.
3. El caso de **Google Photos** (2015) se «resolvió» eliminando la etiqueta «gorila». ¿Es una
   solución? Argumenta qué se perdió y qué habría hecho falta para arreglarlo de verdad.
4. Del accidente de **Uber en Tempe** (2018), identifica **cuántos fallos distintos** concurrieron y
   clasifícalos en fallos del sistema y fallos de la supervisión humana.
5. En el fallo de **Cortana con Satya Nadella**, ¿cuál fue la causa raíz? Relaciónala con una de las
   fuentes de sesgo del §9.1.
6. Explica **tres diferencias** entre depurar un programa clásico y depurar un sistema de aprendizaje
   automático. ¿Por qué no basta con que «pasen los tests»?
7. ¿Qué tres marcos deontológicos rigen la IA? Indica la aportación principal de cada uno.
8. Completa la tabla:

    | Marco | Año | Aportación principal |
    |---|---|---|
    | ACM Code of Ethics | | |
    | IEEE Ethically Aligned Design | | |
    | UNESCO · Recomendación | | |
    | Directrices éticas de la UE | | |

9. Enumera los **principios éticos** comunes a todos los marcos de IA.
10. Las Directrices de la UE dicen que una IA fiable ha de ser **lícita, ética y robusta**. Pon un
    ejemplo de sistema que cumpla dos de las tres y falle la tercera, para cada una de las tres
    combinaciones.
11. 🗣️ **Mittelstadt (2019)** critica los grandes listados de principios éticos por vagos e
    inaplicables. Elige tres principios de la lista del §4.4 y propón, para cada uno, **una forma
    concreta de medirlo** en un proyecto real.
12. De los cinco dilemas deontológicos clásicos del §4.3, elige el que te parezca **más urgente hoy**
    y defiéndelo en un párrafo con un dato.
13. 🗣️ Sobre el **futuro del trabajo**: la agricultura estadounidense pasó del 40 % al 2 % de la
    población activa en cien años. ¿Por qué se considera que el problema actual es el **ritmo** y no
    el volumen? Relaciónalo con la formación permanente.
14. El estudio de **Frey y Osborne** estimó el 47 % del empleo en riesgo, con tres barreras a la
    automatización: percepción y manipulación complejas, creatividad e inteligencia social. ¿Por qué
    hay que citarlo con cuidado en 2026?
15. Explica con el ejemplo de los **cajeros automáticos** qué es un *efecto de compensación*, y con el
    ejemplo del **desarrollador de aplicaciones** por qué la tecnología magnifica la desigualdad.

## B. Privacidad y protección de datos (RA6-b)

16. Define **dato personal**, **tratamiento**, **responsable** y **encargado** (art. 4 RGPD).
17. ¿Qué significa el principio de **minimización** y cómo se aplica al entrenamiento de modelos?
18. Enumera los **derechos ARSULIPO** y explica brevemente cada uno.
19. ¿Qué garantiza el **art. 22 del RGPD** sobre decisiones automatizadas?
20. ¿Cuál es la sanción máxima del RGPD en infracciones muy graves?
21. ¿Por qué conviene **limpiar y justificar los datos** antes de entrenar un modelo?
22. La **limitación de la finalidad** dice que los datos solo valen para el fin declarado. Una empresa
    recogió direcciones para enviar pedidos y ahora quiere entrenar un modelo de predicción de
    demanda con ellas. ¿Puede? Argumenta.
23. Indica el **plazo** que fija la LOPDGDD en cada caso: (a) supresión de imágenes de
    videovigilancia; (b) puesta a disposición judicial de esas imágenes cuando son prueba;
    (c) permanencia de un impago en un sistema de información crediticia.
24. ¿Qué es la **Lista Robinson** y qué obligación genera a quien lanza una campaña publicitaria?
25. Explica el derecho a la **desconexión digital**. ¿Se aplica en teletrabajo? ¿Qué dice la LOPDGDD
    sobre grabar imagen o sonido en vestuarios y comedores, y sobre los geolocalizadores?
26. El **art. 18.4 de la Constitución de 1978** ya limitaba «el uso de la informática». ¿Qué aporta
    ese artículo a la interpretación del RGPD hoy?
27. 🗣️ **Weizenbaum** advirtió en 1976 del riesgo de las escuchas generalizadas. ¿Qué ha cambiado
    para que la amenaza se materializara: la tecnología, el coste o la ley? Justifica.
28. ¿Por qué los marcos deontológicos concluyen que un profesional debe **negarse a trabajar** en
    determinados sistemas de vigilancia? Relaciónalo con el art. 5 del AI Act.

## C. Cumplimiento legal (RA6-c)

29. Clasifica estos sistemas según el riesgo del AI Act: (a) IA en el cribado de CV, (b) chatbot de
    atención, (c) puntuación social, (d) filtro de spam, (e) inferencia de emociones del personal en
    la oficina, (f) *deepfake* publicitario.
30. ¿Qué obligaciones tienen los sistemas de **alto riesgo** según el AI Act?
31. ¿Qué exige el **art. 50** del AI Act (transparencia)?
32. Ordena en una línea temporal las fechas del AI Act: entrada en vigor, prohibiciones, GPAI,
    aplicación general, alto riesgo del anexo III y del anexo I. ¿Cuáles **ya han pasado**?
33. ¿Cómo se canaliza hoy la **responsabilidad por daños** de la IA (qué Directiva)? ¿Qué ocurrió con
    la propuesta AILD?
34. ¿Cuándo se protege por propiedad intelectual una obra generada con IA?
35. Diferencia **verificación** de **validación**. Pon un ejemplo de sistema que esté verificado pero
    no validado.
36. Explica por qué la V&V de un sistema de aprendizaje automático es **distinta** de la de un
    programa clásico. Enumera las tres cosas que hay que verificar según el §6.3.
37. Diferencia sistema **interpretable** de sistema **explicable**. ¿Por qué se dice que una
    explicación «no es la decisión, es una historia sobre la decisión»?
38. Un banco te deniega un préstamo y te explica que es «por tu historial financiero». ¿Por qué esa
    explicación **no basta** para saber si te han discriminado? ¿Qué harías falta pedir?
39. ¿Qué es la **ley de la bandera roja** de Toby Walsh y con qué ley histórica se compara? Relaciona
    la ley de bots de California (2019) con el art. 50 del AI Act.
40. Compara los modelos de certificación posibles para la IA (Estado, IEEE, certificador
    independiente, autorregulación) señalando una ventaja y un riesgo de cada uno. ¿Qué papel juegan
    **UL** e **ISO 26262** como precedentes?
41. 🗣️ Con la tabla del §6.4, sitúa en la escalera de autonomía: mina terrestre, misil guiado, dron
    pilotado a distancia, munición merodeadora tipo Harop. ¿Dónde está exactamente la línea de la
    «plena autonomía»?
42. 🗣️ La CCW exige poder **discriminar**, juzgar la **necesidad militar** y evaluar la
    **proporcionalidad**. ¿Cuáles de las tres son hoy un problema de ingeniería resoluble y cuáles no?
    ¿Qué consecuencia legal tiene eso?
43. 🗣️ Estados Unidos **se opone** a un tratado y a la vez **su política interna excluye** el uso de
    armas autónomas, por motivos de fiabilidad. ¿Es contradictorio? Argumenta las dos posturas.
44. Explica por qué las armas autónomas se describen como **armas de destrucción masiva escalables** y
    en qué se diferencian de las nucleares desde el punto de vista del atacante.
45. ¿Qué dificulta redactar un tratado sobre IA militar, si la misma tecnología sirve para el control
    de vuelo civil? Nombra el concepto y un precedente de tratado que sí funcionó.

## D. Security by design (RA6-d)

46. Explica el concepto **security by design** en el ciclo de vida de un sistema de IA.
47. Relaciona cada ataque con su descripción:

    | Ataque | Descripción |
    |---|---|
    | Adversarial example | |
    | Envenenamiento de datos | |
    | Extracción de modelos | |
    | Fuga de datos | |
    | Prompt injection | |

48. ¿Qué es la **supervisión humana** y qué es el «botón de parada» en el AI Act?
49. Diferencia **security** de **safety** con un ejemplo de cada una. ¿Por qué el criterio RA6-d
    incluye las dos?
50. Un software es **correcto** si implementa la especificación. ¿Qué le falta para ser **seguro**?
    Explica «degradar con elegancia» con el ejemplo del coche autónomo.
51. Aplica un **FMEA** al sistema de detección de un coche autónomo: enumera al menos cuatro
    componentes, un modo de fallo por componente, su efecto y una mitigación.
52. ¿En qué se diferencia el **FTA** del FMEA y qué produce cada uno? ¿Cuál te da una probabilidad
    global de fallo?
53. Explica el problema del **robot que va a por un café** y tira las lámparas. ¿Qué es un **agente de
    bajo impacto** y con qué idea del aprendizaje automático se compara?
54. De los cuatro ejemplos de ***specification gaming*** del §7.4, elige dos y explica **qué métrica
    se optimizó** y **qué se pretendía optimizar** en realidad.
55. ¿Qué es el **problema del rey Midas** (alineación de valores)? ¿Por qué escribir «todas las
    reglas» no lo resuelve? Usa la analogía de las leyes fiscales.
56. Define **externalidad** y **tragedia de los comunes**. De los siete principios de Ostrom, elige
    tres y tradúcelos a un proyecto de IA concreto.

## E. Privacy by design (RA6-e)

57. ¿Qué obliga el **art. 25 del RGPD**? Diferencia «desde el diseño» y «por defecto».
58. Enumera las **cuatro estrategias** operativas de privacidad (AEPD) y pon un ejemplo de cada una.
59. ¿Qué es la **EIPD/DPIA** y cuándo es obligatoria?
60. ¿Qué añade la **FRIA** del AI Act frente a la DPIA?
61. Con el resultado de **Sweeney (2000)**: si publicas un conjunto de datos sin nombre ni DNI pero
    con fecha de nacimiento, sexo y código postal, ¿está anonimizado? Justifica con la cifra.
62. Explica cómo se reidentificaron los datos del **Premio Netflix**. ¿Qué tenían de especial las
    fechas de las valoraciones?
63. Define **k-anonimato**. Si en un conjunto hay una sola persona de 90-100 años en un código postal,
    ¿es 3-anónimo? ¿Qué habría que hacer?
64. Ordena de menor a mayor garantía: generalizar campos, k-anonimato, consultas agregadas,
    privacidad diferencial. Di qué ataque deja pasar cada nivel.
65. Reproduce el **ataque de consultas múltiples** del §8.2 con tus propios números y explica las
    **dos** defensas que se combinan para evitarlo.
66. ¿Qué garantiza exactamente la **privacidad diferencial**? Explica por qué esa garantía elimina el
    «desincentivo de privacidad» para participar en una base de datos.
67. Explica el **aprendizaje federado** con el ejemplo del reconocimiento de voz en el móvil. ¿Qué
    viaja al servidor y qué no?
68. ¿Qué problema del aprendizaje federado resuelve la **agregación segura** y con qué truco? ¿Por qué
    las máscaras tienen que sumar cero?
69. Elige un sistema (app de salud, control de acceso del centro, recomendador de una tienda) y
    propón **una técnica del §8.2 por cada estrategia de la AEPD** aplicada a ese sistema.

## F. Sesgos de género y algorítmicos (RA6-f)

70. Define **sesgo algorítmico** y enumera **cinco** fuentes distintas.
71. ¿Qué es una **variable proxy**? Pon dos ejemplos que revelen el género sin usar el dato.
72. Con los datos de la teoría: ¿qué mostró **Gender Shades** y qué el estudio **NIST FRVT**?
73. Diferencia **paridad demográfica**, **igualdad de oportunidades** y **calibración**.
74. ¿Qué hacen **Fairlearn** y **AIF360**? ¿En qué fase intervienen (pre / modelo / post)?
75. Explica la **paradoja de los sesgos** y cómo se resuelve en la práctica.
76. ¿Qué establece la **Ley 15/2022** sobre los algoritmos en las administraciones? Relaciona la
    inversión de la carga de la prueba con la responsabilidad proactiva del RGPD.
77. Rellena la tabla con las **seis definiciones de justicia** del §9.2, y para cada una: qué exige y
    cuál es su problema.
78. Explica por qué la **equidad por desconocimiento** no funciona, con dos argumentos distintos (uno
    técnico y otro de auditabilidad).
79. 🗣️ El dilema del §9.2: dos personas iguales en todo salvo que ella cobra menos por el mismo
    trabajo. Defiende **por escrito las dos posturas** sobre si aprobar su préstamo, y di cuál
    elegirías y por qué.
80. Con los datos de **COMPAS**: demuestra que cumple la calibración y que no cumple la igualdad de
    oportunidades, citando las cifras de cada caso.
81. Enuncia el resultado de **Kleinberg et al. (2016)**. Explica por qué **ProPublica y Northpointe
    tenían razón los dos** y qué tipo de discusión era en realidad.
82. Los datos de reincidencia «no dicen quién cometió un delito, sino quién fue condenado». Enumera
    **tres** formas distintas en que eso sesga el conjunto de datos.
83. ¿Cómo puede un sistema de IA servir para **justificar** el sesgo de una persona? ¿Qué salvaguarda
    lo evita?
84. ¿Qué alegó el acusado en el caso **Estado contra Loomis** y qué resolvió el Tribunal Supremo de
    Wisconsin? ¿Qué derecho estaba en juego?
85. En el caso de **Obermeyer et al. (2019)**: ¿qué variable usó el algoritmo como proxy, de qué, y
    por qué eso producía discriminación racial **sin usar la raza**? Cita las dos cifras de la
    corrección.
86. Explica la **paradoja de Simpson** con los datos de Berkeley (1973). ¿Dónde estaba realmente el
    sesgo? ¿Qué te obliga a hacer esta paradoja al evaluar un modelo?
87. Una empresa te dice que su modelo tiene un 92 % de precisión global y que por tanto es justo.
    Redacta la respuesta técnica en tres frases.
88. La **disparidad en el tamaño de la muestra** produce sesgo aun sin ningún prejuicio social.
    Explica el mecanismo y nombra dos técnicas de sobremuestreo que lo mitigan.
89. ¿Por qué elegir la **voz, el nombre y la apariencia** de un asistente es una decisión sujeta a
    RA6-f? Cita el resultado sobre productos utilitarios y hedónicos.
90. Del checklist de nueve buenas prácticas del §9.7, elige las **tres que aplicarías primero** a un
    proyecto de cribado de CV y justifica el orden.
91. ¿Qué es un ***datasheet*** de un conjunto de datos y una ***model card***? ¿Con qué objeto
    cotidiano de la electrónica se comparan y por qué es una buena analogía?

## G. Casos prácticos

92. Analiza el caso **Amazon 2018** (reclutamiento): qué ocurrió, por qué, qué principio ético se
    vulneró y cómo se habría evitado.
93. Aplica un **checklist de *privacy* y *security by design*** a un sistema de clasificación de
    correos que propongas en clase.
94. Un ayuntamiento quiere un sistema que priorice las inspecciones de vivienda. Redacta un informe
    de una página: nivel de riesgo del AI Act, base legal del tratamiento, proxies peligrosos que
    evitarías, métrica de equidad que elegirías **y por qué esa**, y una técnica de privacidad del
    §8.2.
95. Coge cualquier noticia de la lista de actualidad de las [actividades
    guiadas](UD06_ActividadesGuiadas.md) y analízala con la plantilla del [Taller
    1](notebooks/UD06_N02_analisis_caso_etico.ipynb): hechos, partes afectadas, principios en conflicto,
    normativa aplicable y propuesta.

---
[Volver a la UD06](UD06_ES.md) · [Notebook 2](notebooks/UD06_N02_analisis_caso_etico.ipynb) ·
[Notebook 3](notebooks/UD06_N03_auditoria_sesgos.ipynb)
