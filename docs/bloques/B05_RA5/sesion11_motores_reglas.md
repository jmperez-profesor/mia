---
sesion: "11"
bloque: B05
ra: RA5
fecha: 2026-10-21
duracion: 2 h
titulo: "Motores de reglas"
---

# Sesión 11 · Motores de reglas (21/10/2026)

> **Bloque B05 · RA5.** Segunda sesión. Del sistema experto «clásico» al **motor de reglas de negocio**: cómo se gestionan, versionan y despliegan las reglas como un activo de empresa.
>
> **CE de esta sesión:** RA5-b (representar y simular comportamientos básicos de ámbitos diversos).

## Qué vas a aprender

| # | Al terminar la sesión serás capaz de… |
|---|---|
| 1 | Explicar qué es el **decision management** y por qué un **BRMS** trata las reglas como activo |
| 2 | Leer y escribir **tablas de decisión** con su **hit policy** |
| 3 | Expresar una decisión en **DMN** y ejecutarla en un motor |
| 4 | Implementar una política con **GoRules ZEN** y con `rule-engine` (Python) |
| 5 | Verificar la **cobertura** (huecos y solapes) y decidir con un **benchmark** si merece la pena un motor |

## Vídeo · DMN en 5 minutos

<iframe width="100%" height="380" src="https://www.youtube.com/embed/Ichayb2cmQw" title="5 Min DMN" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

[Ver en YouTube](https://www.youtube.com/watch?v=Ichayb2cmQw) · *Trisotech*. Qué es DMN y sus tablas de decisión (en inglés).

## 1 · Decision management

**Decision management** es tratar las reglas como un **activo de negocio** gestionable por el área que las posee, no como código disperso. Un **BRMS** (*Business Rule Management System*) permite versionar, probar y desplegar reglas sin tocar la aplicación. Herramientas: **Drools/Apache KIE**, **IBM ODM**, **FICO Blaze**, **SAP BRF+**.

Un BRMS separa el **qué** (las reglas) del **cómo** (la aplicación). La persona de negocio cambia una regla y la despliega sin que intervenga desarrollo.

## 2 · Tablas de decisión y *hit policy*

Una **tabla de decisión** cruza condiciones con acciones. La **hit policy** define qué hacer cuando varias filas encajan:

| Hit policy | Significado |
|---|---|
| **First** | Gana la primera fila que encaja |
| **Unique** | Solo una puede encajar (si no, error de cobertura) |
| **Priority** | Gana la de mayor prioridad |
| **Collect** | Devuelve todas las que encajan (suma, mínimo, lista…) |

La *hit policy* es la respuesta formal al **fallo didáctico** del micro-motor de la sesión anterior (dos reglas contradictorias sobre el mismo hecho).

## 3 · DMN (Decision Model and Notation)

**DMN** (OMG) es el estándar para expresar decisiones como tablas legibles por negocio. Ejemplo para Pagarium:

| Importe | Antigüedad (meses) | Intentos | Decisión |
|---|---|---|---|
| `< 500` | `>= 6` | `< 4` | Aprobar |
| `< 500` | `>= 6` | `>= 4` | Revisar |
| `>= 500` | — | — | Revisar |
| — | `< 6` | — | Rechazar |

La misma tabla se despliega en Drools (KIE) o en GoRules ZEN sin reescribir la lógica.

## 4 · GoRules ZEN: el motor que se usa hoy

**GoRules ZEN** es un motor de decisiones open-source, rápido y embebible, muy usado en **fintech** (pagos, KYC, *scoring*). Define el grafo de decisión en formato **JDM** (JSON Decision Model), normalmente dibujado en su editor web, y se ejecuta desde Python, Node, Rust o Go.

```python
%pip install zen-engine
import json
from zen import ZenEngine

# El grafo JDM suele exportarse del editor de GoRules. Estructura mínima:
# input -> decisionTableNode -> output
graph = {
    "contentType": "application/vnd.gorules.decision",
    "nodes": [
        {"id": "input", "type": "inputNode", "name": "Request",
         "position": {"x": 0, "y": 0}},
        {"id": "table", "type": "decisionTableNode", "name": "Politica",
         "content": {
             "hitPolicy": "first",
             "inputs": [{"id": "i1", "field": "importe", "name": "Importe"}],
             "outputs": [{"id": "o1", "field": "decision", "name": "Decision"}],
             "rules": [
                 {"i1": "< 500", "_id": "r1", "o1": "aprobar"},
                 {"i1": ">= 500", "_id": "r2", "o1": "revisar"},
             ],
         },
         "position": {"x": 200, "y": 0}},
        {"id": "out", "type": "outputNode", "name": "Response",
         "content": {"fields": [{"id": "decision", "field": "decision"}]},
         "position": {"x": 400, "y": 0}},
    ],
    "edges": [
        {"id": "e1", "sourceId": "input", "targetId": "table"},
        {"id": "e2", "sourceId": "table", "targetId": "out"},
    ],
}

engine = ZenEngine()
decision = engine.create_decision(json.dumps(graph))
print(decision.evaluate(json.dumps({"importe": 200})))
```

!!! note "Versiones de ZEN"
    La API de `zen-engine` cambia entre versiones (nombres de módulo y de campos del grafo). Si el grafo no devuelve salida, exporta uno desde el **editor de GoRules** y usa esa estructura: es la fuente fiable.

## 5 · `rule-engine` en Python puro

Para reglas ligeras en un servicio Python, `rule-engine` permite escribir condiciones en texto legible y evaluarlas contra un contexto:

```python
%pip install rule-engine
import rule_engine

ctx = {"importe": 200, "n_intentos": 5, "antiguedad_meses": 10}
aprueba = rule_engine.Rule("importe < 500 and antiguedad_meses >= 6 and n_intentos < 4")
rechaza = rule_engine.Rule("n_intentos >= 4 or antiguedad_meses < 6")

print("aprueba:", aprueba.matches(ctx))   # False (n_intentos=5)
print("rechaza:", rechaza.matches(ctx))   # True
```

## 6 · Verificador de cobertura

Un conjunto de reglas puede tener **huecos** (casos sin cubrir) y **solapes** (varias reglas que encajan). Con `hit policy = unique`, un solape es un error. El **verificador de cobertura** comprueba que toda combinación posible tiene exactamente una decisión. Es una práctica habitual en DMN y en ZEN, y evita el fallo del micro-motor de la sesión anterior.

## 7 · Benchmark: ¿siempre necesitas un motor?

Órdenes de magnitud medidos en el material de referencia para decidir un pago:

| Motor | Tiempo/pago |
|---|---|
| `if/else` a mano | **~0,1 µs** |
| GoRules ZEN | ~54 µs |
| CLIPS (`clipspy`) | ~96 µs |
| `experta` | ~190 µs |

!!! tip "La cifra que hay que leer"
    Un motor de reglas cuesta entre 500 y 2000 veces más que un `if/else`. **No siempre es la respuesta.** Se justifica cuando hay **muchas reglas**, **cambian a menudo** y las **gestiona negocio** (BRMS); no cuando son 3 condiciones fijas.

<iframe width="100%" height="380" src="https://www.youtube.com/embed/1kbmkiMmvAA" title="Business Rule Management Systems: JBoss Drools" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

[Ver en YouTube](https://www.youtube.com/watch?v=1kbmkiMmvAA) · *Ilko Kovacic*. BRMS y Drools, el motor de reglas empresarial más conocido (en inglés).

## Actividad A2 (2 h)

Modela la política de Pagarium como **tabla DMN** con hit policy `unique`, comprueba la cobertura (que no haya huecos ni solapes) e impleméntala con `rule-engine` y con GoRules ZEN. Compara el código y el rendimiento. El cuaderno es `sesion11_motores_reglas.ipynb`.

## Puntos clave de la sesión

- **Decision management** = reglas como activo de negocio; **BRMS** lo permite (Drools/KIE, ODM, Blaze).
- **DMN** y las **tablas de decisión** son el lenguaje de negocio; la **hit policy** formaliza el conflicto.
- **ZEN** (fintech) y `rule-engine` (Python ligero) son dos motores con usos distintos.
- La **cobertura** garantiza que no haya huecos ni solapes.
- Un motor **no siempre compensa**: mide (µs) antes de adoptarlo.
