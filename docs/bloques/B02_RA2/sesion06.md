---
sesion: "06"
bloque: B02
ra: RA2
fecha_prevista: 2026-11-23
duracion: 120 min
ce: [6]
titulo: "Satisfacción de restricciones (CSP)"
---

# Sesión 06 · Satisfacción de restricciones (CSP)

## Objetivos de la sesión
- Modelar un problema real como **CSP**: variables, dominios y restricciones.
- Implementar **backtracking** con heurística **MRV** (mínimo dominio restante).
- Medir el ahorro de nodos frente a un backtracking ingenuo.

## Contenidos
- Triplete (X, D, C): variables, dominios y restricciones.
- Backtracking con consistencia parcial; poda al detectar incompatibilidad.
- Heurísticas de ordenación: MRV y, opcionalmente, grado.
- Aplicación: horario / asignación con conflictos de profesorado.

## Temporalización (120 min)
- **Apertura / activación (10 min):** ejemplo cotidiano (sentarse 5 amigos en fila sin que dos enemigos coincidan); se abstrae a variables/dominios/restricciones.
- **Desarrollo (80 min):** formulación del horario; codificación de `consistente`, `seleccion_mrv` y `backtracking`; conteo de nodos y dibujo del horario.
- **Cierre y evaluación (30 min):** debate sobre el impacto de MRV; entrega del miniproyecto; rúbrica.

## Práctica guiada (con solución)
Modelamos 5 asignaturas en 4 franjas, con pares incompatibles (mismo profesor).

```python
asignaturas = ["IA", "BD", "PROG", "SO", "RED"]
franjas = [1, 2, 3, 4]
incompatibles = [("IA", "BD"), ("PROG", "SO"), ("BD", "RED")]

def consistente(asig, franja, asignacion):
    for a2, f2 in asignacion.items():
        if (a2, asig) in incompatibles or (asig, a2) in incompatibles:
            if f2 == franja:
                return False
    return True

def seleccion_mrv(asignacion):
    sin_asignar = [a for a in asignaturas if a not in asignacion]
    return min(sin_asignar, key=lambda a: sum(
        1 for f in franjas if consistente(a, f, asignacion)))

def backtracking(asignacion=None, nodos=None):
    asignacion = asignacion or {}
    nodos = nodos if nodos is not None else [0]
    nodos[0] += 1
    if len(asignacion) == len(asignaturas):
        return asignacion
    var = seleccion_mrv(asignacion)
    for f in franjas:
        if consistente(var, f, asignacion):
            asignacion[var] = f
            res = backtracking(dict(asignacion), nodos)
            if res:
                return res
            del asignacion[var]
    return None

sol = backtracking()
print("Horario (asignatura -> franja):", sol)
# MRV elige primero la asignatura más restringida, reduciendo la explosión combinatoria.
```

## Práctica propuesta (miniproyecto)
**Miniproyecto:** resuelve un horario de 5 asignaturas en 4 franjas con restricciones de profesorado usando backtracking + MRV.  
**Entregables:** representación CSP, `backtracking` con MRV y tabla del horario resultante.  
**Criterios de evaluación:** modelado correcto como CSP y aplicación de retroceso con poda.  
**Notebook:** [Abrir/Descargar miniproyecto](sesion06_miniproyecto.ipynb)

## Evaluación (criterios CE)
- CE6: modela un problema real como CSP y aplica retroceso con heurística de ordenación.

## Atención a la diversidad
- Refuerzo: 4 asignaturas, 4 franjas, una sola incompatibilidad.
- Ampliación: añadir restricción de aula (dos asignaturas no comparten aula en la misma franja).

## Observaciones
- MRV es una heurística de orden de variables; combinada con detección temprana de inconsistencia recorta drásticamente el árbol.
