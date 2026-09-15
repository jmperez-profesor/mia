# B05 · RA5 — Ejercicios de autoevaluación

> Para las 3 sesiones del RA5 (S2, S3, S4). No son entregables; se corrigen en clase. Hilo conductor: **Pagarium**. Adaptados de la UD05 de David Martínez Peña (CC BY-NC-SA 4.0) y de los apuntes de este bloque.

## A. Sistemas expertos (RA5-a/c) · S2

**A1.** ¿Por qué las reglas siguen usándose en 2026 junto a la IA generativa? Cita dos motivos y un sector.

**A2.** Enumera los componentes de un sistema experto y la función de cada uno.

**A3.** Explica el ciclo **reconocer → resolver → actuar** con tus palabras.

**A4.** El micro-motor de Pagarium emite `aprobar` y `rechazar` para el mismo pago. ¿Por qué ocurre y cómo se corrige? (relaciónalo con `salience` y con el razonamiento no monótono).

**A5.** Diferencia **forward** y **backward chaining** con un ejemplo de cada uno.

**A6.** ¿Qué son los **factores de certeza** y por qué los introdujo MYCIN?

**A7.** ¿Por qué `experta` falla en Python 3.10+ y qué alternativa mantenida usarías en producción?

**A8.** Explica qué aporta **RETE/PHREAK** frente a un *match* ingenuo.

**A9.** Un sensor de Pagarium oscila alrededor del umbral y el sistema conmuta sin parar. ¿Cómo lo mitiga la **histéresis**?

## B. Motores de reglas (RA5-b) · S3

**B1.** ¿Qué es *decision management* y en qué se diferencia de tener las reglas dentro del código?

**B2.** Define **hit policy** y explica `first`, `unique`, `priority` y `collect`.

**B3.** Escribe la política de Pagarium como **tabla DMN** (importe, antigüedad, intentos → decisión).

**B4.** ¿Qué es **DMN** y por qué lo entiende el área de negocio?

**B5.** ¿Qué es **GoRules ZEN** y por qué se usa en fintech? ¿Qué formato usa el grafo de decisión?

**B6.** Escribe con `rule-engine` una regla que apruebe si `importe < 500` y `n_intentos < 4`.

**B7.** ¿Qué comprueba un **verificador de cobertura** y qué evita?

**B8.** Con el benchmark (~0,1 µs `if/else`, ~54 ZEN, ~96 CLIPS, ~190 `experta`): ¿cuándo merece la pena un motor de reglas y cuándo no?

## C. Híbridos y tendencias (RA5-b/d/e) · S4

**C1.** Diferencia **deducir reglas de los datos** (FIGS) de **mejorar reglas propias con ML**.

**C2.** En el caso de Pagarium, FIGS recupera `importe > 997.45` cuando la política real era `> 1000`. ¿Por qué no coincide exactamente?

**C3.** ¿Qué ventaja de interpretabilidad tiene FIGS frente a un árbol de decisión grande?

**C4.** Explica las **reglas como guardarraíl** de un agente LLM con un ejemplo de pago.

**C5.** ¿Qué aportan los **sistemas neuro-simbólicos** frente a un LLM solo? Cita tres cosas.

**C6.** ¿Qué es el **AI Act** y por qué el *scoring* crediticio es de alto riesgo? ¿Qué cambió el Ómnibus Digital?

**C7.** Diseña las dos capas del **proyecto Pagarium**: reglas de negocio y guardarraíl.

**C8.** ¿Qué es un **policy engine** (OPA/Rego) y en qué se diferencia de un BRMS?
