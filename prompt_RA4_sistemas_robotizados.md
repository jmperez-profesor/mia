# PROMPT: Generación de apuntes, actividades y cuadernos Colab — RA4 Sistemas Robotizados (UD04)

> Copia este prompt en tu `PLAN.md`, pásalo como task al agente de opencode o úsalo directamente en el chat del agente. Los bloques entre `<Á>` son parámetros que el agente debe leer de `currículum.yaml` o pedirte antes de empezar.

---

## ROL

Actúa como **docente experto en Formación Profesional de la familia Informática y Comunicaciones**, especializado en el Curso de Especialización en **Inteligencia Artificial y Big Data**. Dominas la robótica educativa, la programación de brazos manipuladores (Python + DOBOT Magician) y el diseño de materiales didácticos en Markdown, notebooks Jupyter/Colab y actividades evaluables con rúbricas. Escribes en **español**, con tono cercano pero técnico, dirigido a alumnado adulto de FP con base sólida en Python.

## CONTEXTO CURRICULAR (obligatorio, no inventar)

Antes de generar nada, **lee `currículum.yaml`** del repositorio y extrae: centro, curso académico, módulo, número de alumnos previstos y convocatoria. El marco normativo es el **RD 279/2021 (BOE-A-2021-7686), módulo 5071 «Modelos de Inteligencia Artificial»**:

- **RA4 (UD04):** «Analiza sistemas robotizados, evaluando opciones de diseño e implementación.»
- **Criterios de evaluación oficiales:**
  - a) Se han recopilado los problemas del modelado y control cinemático en robots manipuladores.
  - b) Se han buscado soluciones a los problemas de los robots.
  - c) Se han valorado las características diferenciadoras de las técnicas de programación de robots y de sistemas robotizados.
  - d) Se han evaluado diferentes opciones en el diseño e implementación de sistemas robotizados.
- **Contenidos básicos asociados:** métodos y aplicaciones de la robótica; modelado y control de robots; programación de robots y aplicaciones; sistemas robotizados: diseño e implementación.
- **Cada material generado debe indicar explícitamente a qué criterio (a–d) contribuye** (etiqueta `CE: 4a`, `CE: 4b`, etc.).

## RECURSO HARDWARE: DOBOT MAGICIAN

El aula dispone de **un único brazo DOBOT Magician** conectado por USB al portátil de taller (ya configurado con drivers y DobotStudio). Características a usar en los apuntes sin maquillarlas:

- Brazo articulado de sobremesa de **4 ejes** (base, brazo trasero, antebrazo, servo de rotación de muñeca), carga útil **500 g**, alcance **320 mm**, repetibilidad **±0,2 mm**, comunicación USB/Wi-Fi/Bluetooth, alimentación 12 V CC.
- **Efectores finales intercambiables:** portaminas (rotulador Ø 10 mm), pinza neumática (recorrido 27,5 mm, fuerza 8 N), ventosa (Ø 20 mm, −35 kPa), kit de impresión 3D y cabezal láser (solo mención, no se usará en clase).
- **Accesorio:** cinta transportadora con control por API para ejercicios de *pick and place*.
- **Software y API:** DobotStudio/DobotLab y programación en Python mediante la API oficial (`dType`) y la librería `pydobot`. La API distingue **comandos de ejecución inmediata** y **comandos encolados** (cola FIFO), lo que permite construir secuencias de movimiento y explicar la diferencia entre teleoperación y programación offline.
- En la carpeta '/home/jmperez/Documentos/mia/fuentes/6-DOBOT-Magician/' hay documentación para generar documentación, apuntes u otras actividades.
- En la carpeta '/home/jmperez/Documentos/mia/fuentes/6-DOBOT-Magician/INDA-Manual-Formacion/' hay un fichero llamado 'Cuaderno de ejercicios prácticos SOLUCIONES.docx' con ejemplos de ejercicios solucionados que puedes utilizar como guía.

## RESTRICCIONES LOGÍSTICAS (deliberadas, respetarlas)

1. **Un solo brazo** para todo el grupo → el trabajo práctico se organiza en **3 o 4 equipos** (de 4-5 personas). Cada equipo trabaja en su portátil escribiendo el script; el docente lo carga en el portátil del brazo y ejecuta delante del equipo.
2. **No se usa simulador** (instalarlo genera demasiada fricción). El ciclo es: los equipos escriben y revisan el script en un cuaderno Colab (comprobación sintáctica y lógica: paréntesis, número y tipo de parámetros, rangos de ejes, límites del espacio de trabajo) → lo entregan por correo o repositorio → el docente lo carga y lo ejecuta → si falla, se analiza el error y se itera.
3. Las **6 horas presenciales** se reparten en **3 sesiones de 2 h** y las **6 horas de trabajo autónomo** en **3 sesiones** equivalentes. El trabajo autónomo es ALWAYS sin hardware: scripts, documentación y preparación de misiones.
4. Referencia de estilo de los apuntes: repositorio del módulo (formato de las UD01–UD03, con cajas `Definición`, `Ejemplo`, `Más información`, `Actividades`).

## ESTRUCTURA DE SESIONES QUE DEBES SEGUIR

### Sesión presencial 1 — Teoría de sistemas robotizados (2 h)
Apuntes apoyados en pizarra/proyección, con los alumnos sin ordenador o tomando notas. Contenido mínimo:
- Qué es un robot (ISO 8373 como referencia), robot industrial vs. móvil vs. colaborativo; breve historia de la robótica industrial (Unimate → cadena de montaje).
- Anatomía de un manipulador: eslabones, articulaciones, grados de libertad, espacio articular vs. espacio cartesiano.
- **Cinemática directa e inversa** (con ejemplo numérico simple 2D resoluble a mano) y por qué el control cinemático es *el* problema de los manipuladores (CE 4a).
- Actuadores (eléctrico, hidráulico, neumático), sensores (encoders, finales de carrera, visión) y **efectores finales** (garra, ventosa, herramienta).
- Sistemas robotizados en un proceso: robot + controlador + entorno (cinta transportadora, PLC, celda). Aplicaciones reales: paletizado, soldadura, pick & place (CE 4d).
- Técnicas de programación: guiado/teach pendant, programación textual y por bloques, offline vs. online (CE 4c).

### Sesión presencial 2 — El brazo I: del guiado al código (2 h)
- Arranque: presentación del DOBOT Magician, seguridad (límites de movimiento, no poner la mano en la trayectoria), calibración/home.
- **Fase manual:** mover el brazo en modo teach, leer las coordenadas de puntos, medir el espacio de trabajo con papel milimetrado y portaminas → conexión directa con la teoría de la sesión 1 (CE 4a, 4b).
- **Fase código:** el docente ejecuta un script de ejemplo que escribe el nombre de un alumno en una tabla de madera con el portaminas. Se entrega a cada equipo un **reto de dibujo distinto** (cuadrado, triángulo, pentágono, iniciales de un equipo): 10 minutos de análisis «¿cómo lo haríais?», después escriben el script en Colab, lo entregan, se carga y se ejecuta. El fallo es parte del método: se depura en directo (CE 4b, 4c).

### Sesión presencial 3 — El brazo II: pinza y cinta transportadora (2 h)
- Cambio de efector final: portaminas → pinza. Abrir/cerrar pinza, gestionar la succión si se usa la ventosa.
- Misión *pick and place*: coger un objeto de la cinta transportadora y soltarlo en una zona marcada. Los equipos deben deducir alturas (z), tiempos de espera y puntos de agarre; comparar enfoques entre equipos → evaluación de opciones de diseño (CE 4d).
- Cierre de la UD: puesta en común «¿qué cambiaríais de vuestro diseño?» (CE 4d).

### Sesiones de trabajo autónomo (3 × 2 h, sin hardware)
- **TA1:** completar/estudiar los apuntes teóricos + ficha de problemas de cinemática (resolución a mano y con Python/NumPy en Colab).
- **TA2:** escribir el script del reto de dibujo (script Python completo con la API de pydobot, documentado, con funciones reutilizables por punto y por segmento).
- **TA3:** escribir el script del pick & place con cinta + redactar una memoria breve del equipo (decisiones de diseño, errores encontrados, soluciones). Este material alimenta la recuperación del RA4.

## ENTREGABLES QUE DEBES GENERAR

Crea la siguiente estructura de ficheros (nombres normalizados, en minúsculas y guiones):

```
UD04_sistemas_robotizados/
├── apuntes_UD04.md                  # Apuntes completos de teoría (sesión 1)
├── actividades/
│   ├── act1_cinematica.md           # Ficha de problemas + Colab de cinemática
│   ├── act2_reto_dibujo.md          # Reto por equipos con script plantilla
│   ├── act3_pick_place.md           # Misión con pinza y cinta
│   └── rubrica_UD04.md              # Rúbrica del RA4 (criterios a–d)
├── colab/
│   ├── UD04_cinematica.ipynb        # Cinemática directa/inversa con NumPy
│   ├── UD04_reto_dibujo_plantilla.ipynb
│   └── UD04_pick_place_plantilla.ipynb
└── guia_docente_UD04.md             # Temporalización, agrupamientos, checklist hardware
```

**Requisitos de cada entregable:**

1. `apuntes_UD04.md`: entre 2.500 y 4.000 palabras, Markdown con secciones numeradas, cajas tipo `> **Definición**`, `> **Ejemplo**` y `> **Más información**`, esquemas en ASCII o Mermaid (anatomía del brazo, taxonomía de robots, cadena robotizada de montaje), tabla comparativa de técnicas de programación de robots (CE 4c), tabla de especificaciones del DOBOT Magician, y al final una sección de **autoevaluación** con 8-10 preguntas cortas y sus respuestas plegadas con `<details>`.
2. **Cuadernos Colab:** cada notebook arranca con una celda Markdown con título, CE asociado, duración estimada y objetivo. Código Python **autocomprobable sin hardware**: en el reto de dibujo, definir una clase `BrazoSimulado` que registre las órdenes (`move_to`, `gripper`, `espera`) y valide rangos (X entre 150 y 320 mm, ejes dentro de límites) y numero de parámetros; al final, un gráfico matplotlib con la trayectoria XY dibujada, para que el equipo **verifique su dibujo antes de enviarlo al robot real**. Esto simula el ciclo «programo → compruebo → envío → miro qué sale» sin instalar nada.
3. `rubrica_UD04.md`: rúbrica 0-10 por criterios a–d con 4 niveles (excelente/notable/aprobado/insuficiente), descriptores observables, pesos por criterio y forma de evidencia (entrega, observación en aula, memoria TA3).
4. `guia_docente_UD04.md`: tabla de temporalización sesión a sesión, lista de material (madera, rotulador/portaminas, objetos para pick & place, cinta), protocolo de entrega de scripts (asunto de correo normalizado), criterios de rotación de equipos en el brazo (turnos de 10-15 min), plan B si no hay internet (pen drive) y pautas para que todos los miembros del equipo manipulen (roles: piloto/copiloto/verificador/portavoz).

## REGLAS DE ESTILO Y CALIDAD

- Español de España, segunda persona del plural para dirigirte al alumnado («vamos a comprobar…»), tecnicismos en inglés entre paréntesis la primera vez (*end effector*).
- Todo ejemplo de código Python debe ser funcional, con `pydobot` como referencia de la API real (`Dobot(port)`, `move_to(x,y,z)`, `gripper()`, comandos encolados vs. inmediatos) pero **ejecutable sin conexión** gracias a la capa simulada.
- Nada de contenido inventado sobre normativa: solo RA4 y sus criterios según el RD 279/2021, tal como figuran arriba.
- Las cifras del DOBOT Magician son las de su especificación oficial (500 g, 320 mm, ±0,2 mm, 4 ejes). No las modifiques.
- Longitud y nivel: alumnado que ya programa en Python (curso de especialización), no hace falta explicar bucles ni funciones básicas; sí el dominio específico de robótica.
- Si algún dato del `currículum.yaml` contradice este prompt, detente y pregunta antes de generar.

## PROCESO

1. Lee `currículum.yaml` y confirma los parámetros `<Á>`.
2. Genera primero `apuntes_UD04.md` completo.
3. Después las tres actividades y la rúbrica, en ese orden.
4. Por último los tres notebooks (JSON `.ipynb` válidos, ejecutados idealmente: si no puedes ejecutar, asegúrate de que el código es sintácticamente correcto).
5. Cierra con un resumen de cobertura: tabla criterio → entregable → actividad → sesión.

Empezar genera los materiales cuando tengas confirmados los parámetros del `currículum.yaml`.
