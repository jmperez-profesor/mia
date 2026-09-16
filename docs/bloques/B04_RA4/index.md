# B04 · RA4 — Análisis de sistemas robotizados

Unidad de **12 horas**: **3 sesiones presenciales de 2 h** + **3 sesiones de trabajo autónomo de 2 h**. Reescrita a partir de la UD04 de David Martínez Peña (CC BY-NC-SA 4.0) y actualizada al **mercado actual** (cobots, AMR, ROS 2, sim-to-real, ISO 10218:2025), con cuadernos de **Google Colab** en Python.

- [Apuntes (3 sesiones + autónomo)](apuntes.md)
- [Ejercicios guiados y propuestos](ejercicios.md)

Hilo conductor único: **Célula-07**, una célula robotizada de *pick-and-place* en un almacén (brazo manipulador + robot móvil AMR).

| Bloque | Horas | Contenido |
|---|---|---|
| **S1 presencial** | 2 h | El robot y su cinemática: tipos, sensores/actuadores, grados de libertad, FK/IK, jacobiano, singularidades, control |
| **Autónomo 1** | 2 h | Actividad A1: cinemática de un manipulador (DH, FK/IK, singularidades) |
| **S2 presencial** | 2 h | Planificación y percepción: espacio de configuración, RRT/PRM, SLAM, filtro de partículas, sim-to-real |
| **Autónomo 2** | 2 h | Actividad A2: planificador de movimiento + navegación AITK |
| **S3 presencial** | 2 h | Programación, humanos y diseño: técnicas de programación, cobots, ISO 10218, selección y célula |
| **Autónomo 3** | 2 h | Actividad A3: proyecto de célula robotizada (selección + seguridad + memoria) |

> Fuente base: `material_david/docs/UD04/UD04_ES.md` y https://martinezpenya.es/ModelosIA/UD04/UD04_ES.html. Los cuadernos usan `numpy`, `scipy`, `roboticstoolbox-python` y `aitk`.
