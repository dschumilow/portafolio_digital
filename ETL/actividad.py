import pandas as pd

# Cargar el archivo CSV con los datos de ventas
df = pd.read_csv(r'C:\Users\dschu\OneDrive\Documentos\CursoCienciasDeDatos\M3\s4\ventas.csv')
df

# Mostrar información general del DataFrame (tipos de datos, valores nulos, etc.)
df.info()

# Verificar duplicados y valores nulos
print(df.duplicated())      # Muestra qué filas están duplicadas
print(df.isna().sum())      # Muestra el conteo de valores nulos por columna

# Eliminar filas duplicadas
df_sin_duplicados = df.drop_duplicates()
df_sin_duplicados

# Imputar valores nulos en la columna 'Precio' con el promedio de la columna
df_sin_duplicados['Precio'].fillna(df.Precio.mean(), inplace=True)
df_sin_duplicados

# Eliminar cualquier fila que aún tenga valores nulos
df_final = df_sin_duplicados.dropna()

# Reiniciar el índice del DataFrame final
df_final.reset_index(drop=True, inplace=True)

df_final

# Calcular los límites para detectar outliers en la columna 'Cantidad' usando el rango intercuartílico (IQR)
Q1 = df_final['Cantidad'].quantile(0.25)
Q3 = df_final['Cantidad'].quantile(0.75)
IQR = Q3 - Q1

limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

# Identificar filas que son outliers en la columna 'Cantidad'
outliers = df_final[(df_final['Cantidad'] < limite_inferior) | (df_final['Cantidad'] > limite_superior)]

print(outliers)

# Corregir manualmente los valores de 'Cantidad' en las filas 5 y 6
df_final.loc[[5, 6], 'Cantidad'] = [5, 6]

print(df_final)