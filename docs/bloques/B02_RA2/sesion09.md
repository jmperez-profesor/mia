---
sesion: "09"
bloque: B02
ra: RA2
fecha_prevista: 2026-12-02
duracion: 120 min
ce: [6]
titulo: "Motores de reglas e inferencia"
---

# Sesión 09 · Motores de reglas e inferencia

## Objetivos de la sesión
- Construir un **motor de inferencia** por encadenamiento hacia delante en Python puro.
- Separar **base de conocimiento** (hechos + reglas) del **motor** (ciclo reconocer-actuar).
- Aplicar el motor a un sistema experto de diagnóstico.

## Contenidos
- Regla de producción: `SI <condiciones> ENTONCES <conclusión>`.
- Ciclo reconocer-actuar: detectar reglas activas, resolver conflictos, disparar.
- Cierre de conjunto de hechos (forward chaining) hasta punto fijo.
- Explicabilidad: traza de reglas disparadas.

## Temporalización (120 min)
- **Apertura / activación (10 min):** "¿por qué una impresora 3D no extrude?"; se listan síntomas y se deduce la causa con reglas.
- **Desarrollo (80 min):** diseño del motor `encadenar`; codificación de la base de conocimiento del dominio; ejecución y traza de reglas disparadas.
- **Cierre y evaluación (30 min):** discusión sobre resolución de conflictos y explicabilidad; entrega del miniproyecto; rúbrica.

## Práctica guiada (con solución)
Motor genérico de encadenamiento hacia delante y base de diagnóstico de una impresora 3D.

```python
hechos = {"sin_calientar", "filamento_presente", "ruido_extrusion"}

reglas = [
    (frozenset({"sin_calientar", "filamento_presente"}), "baja_temperatura_hotend"),
    (frozenset({"ruido_extrusion", "filamento_presente"}), "engranaje_obstruido"),
    (frozenset({"baja_temperatura_hotend"}), "revisar_termostato"),
    (frozenset({"engranaje_obstruido"}), "limpiar_extrusor"),
    (frozenset({"revisar_termostato"}), "fallo_hardware"),
    (frozenset({"sin_calientar", "ruido_extrusion"}), "fallo_filamento"),
]

def encadenar(hechos, reglas):
    hechos = set(hechos)
    disparadas = []
    cambio = True
    while cambio:
        cambio = False
        for cond, conc in reglas:
            if cond <= hechos and conc not in hechos:
                hechos.add(conc); disparadas.append((cond, conc)); cambio = True
    return hechos, disparadas

nuevos, traza = encadenar(hechos, reglas)
print("Hechos deducidos:", sorted(nuevos))
print("Reglas disparadas:")
for cond, conc in traza:
    print("  ", set(cond), "=>", conc)
# El motor deduce baja_temperatura_hotend -> revisar_termostato -> fallo_hardware, etc.
```

## Práctica propuesta (miniproyecto)
**Miniproyecto:** implementa un motor de reglas por forward chaining y aplícalo a un sistema experto de diagnóstico (≥ 6 reglas); entrega la traza de inferencia.  
**Entregables:** `encadenar`, base de conocimiento del dominio y diagnóstico final con traza.  
**Criterios de evaluación:** separación base de conocimiento/motor e implementación del ciclo reconocer-actuar.  
**Notebook:** [Abrir/Descargar miniproyecto](sesion09_miniproyecto.ipynb)

## Evaluación (criterios CE)
- CE6: implementa un motor de inferencia y explica el ciclo reconocer-actuar y la resolución de conflictos.

## Atención a la diversidad
- Refuerzo: 4 reglas y 3 hechos iniciales en dominio de "riego automático".
- Ampliación: añadir prioridad a las reglas para desempatar conflictos.

## Observaciones
- El mismo esquema sirve para sistemas expertos clásicos (`experta`, `CLIPS`); aquí se implementa a mano para entender el ciclo.
