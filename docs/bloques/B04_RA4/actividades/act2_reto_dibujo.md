# Actividad 2 · Reto de dibujo (CE 4b, 4c)

**Sesión presencial S2 (2 h) + trabajo autónomo TA2 (2 h)** · Cuaderno [UD04_reto_dibujo_plantilla.ipynb](../colab/UD04_reto_dibujo_plantilla.ipynb)

## Objetivo

Pasar del **guiado (teach)** al **código**: escribir un script que haga al DOBOT dibujar una figura con el **portaminas**, validarlo sin hardware y ejecutarlo en el brazo (CE 4b), valorando las técnicas de programación (CE 4c).

## Fase 1 · En clase (S2)

1. **Seguridad y home** del brazo. No invadir la trayectoria.
2. **Modo teach:** mover el brazo, leer coordenadas de puntos y **medir el espacio de trabajo** con papel milimetrado y el portaminas.
3. El docente ejecuta un **script de ejemplo** que escribe un nombre.
4. Cada equipo recibe un **reto distinto**: cuadrado, triángulo, pentágono o las iniciales del equipo.

## Fase 2 · Trabajo autónomo (TA2)

En `UD04_reto_dibujo_plantilla.ipynb`, completad:

1. Una función **`dibujar(figura)`** que recorra los puntos de la figura con `move_to` y baje/suba el lápiz (Z).
2. **Validación con `BrazoSimulado`:** debe comprobar que **X está entre 150 y 320 mm**, que el radio no supera 320 mm, que Z está dentro de límites y que el número de parámetros es correcto.
3. **Gráfica matplotlib** de la trayectoria XY: verificad que el dibujo es la figura pedida **antes** de enviarlo.

> **Pista de estructura:** definid funciones `ir_a(punto)`, `bajar_lapiz()`, `subir_lapiz()` y una lista de vértices por figura; el reto es que el mismo código sirva para todas.

## Entregable

- `UD04_reto_dibujo_plantilla.ipynb` **ejecutado**, con la trayectoria dibujada y el script listo para cargar en el robot.
- Envío con asunto `UD04-S2-EQUIPO<N>-reto_dibujo`.

## Criterios de evaluación (rúbrica RA4)

- **4b:** el script funciona, valida rangos y depura errores.
- **4c:** justifica por qué programa en modo **offline** y qué aporta frente al teach.
