# Actividad 2 · Comandos de movimiento y dibujo en el simulador (CE 4b, 4c)

**Sesión presencial S2 (2 h) + trabajo autónomo TA2 (2 h)** · Cuaderno [sesion23_brazo_robotico_1.ipynb](../sesion23_brazo_robotico_1.ipynb)

## Objetivo

Practicar los **comandos de movimiento** (MoveJ, MoveL, Jump, Arc) y el **dibujo** en el **simulador DobotLab** (Blockly o Python), y validar el script con `BrazoSimulado` (CE 4b), valorando las técnicas de programación (CE 4c).

## Fase 1 · En clase (S2)

1. **Seguridad y home** del brazo (con la **ventosa** montada). No invadir la trayectoria.
2. **Simulador DobotLab:** entra en **Basic scene** y localiza los bloques/comandos de movimiento.
3. Practica los **comandos de movimiento** (MoveJ, MoveL, Jump, Arc) con las velocidades y aceleraciones del **PDF, Práctica 3** (p. ej. v=50 °/s, a=50 °/s², y tramos con tiempos fijos).
4. **Dibujo:** usa la función **«Escribir/Dibujar»** para dibujar una figura dentro de la zona de trabajo.
5. **Rotación:** mientras una pareja prueba en el brazo real, el resto trabaja en el simulador.

## Fase 2 · Trabajo autónomo (TA2)

En `sesion23_brazo_robotico_1.ipynb` (con `BrazoSimulado`):

1. **Comandos de movimiento:** escribe una secuencia tipo *Jump* (subir → desplazarse → bajar) y explica la diferencia entre **MoveJ** (articular) y **MoveL** (lineal).
2. **Dibujo:** define una figura (cuadrado, triángulo, pentágono o iniciales) con `move_to` y dibuja la trayectoria.
3. **Valida rangos:** comprueba que `BrazoSimulado` lanza error con un punto fuera de alcance (p. ej. `X < 150` o radio > 320 mm).

> **Pista:** definid funciones `ir_a(punto)`, `bajar()`, `subir()` y una lista de vértices; el mismo código sirve para cualquier figura.

## Entregable

- `sesion23_brazo_robotico_1.ipynb` **ejecutado**, con la trayectoria dibujada y la diferencia MoveJ/MoveL explicada.
- Envío con asunto `UD04-S2-EQUIPO<N>-movimientos`.

## Criterios de evaluación (rúbrica RA4)

- **4b:** el script funciona, valida rangos y depura errores.
- **4c:** justifica por qué programa en **offline** (simulador/Colab) y qué aporta frente al teach.
