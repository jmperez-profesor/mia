# PLAN.md — Proyecto `_MIA` (Módulo 5071 "Modelos de Inteligencia Artificial")

> Plan maestro recuperable entre sesiones. Última actualización: 2026-09-15 (reestructuración del bloque RA5 en 3 sesiones, nav y curriculo.yml).

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
- **Sesión 5 · 2026-10-28 · RA4.1 Sistemas robotizados. Brazo robótico**
  - RA: RA4
  - Contenidos detallados:
     - Ellos son los que trabajan, no hablar tanto.
  - Ejercicios y práctica en clase: por hacer
  - Materiales / Recursos:
    - https://sever8a.github.io/artint/redes-neuronales/introduccion.html
    - https://sever8a.github.io/artint/redes-neuronales/perceptron.html
    - https://sever8a.github.io/artint/redes-neuronales/multicapa.html
    - https://sever8a.github.io/artint/redes-neuronales/regresion.html
    - https://sever8a.github.io/artint/redes-neuronales/clasificacion.html
    - https://sever8a.github.io/artint/redes-neuronales/convolucionales.html
    - https://sever8a.github.io/artint/redes-neuronales/lstm.html
    - https://sever8a.github.io/artint/redes-neuronales/transformers.html
  - Observaciones:
- **Sesión 6 · 2026-11-04 · RA4.2 Sistemas robotizados. Brazo robótico 2**
  - RA: RA4
  - Contenidos detallados:
     - Ellos son los que trabajan, no hablar tanto.
  - Ejercicios y práctica en clase: por hacer
  - Materiales / Recursos:
    - https://sever8a.github.io/artint/redes-neuronales/introduccion.html
    - https://sever8a.github.io/artint/redes-neuronales/perceptron.html
    - https://sever8a.github.io/artint/redes-neuronales/multicapa.html
    - https://sever8a.github.io/artint/redes-neuronales/regresion.html
    - https://sever8a.github.io/artint/redes-neuronales/clasificacion.html
    - https://sever8a.github.io/artint/redes-neuronales/convolucionales.html
    - https://sever8a.github.io/artint/redes-neuronales/lstm.html
    - https://sever8a.github.io/artint/redes-neuronales/transformers.html
  - Observaciones:

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
6. Generar el bloque **RA4** (sistemas robotizados) para las sesiones 5 y 6 (28/10 y 04/11).
7. Completar `curriculo.yml` con las semanas/fechas de UD01 y UD05 (hecho) y revisar UD04.
