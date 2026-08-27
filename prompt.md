Eres mi asistente de agentes en opencode. Vamos a construir DESDE CERO, en modo PLAN primero, un proyecto de apuntes y materiales docentes para el módulo: "Modelos de IA" (5071) — Curso de Especialización en Inteligencia Artificial y Big Data (FP, Grado E) Comunidad/normativa: Comunitat Valenciana, curso 2026-2027 
Profesor: José Manuel Pérez Torres

## Referencia de proceso (NO de contenido)
Existe un proyecto hermano de un compañero (David Martínez Peña, IES Eduardo Primo Marqués) en 
https://github.com/martinezpenya/ModelosIA (también ubicado en la carpeta "/home/jmperez/Documentos/ModelosIA") 
con su web publicada en https://martinezpenya.es/ModelosIA/index.html. Quiero que uses ESE PROYECTO SOLO COMO 
REFERENCIA DE METODOLOGÍA DE TRABAJO (estructura de carpetas, ficheros de gobierno PLAN.md/
AGENTS.md/FUENTES.md, forma de documentar sesiones, forma de citar legislación, estructura
mkdocs con tema Material). NO copies literalmente contenidos, redacciones ni textos de su web
o su repo: yo tengo mi propio enfoque didáctico y mis propias 6 sesiones/temas ya generados con
NotebookLM que aportaré yo. Si accedes al repo, analiza solo su ARQUITECTURA de proyecto y su
flujo de trabajo por sesiones, no reutilices su prosa.

## Diferencia clave respecto al proyecto de referencia
El compañero organiza el curso por "Unidades Didácticas" (UD00-UD07) con una duración variable
en horas. YO organizo mi docencia en SESIONES DE TRABAJO DE 2 HORAS (mi unidad mínima real de
programación de aula), agrupadas después en bloques temáticos/RA. Por tanto:
- La unidad de planificación temporal del proyecto debe ser la SESIÓN DE 2 HORAS, no la UD.
- Cada sesión de 2h debe tener: objetivos, contenidos, actividades, duración desglosada en
  minutos (apertura, desarrollo, cierre/evaluación), materiales/recursos, y enlace a la
  práctica/notebook si aplica.
- Las Unidades/Bloques temáticos agrupan varias sesiones de 2h y se alinean con los RA/CE del
  currículo oficial.

## Objetivo del proyecto
Generar, en sesiones de trabajo independientes con opencode (yo iré retomando la conversación
en distintos días), TODO el material del módulo:
1. Legislación y currículo aplicable (normativa estatal + autonómica CV vigente para 26-27).
2. Programación didáctica: RA-CE -> Bloques temáticos -> sesiones de 2h, con temporalización real.
3. Web de apuntes con MkDocs (tema Material, en español), organizada por bloques y sesiones,
   con notebooks Jupyter renderizados (mkdocs-jupyter) y botones "Descargar .ipynb" / "Abrir en Colab".
4. Prácticas y talleres en Python (numpy, pandas, matplotlib, scikit-learn, NLP con spaCy/nltk,
   sistemas expertos, robótica simulada, etc.) según cada RA.
5. Banco de pruebas/evaluación (test + desarrollo) y rúbricas por RA.
6. Opcionalmente, especificación/backup Moodle si decido exportarlo más adelante.
7. Informe final de mejoras y decisiones (equivalente a PROPUESTAS_MEJORA.md).

## Fuentes:
Usa el material de David como fuente de contenido, ya que, voy revisarlo y aportar ideas y mejoras. 


## Estructura de proyecto a crear (adaptar del patrón de referencia)
_MIA/
├── PLAN.md            # plan maestro recuperable entre sesiones (con temporalización por SESIONES de 2h)
├── AGENTS.md          # estado, historial de decisiones, convenciones, mapa de ficheros
├── FUENTES.md         # fichas de fuentes legales y técnicas (ref. oficial, URL, uso)
├── README.md, .gitignore, requirements.txt, serve.sh
├── mkdocs.yml, hooks.py
├── fuentes/           # PDFs normativa oficial
├── legislacion/       # análisis normativo + programación didáctica (por sesiones de 2h)
├── material_david/    # descarga los apuntes de David para análisis y extracción de mejoras
├── docs/              # web mkdocs: index, normativa/, bloques temáticos con sus sesiones de 2h
├── practicas/         # notebooks por sesión/bloque
├── evaluacion/        # bancos de pruebas y rúbricas
└── PROPUESTAS_MEJORA.md

## Primera sesión de trabajo (lo que quiero que hagas AHORA, en modo plan)
1. Investiga y confírmame la normativa vigente aplicable (estatal RD del curso de
   especialización + decreto/currículo autonómico CV para 26-27, orden de evaluación vigente).
2. Propón el scaffolding completo de carpetas y ficheros de gobierno (PLAN.md, AGENTS.md,
   FUENTES.md, README.md) adaptados a mi enfoque por sesiones de 2h.
3. Pregúntame explícitamente: número real de sesiones de 2h/semana, horario, días exactos que hay clase, días de fiestas. 
   El proyecto intermodular (RA7) lo gestionan otros compañeros (bloque final con todos los
   docentes).
4. Propón una plantilla estándar de "ficha de sesión de 2h" (objetivos, contenidos, timing,
   actividades, recursos, evaluación) que usaremos para TODAS las sesiones del curso.
5. NO generes contenido de las sesiones todavía: primero cerramos plan, estructura y plantillas.
6. Al final de cada sesión de trabajo futura, actualiza PLAN.md y AGENTS.md con el progreso,
   igual que hace el flujo de referencia, para poder retomar en la siguiente sesión sin perder
   contexto.

Responde en modo PLAN: no escribas ficheros todavía, preséntame el plan de scaffolding y las
preguntas abiertas para que las valide antes de que empieces a generar nada.