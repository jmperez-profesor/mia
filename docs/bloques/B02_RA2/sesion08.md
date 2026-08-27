---
sesion: "08"
bloque: B02
ra: RA2
fecha_prevista: 2026-11-30
duracion: 120 min
ce: [6]
titulo: "Programación lógica con Prolog"
---

# Sesión 08 · Programación lógica con Prolog

## Objetivos de la sesión
- Escribir **hechos** y **reglas** en lógica de primer orden con Prolog.
- Entender la **unificación** y el **backtracking** como motor de inferencia.
- Plantear consultas y leer las respuestas (incluido el conjunto de soluciones).

## Contenidos
- Hechos `padre/2`, `madre/2`; reglas con el cuerpo separado por `:-`.
- Reglas recursivas (`ancestro`); variables en mayúscula; unificación.
- Resolución SLD por backtracking; múltiples respuestas con `;`.
- `pyswip` como puente Python↔SWI-Prolog.

## Temporalización (120 min)
- **Apertura / activación (10 min):** "¿Quién es el abuelo de quién?" a partir de una lista de padres; se motiva la regla `abuelo`.
- **Desarrollo (80 min):** sintaxis Prolog (hechos, reglas, consultas); demostración con `pyswip` en vivo; codificación de la base genealógica y 5 consultas.
- **Cierre y evaluación (30 min):** puesta en común de consultas; entrega del miniproyecto; rúbrica.

## Práctica guiada (con solución)
Programa Prolog (hechos + reglas) y su ejecución con `pyswip`:

```prolog
% Hechos
padre(juan, maria).
padre(juan, pedro).
padre(carlos, juan).
madre(lucia, maria).
madre(lucia, pedro).
madre(ana, juan).

% Reglas
abuelo(X, Y) :- padre(X, Z), padre(Z, Y).
abuela(X, Y) :- madre(X, Z), padre(Z, Y).
hermano(X, Y) :- padre(P, X), padre(P, Y), madre(M, X), madre(M, Y), X \= Y.
ancestro(X, Y) :- padre(X, Y).
ancestro(X, Y) :- padre(X, Z), ancestro(Z, Y).
```

```python
# Equivalente ejecutable con pyswip (requiere swipl instalado)
from pyswip import Prolog
prolog = Prolog()
for he in ["padre(juan, maria)", "padre(juan, pedro)", "padre(carlos, juan)",
           "madre(lucia, maria)", "madre(lucia, pedro)", "madre(ana, juan)"]:
    prolog.assertz(he)
prolog.assertz("abuelo(X,Y) :- padre(X,Z), padre(Z,Y)")
prolog.assertz("hermano(X,Y) :- padre(P,X), padre(P,Y), madre(M,X), madre(M,Y), X\\=Y")
prolog.assertz("ancestro(X,Y) :- padre(X,Y)")
prolog.assertz("ancestro(X,Y) :- padre(X,Z), ancestro(Z,Y)")

print("Abuelos de Maria:", list(prolog.query("abuelo(X, maria)")))
print("Hermanos de Maria:", list(prolog.query("hermano(X, maria)")))
print("Ancestros de pedro:", list(prolog.query("ancestro(X, pedro)")))
# Salida: carlos es abuelo de maria/pedro; maria y pedro son hermanos; juan y carlos son ancestros de pedro.
```

## Práctica propuesta (miniproyecto)
**Miniproyecto:** construye una base de conocimiento genealógica en Prolog (hechos + reglas: abuelo, hermano, ancestro) y resuelve al menos 5 consultas.  
**Entregables:** programa Prolog, consultas resueltas (con `pyswip` o razonadas a mano) y explicación de la unificación.  
**Criterios de evaluación:** representación lógica correcta y obtención de respuestas por inferencia.  
**Notebook:** [Abrir/Descargar miniproyecto](sesion08_miniproyecto.ipynb)

## Evaluación (criterios CE)
- CE6: representa conocimiento como hechos y reglas y deduce respuestas por inferencia automática.

## Atención a la diversidad
- Refuerzo: base de 4 personas y solo `abuelo`/`hermano`.
- Ampliación: añadir `tio`, `primo` y consultas con变量 en ambas posiciones.

## Observaciones
- Prolog resuelve por backtracking: una consulta con varias soluciones las devuelve una a una (en el intérprete, pulsando `;`).
