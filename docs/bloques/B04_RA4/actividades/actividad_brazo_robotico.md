# Actividad · Práctica con el brazo robótico (CE 4b, 4c, 4d)

**Sesión presencial 23-24 (4 h) + trabajo autónomo** · Cuaderno [S23_24_brazo_robotico.ipynb](../S23_24_brazo_robotico.ipynb)

## Objetivo

Pasar del **simulador** al **código** y de ahí al **brazo real**: programar los comandos de movimiento y el dibujo (CE 4b, 4c), y diseñar una **célula de pick & place con ventosa** (CE 4b, 4d), todo en un único cuaderno.

## Fase 1 · Comandos de movimiento y dibujo (simulador)

En el **simulador DobotLab** (Blockly o Python) y en el cuaderno con `BrazoSimulado`:

1. **Seguridad y home** del brazo (con la **ventosa** montada). No invadir la trayectoria.
2. Practica los **comandos de movimiento** (MoveJ, MoveL, Jump, Arc) con velocidades y aceleraciones (ver PDF, Práctica 3). Explica la diferencia entre **MoveJ** (articular) y **MoveL** (lineal).
3. **Dibujo:** usa «Escribir/Dibujar» en el simulador y, en el cuaderno, define una figura (cuadrado, triángulo, pentágono o iniciales) con `move_to` y dibuja la trayectoria.
4. **Valida rangos:** comprueba que `BrazoSimulado` lanza error con un punto fuera de alcance (p. ej. `X < 150` o radio > 320 mm).

## Fase 2 · Pick & place con ventosa y cinta

En el cuaderno, con `BrazoSimulado` + `CintaSimulada`:

1. **Repaso de la secuencia canónica:** punto inicial → pre-pick → pick (aspirar) → esperar → pre-pick → pre-place → place (soltar) → pre-place → inicio.
2. Completa la secuencia **con ventosa** (`suction(True/False)`): activar cinta, esperar detección (fotocélula), aspirar, desplazar, soltar.
3. Define las **alturas Z** (pre-pick, pick, pre-place, place) y los **tiempos de espera** justificados. Usa **Jump** (o puntos seguros) para no chocar con la cinta.
4. **Extensión — paletización:** coloca varias piezas en una **cuadrícula** (filas × columnas) con **bucles** anidados, calculando `x = x0 + col·paso_x`, `y = y0 + fila·paso_y`.
5. **Optativa — clasificación por color:** con el **sensor de color**, deposita cada cubo según su color (`rojo` / `verde` / `azul`).
6. Redacta la **memoria del equipo** (media página): decisiones de diseño, errores y soluciones, y **qué cambiaríais**.

## Entregable

- `S23_24_brazo_robotico.ipynb` **ejecutado**, con las dos fases y la memoria.
- Envío con asunto `UD04-BRAZO-EQUIPO<N>`.

## Criterios de evaluación (rúbrica RA4)

- **4b:** el script funciona, valida rangos y depura errores.
- **4c:** justifica por qué programa en **offline** (simulador/Colab) y qué aporta frente al teach.
- **4d:** compara enfoques, justifica el diseño (ventosa) y propone mejoras con criterios (cadencia, precisión, seguridad).
