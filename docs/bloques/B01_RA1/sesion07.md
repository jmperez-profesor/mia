---
sesion: "07"
bloque: B01
ra: RA1
fecha_prevista: 2026-11-04
duracion: 120 min
ce: [4]
titulo: "IA y eficiencia operativa II"
---

# Sesión 07 · IA y eficiencia operativa II

> **Hilo conductor:** pasar de "la IA puede" a "la IA ahorra X € y Y minutos". Adaptado de `material_david/docs/UD01/UD01_ES.md` §§6.2–6.5 (KPIs, técnica→beneficio, ejemplo guiado de la tienda online) + `artint/docs/ia/modelos/machine.md` (definición formal E/T/R y ejemplo filtro spam) + `artint/docs/ia/fases_aa/evaluacion.md`.

## Objetivos de la sesión

Al finalizar, serás capaz de (RA1 · CE RA1-b/d):

- **Cuantificar** una mejora de eficiencia con **KPIs antes/después** (tiempo de ciclo, coste unitario, tasa de error, disponibilidad).
- **Mapear técnica → beneficio** (clasificación, regresión, clustering, PLN, visión, agentes) y elegir la que toca para cada caso.
- **Comparar** un modelo IA frente a una **regla fija** con métrica honesta (MAE) y traducir el error a **ahorro de inventario / tiempo**.

## Contenidos

### 1. Medir es decidir — KPIs que importan

| Indicador base | Qué mide | Ejemplo operativo |
|---|---|---|
| **Tiempo de ciclo** | duración de una operación | 8 min / reclamación |
| **Coste unitario** | € por consulta/pedido/transacción | 3 € / reclamación |
| **Tasa de error** | errores / N operaciones | 15 % mal clasificadas |
| **Disponibilidad** | horas/día operativo | chatbot 24/7 vs. 8 h |
| **Rendimiento** | ops / tiempo / empleado | pedidos/hora |

**KPIs específicos por ámbito** (`UD01_ES.md` §6.3):

| Ámbito | KPI | Lee así |
|---|---|---|
| Atención | **FCR** | % resueltas al primer contacto |
| Atención | **AHT** | tiempo medio por consulta |
| Atención | **Containment** | % cerradas solo por IA |
| Industria | **OEE** | disponibilidad × rendimiento × calidad |
| Industria | **MTBF** | tiempo medio entre averías |

!!! tip "KPI ≠ anécdota"
    *"Va muy bien"* no justifica inversión. *"AHT de 5→2 min y FCR de 40→68 %"* sí. Esa es la diferencia entre la S06 y la S07.

### 2. De la técnica al beneficio — sin hype

| Técnica | Ejemplo RA1 | Beneficio típico |
|---|---|---|
| Clasificación | Priorizar incidencias, cribar CV | Tiempo y error ↓ |
| Regresión | Prever demanda, precio | Stock roto ↓ |
| Clustering | Segmentar clientes | Campañas más rentables |
| Anomalías | Fraude, averías | Pérdidas ↓ |
| PLN / Voz | Chatbot, sentimiento | coste/consulta ↓ |
| Visión | Inspección, OCR | error y tiempo ↓ |
| Agentes / GenAI | Redacción, tramitación | tareas repetitivas ↓ |

Definición formal que usarás en el informe (`artint/docs/ia/modelos/machine.md`): un programa aprende de **E** (experiencia) en **T** (tarea) si su **R** (rendimiento) mejora con **E**. Ej. filtro spam: `T=clasificar`, `E=miles de correos etiquetados`, `R=% aciertos`.

### 3. Caso faro (resuelto) — la tienda de 200 reclamaciones/día

> Tomado de `UD01_ES.md` §6.5.

**Situación:** 2 personas, 8 min/correo, 15 % error. KPI base: `tiempo=8`, `error=15 %`, `coste=2 jornadas`.

**Técnica elegida:** **PLN + clasificación supervisada** (p. ej. Naive Bayes sobre texto vectorizado) — encaja porque es texto → categorías (devolución/cambio/defecto/consulta).

**Antes/después estimado:** clasificador resuelve 70 % en 30 s, resto lo revisa persona → `tiempo medio ≈ 0.7·0.5 + 0.3·8 = 2.75 min` (de 8), `error <5 %`, las 2 personas pasan a casos complejos.

**Decisión:** se comunica con KPIs y se advierte de riesgos (ambigüedad, RGPD). Ese esquema *problema→KPI→técnica→antes/después→decisión* es **caracterizar** (lo que pide RA1, sin entrenar aún).

### 4. Hoy: previsión de demanda → inventario

Mismo esquema, pero con **serie temporal** sintética (tendencia + estacionalidad semanal). Compararemos **IA (RandomForest)** vs. **regla fija** (stock = media) con **MAE** y traduciremos el error a **ahorro de inventario** (percentil 95).

## Temporalización (120 min)

- **Apertura (15 min):** repaso del caso de la tienda (KPIs en pizarra) + pregunta *¿qué KPI movería LARA / hidrógeno / colmena?*
- **Desarrollo (70 min):** §§1–3 + **práctica guiada en vivo** (ver abajo) con MAE y gráfico demanda real vs. predicha.
- **Cierre (35 min):** cada grupo estima su *antes/después* para su caso y arranca el notebook.

## Práctica guiada (con solución) — en vivo

Previsión 90 días, entrena en 72 y prueba en 18. El ahorro se estima llevando el stock al percentil 95 de la predicción.

```python
import numpy as np, pandas as pd, matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

np.random.seed(42)
dias = np.arange(1, 91)
demanda = 50 + 0.3*dias + 10*np.sin(2*np.pi*dias/7) + np.random.normal(0, 5, 90)
df = pd.DataFrame({"dia": dias, "demanda": demanda})
df["dia_semana"] = df["dia"] % 7
df["tendencia"] = df["dia"]

train, test = df.iloc[:72], df.iloc[72:]
Xc = ["dia", "dia_semana", "tendencia"]
modelo = RandomForestRegressor(n_estimators=200, random_state=0).fit(train[Xc], train["demanda"])
pred = modelo.predict(test[Xc])

mae_ia = mean_absolute_error(test["demanda"], pred)
mae_fija = mean_absolute_error(test["demanda"], [test["demanda"].mean()]*len(test))
print(f"MAE IA: {mae_ia:.2f} | MAE regla fija: {mae_fija:.2f} | mejora: {(1-mae_ia/mae_fija)*100:.1f}%")

# Ahorro: stock al P95 de la predicción vs. media histórica
stock_ia = np.quantile(pred, 0.95)
stock_fija = test["demanda"].mean()
print(f"Stock P95 IA: {stock_ia:.1f} | Stock regla fija: {stock_fija:.1f} | ahorro: {(1-stock_ia/stock_fija)*100:.1f}%")

plt.plot(test["dia"], test["demanda"], label="real")
plt.plot(test["dia"], pred, label="predicción IA")
plt.axhline(stock_ia, ls="--", label="stock IA P95")
plt.xlabel("día"); plt.ylabel("demanda"); plt.legend(); plt.title("Previsión de demanda"); plt.show()
```

**Qué leer:** `MAE_IA < MAE_fija` ya es victoria; el **ahorro %** conecta error con dinero — justo lo que pide un *coste por documento/pedido* en `UD01_ES.md` §6.3.

## Práctica propuesta (miniproyecto) — entregable

**Reto:** en `sesion07_miniproyecto.ipynb`, replica el experimento para **3 tiendas** sintéticas (varía `tendencia` y amplitud estacional) y entrega:

1. Tabla `MAE IA vs. fija` y **% mejora** por tienda.
2. Gráfica real vs. predicha (una tienda a elegir).
3. Párrafo: *¿compensa desplegar IA aquí?* Usa **un KPI** (tiempo, coste o error) con números antes/después.

**Criterios (RA1):** relaciona técnica→beneficio con KPI; la cuantificación es coherente; el notebook es reproducible.

**Notebook:** [Abrir/Descargar miniproyecto](sesion07_miniproyecto.ipynb)

## Materiales / recursos

- **Apuntes base:** `material_david/docs/UD01/UD01_ES.md` §§6.2–6.5; `artint/docs/ia/modelos/machine.md` (E/T/R, filtro spam, DL).
- **KPI de referencia:** tablas 6.2/6.3 de UD01.

## Evaluación (criterios CE)

- **CE RA1-d:** argumenta eficiencia operativa con KPI comparado, no con adjetivos.

## Atención a la diversidad

- **Refuerzo:** plantilla con `mae_ia/mae_fija` ya calculados; solo interpretar.
- **Ampliación:** añade evento promocional (`promo=1` 5 días) y mide el salto de MAE; propone mitigación.

## Observaciones

- El percentil de stock (P95) fija el **nivel de servicio**; discutir *trade-off* disponibilidad vs. sobre-stock.
- Si el grupo va justo de tiempo, deja la variante 3 tiendas como ampliación y cierra con una sola.
