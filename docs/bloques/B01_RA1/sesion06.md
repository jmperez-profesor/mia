---
sesion: "06"
bloque: B01
ra: RA1
fecha_prevista: 2026-10-28
duracion: 120 min
ce: [4]
titulo: "IA y eficiencia operativa I"
---

# Sesión 06 · IA y eficiencia operativa I

## Objetivos de la sesión
- Aplicar técnicas de IA (clustering y regresión) a un problema operativo realista.
- Detectar operaciones ineficientes mediante K-Means y residuales de regresión.
- Interpretar los resultados como oportunidades de mejora de eficiencia.

## Contenidos
- Aprendizaje no supervisado: K-Means para segmentación de operaciones.
- Aprendizaje supervisado: regresión lineal para modelar el tiempo de proceso.
- Residuales como indicador de ineficiencia.

## Temporalización (120 min)
- **Apertura / activación (10 min):** "¿por qué unas operaciones de almacén tardan más?" → detección de ineficiencia.
- **Desarrollo (80 min):** pipeline K-Means + regresión; se resuelve la práctica guiada; alumnos arrancan su notebook.
- **Cierre y evaluación (30 min):** revisión de la lista top-10 ineficientes; rúbrica de interpretación.

## Práctica guiada (con solución)
Analizamos operaciones de almacén con clustering y regresión.

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

np.random.seed(33)
n = 300
carga = np.random.uniform(10, 100, n)
tipo = np.random.randint(0, 3, n)
errores = np.random.poisson(0.3 + carga / 200)
inef = np.random.choice([0, 1], n, p=[0.85, 0.15])
tiempo = 2 + 0.08 * carga + 4 * inef + np.random.normal(0, 1.5, n)
df = pd.DataFrame({"carga": carga, "tipo": tipo, "errores": errores, "tiempo": tiempo})

X = StandardScaler().fit_transform(df[["carga", "tipo", "errores"]])
df["cluster"] = KMeans(n_clusters=3, random_state=0).fit_predict(X)

modelo = LinearRegression().fit(df[["carga"]], df["tiempo"])
df["pred"] = modelo.predict(df[["carga"]])
print("R2:", round(r2_score(df["tiempo"], df["pred"]), 3))
df["residual"] = df["tiempo"] - df["pred"]
top_inef = df.sort_values("residual", ascending=False).head(10)
print(top_inef[["carga", "errores", "tiempo", "pred", "residual"]])

plt.scatter(df["carga"], df["tiempo"], c=df["cluster"], cmap="viridis", alpha=0.6)
plt.plot(df["carga"], df["pred"], "k--", label="regresión")
plt.xlabel("carga"); plt.ylabel("tiempo"); plt.legend()
plt.title("Operaciones de almacén: clusters e ineficiencia"); plt.show()
```

**Resultado:** K-Means segmenta las operaciones, la regresión explica gran parte de la varianza (R² alto) y los residuales positivos grandes señalan las 10 operaciones más ineficientes a investigar.

## Práctica propuesta (miniproyecto)
**Miniproyecto:** aplicar K-Means y regresión lineal a un registro sintético de operaciones de almacén para detectar las 10 operaciones más ineficientes.

**Entregables:** pipeline de clustering + regresión, métrica R² y lista top-10 ineficientes.

**Criterios de evaluación:** aplica una técnica de IA a un problema operativo; interpreta la mejora.

**Notebook:** [Abrir/Descargar miniproyecto](sesion06_miniproyecto.ipynb)

## Evaluación (criterios CE)
- CE4: el alumno aplica IA a eficiencia operativa e interpreta el resultado.

## Atención a la diversidad
- Refuerzo: explicar residual como "lo que la carga no explica".
- Ampliación: probar otro número de clusters y comparar silueta.

## Observaciones
- sklearn debe estar disponible en el entorno del alumno.
