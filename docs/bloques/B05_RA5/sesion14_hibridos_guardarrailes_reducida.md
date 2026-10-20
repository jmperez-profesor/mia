---
sesion: "14"
bloque: B05
ra: RA5
fecha: 2026-10-26
duracion: 2 h
titulo: "Híbridos y guardarraíles (reducida)"
---

# Sesión 14 · Híbridos, guardarraíles y neuro-simbólico (26/10/2026) — versión reducida

> **RA5.** Tercera sesión del RA5: guardarraíles para LLM, sistemas neuro-simbólicos y el AI Act, culminando en el proyecto integrador.
> **CE:** RA5-b (simular comportamientos), RA5-d (estrategias de control) y RA5-e (controladores inteligentes).

## Cuaderno de la sesión

[Abrir en Colab](https://colab.research.google.com/github/jmperez-profesor/mia/blob/main/docs/bloques/B05_RA5/sesion14_hibridos_guardarrailes.ipynb){ .md-button } · [ver en el sitio](sesion14_hibridos_guardarrailes.ipynb)

## Qué vas a aprender

| # | Al terminar la sesión serás capaz de… |
|---|---|
| 1 | Construir un **guardarraíl** que acota las acciones de un agente LLM |
| 2 | Explicar qué es un **sistema neuro-simbólico** y qué aporta |
| 3 | Situar el **AI Act** y el derecho a explicación |
| 4 | Integrar reglas + guardarraíl en el **proyecto Pagarium** |

## 1 · Reglas como guardarraíl de agentes LLM

Un agente LLM **propone**; las reglas **validan y acotan** antes de ejecutar. Patrón actual en pagos, salud y cloud:

```python
import re

def validar_accion_llm(texto):
    # findall(...) busca números seguidos de EUR
    importes = [float(x) for x in re.findall(r"(\d+(?:\.\d+)?)\s*EUR", texto)]
    if any(i > 1000 for i in importes):      # ¿alguno supera el límite?
        return False, "importe fuera de rango"
    if "cuenta no verificada" in texto.lower():
        return False, "destino no permitido"
    return True, "ok"

for t in ["Transferir 500 EUR a la cuenta A", "Transferir 5000 EUR", "Pagar a cuenta no verificada"]:
    print(t, "->", validar_accion_llm(t))
```

## 2 · Sistemas neuro-simbólicos

Combinan **redes neuronales** (aprendizaje) con **razonamiento simbólico** (reglas). Aportan **menos alucinaciones**, **explicabilidad** y **trazabilidad**. Es la tendencia dominante en IA aplicada a negocio.

## 3 · AI Act y decisiones automatizadas

El **AI Act** (Reglamento UE 2024/1689) regula la IA por riesgo. La **explicación** (de la que MYCIN fue pionero) es hoy obligatoria: el **RGPD** recoge el **derecho a explicación** de las decisiones automatizadas.

!!! warning "Verifica el calendario"
    El calendario del AI Act ha cambiado varias veces (transparencia desde agosto 2026; alto riesgo aplazado a diciembre 2027 por el Ómnibus Digital). Contrasta la fecha vigente antes de evaluar.

## 4 · Proyecto integrador Pagarium

**Reto (individual o parejas):** construir la política de decisión de Pagarium con **dos capas**:

1. **Reglas de negocio** (elegibilidad) en DMN/ZEN o `rule-engine`.
2. **Guardarraíl** que valida las acciones de un agente LLM.

**Entregables:** tabla DMN con hit policy y cobertura verificada, implementación ejecutable e informe (300 palabras) con huecos/solapes detectados, decisión sobre usar o no un motor (con el benchmark) y 1 riesgo de cumplimiento (AI Act/RGPD).

## Opcional (para casa)

- **FIGS**: recuperar reglas legibles de los datos (`imodels`), cuando nadie las escribió a mano.
- Vídeo: [¿Qué es la IA neuro-simbólica? (IBM)](https://www.youtube.com/watch?v=ZfWDVO3rzeA).
- Tabla de **aplicaciones por sector** (banca, salud, industria, cloud, legal).

## Puntos clave

- Los **guardarraíles** acotan a los LLM/agentes; lo **neuro-simbólico** reduce alucinaciones y aporta explicabilidad.
- El **AI Act** y el derecho a explicación del RGPD hacen que la explicación ya no sea opcional.
- El **proyecto Pagarium** integra las tres sesiones: reglas + DMN/ZEN + guardarraíl.
