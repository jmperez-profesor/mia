# S04 · Ejercicios de autoevaluación — IA 3: Ciclo del dato y preprocesamiento

> Adaptados de `material_david/docs/UD01/UD01_Ejercicios.md` bloques **C–D** (CC BY-NC-SA 4.0) + `artint/docs/ia/modelos/datos.md` + `docs/bloques/B01_RA1/sesion04.md` (Telco Churn). Distintos de S01–S03.

## C. Datos y tipos (RA1-b/c)

**C1.** Explica con **Telco Churn** cómo detectar un nulo sistemático (`TotalCharges` en `tenure=0`) vs. aleatorio. ¿Por qué mediana condicionada y no global?

**C2.** ¿Por qué `Contract` nominal debe ir con **One-Hot** y no con `rojo=0, verde=1`? Pon el ejemplo de la tabla de codificación.

**C3.** Clasifica el tipo de problema: ¿`Churn` es clasificación, regresión o clustering? ¿Qué métrica usarías (accuracy/F1, MAE, silueta)?

## D. Técnicas y pipeline (RA1-c)

**D1.** Clasifica: (a) grietas por foto, (b) agrupar clientes churn por riesgo, (c) predecir `MonthlyCharges`, (d) agente que responde facturas.

**D2.** Describe el **pipeline honesto** `SimpleImputer(median/most_frequent) + StandardScaler + OneHot` dentro de `ColumnTransformer`. ¿Dónde se ajusta el scaler y por qué?

**D3.** Ante `pipe.score=0.78` que no sube al cambiar `max_depth`, ¿cambiarías **modelo** o **datos**? Justifica con el diagrama de 6 pasos (fuga, sesgo).

**D4.** (práctico) Dibuja `df["TotalCharges"].isna().sum()` antes/después de `pd.to_numeric(errors="coerce")`. ¿Qué revela?

> Soluciones en clase. Bases: `UD01_Ejercicios.md` C–D + `artint/ia/modelos/datos.md` + `sesion04.md`.
