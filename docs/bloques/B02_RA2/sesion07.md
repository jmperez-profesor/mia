---
sesion: "07"
bloque: B02
ra: RA2
fecha_prevista: 2026-11-25
duracion: 120 min
ce: [6]
titulo: "Planificación: STRIPS"
---

# Sesión 07 · Planificación: STRIPS

## Objetivos de la sesión
- Representar un problema de planificación con la librería **STRIPS**: estados, acciones con precondiciones y efectos.
- Implementar un **planificador hacia delante** (forward search) sobre el espacio de estados.
- Verificar que el plan alcanza el estado objetivo.

## Contenidos
- Estado = conjunto de literales (átomos); acción = `(precondiciones, añadir, eliminar)`.
- Diferencia entre estado y plan; plan = secuencia de acciones aplicables.
- Búsqueda en el espacio de estados (BFS) con memoización de estados visitados.
- Mundo de los bloques como dominio canónico.

## Temporalización (120 min)
- **Apertura / activación (10 min):** "torre de bloques": ¿cómo pasar de una configuración a otra?"; se introducen precondiciones y efectos.
- **Desarrollo (80 min):** codificación de `acciones` (mover bloque), `aplicable`, `aplicar` y `planificar` por BFS; ejecución y traza del plan.
- **Cierre y evaluación (30 min):** verificación del estado final; entrega del miniproyecto; rúbrica.

## Práctica guiada (con solución)
En el mundo de los bloques, mover `X` de `Y` a `W` requiere que `X` y `W` estén libres y que `X` repose sobre `Y`.

```python
estado_inicial = {"on(A,table)", "on(B,A)", "on(C,table)", "clear(A)", "clear(C)", "clear(B)"}
estado_objetivo = {"on(A,B)", "on(B,C)", "on(C,table)", "clear(A)"}
bloques = ["A", "B", "C"]

def acciones(estado):
    out = []
    libres = {b for b in bloques if f"clear({b})" in estado}
    for X in bloques:
        for Y in bloques + ["table"]:
            if f"on({X},{Y})" in estado:
                for W in bloques + ["table"]:
                    if W != Y and f"clear({W})" in estado:
                        pre = {f"on({X},{Y})", f"clear({X})", f"clear({W})"}
                        add = {f"on({X},{W})", f"clear({Y})"}
                        dele = {f"on({X},{Y})"}
                        if W == "table":
                            dele |= {f"clear({Y})"}
                        else:
                            dele |= set()
                        out.append((f"mover({X},{Y},{W})", pre, add, dele))
    return out

def aplicable(pre, estado):
    return pre <= estado

def aplicar(add_s, dele_s, estado):
    return frozenset((estado - dele_s) | add_s)

def planificar(ini, obj):
    ini = frozenset(ini)
    obj = set(obj)
    from collections import deque
    q = deque([(ini, [])]); vistos = {ini}
    while q:
        s, plan = q.popleft()
        if obj <= s:
            return plan
        for nombre, pre, add_s, dele_s in acciones(s):
            if aplicable(pre, s):
                ns = aplicar(add_s, dele_s, s)
                if ns not in vistos:
                    vistos.add(ns); q.append((ns, plan + [nombre]))
    return None

plan = planificar(estado_inicial, estado_objetivo)
print("Plan:", plan)
# El planificador encuentra la secuencia de movimientos que transforma el estado inicial en el objetivo.
```

## Práctica propuesta (miniproyecto)
**Miniproyecto:** implementa un planificador STRIPS para el mundo de los bloques y resuelve un objetivo dado.  
**Entregables:** definición de acciones con precondiciones/efectos, `planificar` y traza del plan.  
**Criterios de evaluación:** modelado STRIPS correcto y planificador hacia delante terminante.  
**Notebook:** [Abrir/Descargar miniproyecto](sesion07_miniproyecto.ipynb)

## Evaluación (criterios CE)
- CE6: modela acciones simbólicas y aplica un planificador hacia delante para resolver el problema.

## Atención a la diversidad
- Refuerzo: 2 bloques y objetivo de una sola torre.
- Ampliación: añadir la acción `mover_a_mesa` y objetivos con 4 bloques.

## Observaciones
- La memoización de estados visitados es clave para evitar ciclos en el espacio de estados.
