# Actividad 3 · Pick & place con pinza y cinta (CE 4b, 4d)

**Sesión presencial S3 (2 h) + trabajo autónomo TA3 (2 h)** · Cuaderno [UD04_pick_place_plantilla.ipynb](../colab/UD04_pick_place_plantilla.ipynb)

## Objetivo

Diseñar e implementar una **célula** de *pick & place*: coger un objeto de la **cinta transportadora** y dejarlo en una zona marcada, comparando enfoques y evaluando opciones de diseño (CE 4d).

## Fase 1 · En clase (S3)

1. **Cambio de efector:** portaminas → **pinza** (o ventosa). Probar abrir/cerrar y la succión.
2. **Repaso de la secuencia canónica** de pick & place: punto inicial → pre-pick → pick (abierto) → pick (cerrado) → pre-pick → pre-place → place (cerrado) → place (abierto) → pre-place → inicio.
3. **Misión:** la cinta avanza; cuando la **fotocélula** detecta el objeto, el robot lo coge y lo deja en la zona marcada.
4. Ejecución **por turnos** y comparación de enfoques entre equipos.

## Fase 2 · Trabajo autónomo (TA3)

En `UD04_pick_place_plantilla.ipynb`:

1. Completa la secuencia con **`BrazoSimulado`** + **`CintaSimulada`** (activar cinta, esperar detección, coger, dejar).
2. Define las **alturas Z** (pre-pick, pick, pre-place, place) y los **tiempos de espera** justificados.
3. Usa **Jump** (o puntos seguros) para no chocar con la cinta.
4. Redacta la **memoria del equipo** (media página): decisiones de diseño, errores encontrados y soluciones, y **qué cambiaríais**.

## Entregables

- `UD04_pick_place_plantilla.ipynb` **ejecutado**.
- **Memoria** con decisiones y propuestas de mejora (alimenta la recuperación del RA4).
- Envío con asunto `UD04-S3-EQUIPO<N>-pick_place`.

## Criterios de evaluación (rúbrica RA4)

- **4b:** la secuencia funciona y respeta límites y tiempos.
- **4d:** compara enfoques, justifica el diseño y propone mejoras con criterios (cadencia, precisión, seguridad).
