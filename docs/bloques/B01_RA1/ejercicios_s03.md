# S03 · Ejercicios de autoevaluación — IA 2: Entornos actuales. Proyectos IA fases

> Adaptados de `material_david/docs/UD00/UD00_Ejercicios.md` (bloques B–D, CC BY-NC-SA 4.0) y de `material_david/docs/UD01/UD01_Ejercicios.md` + `artint/docs/ia/fases_aa/` + `docs/bloques/B01_RA1/sesion03.md`. Distintos de S01/S02.

## A. Ciclo de vida (RA1-b/d)

**A1.** Enumera y explica en una frase cada fase: Definir problema/KPI → Datos → Preproceso → Entrenamiento → Evaluación → Despliegue. ¿Qué entregable mínimo deja cada una?

**A2.** Dado el caso LARA/hidrógeno/colmena, elige un KPI (tiempo, coste, error) y describe su valor *antes* y *después* estimado.

## B. Entornos (UD00)

**B1.** Diferencia **imagen** y **contenedor** con un ejemplo (`jupyter/scipy-notebook`).

**B2.** ¿Qué hace `docker run` cuando la imagen aún no está descargada? Describe 3 pasos.

**B3.** Colab vs. Docker vs. local: ¿cuándo usarías cada uno en clase y en entrega? Justifica reproducibilidad.

**B4.** Escribe el `compose.yaml` mínimo para Jupyter en `8888` montando `./practicas:/home/jovyan/work` con `JUPYTER_TOKEN=cursoia`.

## C. Datos y preproceso (artint fases_aa)

**C1.** ¿Por qué el 80 % del tiempo se va en preproceso? Cita escalado y división train/test honesta (Iris 150×4).

**C2.** ¿Qué fuga provocas si ajustas `StandardScaler` o PCA con *todo* el dataset antes del `split`?

**C3.** Clasifica: ¿tu problema es clasificación, regresión o clustering? ¿Qué métrica mirarías en evaluación?

## D. Entrenamiento y evaluación

**D1.** Ningún algoritmo gana siempre. Explica el flujo *probar varios → comparar con métrica común → elegir* y qué es validación cruzada.

**D2.** Escribe el `Pipeline` honesto `StandardScaler + DecisionTree` (como en S03) y señala dónde se ajusta el scaler.

> Soluciones en clase. Bases: `UD00_Ejercicios.md` B8–B14, D21–D26 + `UD01` + `artint/ia/fases_aa/`.
