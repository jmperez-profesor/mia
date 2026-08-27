# UD03 · Ejercicios de autoevaluación

!!! note "Cómo se trabajan"
    Resuélvelos en tu cuaderno o en un documento Markdown. No se entregan por separado: son la
    preparación de la **prueba escrita del RA3** y de los talleres. Los entregables evaluables son
    los [cuatro notebooks](UD03_Entregas.md).

## A. Qué es el PLN (RA3-a)

1. Define **PLN** y di qué tres disciplinas combina, con la aportación de cada una.
2. Explica por qué un traductor automático «no entiende» aunque acierte, y por qué esa distinción no
   es filosófica sino operativa.
3. Relaciona cada nivel del lenguaje (fonología, morfología, sintaxis, semántica, pragmática) con una
   tarea de PLN.
4. Describe el *pipeline* típico en cuatro pasos y pon un ejemplo de cada paso con la frase
   *«El servicio fue excelente»*.
5. Diferencia **tokenización**, **etiquetado POS** y **reconocimiento de entidades** con la frase
   *«María trabaja en Madrid desde 2019»*.
6. Explica qué hace un asistente de voz desde que oye tu orden hasta que responde, nombrando las
   tareas de PLN implicadas.
7. Diferencia ***stemming*** y **lematización**, con un ejemplo en español, y di cuándo prefieres
   cada uno.

## B. El potencial (RA3-c)

8. Los sistemas superan la precisión humana en **SQuAD 2.0**. ¿Significa que «entienden» mejor que
   una persona? Justifica.
9. El sentimiento en reseñas pasó de ~89 % a **95-97 %**. ¿Qué cambió técnicamente para conseguirlo?
10. Según el **AI Act**, ¿qué es un *modelo de IA de uso general*? Da los dos requisitos.
11. ¿Qué umbral de cómputo hace presumir **capacidades de gran impacto**, y qué implica?
12. Busca tres aplicaciones de PLN que uses cada semana sin darte cuenta y di qué tarea resuelve cada
    una.

## C. La ambigüedad (RA3-c)

13. Enumera los **seis tipos de ambigüedad** y da un ejemplo propio de cada uno, distinto de los de
    la teoría.
14. Clasifica el tipo de ambigüedad de cada frase:

    | Frase | Tipo |
    |---|---|
    | *Vino de la Rioja* | |
    | *Compré unos zapatos de piel de señora* | |
    | *La policía observó al sospechoso con unos prismáticos* | |
    | *El pescado está listo para comer* | |
    | *Antonio no nada nada* | |
    | *Me quedé esperándote en el banco* | |

15. *«El Villarreal le ganó al Valencia en su campo.»* ¿Qué es exactamente lo ambiguo, y qué
    información resolvería la duda?
16. Explica por qué la ambigüedad **no se puede eliminar** y qué hace en su lugar un sistema de PLN.
17. ¿Qué es una **ventaja** de la ambigüedad para las personas? Da un caso donde nos resulte útil.
18. Resume el argumento de **Bender y Koller** sobre forma y significado, y qué predice sobre los
    errores de un modelo generativo.
19. Un modelo responde a una pregunta con un dato falso, redactado con total seguridad. ¿Es un fallo
    de ambigüedad, de comprensión o de datos? Justifica.

## D. Desambiguación y POS (RA3-a, RA3-c)

20. Define **POS *tagging*** y explica por qué una palabra aislada suele ser ambigua respecto a su
    categoría.
21. Etiqueta la categoría de **sobre** en las tres frases del ejemplo de la teoría, y explica qué
    información usas en cada caso.
22. Explica el compromiso al elegir el ***tagset***. ¿Qué se gana y qué se pierde al pasar de 45 a
    250 etiquetas?
23. Ordena por número de etiquetas: Penn Treebank, Brown, LexEsp (PAROLE), Susanne. ¿Cuál usarías
    para un buscador simple y cuál para un análisis morfológico del español?
24. Diferencia categorías **abiertas** y **cerradas**, con dos ejemplos de cada una. ¿Por qué la
    distinción importa al etiquetar?
25. Compara los tres enfoques de etiquetado (reglas, HMM/TnT, neuronal) en precisión, datos
    necesarios y transparencia.
26. ¿Por qué decidir el *tagset* y escribir la guía de anotación **no es una tarea de programación**?

## E. Las otras limitaciones (RA3-c)

27. Explica el sesgo de género en los *embeddings* con un ejemplo, y por qué **no basta con quitar la
    variable** para eliminarlo.
28. ¿Qué advierte el AI Act sobre los bucles de retroalimentación y los sesgos?
29. El AI Act **prohíbe** inferir emociones en dos contextos. ¿Cuáles, y con qué dos argumentos?
30. ¿Por qué en una lengua con pocos recursos una técnica estadística clásica puede **ganar** a una
    neuronal?
31. *«¡Qué buena idea, se me ha caído el móvil al agua!»* Explica por qué falla un clasificador de
    sentimiento y de qué tipo de ambigüedad se trata.

## F. Cuándo es factible (RA3-d)

32. Enumera los **cinco criterios** de factibilidad y formula la pregunta guía de cada uno.
33. Para cada caso, di si es factible hoy, no factible o **prohibido**, justificando:

    | Caso | Veredicto |
    |---|---|
    | Clasificar automáticamente los correos de soporte por tema | |
    | Detectar el estado de ánimo de los alumnos por sus mensajes | |
    | Extraer importes y fechas de 5.000 facturas | |
    | Resumir informes médicos para el diagnóstico, sin revisión | |
    | Traducir la documentación interna de una empresa | |
    | Detectar ironía en reseñas con un 95 % de acierto | |

34. Tienes 200 correos anotados de un dominio muy concreto. ¿Elegirías tf-idf o afinar un
    *transformer*? Justifica con los criterios del §9.1.
35. Usa el **considerando 53** y el **artículo 5** del AI Act para decidir si construirías un sistema
    que clasifica currículos por idoneidad.
36. Un cliente quiere un chatbot que responda consultas legales «sin supervisión». ¿Qué le
    responderías, y con qué criterio?

## G. El papel del lingüista (RA3-b)

37. Enumera **cinco aportaciones** del lingüista a un proyecto de PLN y pon un ejemplo concreto de
    cada una.
38. Explica la frase «**las anotaciones deciden las predicciones**» y por qué el problema **no se
    arregla con más datos**.
39. Dos anotadores etiquetan el mismo corpus y coinciden en el 70 % de los casos. ¿Qué problema hay y
    qué harías antes de entrenar nada?
40. ¿Por qué construir un *treebank* puede llevar años? ¿Qué se obtiene a cambio?
41. Un modelo preentrenado falla en los textos de tu empresa. Describe qué haría un lingüista para
    averiguar por qué.
42. Relaciona el §7.2 (elegir el *tagset*) con el papel del lingüista: ¿por qué esa decisión fija el
    techo de precisión del sistema?

## H. El trabajo cooperativo (RA3-e)

43. Explica qué hizo **Meta NLLB** con los hablantes nativos y qué consiguió, con la cifra.
44. ¿Qué es la investigación **paracaidista** y por qué **Masakhane** la rechaza explícitamente?
45. Completa la tabla con **dos ventajas** y **dos costes** del trabajo cooperativo entre lingüistas
    e informáticos.
46. El CE dice **«evaluar»** el trabajo cooperativo, no describirlo. Propón **tres criterios** para
    juzgar si una colaboración se ha hecho bien o mal.
47. Una empresa contrata anotadores en un país con salarios bajos, publica el modelo y no deja
    formación ni datos en el país. ¿Es cooperación? Argumenta las dos posturas.
48. Además de lingüistas e informáticos, ¿qué otros perfiles pueden hacer falta? Pon un proyecto
    donde cada uno sea imprescindible.

## I. La formación del investigador (RA3-f)

49. Describe las **tres patas** de la formación en PLN y qué aporta cada una.
50. Ordena el itinerario de lectura recomendado y justifica **por qué ese orden** y no otro.
51. ¿Qué formación necesita un **anotador especializado** en textos médicos que no necesita uno
    generalista?
52. Los perfiles de **prompt engineer** y **evaluador de sesgos** no existían hace unos años. ¿Qué
    base comparten con el lingüista computacional clásico?
53. Un titulado en informática sin formación lingüística entra en un proyecto de PLN. ¿Qué le va a
    costar más, y qué leería primero?

## J. Las herramientas (RA3-c, RA3-g)

54. Escribe el código con `nltk` que tokenice una frase en español, quite las *stopwords* y aplique
    *stemming*.
55. Escribe el código con spaCy que muestre, para cada token, su texto, categoría y lema, y luego las
    entidades.
56. ¿Por qué **NLTK para aprender y spaCy para producir**? Da dos razones técnicas.
57. Explica el error de escribir `TfidfVectorizer(stop_words='spanish')` y cómo se hace bien.
58. ¿Qué es **DistilBERT** y por qué es el modelo elegido en esta unidad? Da las tres cifras.
59. Di qué notebooks de la unidad van en el **contenedor** y cuáles en **Colab**, y por qué.
60. ¿Qué diferencia hay entre usar un `pipeline` de `transformers` ya hecho y **afinar** el modelo?

## K. Construir un sistema (RA3-g)

61. Enumera los **seis pasos** de la metodología y di qué se decide en cada uno.
62. ¿Por qué el paso de **analizar los errores** es el que más se salta, y qué se pierde al saltarlo?
63. En el ejemplo guiado se elige tf-idf con 60 reseñas en vez de un *transformer*. Justifica esa
    decisión.
64. Diseña en seis pasos un sistema que clasifique los correos de una FAQ por tema. Indica datos,
    herramienta y cómo lo evaluarías.
65. Tu clasificador da un 92 % de exactitud, pero al leer los errores ves que **todos** son reseñas
    irónicas. ¿Qué harías: más datos, otro modelo o cambiar la tarea? Justifica.
66. ¿Por qué hay que documentar el **origen y la licencia** de los datos? Relaciónalo con la UD06.
67. Explica la progresión de los cinco notebooks guiados: qué representación del texto usa cada uno y
    por qué el orden es ese.
68. Los cuatro entregables suben de nivel. Di qué demuestra cada uno y qué criterio cubre.

## L. Integración

69. Relaciona la ambigüedad del §6 con el papel del lingüista del §10.1: ¿por qué una explica la
    necesidad del otro?
70. Un proyecto de PLN falla. Escribe tres hipótesis —una técnica, una de datos y una de
    **organización del equipo**— y cómo comprobarías cada una.
71. Compara el PLN con los sistemas expertos de la UD05: ¿en qué se parecen las **reglas de
    anotación** a las **reglas de producción**? ¿En qué se diferencian?
72. Enlaza esta unidad con la UD06: nombra **tres** decisiones de un proyecto de PLN que sean a la
    vez técnicas y éticas.

!!! note "Soluciones"
    Las soluciones no se publican: se corrigen y comentan en clase.

---
[Volver a la UD03](UD03_ES.md) · Talleres: [N08](notebooks/UD03_N08_del_texto_al_vector.ipynb) · [N12](notebooks/UD03_N12_sistema_pln.ipynb) · [Entregables](UD03_Entregas.md)
