# B05 · RA5 — Ejercicios de autoevaluación

> Para las 12 h del RA5. No son entregables; se corrigen en clase. Adaptados de `material_david/docs/UD05/UD05_Ejercicios.md` (CC BY-NC-SA 4.0) y de los apuntes de este bloque.

## A. Del conocimiento a la arquitectura (RA5-a) · S1

**A1.** Sitúa en la jerarquía DIKW: «37», «la temperatura es 37 ºC», «si supera 37 ºC hay fiebre», «si hay fiebre, pauta paracetamol».

**A2.** Define **sistema experto** y en qué se diferencia de un programa tradicional.

**A3.** Enumera los componentes de un sistema experto y la función de cada uno.

**A4.** Explica el ciclo **reconocer-actuar** (match, resolve, act) con tus palabras.

**A5.** Diferencia **forward** y **backward chaining** con un ejemplo de cada uno.

**A6.** Enuncia **Modus Ponens** y **Modus Tollens** y relaciónalos con cada encadenamiento.

**A7.** ¿Qué son los **factores de certeza** y por qué los introdujo MYCIN? Pon el ejemplo fiebre (0,6) + rigidez (0,4).

**A8.** ¿Por qué la **explicación** es una ventaja clave frente al ML?

## B. Representación y motores (RA5-a) · S2

**B1.** Completa: pares atributo-valor, reglas de producción, jerarquías, frames, lógica formal, redes semánticas y ontologías (estructura + inferencia típica).

**B2.** Escribe «si llueve, coge el paraguas» en tres representaciones distintas.

**B3.** ¿Cuándo conviene una **ontología** y cuándo **reglas**?

**B4.** ¿Qué es el *bottleneck* de la adquisición de conocimiento?

**B5.** Cita 3 motores de reglas del mercado actual y un uso de cada uno. ¿Qué es **DMN**?

**B6.** Diferencia un **BRMS** (Drools) de un **policy engine** (OPA/Rego). Pon un caso de cada uno.

## C. Simular con `experta` (RA5-b) · S3

**C1.** ¿Por qué `experta` falla en Python 3.10+ y cuál es la solución?

**C2.** Escribe un sistema `experta` que clasifique una incidencia como crítica si `impacto=alto` o `usuarios>50`.

**C3.** Explica qué hacen `engine.reset()` y `engine.run()`.

**C4.** ¿Qué hace `P(...)` y qué error sutil provoca olvidarlo? (pista: el motor se queda congelado sin excepción).

**C5.** Propón un dominio distinto a los vistos y describe 3 reglas de su sistema experto.

## D. Híbridos reglas/datos (RA5-b) · S4

**D1.** Diferencia **deducir reglas de datos** de **mejorar reglas propias con ML**.

**D2.** ¿Qué aporta **FIGS** frente a un árbol de decisión grande en interpretabilidad?

**D3.** En un notebook con `FIGSClassifier`, ¿quién escribe las reglas: el experto o el algoritmo?

**D4.** Propón un caso donde usarías **skope-rules** en lugar de escribir reglas a mano.

**D5.** Explica las **reglas como guardarraíl** de un LLM con un ejemplo (importes, rangos, acciones permitidas).

## E. Lógica difusa (RA5-b/d) · S5

**E1.** Diferencia lógica proposicional y difusa con el ejemplo de «hace frío».

**E2.** Define **variable lingüística**, **valor lingüístico** y **función de pertenencia**.

**E3.** Describe los tres pasos: fuzzificación, evaluación de reglas y desfuzzificación.

**E4.** Con servicio 9,8 y comida 6,5, ¿por qué la propina (≈19,24 €) sale en la banda alta?

**E5.** ¿Qué función de pertenencia usarías para un ciclo (hora del día) y por qué no una triangular?

## F. Variación y dinámica (RA5-c) · S5

**F1.** Diferencia **sensibilidad** y **robustez**.

**F2.** ¿Qué ocurre si añades demasiadas condiciones a una regla crítica? ¿Y si simplificas en exceso?

**F3.** Explica la **histéresis** en un sistema de ventilación con sensor de CO y su solución.

**F4.** ¿Cómo afecta **subir el umbral de certeza** a falsos positivos y a alertas tempranas?

## G. Estrategias de control (RA5-d) · S6

**G1.** ¿Qué es la **salience** y por qué se usa para emergencias?

**G2.** ¿Qué es el **control de meta**? Relaciónalo con la «sabiduría» del DIKW.

**G3.** Define las **especificaciones de respuesta**: precisión, tiempo de asentamiento, sobreimpulso y estabilidad.

**G4.** Para controlar una sala a 21 ºC con error ±0,5 ºC y sobreimpulso máximo 1 ºC, ¿qué controlador elegirías y por qué?

## H. Controladores inteligentes (RA5-e) · S6

**H1.** Describe el **lazo de control** (SP, error, controlador, actuador, planta, PV) y la fórmula del PID.

**H2.** ¿Qué limitaciones tiene el PID ante no linealidades o retraso?

**H3.** Enumera los cuatro controladores inteligentes y su ventaja sobre el PID.

**H4.** Con los datos de los apuntes: ¿qué mejora aportó el control difuso (asentamiento y sobreimpulso)?

**H5.** Explica cómo un sistema experto actúa como controlador **directo** y **supervisor**, y qué aporta la explicación.

## I. Aplicaciones y tendencias · S6

**I1.** Enumera 4 sectores donde se aplican sistemas expertos y un uso en cada uno.

**I2.** ¿Qué es un **BRMS** y cuál es la herramienta más conocida?

**I3.** ¿Qué son los **sistemas neuro-simbólicos** y qué relación tienen con los híbridos del bloque D?

**I4.** ¿Qué es la **XAI** y qué relación tiene con MYCIN y con el RGPD?

**I5.** Explica el uso de **reglas como guardarraíl** del ML/LLM con un ejemplo.
