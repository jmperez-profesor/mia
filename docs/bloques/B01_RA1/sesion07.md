---
sesion: "07"
bloque: B01
ra: RA1
fecha_prevista: 2026-10-28
duracion: 120 min
ce: [4]
titulo: "IA y eficiencia operativa II"
---

# Sesión 07 · IA y eficiencia operativa II

## Objetivos de la sesión
- Construir un modelo de previsión de demanda y relacionarlo con el coste de inventario.
- Comparar un modelo de IA frente a una regla fija de stock mediante MAE.
- Cuantificar el ahorro de inventario estimado sin perder nivel de servicio.

## Contenidos
- Series temporales sintéticas: tendencia y estacionalidad.
- Modelos de regresión para previsión (RandomForest, estacionalidad).
- Eficiencia operativa: reducción de inventario y coste asociado.

## Temporalización (120 min)
- **Apertura / activación (10 min):** "¿cuánto stock guardas por miedo a quedarte sin él?" → sobre-stock.
- **Desarrollo (80 min):** construcción del modelo y comparación MAE; se resuelve la práctica guiada; alumnos arrancan su notebook.
- **Cierre y evaluación (30 min):** presentación del ahorro estimado; rúbrica de la cuantificación.

## Práctica guiada (con solución)
Modelamos demanda y comparamos IA vs regla fija de stock.

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

np.random.seed(42)
dias = np.arange(1, 91)
demanda = 50 + 0.3 * dias + 10 * np.sin(2 * np.pi * dias / 7) + np.random.normal(0, 5, 90)
df = pd.DataFrame({"dia": dias, "demanda": demanda})
df["dia_semana"] = df["dia"] % 7
df["tendencia"] = df["dia"]

train, test = df.iloc[:72], df.iloc[72:]
Xc = ["dia", "dia_semana", "tendencia"]
modelo = RandomForestRegressor(n_estimators=100, random_state=0).fit(train[Xc], train["demanda"])
pred = modelo.predict(test[Xc])

mae_ia = mean_absolute_error(test["demanda"], pred)
mae_fija = mean_absolute_error(test["demanda"], [test["demanda"].mean()] * len(test))
ahorro_pct = (1 - test["demanda"].quantile(0.95) / test["demanda"].mean()) * 100

print(f"MAE modelo IA: {mae_ia:.2f}")
print(f"MAE regla fija: {mae_fija:.2f}")
print(f"Ahorro de inventario estimado: {ahorro_pct:.1f}%")

plt.plot(test["dia"], test["demanda"], label="real")
plt.plot(test["dia"], pred, label="predicción IA")
plt.xlabel("día"); plt.ylabel("demanda"); plt.legend()
plt.title("Previsión de demanda"); plt.show()
```

**Resultado:** el modelo IA reduce el MAE respecto a la regla fija; el ahorro de inventario estimado (reducción del stock al percentil 95 de la predicción) se cuantifica como porcentaje.

## Práctica propuesta (miniproyecto)
**Miniproyecto:** construir un modelo de previsión de demanda para 12 tiendas sintéticas, comparar MAE (IA vs regla fija) y estimar el ahorro de inventario.

**Entregables:** serie temporal + modelo, comparación de MAE y cálculo de ahorro %.

**Criterios de evaluación:** relaciona predicción con eficiencia; cuantifica la mejora de la IA.

**Notebook:** [Abrir/Descargar miniproyecto](sesion07_miniproyecto.ipynb)

## Evaluación (criterios CE)
- CE4: el alumno relaciona la IA con eficiencia operativa y cuantifica la mejora.

## Atención a la diversidad
- Refuerzo: descomponer la serie en tendencia + estacionalidad en pizarra.
- Ampliación: añadir evento promocional y medir su efecto en el error.

## Observaciones
- El ahorro depende del nivel de servicio elegido (percentil); debatir el trade-off.
