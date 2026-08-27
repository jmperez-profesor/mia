# UD06 · Práctica: documentales, noticias y notebooks

<!-- AUTO:notebooks inicio -->
!!! info "Práctica: se hace, no se entrega"
    2 actividades que se trabajan **en clase**, con el profesor. **No se
    entregas ni puntúas**: preparas las [entregas de la unidad](UD06_Entregas.md) y la prueba escrita del RA6.

    Los documentales de partida **se ven en casa**, antes de la sesión que les corresponde: la unidad
    tiene 6 horas y en clase se debate, no se proyecta. Los enlaces se comprobaron el **22 de agosto
    de 2026**.

| Actividad | Qué es | Descargar | Abrir en Colab |
|---|---|---|---|
| [`N01` · Detección y corrección de sesgos](notebooks/UD06_N01_sesgos_ia.ipynb) | Detección y corrección de sesgos · da soporte a `N03` | [![Descargar](https://img.shields.io/badge/Descargar-.ipynb-blue?logo=jupyter)](https://raw.githubusercontent.com/martinezpenya/ModelosIA/main/docs/UD06/notebooks/UD06_N01_sesgos_ia.ipynb){:target="_blank"} | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/martinezpenya/ModelosIA/blob/main/docs/UD06/notebooks/UD06_N01_sesgos_ia.ipynb){:target="_blank"} |
| [`N02` · Análisis de un caso ético](notebooks/UD06_N02_analisis_caso_etico.ipynb) | Método de análisis ético sobre un caso real | [![Descargar](https://img.shields.io/badge/Descargar-.ipynb-blue?logo=jupyter)](https://raw.githubusercontent.com/martinezpenya/ModelosIA/main/docs/UD06/notebooks/UD06_N02_analisis_caso_etico.ipynb){:target="_blank"} | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/martinezpenya/ModelosIA/blob/main/docs/UD06/notebooks/UD06_N02_analisis_caso_etico.ipynb){:target="_blank"} |

## `N01` · Detección y corrección de sesgos

Auditoría de equidad de un modelo real con **Fairlearn**: medir el sesgo por grupos, mitigarlo con
postprocesado y ver el precio que se paga. Es el soporte técnico de `N03`.

## `N02` · Análisis de un caso ético

Un método de análisis ético reproducible aplicado a un caso real de sesgo o riesgo de la IA
(RA6-a, RA6-c, RA6-f), argumentando con principios deontológicos, métricas y normativa. Trae una
tabla con ocho casos reales y sus cifras para elegir.
<!-- AUTO:notebooks fin -->

## Antes de cada debate

| Debate | Documental de partida | Enlace |
|---|---|---|
| [D01 · Límites éticos de la IA](UD06_D01_Debate_limites_eticos_ES.md) · sesión 2 | *Límites éticos para la Inteligencia Artificial* | [Ver](https://youtu.be/sHVwwriaT6k){:target="_blank"} |
| [D02 · El algoritmo contra el crimen](UD06_D02_Debate_algoritmo_crimen_ES.md) · sesión 4 | *El algoritmo contra el crimen* | En **Moodle** (ver aviso más abajo) |

Mientras lo ves, anota **un caso con su dato**, **una afirmación discutible** y **un ejemplo de la
teoría** que encaje. Con eso llegas preparado a la fase 3 del debate.

!!! warning "Por qué algunos enlaces están solo en Moodle"
    Parte del material audiovisual del curso se sirve desde un servidor propio cuyos enlaces de
    descarga **llevan la clave de API dentro de la URL**. Publicarlos en un sitio abierto e indexado
    equivaldría a regalar esa clave — y en la unidad de privacidad sería, además, un mal ejemplo. Esos
    recursos se enlazan **desde Moodle**, donde el acceso ya está autenticado.

    Guarda el detalle: es un caso real de **fuga de credenciales en una URL**, uno de los fallos más
    comunes del §7.

## Para ampliar

Ninguno es obligatorio, pero todos dan munición para los debates y para el
[Notebook 2](notebooks/UD06_N02_analisis_caso_etico.ipynb).

| Recurso | Tipo | Con qué apartado engancha | Enlace |
|---|---|---|---|
| *¡AI, AI, AI! Inteligencia artificial* | Documental (RTVE) | §4 riesgos, §4.5 futuro del trabajo | [Ver](https://www.rtve.es/play/videos/somos-documentales/inteligencia-artificial/6235298/){:target="_blank"} |
| *Madagascar: la mano de obra barata de la IA* | Documental | §4.5 futuro del trabajo, desde el ángulo del Sur global: quién etiqueta los datos y en qué condiciones | [Ver](https://youtu.be/9rvq1AR3nRo){:target="_blank"} |
| **Luz Rello** · *Los sesgos en inteligencia artificial* | Entrevista (RTVE, *La aventura del saber*) | **§9 completo**. Es la más directamente aprovechable de las tres | [Ver](https://www.rtve.es/play/videos/la-aventura-del-saber/luz-rello-sesgos-inteligencia-artificial/16464838/){:target="_blank"} |
| **Luz Rello** · *Impacto y desafíos de la inteligencia artificial* | Entrevista (RTVE) | §4 riesgos y §4.4 principios | [Ver](https://www.rtve.es/play/videos/la-aventura-del-saber/luz-rello-impacto-desafios-inteligencia-artificial/16406355/){:target="_blank"} |
| **Luz Rello** · *Desafíos de la inteligencia artificial* | Entrevista (RTVE) | §4 riesgos | [Ver](https://www.rtve.es/play/videos/la-aventura-del-saber/luz-rello-desafios-inteligencia-artificial/16425416/){:target="_blank"} |
| *The Artifice Girl* (2023) | Película | §4.3 dilemas deontológicos, §6.3 transparencia | En **Moodle** |
| *Justicia Artificial* (2024) | Película | **§9.4** justicia algorítmica: es la mejor entrada al debate 2 | En **Moodle** |
| *Sin Piedad* (2026) | Película · sugerencia de un compañero de otro curso | §4 riesgos | Ficha en FilmAffinity (`film385719`) |

## Tertulia de ciencia-ficción

Actividad **voluntaria de ampliación**, sin nota. La ciencia-ficción lleva décadas planteando los
dilemas de esta unidad antes de que fueran técnicamente posibles, y sirve para llegar al debate con
ejemplos que todo el mundo reconoce.

Elige **una** obra, míralas o léela, y prepara tres minutos: qué dilema plantea, con qué apartado de
la teoría se corresponde y si lo que describe ya es posible hoy.

| Obra | Año | Temas | Apartado |
|---|---|---|---|
| **Black Mirror** (serie) | 2011– | Privacidad y datos personales («Nosedive», «The Entire History of You»); responsabilidad y rendición de cuentas («White Bear», «Hated in the Nation») | §5, §6.2 |
| **Westworld** (serie) | 2016-2022 | Autonomía y control humano; conciencia y moralidad de crear seres conscientes | §4.3, FAQ de derechos de los robots |
| **Person of Interest** (serie) | 2011-2016 | Vigilancia masiva y prevención de delitos; supervisión humana de un sistema autónomo | §5.5, §9.4 |
| **Years and Years** (serie) | 2019 | Vigilancia masiva y autoritarismo digital: reconocimiento facial y crédito social | §5.5, §6.1 (usos prohibidos) |
| **Cassandra** (serie) | 2025 | Un asistente doméstico con IA diseñado en los años 60: problemas de diseño y de convivencia cotidiana | §7.3, §7.4 |
| **Ex Machina** | 2014 | Transparencia y explicabilidad; sesgos y dinámicas de poder entre creador y criatura | §6.3, §9 |
| **Her** | 2013 | Privacidad en la interacción con una IA; responsabilidad emocional | §5, §9.6 |
| **Minority Report** | 2002 | Predicción del delito y precrimen; libertad frente a determinismo | **§9.4** |
| **The Matrix** | 1999 | Control y manipulación de la realidad; impacto social y económico | §4.5, §7.4 |
| **El hombre bicentenario** | 1999 | Derechos de las IA; identidad y autonomía | FAQ de derechos de los robots |
| **1984**, de George Orwell (novela) | 1949 | Vigilancia y control totalitario; manipulación de la información | §5.5 |

!!! tip "La pregunta que hace interesante la tertulia"
    No es «¿esto podría pasar?». Es **«¿qué parte de esto ya está pasando, y con qué nombre técnico
    lo llamamos en esta unidad?»**. *Minority Report* es puntuación de riesgo (§9.4). *Nosedive* es
    puntuación social, que el AI Act **prohíbe** (§6.1). *Years and Years* es reconocimiento facial
    masivo, también prohibido. La ficción envejeció; el temario, no.

## Actualidad: veinticinco noticias para el debate

Un argumento con una noticia reciente y verificable vale más que tres opiniones. Esta selección está
comprobada y **fechada**, porque la fecha es parte del argumento (§4.5), y cubre los diez ejes de la
unidad con hechos de los últimos cuatro años, la mitad de ellos del último curso.

| Fecha | Titular | Eje del debate |
|---|---|---|
| **27/09/2022** | [Israel Deploys AI-Powered Turret in the West Bank](https://www.vice.com/en/article/israel-deploys-ai-powered-turret-in-the-west-bank/){:target="_blank"} (Vice) | **§6.4 · armas autónomas**, caso real: torreta de la empresa Smart Shooter en la calle Shuhada, Hebrón |
| **09/05/2024** | [El Gobierno se niega a que nadie revise el código de un software que reparte ayudas](https://www.genbeta.com/actualidad/gobierno-se-niega-a-que-nadie-revise-codigo-software-que-reparte-ayudas-hacerlo-permitiria-hackear-ministerio-dicen){:target="_blank"} | Transparencia y poder · opacidad en la administración |
| **01/08/2024** | [Entra en vigor la Ley Europea de Inteligencia Artificial](https://www.microsiervos.com/archivo/ia/entra-vigor-ley-europea-inteligencia-artificial.html){:target="_blank"} | §6.1 · el día 1 del calendario del AI Act |
| **15/01/2025** | [Más propuestas de leyes de la robótica (y la IA)](https://www.microsiervos.com/archivo/frases-citas/mas-leyes-roboticas.html){:target="_blank"} | §4.4 · principios éticos y su vaguedad |
| **23/01/2025** | [La IA consumirá tanta energía como toda España junta](https://www.genbeta.com/inteligencia-artificial/ia-consumira-tanta-energia-como-toda-espana-junta-gran-problema-estados-unidos-que-parece-no-tener-freno){:target="_blank"} | Sostenibilidad (principio de la UNESCO, §4.3) |
| **20/03/2025** | [La Policía Nacional abandonó su IA estrella para detectar denuncias falsas](https://www.genbeta.com/actualidad/policia-nacional-abandono-su-ia-estrella-para-detectar-denuncias-falsas-este-juego-prueba-problema-que-tenia-base){:target="_blank"} | §9 · caso español de sesgo, y de retirada de un sistema |
| **21/04/2025** | [Ser educado sí cuesta: decir «por favor» y «gracias» a ChatGPT no sale gratis](https://www.genbeta.com/actualidad/ser-educado-cuesta-decir-favor-gracias-a-chatgpt-no-sale-gratis-decenas-millones-dolares-sam-altman){:target="_blank"} | Coste e impacto ambiental de la IA |
| **17/09/2025** | [El Supremo condena al Gobierno a entregar el código fuente de BOSCO](https://civio.es/novedades/2025/09/17/civio-abre-camino-en-la-transparencia-algoritmica-el-supremo-condena-al-gobierno-a-entregar-el-codigo-fuente-de-bosco/){:target="_blank"} (Civio) | §6.3 · opacidad administrativa, el caso español de referencia tras 7 años de litigio |
| **06/11/2025** | [156 states support UNGA resolution on autonomous weapons](https://www.stopkillerrobots.org/news/156-states-support-unga-resolution/){:target="_blank"} (Stop Killer Robots) | **§6.4 · armas autónomas**, la ONU avanza hacia un tratado vinculante |
| **25/11/2025** | [Multa de 10 millones a Aena por reconocimiento facial sin justificar su necesidad](https://www.eldiario.es/tecnologia/multa-10-millones-aena-reconocimiento-facial-pasajeros-justificar-necesidad_1_12796042.html){:target="_blank"} (elDiario.es) | §5 · RGPD, sanción real y reciente (más de 62.000 pasajeros afectados) |
| **04/01/2026** | [Un mapa global de los riesgos de la inteligencia artificial](https://www.microsiervos.com/archivo/ia/mapa-global-riesgos-inteligencia-artificial-soluciones.html){:target="_blank"} | §4 · panorama de riesgos, con soluciones |
| **08/01/2026** | [Google and Character.AI agree to settle lawsuit linked to teen suicide](https://www.jurist.org/news/2026/01/google-and-character-ai-agree-to-settle-lawsuit-linked-to-teen-suicide/){:target="_blank"} (JURIST) | §6.2 · responsabilidad por daños de la IA. Tratamiento sobrio: el hecho es el acuerdo legal, no el suceso |
| **11/03/2026** | [Aragón avanza el primer litigio contra los centros de datos en España](https://climatica.coop/aragon-primer-litigio-centros-de-datos-espana-amazon/){:target="_blank"} (Climática) | Sostenibilidad, primer litigio español contra un macroproyecto de IA |
| **28/03/2026** | [AI deepfakes blur reality in 2026 U.S. midterm campaigns](https://www.staradvertiser.com/2026/03/28/breaking-news/ai-deepfakes-blur-reality-in-2026-us-midterm-campaigns/){:target="_blank"} (AP) | §6.3 · confianza y transparencia, desinformación electoral generada por IA |
| **13/04/2026** | [Europa abre la puerta a Palantir: vigilancia, opacidad y dependencia bajo contrato público](https://spanishrevolution.net/video-europa-abre-la-puerta-a-palantir-vigilancia-opacidad-y-dependencia-bajo-contrato-publico/){:target="_blank"} | §5.5 · vigilancia y §6.3 · opacidad |
| **22/04/2026** | [Capgemini e Inetum lanzan los primeros ERE por IA: 1.173 despidos](https://www.merca2.es/2026/04/22/ere-capgemini-inetum-despidos-ia-espana-2372341/){:target="_blank"} (Merca2) | §4.5 · futuro del trabajo, primer ERE español atribuido a la IA generativa |
| **23/04/2026** | [Autonomous weapons will be "key part" of US warfare, says Joint Chiefs chairman](https://www.defenseone.com/policy/2026/04/autonomous-weapons-warfare-joint-chiefs/413065/){:target="_blank"} (Defense One) | **§6.4 · armas autónomas**, la postura militar de EE. UU. frente al debate de la ONU |
| **07/05/2026** | [AI emerges as a top cause of layoffs, accounting for 26% of April's job cuts](https://www.cbsnews.com/news/ai-layoffs-job-cuts-challenger-report-april-2026/){:target="_blank"} (CBS News) | §4.5 · futuro del trabajo, cifra agregada de EE. UU. que complementa el caso español |
| **17/05/2026** | [How a victim lost US$3.8 million in Singapore deepfake Zoom scam impersonating PM Wong](https://www.scmp.com/news/asia/southeast-asia/article/3353868/how-victim-lost-us38-million-singapore-deepfake-zoom-scam-impersonating-pm-wong){:target="_blank"} (South China Morning Post) | §4.1 · manipulación con deepfakes, la escala del fraude de Hong Kong repetida en Singapur |
| **10/06/2026** | [Florida Man Sues Police Over Wrongful Arrest Due to False Facial Recognition Match](https://www.aclu.org/press-releases/florida-man-sues-police-over-wrongful-arrest-due-to-false-facial-recognition-match){:target="_blank"} (ACLU) | §5.5 · vigilancia, error de reconocimiento facial con una detención real de por medio |
| **22/06/2026** | [Judge rules Workday must face lawsuit alleging its AI applicant-screening tools discriminate](https://www.business-humanrights.org/en/latest-news/usa-judge-rules-workday-must-face-lawsuit-alleging-its-ai-applicant-screening-tools-discriminate-against-women-applicants-with-disabilities-black-applicants-and-older-applicants/){:target="_blank"} (Business & Human Rights RC) | **§9.4 · sesgo algorítmico**, caso real de discriminación en un sistema de cribado de RRHH |
| **27/06/2026** | [Un David aragonés contra el Goliat de la IA: así es la primera batalla contra los centros de datos en España](https://www.publico.es/sociedad/m-ambiente/david-aragones-goliat-ia-asi-primera-batalla-centros-datos-espana.html){:target="_blank"} (Público) | Sostenibilidad, la cifra: un solo centro consumirá el 16,5 % de la electricidad de Aragón |
| **23/07/2026** | [Registro de algoritmos: el reto de iluminar la IA pública en Europa](https://hazrevista.org/transparencia/2026/07/registro-algoritmos-reto-iluminar-ia-publica-europa/){:target="_blank"} (Revista Haz) | §6.3 · opacidad, panorama europeo: solo 34 registros de algoritmos públicos activos |
| **02/08/2026** | [Safer and more transparent AI](https://commission.europa.eu/news-and-media/news/safer-and-more-transparent-ai-2026-08-02_en){:target="_blank"} (Comisión Europea) | §6.1 · AI Act, entrada en vigor de las obligaciones de transparencia del art. 50 |
| **19/08/2026** | ['I Saw a Shiny Thing': Cop Explains Why He Used License Plate Reader to Stalk Woman](https://www.404media.co/i-saw-a-shiny-thing-cop-explains-why-he-used-license-plate-reader-to-stalk-woman/){:target="_blank"} (404 Media) | **§5.5 · vigilancia**, y la mejor entrada al [debate 2](UD06_D02_Debate_algoritmo_crimen_ES.md): un agente de Florida metió la matrícula de una mujer en la *hot list* del lector automático (ALPR Guardian, de Turing) para que el sistema le avisara cada vez que pasaba ante una cámara. No falló la técnica: funcionó exactamente como está diseñada. Al menos **50 casos documentados** de uso policial de ALPR para acosar a exparejas y particulares en EE. UU. |

---
[Volver a la UD06](UD06_ES.md) · [Debate 1](UD06_D01_Debate_limites_eticos_ES.md) ·
[Debate 2](UD06_D02_Debate_algoritmo_crimen_ES.md) ·