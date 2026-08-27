# RA3 · Procesamiento de lenguaje natural — Banco de pruebas y rúbrica

**Resultado de aprendizaje:** Relaciona el procesamiento de lenguaje natural (PLN) con sus aplicaciones y limitaciones.
**Criterio de evaluación (CE7).**

## 1. Prueba tipo test (10 ítems)

1. El PLN trata de:
   a) Solo traducir · b) **Que las máquinas procesen lenguaje humano** ✅ · c) Imágenes · d) Audio puro
2. La lematización consiste en:
   a) Contar palabras · b) **Reducir a la forma base (lema)** ✅ · c) Borrar texto · d) Traducir
3. TF-IDF mide:
   a) Sinónimos · b) **Importancia de un término en un documento frente al corpus** ✅ · c) Gramática · d) Sonido
4. Un embedding de palabra representa:
   a) Frecuencia · b) **Un vector de significado en un espacio continuo** ✅ · c) Una letra · d) Un número de página
5. Word2Vec permite:
   a) Solo contar · b) **Calcular similitud semántica (rey–hombre ≈ reina–mujer)** ✅ · c) Traducir · d) Nada
6. Los transformers usan:
   a) Solo CNN · b) **Mecanismo de atención** ✅ · c) Árboles · d) Reglas
7. El análisis de sentimiento clasifica:
   a) Colores · b) **La polaridad (positivo/negativo/neutro)** ✅ · c) Idioma · d) Autor
8. NER significa:
   a) Red neuronal · b) **Extracción de entidades nombradas** ✅ · c) Nube de palabras · d) Ruido
9. Un LLM puede alucinar porque:
   a) No tiene memoria · b) **Genera texto probable, no verificado** ✅ · c) Siempre miente · d) No usa datos
10. Limitación del PLN en español:
    a) No existe · b) **Menos recursos que inglés y ambigüedad morfológica** ✅ · c) Es perfecto · d) Solo vocabulario

## 2. Prueba de desarrollo (3 ejercicios)

**D1.** Diseña un pipeline de PLN para clasificar reseñas y justifica cada paso (tokenización, lematización, vectorización, modelo).
*Criterios:* pipeline completo (2 p); justificación de cada paso (2 p); elección de modelo (1 p).

**D2.** Entrena (o describe) un clasificador de texto con scikit-learn y explica las métricas de evaluación.
*Criterios:* código/descripción válida (2 p); métricas (precisión/recall/F1) (2 p); interpretación (1 p).

**D3.** Analiza las limitaciones de un LLM en una aplicación real y propón mitigaciones.
*Criterios:* caso concreto (2 p); limitaciones (alucinaciones, sesgo, coste) (2 p); mitigaciones (1 p).

## 3. Rúbrica de RA3 (escala 1–10, entera)

| Dimensión | 1–4 | 5–6 | 7–8 | 9–10 |
|-----------|-----|-----|-----|------|
| Preprocesamiento (tokenización, lemas, POS) | Errores | Aplica pasos básicos | Pipeline correcto | Optimiza para el dominio |
| Representación (BoW, TF-IDF, embeddings) | Confunde | Usa una representación | Elige y justifica | Compara y mejora |
| Clasificación/sentimiento | No clasifica | Modelo simple funcional | Modelo evaluado | Modelo ajustado y validado |
| Transformers/LLM | Desconoce | Describe concepto | Explica atención/aplicación | Analiza limitaciones a fondo |
| Aplicaciones y limitaciones | Ignora | Menciona alguna | Relaciona aplicación–limitación | Propone mitigaciones sólidas |

**Conversión a nota:** media de dimensiones (entera). Mínimo para superar el RA = 5.
