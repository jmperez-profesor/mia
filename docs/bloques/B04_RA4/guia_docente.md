# Guía docente · UD04 · RA4 (DOBOT Magician)

**Módulo:** 5071 «Modelos de Inteligencia Artificial» · **Curso de Especialización IA y Big Data**
**Centro:** I.E.S. Severo Ochoa (Elche) · **Curso:** 2026-2027 · **Convocatoria:** ordinaria
**Alumnado:** ~16-20 personas (grupo adulto con base de Python)
**RA4:** *Analiza sistemas robotizados, evaluando opciones de diseño e implementación.*

## 1. Temporalización

| Sesión | Tipo | Minutos | Contenido | Evidencia |
|---|---|---|---|---|
| **S1** | Presencial | 2 h | Teoría: tipos, anatomía, FK/IK, efectores, célula, técnicas de programación | Apuntes + preguntas |
| **TA1** | Autónoma | 2 h | Ficha de cinemática (a mano + Colab) | `act1` + notebook |
| **S23-24** | Presencial | 4 h | Práctica: simulador DobotLab (movimientos + dibujo) y pick & place **con ventosa** + cinta y paletización | Guiado + script |
| **TA** | Autónoma | 4 h | Completar el cuaderno (dos fases) + memoria del equipo | Cuaderno + memoria |

**S1 (minuto a minuto):** 0-20 qué es un robot (ISO 8373) y tipos; 20-50 anatomía y GDL; 50-80 cinemática FK/IK con el ejemplo 2D a mano; 80-100 efectores y célula; 100-120 técnicas de programación y cierre.

**S23-24 (4 h, minuto a minuto):** 0-20 presentación del DOBOT, **seguridad** y la **ventosa**; 20-60 **simulador DobotLab** (coordenadas cartesianas y comandos MoveJ/MoveL/Jump/Arc, en Blockly y Python) + **dibujo** con «Escribir/Dibujar»; 60-90 repaso de la secuencia de *pick & place* (pre-pick, pick, pre-place, place) y misión con la **cinta**; 90-225 práctica por turnos (una pareja en el brazo real con ventosa, el resto en el simulador/Colab); 225-240 puesta en común «¿qué cambiaríais?» y paletización como extensión.

## 2. Material necesario

- **DOBOT Magician** + portátil de taller con drivers y DobotStudio.
- **Ventosa** + **bomba de aire** (único efector que se monta en el brazo real; el portaminas y la pinza se usan en el simulador).
- **Cinta transportadora** con **fotocélula** y **sensor de color** + cubos de colores.
- Acceso a **DobotLab** (simulador web, Blockly/Python) para la sesión 2.
- Objetos para pick & place con ventosa (piezas **lisas y no porosas**, < 500 g).
- **Papel milimetrado** y regla para medir el espacio de trabajo.

## 3. Agrupamiento y roles

- **4 equipos** de 4-5 personas (o 3 si el grupo es menor).
- **Roles rotatorios** en cada tarea: **piloto** (escribe el código), **copiloto** (revisa), **verificador** (comprueba rangos con `BrazoSimulado`), **portavoz** (defiende el diseño). Todos deben pasar por el brazo al menos una vez.
- **Turnos de brazo:** 10-15 min por equipo. Mientras un equipo ejecuta, los demás escriben/validan en Colab.

## 4. Protocolo de entrega de scripts

1. El equipo valida el script en Colab (`BrazoSimulado`, sin errores de rango).
2. Lo envía con **asunto normalizado:** `UD04-BRAZO-EQUIPO3`.
3. Adjunta el `.ipynb` **con las celdas ejecutadas** y, si procede, la memoria en PDF.
4. El docente lo carga en el portátil del brazo y lo ejecuta. Si falla, se analiza y se itera.

## 5. Rotación y seguridad

- Antes de ejecutar: **home** del robot y comprobar que nadie tiene la mano en la trayectoria.
- Velocidad y aceleración reducidas en los primeros ensayos.
- Un solo equipo frente al brazo; el resto a distancia.
- No forzar los ejes a mano salvo en modo **teach** (guiado) con el robot habilitado.

## 6. Plan B sin internet

- Los cuadernos Colab se entregan también como `.ipynb` en un **pen drive** para ejecutarlos en local (Jupyter).
- Los apuntes y las plantillas están en la web del módulo (descargables).
- Si falla el portátil del brazo, se hacen las sesiones 2-3 en **modo teach** y se corrigen los scripts en mesa.

## 7. Checklist de hardware (antes de cada sesión)

- [ ] DOBOT conectado por USB y reconocido (puerto `COMx`/`/dev/ttyUSB0`).
- [ ] Alimentación 12 V y compresor de aire encendido.
- [ ] Ventosa montada y bomba de aire encendida.
- [ ] Espacio de trabajo libre y mesa sujeta.
- [ ] Cinta conectada y fotocélula probada.
- [ ] Scripts de los equipos recibidos y revisados.

## 8. Evaluación

- **40 % actividades** (act1 + actividad práctica con memoria), con la [rúbrica](rubrica.md).
- **60 % prueba escrita** del RA4.
- La normativa exige **todos los RA** y **≥5 en cada RA** (Orden 8/2025, art. 5.1).
