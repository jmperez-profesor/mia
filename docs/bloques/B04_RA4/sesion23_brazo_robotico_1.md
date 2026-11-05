---
sesion: "23"
bloque: B04
ra: RA4
fecha: 2026-11-11
duracion: 2 h
titulo: "Brazo robótico 1"
---

# Sesión 23 · Brazo robótico 1 (11/11/2026)

> **RA4.** Primera sesión práctica: movimientos y dibujo en el **simulador DobotLab** (Blockly y Python) y primeros pasos con la **ventosa** en el brazo real. Trabajo por parejas: un grupo prueba en el brazo y el resto avanza en el simulador.

> **Hardware del aula.** En las dos sesiones prácticas (4 h) el brazo lleva montada **solo la ventosa**: montar y desmontar herramientas cuesta, así que la pinza y el portaminas se trabajan en el simulador.

## Cuaderno de la sesión

El código se trabaja en el cuaderno **`S23_24_brazo_robotico.ipynb`**:

[Abrir en Colab](https://colab.research.google.com/github/jmperez-profesor/mia/blob/main/docs/bloques/B04_RA4/S23_24_brazo_robotico.ipynb){ .md-button } · [ver en el sitio](S23_24_brazo_robotico.ipynb)

## Qué vas a aprender

| # | Al terminar la sesión serás capaz de… |
|---|---|
| 1 | Usar el **simulador DobotLab** (Basic scene) con **Blockly** y **Python** |
| 2 | Programar los **comandos de movimiento** (MoveJ, MoveL, Jump, Arc) |
| 3 | Dibujar con la función **«Escribir/Dibujar»** del simulador |
| 4 | Aplicar el **protocolo de seguridad** y manejar la **ventosa** del brazo real |

## 8. El DOBOT Magician y su API

| Especificación | Valor |
|---|---|
| Ejes | **4** (base, brazo trasero, antebrazo, muñeca) |
| Carga útil | **500 g** |
| Alcance | **320 mm** |
| Repetibilidad | **±0,2 mm** |
| Comunicación | USB / Wi-Fi / Bluetooth |
| Alimentación | 12 V CC |
| Accesorio | Cinta transportadora con fotocélula y sensor de color |

> **Ver el DOBOT en 3D.** [RoboDK for Web](https://robodk.com/3D/es/robot/Dobot-Magician) muestra el modelo 3D del DOBOT en el navegador para inspeccionar sus 4 ejes antes de programarlo.

![Material necesario para montar el DOBOT](assets/dobot_basic_setup.jpg)

*Montaje básico del DOBOT Magician. Fuente: UAL Creative Computing Institute.*

**Dos formas de programarlo:**

1. **DobotLab** (interfaz web): teach, **Blockly** y editor de script (Python).
2. **Python** con la API oficial (`dType`) o las librerías **`pydobot`** (Luis Mesas) y **`dobot-python`** (Alex Gustafsson, protocolo v1.1.5).

![Panel de control de DobotLab](assets/dobotlab_control_panel.jpg)

*Panel de control de **DobotLab** (interfaz web). Fuente: UAL Creative Computing Institute.*

> **Simulador DobotLab.** [DobotLab](https://dobotlab.dobot.cc/#/) incluye un **simulador integrado**: entra en **«Basic scene»** para probar movimientos y programas **sin conectar el robot real**. Tiene **Blockly** y **Python**, así que los ejercicios de esta sesión (coordenadas, MoveJ/MoveL/Jump y dibujo) se hacen ahí. Es la herramienta para practicar **mientras un grupo ocupa el brazo real**.

> **Definición · Comandos inmediatos vs. encolados.** La API permite ejecutar una orden **ya** (inmediata) o **encolarla** en una cola FIFO (`isQueued=1`). Encolar es lo que permite **construir una secuencia de movimiento** sin esperar: el robot la ejecuta en orden. Es la diferencia entre **teleoperar** (orden a orden) y **programar** (una secuencia completa). Para sincronizar, se puede consultar la pose con `GetPose` hasta que el robot llegue al punto.

```python
# API oficial (dType) — movimiento cartesiano lineal a un punto
dType.SetPTPCoordinateParams(api, 150, 500, 150, 500, isQueued=0)  # vel, ac
dType.SetPTPCmd(api, 2, x, y, z, r, isQueued=1)                    # modo 2 = lineal
dType.SetWAITCmd(api, 500, isQueued=1)                             # esperar 0,5 s
```

```python
# pydobot — misma idea, API de alto nivel
from pydobot import Dobot
robot = Dobot(port="/dev/ttyUSB0")
robot.move_to(250, 0, 50, 0)     # x, y, z, r
robot.suck(True)                  # ventosa: aspirar (soltar: suck(False))
robot.wait(500)
robot.home()
robot.close()
```

> **Más información.** En el cuaderno Colab usamos una clase **`BrazoSimulado`** que imita esta API: registra las órdenes, **valida rangos** (X entre 150 y 320 mm, radio ≤ 320 mm, Z dentro de límites) y **dibuja la trayectoria XY** con matplotlib. Es el equivalente en Python al simulador DobotLab: sirve para **verificar el script antes de enviarlo al robot real**.

## 9. Trabajo por parejas (rotación robot ↔ simulador)

Con **un solo brazo** y la **ventosa** montada, el grupo se organiza así:

- **Una pareja en el brazo** (turnos de ~10–15 min): prueba la secuencia de **pick & place con ventosa** y aplica el protocolo de seguridad.
- **El resto en el simulador DobotLab** (o en Colab con `BrazoSimulado`): practica los comandos de movimiento y el dibujo.
- Se **rota** para que todas las parejas pasen por el brazo real.

## 10. Buenas prácticas y seguridad en el aula

Trabajar con un robot real exige un protocolo. No es burocracia: es lo que evita dañar el brazo, la pieza o a un compañero.

- **Antes de ejecutar:** hacer **home**, comprobar que la trayectoria está libre y que **nadie tiene la mano** en el espacio de trabajo.
- **Velocidad reducida** en los primeros ensayos; subirla solo cuando el movimiento es correcto.
- **Sujetar** la mesa y la pieza; una pieza que se mueve arruina la repetibilidad.
- **No forzar los ejes a mano** salvo en modo **teach** con el robot habilitado.
- **Validar siempre** en Colab (`BrazoSimulado`) o en el simulador DobotLab **antes** de cargar el script: el 90 % de los errores (parámetros, rangos, fuera de alcance) se detectan sin tocar el robot.
- **Un solo equipo frente al brazo**; el resto trabaja a distancia. Turnos de 10–15 minutos.
- **Protocolo de entrega:** asunto normalizado (`UD04-S2-EQUIPO3-movimientos`), `.ipynb` con celdas ejecutadas.

> **Puesta en marcha (LED del DOBOT).** Al encender, el **LED** pasa a **amarillo** y, tras un pitido (~7 s), a **verde** (listo). Si se queda **rojo/ámbar**, el brazo ha tocado un **límite de eje**: mantén pulsado el botón de **desbloqueo** (candado abierto, en el antebrazo) y llévalo a una posición segura.

![Conexión del DOBOT: USB y alimentación](assets/connecting_dobot_magician.jpg)

*Conexión del DOBOT Magician: cable **USB** al ordenador y **adaptador de alimentación**. Fuente: UAL Creative Computing Institute.*

> **Más información.** Este protocolo conecta con la idea de **sistema robotizado** del §6: la seguridad no es una propiedad del brazo, sino del **conjunto** robot + herramienta + entorno + tarea. Es el mismo principio que recoge la ISO 10218:2025 para las aplicaciones colaborativas.

## Actividad 2 · Comandos de movimiento y dibujo (simulador)

Practica los **comandos de movimiento** (MoveJ, MoveL, Jump, Arc) y el **dibujo** con la función «Escribir/Dibujar» del simulador DobotLab (en Blockly o Python), y valida el script con `BrazoSimulado`. Cuaderno [S23_24_brazo_robotico.ipynb](S23_24_brazo_robotico.ipynb). Detalle en [actividades/act2_reto_dibujo.md](actividades/act2_reto_dibujo.md).

## Puntos clave

- El DOBOT tiene **4 ejes**, 500 g de carga, 320 mm de alcance y ±0,2 mm de repetibilidad; en el aula solo se monta la **ventosa**.
- **Encolar** (`isQueued=1`) construye una secuencia FIFO; es la base de **programar** frente a **teleoperar**.
- El **simulador DobotLab** (Blockly/Python) y `BrazoSimulado` permiten **practicar sin el brazo real** mientras un grupo lo ocupa.
- Antes de ejecutar: **home**, trayectoria libre, velocidad reducida y **validar** sin hardware.
