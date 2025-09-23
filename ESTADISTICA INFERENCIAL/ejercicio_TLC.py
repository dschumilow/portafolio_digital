import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import gamma
import seaborn as sns

"""
DEMOSTRACIÓN DEL TEOREMA CENTRAL DEL LÍMITE (TLC)

Este ejercicio demuestra cómo las medias muestrales de una población con distribución 
sesgada tienden a seguir una distribución normal conforme aumenta el tamaño de la muestra.

OBJETIVO:
- Simular una población con distribución gamma (sesgada a la derecha)
- Extraer múltiples muestras y calcular sus medias
- Verificar que la distribución de medias muestrales es aproximadamente normal
- Comparar el error estándar empírico con el teórico
"""

np.random.seed(42)  # Para reproducibilidad de resultados

# Parámetros de la población sesgada
mu = 150    # Media poblacional deseada
sigma = 20  # Desviación estándar poblacional deseada

# Para una distribución GAMMA: E[X] = alpha * beta, Var[X] = alpha * beta^2
# Calculamos los parámetros alpha y beta para obtener mu y sigma deseados
alpha = (mu/sigma)**2    # Parámetro de forma
beta = (sigma**2)/mu     # Parámetro de escala

# Generar población sesgada con distribución Gamma
poblacion_sesgada = gamma.rvs(a=alpha, scale=beta, size=100000)
# rvs: Random Variates Sampling - Generación de Variables Aleatorias

# Visualización de la población y distribución muestral
plt.figure(figsize=(14,8))

# Gráfico 1: Distribución poblacional (sesgada)
plt.subplot(1,2,1)
sns.histplot(poblacion_sesgada, kde=True, color='orange', bins=50)
plt.title(f'Distribución poblacional (sesgada a la derecha)\n'
          f'Media = {np.mean(poblacion_sesgada):.1f} gr, '
          f'σ = {np.std(poblacion_sesgada):.1f} gr')
plt.xlabel('Peso manzana (gr)')
plt.ylabel('Frecuencia')
plt.axvline(mu, color='brown', linestyle='--', label='Media poblacional')
plt.legend()

# Simulación de la distribución muestral de la media
numero_muestra = 5000    # Número de muestras a extraer
tam_muestra_tlc = 30     # Tamaño de cada muestra
media_muestral_tlc = []  # Lista para almacenar las medias muestrales

# Extraer múltiples muestras y calcular sus medias
for _ in range(numero_muestra):
    muestra = np.random.choice(poblacion_sesgada, tam_muestra_tlc, replace=True)
    media_muestral_tlc.append(np.mean(muestra))

# Gráfico 2: Distribución muestral de la media (aproximadamente normal)
plt.subplot(1,2,2)
sns.histplot(media_muestral_tlc, kde=True, color='purple', bins=30)
plt.title(f'Distribución muestral de la media (n={tam_muestra_tlc})\n'
          f'Distribución aproximadamente normal')
plt.xlabel('Media muestral (gr)')
plt.ylabel('Frecuencia')
plt.axvline(mu, color='brown', linestyle='--', label='Media poblacional')
plt.legend()

plt.tight_layout()  # Ajustar automáticamente el espaciado entre gráficos
plt.show()

# Estadísticas comparativas
print("="*70)
print("VERIFICACIÓN DEL TEOREMA CENTRAL DEL LÍMITE")
print("="*70)
print(f'Media de la población simulada: {np.mean(poblacion_sesgada):.2f} gr')
print(f'Desv. estándar de la población: {np.std(poblacion_sesgada):.2f} gr')
print(f'Media de las medias muestrales (empírica): {np.mean(media_muestral_tlc):.2f} gr')
print(f'Error estándar empírico: {np.std(media_muestral_tlc):.2f} gr')
print(f'Error estándar teórico (σ/√n): {sigma/np.sqrt(tam_muestra_tlc):.2f} gr')

"""
RESULTADOS OBTENIDOS:

1. TRANSFORMACIÓN DE LA DISTRIBUCIÓN:
   - La población original tiene una distribución Gamma (sesgada a la derecha)
   - Las medias muestrales siguen una distribución aproximadamente normal
   - Esto confirma el TLC: independientemente de la forma de la población original,
     la distribución de medias muestrales tiende a la normalidad

2. CENTRADO EN LA MEDIA POBLACIONAL:
   - La media de las medias muestrales ≈ media poblacional (150 gr)
   - Esto demuestra que el estimador es insesgado: E[X̄] = μ

3. REDUCCIÓN DE LA VARIABILIDAD:
   - El error estándar empírico coincide muy bien con el teórico (σ/√n)
   - La variabilidad de las medias muestrales es menor que la poblacional
   - Con n=30, el error estándar se reduce a ~3.65 gr vs 20 gr poblacional

4. APLICACIÓN PRÁCTICA:
   - Podemos hacer inferencias sobre poblaciones no normales usando estadística normal
   - Las medias muestrales son más estables y predecibles que valores individuales
   - Fundamental para intervalos de confianza y pruebas de hipótesis

CONCLUSIÓN:
El TLC permite aplicar métodos estadísticos basados en la distribución normal 
incluso cuando trabajamos con poblaciones que no siguen esta distribución,
siempre que el tamaño de muestra sea suficientemente grande (n≥30).
"""

