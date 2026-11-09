# RA4 - Análisis de sistemas robotizados

Unidad **UD04** de **12 h**: **2 sesiones presenciales (2 h + 4 h) + 3 sesiones autónomas de 2 h**. Hardware del aula: **un brazo DOBOT Magician** (4 ejes) con cinta transportadora (fotocélula y sensor de color). El grupo (~16-20 alumnos) se organiza en **4 equipos** que trabajan por turnos en el brazo.

- [Apuntes (teoría, sesión 1)](apuntes.md)
- [Actividades](actividades/actividad_brazo_robotico.md)
- [Cuaderno de cinemática (Colab)](sesion19_sistemas_robotizados.ipynb)
- [Cuaderno práctico (Colab)](S23_24_brazo_robotico.ipynb)
- [Rúbrica del RA4](rubrica.md)
- [Guía docente](guia_docente.md)

## Planificación

| Sesión | Tipo | Contenido | CE |
|---|---|---|---|
| **S1** | Presencial 2 h | Teoría de sistemas robotizados: tipos, anatomía, cinemática (FK/IK), actuadores/sensores/efectores, la célula, técnicas de programación | 4a, 4c, 4d |
| **TA1** | Autónoma 2 h | Estudiar apuntes + **ficha de cinemática** (a mano y con NumPy en Colab) | 4a, 4b |
| **S23-24** | Presencial 4 h | Práctica: **simulador DobotLab** (comandos de movimiento + dibujo) y **pick & place con ventosa** + cinta y paletización | 4b, 4c, 4d |
| **TA** | Autónoma 4 h | Completar el **cuaderno** (dos fases) + **memoria** del equipo (decisiones, errores, soluciones) | 4b, 4c, 4d |

## Cómo se trabaja (resumen)

- **Un solo brazo** (con la **ventosa** montada) → una pareja prueba en el brazo real mientras el resto trabaja en el **simulador DobotLab** (Blockly/Python) o en Colab.
- **Dos simuladores**: el **DobotLab** (visual, en el navegador) y la clase **`BrazoSimulado`** en Colab (rangos + trayectoria). Ambos validan el script **sin hardware**.
- **El fallo es parte del método**: se depura en directo y se itera.

> Fuente de los ejemplos: manuales y programas del kit DOBOT Magician (INDALevante) + especificaciones oficiales del fabricante.
