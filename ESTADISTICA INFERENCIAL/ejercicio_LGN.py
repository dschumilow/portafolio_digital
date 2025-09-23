import numpy as np
import matplotlib.pyplot as plt

"""
DEMOSTRACIÓN DE LA LEY DE LOS GRANDES NÚMEROS (LGN)

Este ejercicio demuestra cómo la media de una muestra se aproxima a la media poblacional 
conforme aumenta el tamaño de la muestra, según establece la Ley de los Grandes Números.

OBJETIVO:
- Simular el peso de manzanas con distribución normal
- Calcular medias acumulativas para diferentes tamaños de muestra
- Visualizar la convergencia hacia la media poblacional
"""

# Parámetros de la población de manzanas
mu_poblacional = 150      # Media poblacional: 150 gramos
sigma_poblacional = 20    # Desviación estándar poblacional: 20 gramos

# Tamaños de muestra a evaluar
numero_muestra_lgn = [10, 100, 500, 1000, 5000, 10000]
medias_acumuladas = []

# Generar observaciones de pesos de manzanas con distribución normal
np.random.seed(42)  # Para reproducibilidad de resultados
observaciones_manzanas = np.random.normal(loc=mu_poblacional, scale=sigma_poblacional, size=10000)

# Calcular medias acumulativas
suma = 0
contador = 0

for i in range(len(observaciones_manzanas)):
    suma += observaciones_manzanas[i]
    contador += 1
    media_actual = suma / contador
    medias_acumuladas.append(media_actual)

# Visualización de la convergencia
plt.figure(figsize=(12, 8)) 
plt.plot(medias_acumuladas, label='Medias acumuladas de pesos de manzana', linewidth=2)
plt.axhline(mu_poblacional, color='red', linestyle="--", linewidth=2, 
            label=f'Media poblacional = {mu_poblacional} gr')

# Configuración del gráfico
plt.xlabel('Tamaño de la muestra (escala logarítmica)', fontsize=12)
plt.ylabel('Media acumulada (gramos)', fontsize=12)
plt.title('Demostración de la Ley de los Grandes Números\nConvergencia de la media muestral hacia la media poblacional', 
          fontsize=14, fontweight='bold')
plt.xscale('log')  # Escala logarítmica para ver mejor la convergencia
plt.grid(True, alpha=0.3)
plt.legend(fontsize=12)
plt.ylim([140, 160])  # Limitar el eje y para mejor visualización

# Mostrar valores específicos en ciertos tamaños de muestra
for n in numero_muestra_lgn:
    if n <= len(medias_acumuladas):
        plt.annotate(f'n={n}\nμ={medias_acumuladas[n-1]:.2f}', 
                    xy=(n, medias_acumuladas[n-1]), 
                    xytext=(n*1.5, medias_acumuladas[n-1]+2),
                    arrowprops=dict(arrowstyle='->', alpha=0.7),
                    fontsize=10, ha='center')

plt.tight_layout()
plt.show()

"""
RESULTADOS OBTENIDOS:

1. CONVERGENCIA: La gráfica muestra claramente cómo la media muestral se acerca 
   progresivamente a la media poblacional (150 gr) conforme aumenta el tamaño de la muestra.

2. VARIABILIDAD INICIAL: Con muestras pequeñas (n<100), la media muestral presenta 
   mayor variabilidad y puede alejarse significativamente de la media poblacional.

3. ESTABILIZACIÓN: A partir de muestras grandes (n>1000), la media se estabiliza 
   muy cerca del valor poblacional, con fluctuaciones mínimas.

4. VALIDACIÓN DE LA LGN: Este experimento confirma empíricamente la Ley de los 
   Grandes Números, demostrando que lim(n→∞) X̄ₙ = μ.

CONCLUSIÓN:
La simulación demuestra que necesitamos muestras suficientemente grandes para obtener 
estimaciones confiables de parámetros poblacionales. En este caso, con n≥1000 
obtenemos estimaciones estables del peso promedio de las manzanas.
"""

# Estadísticas finales
print("="*60)
print("ESTADÍSTICAS FINALES")
print("="*60)
print(f"Media poblacional real: {mu_poblacional} gramos")
print(f"Media muestral final (n=10000): {medias_acumuladas[-1]:.4f} gramos")
print(f"Error absoluto: {abs(medias_acumuladas[-1] - mu_poblacional):.4f} gramos")
print(f"Error relativo: {abs(medias_acumuladas[-1] - mu_poblacional)/mu_poblacional*100:.4f}%")
