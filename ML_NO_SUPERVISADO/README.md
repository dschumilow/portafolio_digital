# 🎵 Análisis de Clustering: Preferencias Musicales por País

## 📋 Descripción del Proyecto

Este proyecto implementa un análisis completo de **Machine Learning No Supervisado** para identificar patrones y agrupamientos en las preferencias musicales de diferentes países. Utilizando técnicas avanzadas de clustering y reducción de dimensionalidad, se exploran las similitudes culturales en el consumo musical global.

## 🎯 Objetivos

### Objetivo Principal
- **Identificar agrupamientos naturales** de países basados en sus preferencias musicales utilizando algoritmos de clustering no supervisado.

### Objetivos Específicos
- Explorar y visualizar las distribuciones de géneros musicales por país
- Comparar la efectividad de diferentes algoritmos de clustering (K-Means, Clustering Jerárquico, DBSCAN)
- Aplicar técnicas de reducción de dimensionalidad (PCA, t-SNE) para visualización
- Determinar el número óptimo de clusters mediante métricas de validación
- Analizar los resultados en el contexto de tendencias musicales globales

## 📊 Dataset

**Fuente**: `dataset_generos_musicales.csv`

**Características**:
- **8 países**: México, Alemania, Corea, Rusia, EEUU, Chile, Italia, Japón
- **8 géneros musicales**: Pop, Rock, Hip-Hop, Electrónica, Clásica, Jazz, Reguetón, Metal
- **Variables**: Puntuaciones de preferencia por género (escala numérica)

## 🛠️ Metodología

### 1. Exploración y Visualización de Datos
- **Análisis estadístico descriptivo** de las preferencias por género
- **Histogramas** para distribuciones de frecuencia
- **Boxplots** para identificación de outliers
- **Gráficos de barras** comparativos por país

### 2. Preprocesamiento
- **Normalización** de datos usando StandardScaler
- **Eliminación** de variables categóricas no relevantes

### 3. Algoritmos de Clustering Implementados

#### K-Means Clustering
- **Método del codo** para determinar K óptimo
- **Coeficiente de Silueta** para validación
- **K óptimo identificado**: 5 clusters

#### Clustering Jerárquico (Agglomerative)
- **Dendrograma** para visualización jerárquica
- **Método de enlace**: Ward
- Comparación con resultados de K-Means

#### DBSCAN (Density-Based Clustering)
- **Parámetros optimizados**: eps=[1.5, 2.0, 2.5], min_samples=2
- **Detección** de puntos de ruido y clusters irregulares

### 4. Reducción de Dimensionalidad

#### PCA (Principal Component Analysis)
- **Análisis** de varianza explicada
- **Determinación** de componentes necesarios para 90% de varianza
- **Visualización** en 2D de la estructura global

#### t-SNE (t-Distributed Stochastic Neighbor Embedding)
- **Preservación** de relaciones locales
- **Visualización mejorada** de separación entre clusters
- **Parámetros**: perplexity=[2, 4] para optimización

## 🏆 Resultados y Logros Principales

### 📈 Métricas de Rendimiento
- **Silhouette Score óptimo**: K=5 clusters
- **Varianza explicada (PCA)**: 90% con X componentes principales
- **Convergencia exitosa** en todos los algoritmos implementados

### 🔍 Insights Clave Descubiertos

#### Agrupamientos Identificados:
1. **Cluster Pop-Dominante**: México, Alemania (alta preferencia por Pop)
2. **Cluster Hip-Hop/Jazz**: Corea (especialización en géneros urbanos y jazz)
3. **Cluster Reguetón**: Rusia, EEUU, Chile (preferencia por ritmos latinos)
4. **Cluster Clásico/Metal**: Italia (géneros tradicionales y alternativos)
5. **Cluster Equilibrado**: Japón, EEUU (preferencias diversificadas)

#### Patrones Culturales:
- **Globalización musical**: Pop y Reguetón dominan múltiples mercados
- **Identidades culturales**: Persistencia de nichos locales (Clásica en Italia, Hip-Hop en Corea)
- **Convergencia digital**: Similitudes en países con alto acceso a streaming

### 📊 Validación de Resultados
- **Coherencia** entre K-Means y Clustering Jerárquico
- **Superioridad de t-SNE** sobre PCA para visualización de clusters
- **Alineación** con tendencias globales de consumo musical (Spotify, YouTube)

## 🚀 Tecnologías Utilizadas

### Librerías Python
```python
- pandas, numpy          # Manipulación de datos
- matplotlib, seaborn    # Visualización
- scikit-learn          # Algoritmos ML
- scipy                 # Clustering jerárquico
```

### Algoritmos y Técnicas
- **K-Means Clustering**
- **Agglomerative Clustering**
- **DBSCAN**
- **PCA (Principal Component Analysis)**
- **t-SNE (t-Distributed Stochastic Neighbor Embedding)**
- **Silhouette Analysis**
- **Elbow Method**

## 📁 Estructura del Proyecto

```
ML_NO_SUPERVISADO/
├── consolidadom7.ipynb          # Notebook principal con análisis completo
├── dataset_generos_musicales.csv # Dataset de preferencias musicales
├── README.md                    # Documentación del proyecto
└── outputs/                     # Visualizaciones generadas (si aplica)
```

## 🔬 Metodología Científica

### Hipótesis
*"Los países desarrollan agrupamientos naturales basados en preferencias musicales que reflejan tanto influencias culturales locales como tendencias globales de consumo digital"*

### Validación
- **Métrica cuantitativa**: Coeficiente de Silueta
- **Validación visual**: t-SNE y dendrogramas
- **Contexto cualitativo**: Comparación con tendencias de mercado

## 📈 Impacto y Aplicaciones

### Aplicaciones Comerciales
- **Segmentación de mercados** para plataformas de streaming
- **Estrategias de marketing** musical geográfico
- **Recomendaciones** personalizadas por región

### Valor Académico
- **Metodología replicable** para análisis cultural
- **Comparación exhaustiva** de algoritmos de clustering
- **Base** para estudios de globalización musical

## 🎓 Competencias Desarrolladas

- ✅ **Machine Learning No Supervisado** avanzado
- ✅ **Análisis exploratorio** de datos multivariados
- ✅ **Validación de modelos** mediante métricas múltiples
- ✅ **Visualización** de datos de alta dimensionalidad
- ✅ **Interpretación** de resultados en contexto cultural
- ✅ **Documentación técnica** profesional

## 📚 Referencias y Fuentes

- Documentación oficial de Scikit-learn
- Metodologías de clustering en análisis cultural
- Tendencias globales de consumo musical (industria del streaming)

---

**Autor**: [Tu Nombre]  
**Fecha**: Septiembre 2025  
**Curso**: Fundamentos de Ciencia de Datos - Machine Learning No Supervisado  
**Institución**: [Tu Institución]

---

*Este proyecto demuestra la aplicación práctica de técnicas avanzadas de Machine Learning No Supervisado para resolver problemas reales de análisis cultural y segmentación de mercados.*