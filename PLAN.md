# PLAN.md — Proyecto `_MIA` (Módulo 5071 "Modelos de Inteligencia Artificial")

> Plan maestro recuperable entre sesiones. Última actualización: 2026-09-15 (RA5 en 3 sesiones y RA4/UD04 planificado en las sesiones 5 y 6).

## 1. Contexto

- **Módulo:** 5071 «Modelos de Inteligencia Artificial» (Código IFCES03).
- **Curso de especialización:** Inteligencia Artificial y Big Data (Grado E / FP Grado Superior).
- **Comunidad:** Comunitat Valenciana · **Curso académico:** 2026-2027.
- **Profesor:** José Manuel Pérez Torres.
- **Unidad mínima de planificación:** **sesión de 2 horas**.
- **Alcance de este docente:** **RA1, RA5 y RA4** (ver §3).

## 2. Normativa aplicable (resumen; fichas en `FUENTES.md`)

- **RD 279/2021, de 20 abril** (BOE 10/05/2021): currículo básico; RA/CE del 5071 en su Anexo.
- **RD 497/2024, de 21 mayo**: modifica enseñanzas mínimas de CE.
- **RD 659/2023, de 18 julio**: ordenación del Sistema de FP (LFP).
- **LO 3/2022, de 31 marzo**: ordenación e integración de la FP.
- **DECRETO 95/2026, de 19 junio** (CV): currículos de los CE de FP en la CV; 5071 = 90 h (4 ECTS).
- **ORDEN 8/2025, de 22 abril** (CV): evaluación del proceso de enseñanza-aprendizaje.
- **ORDEN 30/2022, de 12 mayo** (CV): organización en régimen semipresencial.
- **Resolución SAE 15/07/2026** (DOGV 2026/24495): docencia 01/10/2026 → 18/06/2027 máx.

## 3. Alcance del módulo 5071 (este docente)

| Bloque | RA | Enunciado (resumen oficial) |
|--------|----|------------------------------|
| B01 | RA1 | Caracteriza sistemas de IA relacionándolos con la mejora de la eficiencia operativa. |
| B05 | RA5 | Aplicar sistemas expertos y valorar los controladores inteligentes. |
| B04 | RA4 | Analizar sistemas robotizados y evaluar su diseño e implementación. |

**Fuera de alcance de este proyecto:** RA6 (ética y legalidad) y RA7 (proyecto intermodular), que los imparten otros docentes.

## 4. Calendario 26-27 (sesiones de 2h: lunes y miércoles)

- **Inicio docencia:** 2026-10-01. **Primera sesión:** 2026-10-05 (lunes).
- **Fin de centro:** 2027-05-28.
- **Vacaciones:** Navidad 2026-12-22 → 2027-01-06 · Pascua 2027-03-25 → 2027-04-05.
- **Festivos que afectan a lun/mié:** 2026-10-12 (lunes), 2026-12-07 (lunes), 2027-03-17 (miércoles).
- **Sesiones de 2h disponibles:** 57. **Sesiones planificadas (RA1, RA5 y RA4):** 6 en este tramo (ver §5). Las restantes se dejan como margen para refuerzo, evaluación y pruebas por RA.

## 5 Detalle de sesiones (contenido y ejercicios)

Lista de trabajo, sesión a sesión, para redactar el contenido y los ejercicios adaptados al grupo. Por cada sesión usa las subclaves **Contenidos detallados**, **Ejercicios y práctica en clase**, **Materiales / Recursos** y **Observaciones** (enlaza al notebook `sesionNN_miniproyecto.ipynb` cuando proceda).

- **Sesión 1 · 2026-10-05 · Introducción a la IA y tipos de sistemas**
  - RA: RA1
  - Compactar el RA1 en una sola sesión. Utilizar los apuntes de y las prácticas de David Martínez    
  - Contenidos detallados:
    - Situación actual de la IA. Vibecoding, ChatBots, Agentes,
    - Los agentes.
    - Tipos de modelos: predictivos / generativos.
    - Agentes vs fine tuning.
  - Ejercicios y práctica en clase: 
    - Demo del profesor (aprendizaje supervisado y no supervisado): https://martinezpenya.es/ModelosIA/UD01/notebooks/UD01_N01_tecnicas_ia.html
    - https://martinezpenya.es/ModelosIA/UD01/UD01_Ejercicios.html
    - https://martinezpenya.es/ModelosIA/UD01/notebooks/UD01_N02_mapa_sistemas.html
    - https://martinezpenya.es/ModelosIA/UD01/notebooks/UD01_N03_tecnicas_casos.html
    - https://martinezpenya.es/ModelosIA/UD01/notebooks/UD01_N04_nuevas_interacciones.html
    - https://martinezpenya.es/ModelosIA/UD01/notebooks/UD01_N05_linea_tiempo.html
    - https://martinezpenya.es/ModelosIA/UD01/UD01_ES.html
    - https://sever8a.github.io/artint/ia/introduccion/introduccion.html
    - https://sever8a.github.io/artint/ia/introduccion/definicion.html
  - Observaciones: Objetivo didáctico- Al finalizar esta sesión, deberías ser capaz de:
- **Sesión 2 · 2026-10-19 · RA5-1 · Sistemas expertos**
  - RA: RA5
  - Hilo conductor: **Pagarium** (pasarela de pagos que decide sobre transacciones).
  - Contenidos detallados:
    - Por qué reglas en 2026 (BRMS, guardarraíles, compliance); anatomía de un sistema experto; ciclo reconocer-resolver-actuar.
    - **Micro-motor propio en 35 líneas** y su fallo didáctico (dos decisiones contradictorias → razonamiento no monótono y `salience`).
    - Encadenamiento forward/backward; sensibilidad y umbrales; factores de certeza.
    - `experta` (con parche, docencia); **RETE/PHREAK**; **`clipspy`** (CLIPS 6.4) para producción.
  - Ejercicios y práctica en clase:
    - Apuntes S2 y ejercicios bloque A: `docs/bloques/B05_RA5/apuntes.md`, `docs/bloques/B05_RA5/ejercicios.md`.
    - Notebook: `docs/bloques/B05_RA5/sesion02_sistemas_expertos.ipynb`.
    - Actividad A1 (1,5 h).
  - Materiales / Recursos:
    - `material_david/docs/UD05/UD05_ES.md` (solo la parte de sistemas expertos) y `sistemas_expertos.md`.
    - https://martinezpenya.es/ModelosIA/UD05/UD05_ES.html
  - Observaciones:
    - La lógica difusa y los controladores inteligentes de la UD05 se ven en otro bloque.
- **Sesión 3 · 2026-10-21 · RA5-2 · Motores de reglas**
  - RA: RA5
  - Contenidos detallados:
    - **Decision management** y BRMS (Drools/KIE, ODM, Blaze).
    - **Tablas de decisión** y **hit policy** (first, unique, priority, collect).
    - **DMN** (estándar OMG) aplicado a Pagarium.
    - **GoRules ZEN** (fintech, formato JDM) y **`rule-engine`** en Python.
    - **Verificador de cobertura** (huecos/solapes) y **benchmark** (µs/pago: if/else vs ZEN vs CLIPS vs experta).
  - Ejercicios y práctica en clase:
    - Apuntes S3 y ejercicios bloque B.
    - Notebook: `docs/bloques/B05_RA5/sesion03_motores_reglas.ipynb`.
    - Actividad A2 (2 h).
  - Materiales / Recursos:
    - https://martinezpenya.es/ModelosIA/UD05/
    - https://logongas.es/doku.php?id=clase:iabd:pia:1eval:tema01
  - Observaciones:
    - El benchmark sirve para decidir **cuándo NO usar** un motor de reglas.
- **Sesión 4 · 2026-10-26 · RA5-3 · Motores de reglas 2 (híbridos y guardarraíles)**
  - RA: RA5
  - Contenidos detallados:
    - Reglas **extraídas de datos** con **FIGS** (política latente de Pagarium).
    - **Guardarraíles** de agentes LLM con reglas; **sistemas neuro-simbólicos**.
    - **AI Act** y decisiones automatizadas (calendario actualizado; verificar).
    - **Proyecto integrador Pagarium** (capa de negocio + capa guardarraíl).
  - Ejercicios y práctica en clase:
    - Apuntes S4 y ejercicios bloque C.
    - Notebook: `docs/bloques/B05_RA5/sesion04_hibridos_guardarrailes.ipynb`.
    - Actividad A3 (3 h) + proyecto (3,5 h).
  - Materiales / Recursos:
    - https://martinezpenya.es/ModelosIA/UD05/
    - https://logongas.es/doku.php?id=clase:iabd:pia:1eval:tema01
  - Observaciones:
    - Cierre del RA5: entrega del proyecto Pagarium.
- **Sesión 5 · 2026-10-28 · RA4-1 · Sistemas robotizados: robot, cinemática y problemas**
  - RA: RA4
  - Contenidos detallados (UD04 de David, §§4–7):
    - **Métodos y aplicaciones** de la robótica: qué es un robot (percibe-procesa-actúa), tipos (manipulador, móvil, patas, UAV/AUV, cobot), sensores (entorno/ubicación/propioceptivos) y actuadores (eléctrico/hidráulico/neumático); aplicaciones con datos IFR 2025 (542.000 robots, España 3.er mercado europeo).
    - **Qué problema resuelve** la robótica y la jerarquía **tarea → movimiento → control**.
    - **Modelado y control cinemático**: grados de libertad, articulaciones R/P, configuración articulado/cartesiano/SCARA/delta; **cinemática directa con parámetros DH** y **cinemática inversa**; jacobiano; control P/PD/PID y par calculado.
    - **Problemas**: múltiples soluciones (hasta 16), redundancia, sin solución y **singularidades** (muñeca/hombro/codo/límite); **precisión ≠ repetibilidad**; espacio de configuración.
  - Ejercicios y práctica en clase:
    - Cinemática directa e inversa con **`roboticstoolbox-python`** (Panda, Puma 560): `fkine`, `ikine_LM`, tabla DH.
    - Resolución a mano de un brazo plano 3R y cálculo de la pose.
  - Materiales / Recursos:
    - `material_david/docs/UD04/UD04_ES.md` §§4–7 · https://martinezpenya.es/ModelosIA/UD04/UD04_ES.html
    - `pip install roboticstoolbox-python spatialmath-python`
  - Observaciones:
    - Es el bloque RA4-a; el foco es *entender el problema* (cinemática y singularidades), no memorizar álgebra.
- **Sesión 6 · 2026-11-04 · RA4-2 · Planificación, percepción, programación y diseño**
  - RA: RA4
  - Contenidos detallados (UD04 de David, §§8–12):
    - **Planificación de movimiento**: espacio de configuración, espacio libre, grafo de visibilidad (más corto), diagrama de Voronoi (más seguro), descomposición celular y **muestreo (RRT/PRM)**; plan vs. política y control óptimo (LQR/iLQR).
    - **Percepción y SLAM**: localización, mapeo y SLAM; filtro de partículas (MCL); estado de creencia; incertidumbre y **sim-to-real**; aprendizaje por refuerzo en robótica.
    - **Programación de robots**: teach pendant, guiado manual, textual (RAPID/KRL/URScript), offline (OLP) y ROS 2; cobots e **ISO 10218:2025**.
    - **Diseño e implementación**: criterios de selección (payload con herramienta, alcance, repetibilidad, precisión, entorno), sensores de célula, ciclo de vida, célula e Industria 4.0 (PLC, OPC UA/MQTT, gemelo digital) y normativa (ISO 12100, 10218, 9283).
  - Ejercicios y práctica en clase:
    - Navegación con **AITK** (`aitk.robots`): seguir una línea con **reglas** y con **lógica difusa** (mismo problema, dos técnicas).
    - Ejemplo guiado de **selección de robot** (payload + alcance + repetibilidad + seguridad) y verificación en simulación.
  - Materiales / Recursos:
    - `material_david/docs/UD04/UD04_ES.md` §§8–12 · https://martinezpenya.es/ModelosIA/UD04/UD04_ES.html
    - `pip install aitk aitk.robots` · (alternativas 3D: Webots, CoppeliaSim Edu)
  - Observaciones:
    - Cierre del RA4: comparar técnicas de programación resolviendo **un mismo problema** (reglas / difusa / red / NEAT) y justificar la elección.

## 6. Estructura de carpetas (actualizada)

```
_MIA/
├── PLAN.md, AGENTS.md, FUENTES.md, README.md, .gitignore, requirements.txt, serve.sh
├── curriculo.yml       # datos curriculares adaptados (RA/CE, calendario, pesos) en la raíz
├── mkdocs.yml, hooks.py
├── fuentes/           # PDFs de normativa oficial (pendiente de descarga)
├── legislacion/       # análisis normativo + plantilla_sesion.md
├── material_david/    # copia de referencia del proyecto de David (solo análisis)
├── docs/
│   ├── index.md, normativa/index.md
│   ├── evaluacion/    # bancos de pruebas y rúbricas por RA
│   └── bloques/
│       ├── B01_RA1/  (sesion01.md + notebooks y ejercicios)
│       ├── B05_RA5/  (apuntes.md + 3 notebooks de sesión + ejercicios)
│       └── B04_RA4/  (pendiente)
└── PROPUESTAS_MEJORA.md
```

## 7. Plantilla de sesión de 2h

Cada `docs/bloques/Bxx_RAy/sesionNN.md` sigue `legislacion/plantilla_sesion.md` e incluye además:
- **Práctica guiada (con solución):** ejemplo resuelto, con código Python (numpy/pandas/scikit-learn/spaCy/Prolog según toque) y explicación.
- **Práctica propuesta (miniproyecto):** tarea para el alumnado, entregable en `docs/bloques/Bxx_RAy/sesionNN_miniproyecto.ipynb` (renderizado por mkdocs-jupyter, con botones Colab/descargar), con enunciado, entregables y criterios de evaluación.

## 8. Historial de decisiones

- 2026-08-27 (s1): enfoque por sesiones de 2h; 2/semana (lun+mié); viernes = RA7 de otros.
- 2026-08-27 (s1): solo web + notebooks, sin PDF. Festivos desde `material_david/datos/curriculo.yml`.
- 2026-08-27 (s2): **alcance acotado a RA1, RA2 y RA3**; RA4–RA6 y RA7 fuera de este proyecto.
- 2026-08-27 (s2): 26 sesiones planificadas para RA1–RA3; cada sesión con práctica guiada (solución) + miniproyecto propuesto.
- 2026-09-03: RA1 compactado en 1 sesión (2 h) y desplegado en Pages.
- 2026-09-15: alcance redefinido a **RA1, RA5 y RA4**. RA5 reestructurado en **3 sesiones** (19/10, 21/10, 26/10) con enfoque de mercado (Pagarium, DMN, ZEN, FIGS, guardarraíles).

## 9. Pendientes

1. ~~Generar el contenido de las sesiones (RA1 y RA5).~~ **Hecho** (`docs/bloques/B01_RA1/` y `B05_RA5/`).
2. ~~Crear los notebooks de sesión.~~ **Hecho** (RA1 y RA5, con botones Colab/Descargar).
3. ~~Bancos de pruebas y rúbricas en `evaluacion/`.~~ **Hecho**.
4. Descargar PDFs oficiales a `fuentes/`.
5. ~~Fijar `repo_url` / `extra.colab` / `extra.raw_base` en `mkdocs.yml`.~~ **Hecho**.
6. ~~Planificar el bloque **RA4** en las sesiones 5 y 6 (28/10 y 04/11).~~ **Hecho** (§5). Pendiente: generar los apuntes y notebooks de `docs/bloques/B04_RA4/`.
7. ~~Completar `curriculo.yml` con las semanas/fechas de UD01, UD05 y UD04.~~ **Hecho**.
