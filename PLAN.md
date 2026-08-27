# PLAN.md — Proyecto `_MIA` (Módulo 5071 "Modelos de Inteligencia Artificial")

> Plan maestro recuperable entre sesiones. Última actualización: 2026-08-27 (sesión 1, modo PLAN → scaffolding).

## 1. Contexto

- **Módulo:** 5071 «Modelos de Inteligencia Artificial» (Código IFCES03).
- **Curso de especialización:** Inteligencia Artificial y Big Data (Grado E / FP Grado Superior).
- **Comunidad:** Comunitat Valenciana · **Curso académico:** 2026-2027.
- **Profesor:** José Manuel Pérez Torres.
- **Unidad mínima de planificación:** **sesión de 2 horas** (no UD). Las sesiones se agrupan en 6 bloques temáticos alineados con los RA del módulo.
- **RA7 (proyecto intermodular):** lo gestionan otros compañeros (bloque final con todos los docentes). **Fuera del alcance de este proyecto.**

## 2. Normativa aplicable (resumen; fichas completas en `FUENTES.md` y `legislacion/`)

- **RD 279/2021, de 20 abril** (BOE 10/05/2021): crea el CE y fija el currículo básico; RA/CE del módulo 5071 en su Anexo.
- **RD 497/2024, de 21 mayo** (BOE 28/05/2024): modifica enseñanzas mínimas de CE.
- **RD 659/2023, de 18 julio**: desarrolla la ordenación del Sistema de FP (LFP).
- **LO 3/2022, de 31 marzo**: ordenación e integración de la FP (marco de la evaluación).
- **DECRETO 95/2026, de 19 junio** (Consell, CV): currículos de los CE de FP en la CV; concreta el 5071 a **90 h** (4 ECTS).
- **ORDEN 8/2025, de 22 abril** (CV): regula la **evaluación** del proceso de enseñanza-aprendizaje en ciclos y CE (derivada de LO 3/2022). Orden de evaluación vigente.
- **ORDEN 30/2022, de 12 mayo** (CV): organización/autorización en régimen semipresencial.
- **Resolución SAE 15/07/2026** (DOGV 2026/24495): instrucciones de ordenación académica 26-27 (docencia 01/10/2026 → 18/06/2027 máx.).

## 3. Alcance del módulo 5071 (backbone curricular)

| Bloque | RA | Enunciado (resumen oficial) |
|--------|----|------------------------------|
| B01 | RA1 | Caracteriza sistemas de IA relacionándolos con la mejora de la eficiencia operativa. |
| B02 | RA2 | Utiliza modelos de sistemas de IA implementando sistemas de resolución de problemas. |
| B03 | RA3 | Relaciona el procesamiento de lenguaje natural (PLN) con sus aplicaciones y limitaciones. |
| B04 | RA4 | Analiza sistemas robotizados, evaluando opciones de diseño e implementación. |
| B05 | RA5 | Aplica sistemas expertos evaluando la influencia de los controladores inteligentes. |
| B06 | RA6 | Aplica principios legales y éticos al desarrollo de la IA. |

**RA7: excluido** (proyecto intermodular de otros docentes).

## 4. Calendario 26-27 (sesiones de 2h: lunes y miércoles)

- **Inicio docencia:** 2026-10-01 (jueves). **Primera sesión 5071:** 2026-10-05 (lunes).
- **Fin de centro:** 2027-05-28 (junio queda para prueba ordinaria).
- **Días de clase del módulo:** lunes y miércoles (2 sesiones/semana). Las 4 h del viernes son el proyecto RA7 (de otros docentes, no contabilizadas aquí).
- **Vacaciones:** Navidad 2026-12-22 → 2027-01-06 · Pascua 2027-03-25 → 2027-04-05.
- **Festivos que afectan a lun/mié** (del `material_david/datos/curriculo.yml`, adaptados):
  - 2026-10-12 (lunes) Fiesta Nacional
  - 2026-12-07 (lunes) puente
  - 2027-03-17 (miércoles) Fallas
  - (No afectan: 9/10 y 19/3 caen en viernes; 8/12 martes; 18/3 jueves.)
- **Sesiones de 2h disponibles:** **57** (114 h) entre 2026-10-05 y 2027-05-26.

> Nota: el decreto CV asigna 90 h (45 sesiones) al 5071; el horario real del centro (2 sesiones/semana) arroja 57 sesiones. Se respetará el criterio del centro y el margen se usará para evaluación, repaso y pruebas por RA.

## 5. Temporalización por sesiones de 2h (PROVISIONAL, a ajustar con el contenido NotebookLM)

| Bloque | RA | Sesiones 2h estimadas | Periodo orientativo |
|--------|----|----------------------:|---------------------|
| B01 | RA1 | 7 | oct–nov |
| B02 | RA2 | 11 | nov–ene |
| B03 | RA3 | 10 | dic–feb |
| B04 | RA4 | 7 | feb–mar |
| B05 | RA5 | 9 | mar–abr |
| B06 | RA6 | 8 | abr–may |
| Evaluación/repaso/pruebas RA | — | 5 | a lo largo del curso |
| **Total** | | **57** | |

Cada sesión sigue la plantilla en `legislacion/plantilla_sesion.md`. Las fechas exactas se fijarán al volcar el calendario a `legislacion/programacion.yml` (fuente única) y generar las tablas de `docs/`.

## 6. Estructura de carpetas

```
_MIA/
├── PLAN.md            # este fichero (plan maestro por SESIONES de 2h)
├── AGENTS.md          # estado, historial de decisiones, mapa de ficheros, comandos
├── FUENTES.md         # fichas de fuentes legales y técnicas
├── README.md
├── .gitignore, requirements.txt, serve.sh
├── mkdocs.yml, hooks.py
├── fuentes/           # PDFs de normativa oficial (pendiente de descarga)
├── legislacion/       # análisis normativo + programación didáctica (por sesiones 2h)
│   └── plantilla_sesion.md
├── material_david/    # copia de referencia del proyecto de David (solo análisis)
├── docs/              # web mkdocs (Material, español)
│   ├── index.md
│   ├── normativa/
│   ├── bloques/B01_RA1 … B06_RA6/   # cada bloque con sus sesiones
│   └── assets/
├── practicas/         # notebooks .ipynb por sesión/bloque
├── evaluacion/        # bancos de pruebas y rúbricas por RA
└── PROPUESTAS_MEJORA.md
```

## 7. Plantilla de sesión de 2h

Definida en `legislacion/plantilla_sesion.md`. Campos: cabecera (nº sesión, bloque/RA, fecha, duración 120 min), objetivos, contenidos, temporalización (apertura 10' / desarrollo 80' / cierre-evaluación 30'), actividades, materiales/recursos, práctica/notebook (botones Colab/descargar), evaluación (CE), atención a la diversidad, observaciones.

## 8. Historial de decisiones (sesión 1)

- 2026-08-27: Se confirma enfoque por **sesiones de 2h** (no UD). 2 sesiones/semana (lunes y miércoles). Viernes 4h = RA7 (otros). Curso inicia 01/10/2026.
- 2026-08-27: Fuentes de festivos/vacaciones tomadas de `material_david/datos/curriculo.yml` (calendario Carlet 26-27, DOGV 2026/24495).
- 2026-08-27: El material de David se usa **solo como referencia de metodología/contenido a revisar**, no se copia literalmente su prosa.
- 2026-08-27: Solo web MkDocs + notebooks Jupyter (sin generación de PDF «libro»).
- 2026-08-27: Las 6 sesiones/temas de NotebookLM del profesor aún no se aportan; se integrarán más adelante.
- 2026-08-27: No fijarse en el ajuste estricto a 90 h; prevalece el horario real del centro.

## 9. Pendientes y próximos pasos

1. Descargar/ubicar PDFs oficiales en `fuentes/` (RD 279/2021, Decreto 95/2026, Orden 8/2025, etc.).
2. Redactar `legislacion/programacion_didactica.md` + `programacion.yml` (fuente única de temporalización).
3. Cuando el profesor aporte el contenido NotebookLM, generar las fichas de sesión en `docs/bloques/Bxx/`.
4. Crear notebooks de práctica en `practicas/` con botones Colab/descargar (ya cableados en `hooks.py`).
5. Bancos de pruebas y rúbricas en `evaluacion/`.
6. (Opcional, futuro) exportación/backup Moodle.
7. Al cerrar cada sesión de trabajo, actualizar `PLAN.md` y `AGENTS.md`.
