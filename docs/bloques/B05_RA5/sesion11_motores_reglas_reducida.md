---
sesion: "11"
bloque: B05
ra: RA5
fecha: 2026-10-21
duracion: 2 h
titulo: "Motores de reglas (reducida)"
---

# Sesión 11 · Motores de reglas (21/10/2026) — versión reducida

> **RA5.** Del sistema experto «clásico» al **motor de reglas de negocio**: las reglas como activo de empresa.
> **CE:** RA5-b (representar y simular comportamientos básicos).

## Cuaderno de la sesión

[Abrir en Colab](https://colab.research.google.com/github/jmperez-profesor/mia/blob/main/docs/bloques/B05_RA5/sesion11_motores_reglas.ipynb){ .md-button } · [ver en el sitio](sesion11_motores_reglas.ipynb)

## Qué vas a aprender

| # | Al terminar la sesión serás capaz de… |
|---|---|
| 1 | Explicar qué es el **decision management** y qué aporta un **BRMS** |
| 2 | Leer y escribir **tablas de decisión** con su **hit policy** |
| 3 | Detectar **huecos** y **solapes** (cobertura) |

## 1 · Decision management y BRMS (5 min)

**Decision management** = tratar las reglas como un **activo de negocio**, no como código disperso. Un **BRMS** (*Business Rule Management System*: Drools/KIE, IBM ODM, FICO Blaze) separa el *qué* (las reglas) del *cómo* (la aplicación): la persona de negocio cambia una regla y la despliega sin tocar código.

## 2 · Tablas de decisión y hit policy

Una **tabla de decisión** cruza condiciones con acciones. La **hit policy** decide qué hacer cuando varias filas encajan:

| Hit policy | Significado |
|---|---|
| **First** | Gana la primera fila que encaja |
| **Unique** | Solo una puede encajar (si no, error de cobertura) |
| **Priority** | Gana la de mayor prioridad |
| **Collect** | Devuelve todas las que encajan |

Es la respuesta formal al **fallo del micro-motor** de la S9 (dos reglas contradictorias sobre el mismo hecho).

## 3 · DMN y el ejercicio de Pagarium

**DMN** (*Decision Model and Notation*, de OMG) es el estándar para expresar decisiones como **tablas legibles por negocio**, desplegables en distintos motores sin reescribir la lógica. El guion `—` significa «no importa».

### Completa la política de Pagarium

La primera fila está resuelta. Completa la columna **Decisión** de las otras tres:

| Importe | Antigüedad (meses) | Intentos | Decisión |
|---|---|---|---|
| `< 500` | `>= 6` | `< 4` | **Aprobar** |
| `< 500` | `>= 6` | `>= 4` | … |
| `>= 500` | — | — | … |
| — | `< 6` | — | … |

??? tip "Solución"
    | Importe | Antigüedad | Intentos | Decisión |
    |---|---|---|---|
    | `< 500` | `>= 6` | `< 4` | Aprobar |
    | `< 500` | `>= 6` | `>= 4` | Revisar |
    | `>= 500` | — | — | Revisar |
    | — | `< 6` | — | Rechazar |

    La fila 3 y la fila 4 se **solapan** cuando `importe >= 500` y `antigüedad < 6` a la vez → por eso `unique` fallaría.

## 4 · Los motores en la práctica (en el cuaderno)

Dos motores de uso real que montamos **paso a paso en el cuaderno** (con `# TODO`), no aquí para no alargar:

- **GoRules ZEN** (fintech): motor embebible y rápido; el grafo va en formato **JDM** (JSON).
- **`rule-engine`** (Python ligero): reglas en texto evaluadas contra un diccionario.

## 5 · Cobertura

Un conjunto de reglas puede tener **huecos** (casos sin cubrir) y **solapes** (varias reglas encajan a la vez). El **verificador de cobertura** comprueba que toda combinación posible tiene **exactamente una** decisión.

## 6 · ¿Siempre necesitas un motor?

| Motor | Tiempo/pago |
|---|---|
| `if/else` a mano | ~0,1 µs |
| GoRules ZEN | ~54 µs |
| CLIPS (`clipspy`) | ~96 µs |
| `experta` | ~190 µs |

Un motor cuesta **500–2000× más** que un `if/else`: compensa con **muchas reglas**, que **cambian a menudo** y las **gestiona negocio**; no cuando son 3 condiciones fijas.

## Actividad A2 (2 h)

Completa los `# TODO` del cuaderno (las tres reglas y la función `decidir`), detecta el **solape** y despliega la política con **ZEN**. Compara el rendimiento con el benchmark (§6).

## Opcional (para casa)

- Vídeo: [DMN en 5 minutos](https://www.youtube.com/watch?v=Ichayb2cmQw) y [BRMS/Drools](https://www.youtube.com/watch?v=1kbmkiMmvAA).
- Profundizar en `rule-engine` y en el verificador de cobertura.

## Puntos clave

- **BRMS** = reglas como activo; separa el *qué* del *cómo*.
- **Tabla de decisión + hit policy** formalizan el conflicto de reglas.
- **DMN** es el lenguaje de negocio; la **cobertura** evita huecos y solapes.
- Un **motor no siempre compensa**: mide antes de adoptarlo.
