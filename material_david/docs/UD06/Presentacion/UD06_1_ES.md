---
marp: true
style: pre.mermaid { all: unset; }
---
<!--
theme: gaia
size: 16:9
_class: lead
paginate: true
marp: false
backgroundColor: #000
backgroundImage: url('img/hero-backgroundIES.jpg')
-->
<style>
section::after {
  content: attr(data-marpit-pagination) '/' attr(data-marpit-pagination-total);}
img[alt~="center"] {
  display: block;
  margin: 0 auto;
}
section img {
  max-height: 380px;
  width: auto;
}
table {
  margin-left: auto;
  margin-right: auto;
}
footer {
  font-size: 20px;
 }
header {
  font-size: 16px;
 }
</style>
<style scoped>
section {
  @extend .markdown-body;
  font-size: 28px;
  justify-content: top;
 }
</style>

![h:260 center](../assets/cover.png)
# UD06: Principios legales y éticos de la IA
#### Modelos de Inteligencia Artificial
###### version: 2026-08-27
___
<!-- footer: d.martinezpena@edu.gva.es -->
<!-- header: Modelos de Inteligencia Artificial 26-27 (UD06_1)-->
<!-- Cada uno de estos seis bloques se corresponde uno a uno con un criterio de evaluación del RA6, de la a a la f, en el mismo orden en que aparecen aquí. -->
# ¿Qué veremos?
1. Riesgos y deontología
2. Privacidad y protección de datos
3. Cumplimiento de la legalidad
4. *Security by design*
5. *Privacy by design*
6. Sesgos de género y algorítmicos

> Y **dos debates por roles**.
___
## La unidad en una frase
<!-- El tramo de 6 horas se extiende del 15 de marzo al 23 de abril, fragmentado por las fiestas de Fallas y Pascua. Es la última unidad de contenidos del módulo y la que menos carga de laboratorio tiene, por eso se evalúa con debates en vez de con prácticas. -->

Todo el curso ha sido **cómo se construye** un sistema de IA.

Esto es **qué puedes hacer con él y qué no debes**.

| | |
|---|---|
| Duración | **6 h** · semanas 24-28 |
| Criterio | **RA6** y sus 6 CE |
___
<style scoped>section { font-size: 24px; }</style>

## RA6 y sus criterios de evaluación
<!-- El anexo I del RD 279/2021 recoge cinco contenidos oficiales para estos seis criterios de evaluación: los CE d (security by design) y e (privacy by design) no tienen contenido propio en el currículo, y es el centro quien los desarrolla, según el art. 3.3 del Decreto 95/2026. (§2 de los apuntes) -->

> **RA6** — Aplica principios legales y éticos al desarrollo de la Inteligencia Artificial integrándolos como parte del proceso.

| CE | Criterio | Dónde |
|---|---|---|
| **a** | Argumentar los riesgos legales y éticos de aplicar IA | §1 |
| **b** | Reconocer la necesidad de respetar la privacidad de los datos | §2 |
| **c** | Decidir el cumplimiento estricto de la legalidad | §3 |
| **d** | Integrar la protección frente a errores y ataques (*security by design*) | §4 |
| **e** | Comprobar que se cumplen las normas en todas las áreas (*privacy by design*) | §5 |
| **f** | Identificar y corregir los sesgos de género | §6 |
___
<style scoped>section { font-size: 25px; }</style>

## Al terminar la unidad serás capaz de…

- **Argumentar** los riesgos legales y éticos de la IA apoyándote en casos reales con datos.
- **Reconocer** qué obliga el RGPD y la LOPDGDD sobre los datos con los que se entrena un modelo.
- **Clasificar** un sistema según el nivel de riesgo del AI Act y decir qué obligaciones le tocan.
- **Integrar** la protección frente a errores y ataques en el ciclo de vida del sistema.
- **Aplicar** una técnica concreta de privacidad desde el diseño a un caso dado.
- **Medir** el sesgo de un modelo con métricas de equidad y **proponer** una corrección.
___
## Cómo se evalúa
<!-- La exigencia de aprobar cada RA con nota igual o superior a 5 viene del art. 5.1 de la Orden 8/2025, que vincula la calificación del módulo a la consecución de los RA, y de las Instrucciones 26-27, que impiden calificar positivamente un módulo con algún RA no superado. (§15 de los apuntes) -->

| Peso | Instrumento |
|---|---|
| **40 %** | 2 debates, 2 talleres, 1 notebook |
| **60 %** | Prueba del RA6 |

Prueba: test y desarrollo sobre el contenido de la unidad.

> Hace falta **5 o más** en el RA.
___
## La rúbrica de los debates
<!-- La misma rúbrica se aplica a quien tenga el papel de Observador Crítico: en ese caso, el criterio de dominio del rol se lee como coherencia de la postura personal defendida, no como fidelidad a un personaje. -->

| Criterio | Puntos |
|---|---|
| Dominio del rol | 20 |
| Argumentación ética | 20 |
| Participación activa | 15 |
| Empatía y perspectiva | 15 |
| **Reflexión escrita** | **30** |

> **70 de 100 se observan en directo.** Faltar no se recupera.
___
## Lo que puede salir mal
<!-- COMPAS es un sistema comercial de puntuación de riesgo de reincidencia penal usado por jueces en EE. UU. Gender Shades es el estudio de Buolamwini y Gebru (MIT Media Lab, 2018) sobre reconocimiento facial. El caso de Amazon era un cribado automático de currículos que penalizaba términos como «women's chess club captain», y el proyecto se canceló. (§4.1 de los apuntes) -->

| Caso | Dato |
|---|---|
| **COMPAS** (2016) | Falsos positivos **44,9 %** vs **23,5 %** |
| **Amazon** (2018) | Penalizaba «women's chess club» |
| **Gender Shades** (2018) | **33 %** de error en mujeres de piel oscura |
| **Deepfake** HK (2024) | **25,6 M USD** |
___
## Google Photos, 2015
<!-- Quien detectó el fallo fue el ingeniero informático Jacky Alciné, al ver que el sistema etiquetaba a varios de sus amigos negros como gorilas. (§4.1 de los apuntes) -->

El algoritmo etiquetó a personas negras como **gorilas**.

Tres años después, *Wired* comprobó que seguía igual: la solución fue **borrar la etiqueta**.

> Un sesgo de visión no siempre se arregla. Detéctalo **antes** de desplegar.
___
## Uber en Tempe, 18/03/2018
<!-- La peatona cruzaba por una zona señalizada como prohibida para peatones, con poca visibilidad, y empujaba un objeto metálico que pudo dificultar la detección. Uber suspendió las pruebas tras el accidente y las reanudó el 20 de diciembre de 2018 alegando que sus coches ya eran más seguros que los conducidos por humanos. (§4.1 de los apuntes) -->

| Qué falló | Dato |
|---|---|
| Velocidad | **69 km/h** |
| Detección | Bicicleta no reconocida |
| Reacción | Vio 6 s antes, **4,7 s sin actuar** |
| Supervisión | Conductor distraído |

> El fallo **nunca es de un solo componente**.
___
## Depurar IA no es depurar software
<!-- El riesgo característico también cambia: en el software clásico suele ser una excepción no capturada, mientras que en el aprendizaje automático es un sesgo sistemático que nadie llega a medir. (§4.2 de los apuntes) -->

| | Clásico | Aprendizaje automático |
|---|---|---|
| Comportamiento | En el código | En los **datos** |
| Se prueba | La especificación | Que **generaliza y es justo** |
| Un caso | Parche | Puede exigir **reentrenar** |

> Puede pasar el 100 % de los tests y discriminar.
___
## Deontología: cuatro marcos
<!-- ACM son las siglas de Association for Computing Machinery. IEEE EAD significa Ethically Aligned Design, y está ligado al estándar IEEE 7000 sobre consideraciones sociales en el diseño. Las directrices de la UE de 2019 se llaman oficialmente «Directrices éticas para una IA fiable». (§4.3 de los apuntes) -->

| Marco | Aportación |
|---|---|
| **ACM** 2018 | Nada **no monitorizable** |
| **IEEE EAD** 2019 | Ingeniería **basada en valores** |
| **UNESCO** 2021 | 10 principios · **193 estados** |
| **UE** 2019 | **Lícita, ética y robusta** |
___
## Los principios comunes

* Beneficencia y no maleficencia
* Autonomía
* Justicia
* Transparencia
* Rendición de cuentas

> Y «robusta» **también en sentido social**: se puede dañar a terceros con buenas intenciones.
___
## El problema de los principios
<!-- El primer listado de este tipo lo publicó en 2010 el Consejo de Investigación en Ingeniería y Ciencias Físicas del Reino Unido, con sus «Principios de la Robótica»; desde entonces decenas de organismos han repetido listas parecidas. -->

Los listados repiten: seguridad, responsabilidad, equidad, privacidad, transparencia, empleo…

* Muchos valen para **cualquier** software
* Varios son **imposibles de medir**

> **Mittelstadt (2019)**: hacen falta pautas aplicables **por subcampo**. Úsalo en el debate contra la autorregulación.
___
## El futuro del trabajo
<!-- IBM calculaba en 2019 que 120 millones de trabajadores necesitarían recualificarse para 2022, y Oxford Economics estimaba 20 millones de empleos industriales perdidos para 2030. (§4.5 de los apuntes) -->

| Dato | Fuente |
|---|---|
| **47 %** del empleo en riesgo | Frey y Osborne, 2017 |
| Solo **5 %** de ocupaciones automatizable del todo | McKinsey |
| …pero **60 %** automatiza ~**30 %** de tareas | McKinsey |
| **15 billones** al PIB en 2030 | PwC, 2017 |
___
## Ojo con esas cifras

Frey y Osborne es **anterior a los LLM**.

Sus tres barreras a la automatización eran percepción, **creatividad** e **inteligencia social**.

> Justo las que los LLM han empezado a erosionar. **Fecha siempre el dato.**
___
## Lo que duele es el ritmo
<!-- El contraejemplo clásico son los cajeros automáticos: abarataron la sucursal bancaria, así que aumentó el número de sucursales y de empleados, con trabajo menos rutinario. (§4.5 de los apuntes) -->

**Agricultura EE. UU.**: del **40 %** de la población activa en 1900 al **2 %** en 2000.

Enorme… pero en **cien años**. Entre generaciones.

> Hoy te automatizan el empleo, te recualificas, y **te automatizan la nueva profesión**.
___
## Privacidad: no empieza en el RGPD
<!-- LOPDGDD son las siglas de Ley Orgánica de Protección de Datos Personales y garantía de los Derechos Digitales. (§5.1 de los apuntes) -->

**Constitución de 1978, art. 18.4**: *«la ley limitará el uso de la informática para garantizar el honor y la intimidad»*.

| Norma | Qué es |
|---|---|
| **RGPD** 2016/679 | Toda la Unión |
| **LOPDGDD** 3/2018 | España **+ derechos digitales** |
___
## El RGPD aplicado a la IA
<!-- Estos tres principios proceden del art. 5 del RGPD, que en total enumera siete: incluye también licitud, exactitud, limitación del plazo de conservación e integridad y confidencialidad. (§5.2 de los apuntes) -->

| Principio | En IA |
|---|---|
| **Minimización** | Solo lo necesario, **también el *dataset*** |
| **Limitación de la finalidad** | Entrenar **es** otra finalidad |
| **Responsabilidad proactiva** | Hay que **poder demostrarlo** |

> No por tener más datos tienes derecho a usarlos.
___
## LOPDGDD: plazos que hay que saber
<!-- La Lista Robinson la gestiona la asociación Adigital, y la inscripción en ella es gratuita. (§5.3 de los apuntes) -->

| Derecho | Límite |
|---|---|
| **Videovigilancia** | Borrar en **1 mes** · judicial en **< 72 h** |
| **Info. crediticia** | Máximo **5 años** |
| **Exclusión publicitaria** | **Lista Robinson**, obligatoria consultarla |
___
## LOPDGDD: derechos laborales y digitales

* **Desconexión digital**, también en **teletrabajo**
* **Prohibido** grabar en vestuarios, aseos y comedores
* Geolocalizadores: hay que **informar antes**
* **Derecho al olvido** en buscadores y redes

> Son derechos con nombre y plazo, no principios genéricos.
___
## El artículo que más te afectará
<!-- Estas sanciones proceden del art. 83 del RGPD, reservado a las infracciones más graves. (§5.4 de los apuntes) -->

**Art. 22 RGPD**: derecho a **no ser objeto de decisiones automatizadas** sin intervención humana significativa.

* **ARSULIPO**: acceso, rectificación, supresión, limitación, portabilidad, oposición
* Sanciones: **20 M €** o el **4 %** de la facturación
___
## Vigilancia: cambió el coste
<!-- Varios países han empezado además a exportar esta tecnología de vigilancia a países con menos capacidad técnica propia, algunos con antecedentes de maltrato a sus ciudadanos y de señalamiento de comunidades marginadas. (§5.5 de los apuntes) -->

**1976** · Weizenbaum avisó de las escuchas generalizadas.

**2018** · hasta **350 M** de cámaras en China y **70 M** en EE. UU.

> Cuando vigilar a una persona más cuesta casi cero, **la escala cambia de naturaleza**.
___
## Y esto te toca a ti
<!-- El aprendizaje automático sirve a los dos bandos en ciberseguridad: los atacantes lo usan para automatizar el phishing y la detección de vulnerabilidades, y los defensores para detectar tráfico anómalo y fraude. -->

Los marcos deontológicos obligan **al profesional**, no solo a la empresa.

Hay que saber qué usos de la vigilancia son compatibles con los derechos humanos y **negarse** a los que no.

> El **art. 5 del AI Act prohíbe** varios. No es opinión política: es ilegal.
___
## AI Act: cuatro niveles de riesgo
<!-- El nivel inasumible también prohíbe la manipulación subliminal y la categorización biométrica por características sensibles. El alto riesgo incluye además sistemas de educación e infraestructuras críticas. (§6.1 de los apuntes) -->

| Nivel | Ejemplos |
|---|---|
| **Inasumible** | Puntuación social · emociones en el trabajo |
| **Alto riesgo** | RRHH, crédito, salud, **justicia** |
| **Limitado** | Chatbots, *deepfakes* |
| **Mínimo** | Videojuegos, filtros de spam |
___
## Qué obliga cada nivel

* **Inasumible** → prohibido (art. 5)
* **Alto riesgo** → gestión de riesgos, datos de calidad, documentación, **supervisión humana**, robustez
* **Limitado** → **transparencia** (art. 50): decir que es una IA y marcar lo generado
* **Mínimo** → nada específico
___
## El calendario del AI Act
<!-- Los sistemas de alto riesgo del anexo III entran en vigor el 2 de diciembre de 2027, y los del anexo I el 2 de agosto de 2028. (§6.1 de los apuntes) -->

| Fecha | Qué entra |
|---|---|
| **01/08/2024** | Entrada en vigor |
| **02/02/2025** | Prohibiciones del art. 5 |
| **02/08/2025** | Modelos de uso general |
| **02/08/2026** | **Aplicación general** |
| 2027 · 2028 | Alto riesgo: anexo III · anexo I |
___
## ¿Y si el sistema causa un daño?
<!-- PLD son las siglas de Directiva de Responsabilidad por Productos Defectuosos (2024/2853). AILD son las siglas de Artificial Intelligence Liability Directive, la propuesta específica de responsabilidad civil de la IA que se retiró. El AI Act obliga además a los proveedores de modelos de uso general a publicar resúmenes de los contenidos protegidos usados en el entrenamiento. (§6.2 de los apuntes) -->

* La **PLD revisada (2024/2853)** trata el software de IA como **«producto»**, con responsabilidad **objetiva** del fabricante
* La **AILD**, específica de IA, **se retiró en 2025**

> La obra generada por IA solo se protege con **control creativo humano**.
___
## Confianza: verificar y validar
<!-- (§6.3 de los apuntes) -->

* **Verificar** = cumple la especificación
* **Validar** = **la especificación es la correcta**

En IA hay que verificar además los **datos**, la **equidad** y que nadie **influya** en el modelo.

> **PwC 2017**: el **76 %** de las empresas frenaba la IA por dudas de fiabilidad.
___
## Confianza: certificar
<!-- UL son las siglas de Underwriters Laboratories, fundada en 1894 cuando los consumidores desconfiaban de la electricidad doméstica. (§6.3 de los apuntes) -->

| Precedente | Qué es |
|---|---|
| **UL** (1894) | Sello de electrodomésticos |
| **ISO 26262** | Seguridad del automóvil |
| **IEEE P7001** | Transparencia de sistemas autónomos |

> La IA aún no tiene un estándar maduro. El debate: **quién certifica**.
___
## Interpretable ≠ explicable
<!-- A un sistema capaz de explicarse se le llama IA explicable, o XAI por sus siglas en inglés. (§6.3 de los apuntes) -->

| | Qué significa |
|---|---|
| **Interpretable** | Inspeccionas el modelo y **ves** qué hace |
| **Explicable** | Construyes **un relato** de lo que hace |

> La explicación la produce **un segundo sistema** que hay que mantener sincronizado. Y puede sonar bien sin ser cierta.
___
## Una explicación no basta

Si el banco te dice «es por tu historial», no sabes si es verdad **ni** si te discrimina.

Para saberlo hace falta una **auditoría de decisiones pasadas**, con estadísticas **por grupo demográfico**.

> Una explicación sobre **un** caso no dice nada de los demás.
___
## La ley de la bandera roja
<!-- (§6.3 de los apuntes) -->

**Walsh (2015)**: un sistema autónomo debe diseñarse para no confundirse con nada más, e **identificarse al inicio**.

Por la *Locomotive Act* británica de **1865**: alguien con bandera roja delante del vehículo.

> California lo hizo ley en **2019**. En la UE es el **art. 50**.
___
## Armas autónomas: la escalera
<!-- Las minas terrestres están prohibidas por el Tratado de Ottawa. La munición merodeadora citada es del tipo Harop; existen además cuadricópteros armados tipo Kargu, capaces de portar hasta 1,5 kg de explosivo y perseguir objetivos móviles con reconocimiento facial. (§6.4 de los apuntes) -->

| Sistema | ¿Localiza? | ¿Ataca solo? |
|---|---|---|
| Mina terrestre | No | Sí, muy limitado |
| Misil guiado | Persigue | Lo apunta un humano |
| Dron a distancia | No | **No** |
| Munición merodeadora | **Sí**, 6 h | **Sí** |
___
## Dónde está la línea

La ONU define arma letal autónoma: **localiza, selecciona y ataca** sin supervisión humana.

La línea está en **localizar por iniciativa propia** y decidir **sin humano en el circuito**.

> Se las llama «la tercera revolución en la guerra», tras la pólvora y las nucleares.
___
## El problema legal
<!-- CCW son las siglas de la Convención sobre Ciertas Armas Convencionales. (§6.4 de los apuntes) -->

La CCW exige tres cosas:

| Requisito | ¿Es factible hoy? |
|---|---|
| **Discriminar** combatientes | Sí, en algunos casos |
| Juzgar la **necesidad** militar | **No** |
| Evaluar la **proporcionalidad** | **No** |

> Solo serían lícitas misiones **muy restringidas**.
___
## El problema práctico
<!-- (§6.4 de los apuntes) -->

**26 de septiembre de 1983** · el oficial soviético **Stanislav Petrov** vio una alerta de ataque con misiles. El protocolo mandaba contraatacar. Sospechó que era un error.

Tenía razón.

> No sabemos qué habría pasado **sin un humano en el circuito**.
___
## Armas de destrucción masiva escalables

* La escala del ataque depende del **hardware**, no de los operadores
* Un millón de cuadricópteros caben en un contenedor
* **Por ser autónomos**, no necesitan un millón de supervisores
* Dejan la propiedad intacta y pueden usarse **selectivamente**
___
## Y se decide **durante este curso**
<!-- Los tres votos en contra en la ONU fueron de Bielorrusia, Corea del Norte y Rusia; hubo además 15 abstenciones. (§6.4 de los apuntes) -->

| Cuándo | Qué |
|---|---|
| **2/12/2024** | ONU: **166** a favor, 3 en contra |
| Hoy | **+120 países** quieren tratado |
| **Nov. 2026** | Informe del GGE a la CCW |

> Bloquean, por consenso: India, Israel, Rusia y EE. UU.
___
## Security by design
<!-- NCSC son las siglas de National Cyber Security Centre, del Reino Unido, y CISA las de Cybersecurity and Infrastructure Security Agency, de EE. UU. El ciclo de vida seguro completo se conoce como SAiDLC. (§7.1 de los apuntes) -->

La seguridad **no se añade al final**: diseño, desarrollo, despliegue y operación.

Marcos de referencia:

* **NCSC/CISA** (2023)
* **NIST AI 100-2e2023**
* **OWASP ML Top 10** y **GenAI LLM Top 10**
___
## Los cinco ataques
<!-- El ejemplo clásico de adversarial example es el panda de Goodfellow (2014), clasificado como gibón con una perturbación imperceptible. El chatbot Tay de Microsoft aprendió lenguaje ofensivo en un solo día por envenenamiento de datos, y la lógica de ChatGPT-3.5-Turbo se llegó a clonar por unos 50 USD mediante extracción por consultas. (§7.2 de los apuntes) -->

| Ataque | Qué hace |
|---|---|
| **Adversarial** | Entrada imperceptible que engaña |
| **Envenenamiento** | Adultera el entrenamiento |
| **Extracción** | Replica el modelo por consultas |
| **Fuga de datos** | Devuelve datos personales |
| **Prompt injection** | Salta los controles |
___
## Correcto no es seguro

**Correcto** = implementa la especificación.

**Seguro** = la especificación **consideró los modos de fallo** y el sistema **degrada con elegancia**.

> ¿Y si se corta la alimentación del ordenador principal? ¿Y si revienta un neumático a 120?
___
## FMEA y FTA
<!-- Aplicado a Tempe, un FMEA habría recorrido sensores, clasificador, planificador, supervisión humana e interfaz, con una mitigación para cada uno: redundancia de sensores, una clase «objeto desconocido» que fuerce el frenado, alarma sonora y detección de la atención del conductor. (§7.3 de los apuntes) -->

| Técnica | Cómo va | Qué produce |
|---|---|---|
| **FMEA** | Componente a componente | Fallo, efecto y **mitigación** |
| **FTA** | Árbol Y/O con probabilidades | **Probabilidad global** de fallo |

> Son de la ingeniería de puentes y aviones. En Tempe habrían escrito las cinco mitigaciones.
___
## Specification gaming
<!-- Estos ejemplos motivaron los entornos AI Safety Gridworlds, de Leike et al. (2017), pensados para probar este problema antes de desplegar un sistema. (§7.4 de los apuntes) -->

Agentes que maximizan la métrica **sin resolver el problema** (Krakovna, 2018):

* **Pausan la partida** cuando van a perder
* Al penalizarlo, **agotan la memoria en el turno del rival**
* Criaturas «rápidas» que salieron **altísimas y se caen**
___
## El problema del rey Midas

Un maximizador te da **exactamente lo que pediste**, no lo que querías.

Escribir «todas las reglas» no funciona: llevamos siglos con las leyes fiscales.

> Mejor que el sistema **quiera** el objetivo correcto que obligarlo a cumplir una lista.
___
## Security ≠ safety
<!-- (§7.4 de los apuntes) -->

| | Amenaza |
|---|---|
| **Security** | Un **atacante**: manipula, envenena, roba |
| **Safety** | **Tu diseño**: fallo previsible u objetivo mal puesto |

> El criterio lo dice literal: previsibles **errores** *y* **ataques**. Las dos cosas son RA6-d.
___
## Privacy by design

**Art. 25 RGPD**: privacidad **desde el diseño y por defecto**.

Estrategias de la AEPD:

* **Minimizar** · recoger solo lo necesario
* **Abstraer** · resumir y agregar
* **Separar** · datos e identificadores aparte
* **Ocultar** · seudonimizar y cifrar
___
## Desidentificar no basta
<!-- El cruce que reidentificó a los usuarios del Premio Netflix lo hicieron los investigadores Narayanan y Shmatikov, en 2006. (§8.2 de los apuntes) -->

* **Sweeney (2000)**: con fecha de nacimiento, sexo y código postal se reidentifica al **87 %** de la población de EE. UU.
* **Premio Netflix**: reidentificado cruzando **fechas** de valoraciones con IMDb

> Sweeney reidentificó el historial médico **del gobernador de su estado**.
___
## La escalera de técnicas
<!-- El «gasto de presupuesto» de la privacidad diferencial significa que cuantas más consultas se hacen a los datos, más ruido hay que añadir a las respuestas para mantener la garantía. (§8.2 de los apuntes) -->

| Técnica | Deja pasar |
|---|---|
| Generalizar campos | Combinaciones raras |
| **k-anonimato** | Atacante con **datos externos** |
| Consultas agregadas | **Consultas múltiples** |
| **Privacidad diferencial** | (gasta presupuesto) |
___
## Aprendizaje federado
<!-- La técnica de agregación segura la formalizaron Bonawitz et al. en 2017. (§8.2 de los apuntes) -->

**No hay base de datos central**: cada usuario entrena en local y comparte solo **parámetros**.

Con **agregación segura**, cada uno enmascara sus valores y las máscaras **suman cero**: el servidor solo obtiene la **media**.

> Viajan parámetros. **No viajan datos.**
___
## De dónde vienen los sesgos
<!-- Bolukbasi (2016) mostró que los embeddings de lenguaje aprenden asociaciones como hombre:programador :: mujer:ama de casa: el aprendizaje automático no solo refleja los estereotipos de los datos, los amplifica. (§9.1 de los apuntes) -->

* **Datos históricos**: el ML está diseñado **para replicarlos**
* **Sesgo de selección** y datos faltantes
* **Objetivos** que minimizan el error **agregado**
* **Variables proxy**: código postal, ocupación, nombre
* **El propio equipo**: ves antes lo que te afecta
___
## Y basta el tamaño de la muestra
<!-- Las técnicas de sobremuestreo SMOTE y ADASYN mitigan precisamente esta disparidad de tamaño de muestra entre clases minoritarias y mayoritarias. (§9.1 de los apuntes) -->

Aunque **no haya ningún prejuicio social**: hay menos ejemplos de las clases minoritarias, y más datos significa más precisión.

Un modelo restringido puede minimizar el error medio **ajustando solo a la mayoría**.

> El sesgo no necesita mala intención. Necesita descuido.
___
## «Justo» significa seis cosas
<!-- (§9.2 de los apuntes) -->

| Definición | Su problema |
|---|---|
| Justicia individual | Nada sobre agregados |
| Equidad de grupo | No garantiza la individual |
| **Por desconocimiento** | **No funciona** |
| Igual resultado | Rechaza a gente cualificada |
| Igualdad de oportunidades | Ignora el sesgo social |
| Igual impacto | Costes difíciles de calcular |
___
## Quitar la variable no funciona

Si borras «género» del conjunto, el modelo **lo predice** desde el código postal, la ocupación o el texto libre.

Y encima **pierdes la capacidad de auditar** si discriminas.

> Es la «equidad por desconocimiento». Suena bien y no sirve.
___
## COMPAS: las dos verdades
<!-- Northpointe es la empresa que desarrolló y comercializa COMPAS; fue ProPublica quien denunció el sesgo, en 2016. (§9.4 de los apuntes) -->

| Criterio | Resultado |
|---|---|
| **Calibración** | **La cumple**: con 7/10 reincide el 60 % de blancos y el 61 % de negros |
| **Igualdad de oportunidades** | **No**: falsos positivos **44,9 %** vs **23,5 %** |
___
## Y no se pueden tener las dos

**Kleinberg et al. (2016)**: con **tasas base distintas**, cumplir la calibración **y** la igualdad de oportunidades es **matemáticamente imposible**.

> ProPublica y Northpointe **tenían razón los dos**. La discusión no era estadística: era **normativa**.
___
## Tres problemas sin arreglo técnico
<!-- El caso Estado contra Loomis lo resolvió el Tribunal Supremo de Wisconsin: no anuló la condena, pero emitió advertencias sobre la precisión del algoritmo y los riesgos para los acusados de minorías. (§9.4 de los apuntes) -->

1. **No hay verdad de referencia**: los datos dicen quién fue **condenado**
2. **Sirve de coartada**: «el modelo respalda mi decisión»
3. **La opacidad choca con el derecho de defensa** → caso **Estado contra Loomis**
___
## A veces lo que cambia es el objetivo

En una selección de personal, «los mejores expedientes» premia a quien tuvo mejores oportunidades: el modelo **refuerza las fronteras de clase**.

Si el objetivo pasa a ser «mejor capacidad de aprender en el puesto», el grupo se amplía.

> Tras un año de formación, rinden igual.
___
## La variable proxy perfecta
<!-- (§9.5 de los apuntes) -->

**Obermeyer et al.**, *Science* **2019**. El algoritmo **no usaba la raza**: usaba el **coste sanitario** como aproximación de la **necesidad de salud**.

Se gasta menos en pacientes negros → **menos riesgo estando igual de enfermos**.
___
## Y el efecto, medido
<!-- (§9.5 de los apuntes) -->

| Pacientes negros derivados | |
|---|---|
| Con el sesgo | **17,7 %** |
| Corregido | **46,5 %** |

> Nadie programó nada racista. Se eligió un **proxy cómodo** para algo que no se sabía medir. Es el sesgo que más te vas a encontrar.
___
## La paradoja de Simpson · Berkeley 1973
<!-- El análisis por departamento que reveló la paradoja lo publicaron Bickel, Hammel y O'Connell en la revista Science, en 1975. (§9.5 de los apuntes) -->

| Grupo | Solicitantes | Admisión |
|---|---|---|
| Hombres | 8.442 | **44,2 %** |
| Mujeres | 4.321 | **34,6 %** |

Parecía discriminación clara.
___
## Pero por departamento, desaparece
<!-- (§9.5 de los apuntes) -->

En los **101 departamentos** la diferencia deja de ser significativa, y en la mayoría la tasa femenina es **igual o superior**.

Las mujeres solicitaban más los departamentos **más competitivos**.

> El sesgo estaba **antes del comité**. Si solo mides la métrica global, **no ves nada**.
___
## Lo que sale al ejecutarlo
<!-- El conjunto UCI Adult tiene 48.842 filas y predice si una persona gana más de 50.000 dólares al año a partir de datos demográficos y laborales; el ejercicio completo está en el notebook N01 y en el Taller 2, no en los apuntes. -->

UCI Adult. Tasas base: **0,1093** mujeres vs **0,3038** hombres.

| Métrica | Sin mitigar | `eq_odds` | `dem_parity` |
|---|---|---|---|
| Exactitud | 0,8753 | 0,8611 | 0,8528 |
| Igualdad oport. | 0,0731 | **0,0014** | **0,3457** |
| Paridad demog. | 0,1687 | 0,0950 | **0,0091** |
___
## Arreglar una rompe la otra

No existe el botón «hazlo justo».

Existe **elegir** qué justicia quieres, **documentarlo** y decir **a quién perjudica**.

> Y el precio se paga en exactitud: 1,4 puntos con `equalized_odds`, 2,3 con `demographic_parity`.
___
## La métrica global no ve nada

| Grupo | Exactitud | Tasa de selección |
|---|---|---|
| Mujeres | **0,9358** | **0,0850** |
| Hombres | 0,8453 | **0,2538** |

> «Acierta más» con las mujeres porque solo el 10,93 % son positivas: **decir «no» ya acierta**.
___
## Un solo atributo no es una auditoría

Con **`race`** en vez de `sex`, el mismo modelo:

* Igualdad de oportunidades **0,2337** — más del **triple**
* Tras mitigar, solo baja a **0,0973**, no a 0,0014

> Cinco grupos en vez de dos. **Auditar un solo atributo protegido no es auditar.**
___
## La paradoja de los sesgos

Para **detectar** el sesgo de género hace falta tratar el dato… que la **minimización** manda no tratar.

Salidas: **proxies**, **entornos controlados**, o tratarlo **solo para auditar** con base legal y plazo.
___
## Ley 15/2022
<!-- La Ley 15/2022 es la ley de igualdad de trato y no discriminación de España. (§9.8 de los apuntes) -->

Las administraciones deben **favorecer algoritmos que minimicen sesgos**, y se puede **invertir la carga de la prueba**.

> Si no puedes **demostrar** que tu sistema no discrimina, a efectos legales **es como si discriminara**.
___
## Los dos debates
<!-- El documental de partida del Debate 1 es «Límites éticos para la Inteligencia Artificial»; el del Debate 2, «El algoritmo contra el crimen», solo se distribuye a través de Moodle. -->

| | Debate 1 | Debate 2 |
|---|---|---|
| Tema | Límites éticos | El algoritmo contra el crimen |
| Sesión | 2 | 4 |
| Roles | 10 + observadores | 9 + observadores |

> Se sortean en clase. Cada uno recibe **solo su ficha**.
___
## Cómo se juega un debate

* El documental **se ve antes**, en casa
* Se argumenta **desde el rol**, aunque no lo compartas
* **2 minutos** por intervención inicial
* Se atacan **posturas**, nunca personas

> El objetivo no es ganar: es entender **cómo los intereses condicionan la postura**.
___
<style scoped>section { font-size: 22px; }</style>

## Puntos clave

- Los riesgos de la IA **no son hipotéticos**: Google Photos, Uber en Tempe, COMPAS. Depurar IA no es depurar software.
- Los marcos deontológicos coinciden en los principios; el problema es **bajarlos a decisiones concretas**.
- El **RGPD** y la **LOPDGDD** ya obligan; el **AI Act** añade cuatro niveles de riesgo con calendario escalonado.
- **Security by design** protege de errores *y* de ataques; **privacy by design** no se resuelve desidentificando.
- «Justo» significa **seis cosas distintas**, y son **matemáticamente incompatibles** (Kleinberg).
- Una métrica global **no ve** el sesgo: hay que auditar por grupos, y con más de un atributo.
___
<style scoped>section { font-size: 25px; }</style>

## Las cuatro sesiones
<!-- (§13 de los apuntes) -->

| Sesión | Contenido | CE |
|---|---|---|
| 1 | Riesgos, deontología y principios; el futuro del trabajo. Preparación del debate 1 y **sorteo de roles** | a |
| 2 | **Debate 1 · Límites éticos de la IA** | a, c |
| 3 | Normativa como lectura guiada: RGPD, LOPDGDD, AI Act, *security* y *privacy by design*. Taller de sesgos | b, c, d, e |
| 4 | **Debate 2 · El algoritmo contra el crimen**, con COMPAS y Simpson. Cierre | f |

Los documentales se ven **fuera de clase**; la reflexión escrita es trabajo personal.
___
## ¿Y ahora?

1. Ve el documental del **Debate 1**
2. Haz los **talleres** y el **notebook**
3. Prepara los ejercicios marcados 🗣️
4. Cambia la restricción en Fairlearn y **mira qué se rompe**

> Con esto se cierran los contenidos. Lo que viene es el **proyecto (RA7)**.
