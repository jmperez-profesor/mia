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
| **S2** | Presencial | 2 h | Brazo I: teach, medir espacio de trabajo, reto de dibujo | Guiado + script |
| **TA2** | Autónoma | 2 h | Script del reto de dibujo validado | `act2` + notebook |
| **S3** | Presencial | 2 h | Brazo II: pinza/ventosa + pick & place con cinta | `act3` + script |
| **TA3** | Autónoma | 2 h | Script pick & place + memoria del equipo | Memoria |

**S1 (minuto a minuto):** 0-20 qué es un robot (ISO 8373) y tipos; 20-50 anatomía y GDL; 50-80 cinemática FK/IK con el ejemplo 2D a mano; 80-100 efectores y célula; 100-120 técnicas de programación y cierre.

**S2:** 0-15 presentación del DOBOT y **seguridad**; 15-40 **teach** + medir el espacio de trabajo (papel milimetrado y portaminas); 40-55 el docente ejecuta el script de ejemplo (escribe un nombre); 55-70 entrega de retos a los equipos y análisis «¿cómo lo haríais?»; 70-115 escritura y **ejecución por turnos**; 115-120 cierre y depuración.

**S3:** 0-15 cambio a pinza y prueba de succión; 15-30 repaso de la secuencia de pick & place (pre-pick, pick, pre-place, place); 30-45 misión con la cinta; 45-105 ejecución por turnos y comparación de enfoques; 105-120 puesta en común «¿qué cambiaríais?».

## 2. Material necesario

- **DOBOT Magician** + portátil de taller con drivers y DobotStudio.
- **Portaminas/rotulador** (Ø 10 mm) y **tablas de madera** o cartón.
- **Pinza neumática** y **ventosa** + **bomba de aire**.
- **Cinta transportadora** con **fotocélula** y **sensor de color** + cubos de colores.
- **Papel milimetrado**, regla y rotuladores para medir el espacio de trabajo.
- Objetos para pick & place (cubos ligeros, tapones, piezas < 500 g).

## 3. Agrupamiento y roles

- **4 equipos** de 4-5 personas (o 3 si el grupo es menor).
- **Roles rotatorios** en cada tarea: **piloto** (escribe el código), **copiloto** (revisa), **verificador** (comprueba rangos con `BrazoSimulado`), **portavoz** (defiende el diseño). Todos deben pasar por el brazo al menos una vez.
- **Turnos de brazo:** 10-15 min por equipo. Mientras un equipo ejecuta, los demás escriben/validan en Colab.

## 4. Protocolo de entrega de scripts

1. El equipo valida el script en Colab (`BrazoSimulado`, sin errores de rango).
2. Lo envía con **asunto normalizado:** `UD04-S2-EQUIPO3-reto_dibujo` (y `UD04-S3-EQUIPO3-pick_place`).
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
- [ ] Efector correcto montado (portaminas / pinza / ventosa).
- [ ] Espacio de trabajo libre y mesa sujeta.
- [ ] Cinta conectada y fotocélula probada.
- [ ] Scripts de los equipos recibidos y revisados.

## 8. Evaluación

- **40 % actividades** (act1, act2, act3 + memoria), con la [rúbrica](rubrica.md).
- **60 % prueba escrita** del RA4.
- La normativa exige **todos los RA** y **≥5 en cada RA** (Orden 8/2025, art. 5.1).
