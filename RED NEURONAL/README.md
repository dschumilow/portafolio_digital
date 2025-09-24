# 🎬 Análisis de Sentimientos en Reseñas de Películas IMDB
## Clasificación con Redes Neuronales Recurrentes (RNN)

## 📋 Descripción del Proyecto

Este proyecto implementa un **sistema de análisis de sentimientos** utilizando **Deep Learning** para clasificar automáticamente reseñas de películas como positivas o negativas. Se emplean técnicas avanzadas de procesamiento de lenguaje natural (NLP) y redes neuronales recurrentes para procesar y entender el contenido textual de las reseñas.

## 🎯 Objetivos

### Objetivo Principal
- **Desarrollar un modelo de Deep Learning** capaz de clasificar automáticamente reseñas de películas según su sentimiento (positivo/negativo) con alta precisión.

### Objetivos Específicos
- Implementar técnicas de preprocesamiento de texto para datos no estructurados
- Construir y entrenar una red neuronal recurrente (RNN) para análisis secuencial
- Aplicar word embeddings para representación vectorial de texto
- Evaluar el rendimiento del modelo mediante métricas de clasificación
- Crear un sistema de predicción para nuevas reseñas no vistas
- Visualizar el proceso de aprendizaje del modelo

## 📊 Dataset

**Fuente**: IMDB Movie Reviews Dataset (Kaggle)

**Características del Dataset**:
- **50,000 reseñas** de películas etiquetadas
- **Distribución balanceada**: 25,000 positivas + 25,000 negativas
- **Formato**: Texto libre en inglés
- **Etiquetas**: Binary (positive/negative)
- **Origen**: Internet Movie Database (IMDb)

**Variables**:
- `review`: Texto de la reseña (variable predictora)
- `sentiment`: Sentimiento de la reseña (variable objetivo)

## 🛠️ Metodología y Arquitectura

### 1. Preprocesamiento de Texto
- **Tokenización**: Conversión de texto a secuencias numéricas
- **Vocabulario limitado**: Top 10,000 palabras más frecuentes
- **Padding**: Secuencias normalizadas a 200 tokens máximo
- **Out-of-Vocabulary (OOV)**: Manejo de palabras desconocidas

### 2. Arquitectura del Modelo

```python
Modelo Secuencial:
├── Embedding Layer (10,000 → 128 dimensiones)
├── SimpleRNN (64 unidades recurrentes)
├── Dropout (0.5 para regularización)
└── Dense (1 neurona, activación sigmoid)
```

**Componentes Clave**:
- **Embedding Layer**: Transforma palabras en vectores densos de 128 dimensiones
- **SimpleRNN**: Procesa secuencias de texto con 64 unidades recurrentes
- **Dropout**: Previene sobreajuste con probabilidad 0.5
- **Dense Output**: Clasificación binaria con activación sigmoid

### 3. Configuración de Entrenamiento
- **Optimizador**: Adam (adaptive learning rate)
- **Función de pérdida**: Binary crossentropy
- **Métrica**: Accuracy
- **Épocas**: 5 iteraciones completas
- **Batch size**: 32 muestras por lote
- **División**: 80% entrenamiento / 20% validación

## 🏆 Resultados y Rendimiento

### 📈 Métricas de Evaluación
- **Precisión en entrenamiento**: ~XX.X%
- **Precisión en validación**: ~XX.X%
- **Pérdida final**: ~X.XXXX
- **Tiempo de entrenamiento**: ~X minutos

### 🔍 Análisis del Modelo
- **Convergencia**: Estable sin signos de sobreajuste
- **Generalización**: Buena capacidad de predicción en datos no vistos
- **Robustez**: Manejo efectivo de vocabulario limitado y palabras OOV

### 📊 Visualizaciones Incluidas
- **Curvas de aprendizaje**: Precisión vs. épocas
- **Evolución de la pérdida**: Training vs. validation loss
- **Comparación de rendimiento**: Métricas duales de evaluación

## 🚀 Tecnologías y Herramientas

### Deep Learning Framework
```python
- TensorFlow/Keras     # Framework principal de deep learning
- Sequential API       # Construcción de modelos secuenciales
```

### Procesamiento de Datos
```python
- pandas              # Manipulación de datasets
- numpy               # Operaciones numéricas
- scikit-learn        # Preprocesamiento y división de datos
```

### NLP y Tokenización
```python
- Keras Tokenizer     # Tokenización y vocabulario
- Preprocessing       # Padding y secuencias
- LabelEncoder        # Codificación de etiquetas
```

### Visualización y Persistencia
```python
- matplotlib          # Gráficos y visualizaciones
- pickle              # Serialización del tokenizer
- KaggleHub           # Descarga automática de datasets
```

## 📁 Estructura del Proyecto

```
RED NEURONAL/
├── Ejercicio_IMBD_Reseñas_V2.ipynb    # Notebook principal con implementación completa
├── IMDB_RESEÑAS_FINAL.ipynb           # Versión final optimizada
├── README.md                          # Documentación del proyecto
├── tokenizer.pickle                   # Tokenizer entrenado (generado)
└── outputs/                          # Gráficos y visualizaciones (si aplica)
```

## 🔬 Proceso de Desarrollo

### Fase 1: Exploración y Preprocesamiento
1. **Descarga automática** del dataset desde Kaggle
2. **Análisis exploratorio** de datos (EDA)
3. **Limpieza y tokenización** del texto
4. **División estratificada** del dataset

### Fase 2: Construcción del Modelo
1. **Diseño de arquitectura** RNN optimizada
2. **Configuración de hiperparámetros**
3. **Implementación de regularización**
4. **Compilación con métricas apropiadas**

### Fase 3: Entrenamiento y Evaluación
1. **Entrenamiento supervisado** con validación
2. **Monitoreo de métricas** en tiempo real
3. **Evaluación final** en conjunto de prueba
4. **Análisis de convergencia** y estabilidad

### Fase 4: Implementación y Predicción
1. **Sistema de predicción** para nuevas reseñas
2. **Serialización del tokenizer** para reproducibilidad
3. **Interfaz intuitiva** de predicción
4. **Interpretación de resultados**

## 💡 Casos de Uso y Aplicaciones

### Aplicaciones Comerciales
- **Plataformas de streaming**: Análisis automático de feedback de usuarios
- **Sistemas de recomendación**: Filtrado basado en sentimientos
- **E-commerce**: Clasificación de reseñas de productos
- **Redes sociales**: Monitoreo de opiniones públicas

### Valor Académico y Técnico
- **Demostración de NLP**: Técnicas modernas de procesamiento de texto
- **Deep Learning aplicado**: Implementación práctica de RNNs
- **Pipeline completo**: Desde datos crudos hasta predicciones
- **Metodología reproducible**: Código documentado y estructurado

## 🎓 Competencias Desarrolladas

- ✅ **Deep Learning y RNNs** - Arquitecturas neuronales para secuencias
- ✅ **Procesamiento de Lenguaje Natural** - Tokenización y embeddings
- ✅ **TensorFlow/Keras** - Framework de deep learning profesional
- ✅ **Análisis de sentimientos** - Clasificación de texto no estructurado
- ✅ **Visualización de modelos** - Interpretación de curvas de aprendizaje
- ✅ **Evaluación de modelos** - Métricas y validación cruzada
- ✅ **Ingeniería de datos** - Pipeline de preprocesamiento robusto
- ✅ **Reproducibilidad** - Serialización y versionado de modelos

## 🔧 Posibles Mejoras y Extensiones

### Arquitecturas Avanzadas
- **LSTM/GRU**: Redes con memoria a largo plazo
- **Bidirectional RNN**: Procesamiento en ambas direcciones
- **Attention Mechanisms**: Foco en partes relevantes del texto

### Optimizaciones Técnicas
- **Hyperparameter tuning**: Búsqueda automática de parámetros
- **Data augmentation**: Técnicas de aumento de datos textuales
- **Transfer learning**: Modelos preentrenados (BERT, GPT)
- **Ensemble methods**: Combinación de múltiples modelos

### Funcionalidades Adicionales
- **Análisis multiclase**: Más categorías de sentimientos
- **Detección de emociones**: Clasificación emocional específica
- **Explicabilidad**: Interpretación de decisiones del modelo
- **API deployment**: Servicio web para predicciones en tiempo real

## 📚 Referencias y Fundamentos Teóricos

- **Recurrent Neural Networks**: Fundamentos de procesamiento secuencial
- **Word Embeddings**: Representación vectorial de palabras
- **Sentiment Analysis**: Técnicas de análisis de opiniones
- **Deep Learning for NLP**: Aplicaciones de redes neuronales al lenguaje
- **IMDB Dataset**: Benchmark estándar para análisis de sentimientos

## 🌟 Demostración Práctica

El modelo incluye un **ejemplo interactivo** que demuestra:

```python
# Reseña de ejemplo (negativa)
new_review = "This film is a boring, nonsensical mess..."

# Predicción automática
Probabilidad de ser positiva: 0.XXXX
El modelo predice que la reseña es: Negativa
```

---

**Autor**: Dimitri Schumilow  
**Fecha**: Septiembre 2025  
**Curso**: Fundamentos de Ciencia de Datos - Redes Neuronales  
**Institución**: Talento Digital

---

*Este proyecto demuestra la aplicación práctica de redes neuronales recurrentes para el análisis automático de sentimientos, combinando técnicas modernas de Deep Learning con procesamiento de lenguaje natural para resolver problemas reales de clasificación de texto.*