# 🤖 Machine Learning - Proyectos Comparativos

Este módulo contiene dos proyectos aplicados de Machine Learning enfocados en clasificación supervisada. Se comparan distintos algoritmos en contextos reales y académicos, evaluando su rendimiento, interpretabilidad y aplicabilidad.

---

## 📌 Proyecto 1: Análisis Comparativo de Algoritmos de ML  
### Predicción de Contratación de Servicios

### 📝 Descripción del problema
Se busca predecir si un cliente contratará un servicio específico, utilizando sus características demográficas y comportamentales.

### 💼 Contexto empresarial
- **Objetivo**: Identificar clientes con alta probabilidad de contratación.
- **Aplicación**: Optimización de campañas de marketing y recursos comerciales.
- **Beneficio**: Reducción de costos y aumento de conversión.

### 📊 Dataset
- **Variable objetivo**: `Contratara_Servicio` (binaria: 0=No, 1=Sí).
- **Variables predictoras**: Datos del cliente (edad, historial, etc.).

### 🧠 Algoritmos evaluados
1. Regresión Logística  
2. K-Nearest Neighbors (KNN)  
3. Árbol de Decisión  
4. Random Forest  
5. Support Vector Machine (SVM)

### ⚙️ Metodología
- División: 70% entrenamiento / 30% prueba  
- Normalización para modelos sensibles a escala  
- Optimización de hiperparámetros  
- Evaluación con múltiples métricas (accuracy, matriz de confusión, etc.)

### 📈 Resultados destacados
- **Random Forest**: Accuracy ~97–99%  
- **SVM (RBF)**: Accuracy ~96–98%  
- **Árbol de Decisión**: Accuracy ~94–96%  
- **KNN**: Accuracy ~92–95%  
- **Regresión Logística**: Accuracy ~88–92%

### 🔍 Insights clave
- Variables más influyentes: `[Top 3 del análisis]`  
- K óptimo para KNN: `{best_k}`  
- Kernel óptimo para SVM: `{best_kernel}`  
- Profundidad ideal para Árbol: 5

### 🧭 Recomendaciones estratégicas
- **Producción**: Random Forest  
- **Explicabilidad**: Árbol de Decisión  
- **Prototipado rápido**: Regresión Logística  
- **Segmentación de clientes**: Basada en probabilidades de contratación

### ⚠️ Limitaciones
- Validación temporal pendiente  
- Costos de error deben ser considerados  
- Posible deriva del comportamiento del cliente

### 🚀 Próximos pasos
1. Validación cruzada  
2. Técnicas de ensemble avanzadas  
3. Ingeniería de características  
4. Pipeline de MLOps

### 📎 Enlace al proyecto
[🔗 Ver notebook del proyecto](./M4/s1/contratacion_servicios.ipynb)

---

## 📌 Proyecto 2: Clasificación Supervisada - Dataset Iris

### 📝 Descripción del problema
Clasificar especies de flores iris (Setosa, Versicolor, Virginica) usando características morfológicas.

### 🌸 Características del dataset
- Longitud y ancho del sépalo  
- Longitud y ancho del pétalo  
- 150 muestras, 3 clases

### 🧠 Algoritmos comparados
1. Regresión Logística  
2. Árbol de Decisión  
3. Random Forest  
4. Support Vector Machine (SVM)

### 📊 Métricas de evaluación
- Accuracy  
- Matriz de confusión  
- Reporte de clasificación (Precision, Recall, F1-Score)

### 📈 Resultados
- Todos los modelos lograron **100% de accuracy** en el conjunto de prueba  
- Dataset ideal para clasificación por su limpieza y separación de clases

### 🔍 Observaciones clave
- Random Forest y SVM son más robustos para producción  
- Regresión Logística y Árbol de Decisión son altamente interpretables  
- Dataset pequeño y limpio: ideal para demostración, no para generalización

### 🧭 Recomendaciones
- Para producción: Random Forest o SVM  
- Para interpretabilidad: Árbol o Regresión Logística  
- Para datasets reales: aplicar validación cruzada

### 📎 Enlace al proyecto
[🔗 Ver notebook del proyecto](./M4/s2/iris_clasificacion.ipynb)

---

## 🧠 Conclusión general

Estos proyectos demuestran cómo distintos algoritmos de clasificación pueden adaptarse a diferentes contextos. La elección del modelo depende del equilibrio entre precisión, interpretabilidad y robustez. Se recomienda siempre evaluar múltiples enfoques y validar con datos reales antes de implementar en producción.
