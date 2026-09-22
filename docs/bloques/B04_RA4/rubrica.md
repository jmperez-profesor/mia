# Rúbrica del RA4 · Análisis de sistemas robotizados

**RA4:** *Analiza sistemas robotizados, evaluando opciones de diseño e implementación.*
Escala **0-10** (entera). Nota mínima para superar el RA: **5** (Orden 8/2025).

## Pesos por criterio

| CE | Criterio | Peso |
|----|----------|------|
| **4a** | Problemas del modelado y control cinemático | 25 % |
| **4b** | Soluciones a los problemas de los robots | 25 % |
| **4c** | Características de las técnicas de programación | 20 % |
| **4d** | Evaluación de opciones de diseño e implementación | 30 % |

**Evidencias:** `act1` (cinemática), `act2` (reto de dibujo), `act3` (pick & place), **memoria TA3**, observación en aula y prueba escrita.

## 4a · Modelado y control cinemático (25 %)

| Nivel | Descriptor observable |
|---|---|
| **9-10 (Excelente)** | Resuelve FK e IK con el ejemplo 2D, identifica múltiples soluciones y explica las singularidades y el espacio de trabajo del DOBOT con precisión. |
| **7-8 (Notable)** | Calcula FK e IK correctamente y menciona singularidades y límites con algún ejemplo. |
| **5-6 (Aprobado)** | Calcula la FK y reconoce que la IK puede tener varias soluciones, con imprecisiones menores. |
| **0-4 (Insuficiente)** | Confunde FK con IK o no resuelve el ejemplo numérico. |

## 4b · Soluciones a los problemas (25 %)

| Nivel | Descriptor observable |
|---|---|
| **9-10** | Su script **valida rangos y número de parámetros** con `BrazoSimulado`, depura errores de forma autónoma y justifica la solución. |
| **7-8** | El script funciona tras alguna iteración y aplica la validación de rangos. |
| **5-6** | El script funciona con ayuda del docente; valida parcialmente. |
| **0-4** | El script no funciona o no contempla los límites del robot. |

## 4c · Técnicas de programación (20 %)

| Nivel | Descriptor observable |
|---|---|
| **9-10** | Compara teach/Blockly/textual y online/offline con criterios, y elige y justifica la técnica para cada tarea. |
| **7-8** | Describe las técnicas y su uso en el aula con ejemplos. |
| **5-6** | Enumera las técnicas con alguna confusión. |
| **0-4** | No distingue las técnicas o no las relaciona con la tarea. |

## 4d · Diseño e implementación (30 %)

| Nivel | Descriptor observable |
|---|---|
| **9-10** | Diseña la secuencia de pick & place con puntos de paso y tiempos justificados, **compara enfoques** entre equipos y propone mejoras con criterios (cadencia, precisión, seguridad). |
| **7-8** | Diseña una secuencia correcta y explica sus decisiones con claridad. |
| **5-6** | Completa la secuencia con apoyo y describe lo que hace. |
| **0-4** | No completa la misión o no justifica el diseño. |

## Conversión a nota

`Nota = 0,25·(4a) + 0,25·(4b) + 0,20·(4c) + 0,30·(4d)`, redondeada a entero.
