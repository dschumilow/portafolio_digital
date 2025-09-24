# 🧼 Limpieza y preparación de datos con pandas

Este repositorio contiene un ejercicio práctico de limpieza de datos utilizando Python y la biblioteca pandas. El objetivo es aplicar técnicas fundamentales para transformar un conjunto de datos crudo en un DataFrame limpio y listo para análisis.

## 🎯 Objetivos del ejercicio

- 📥 **Carga de datos**: Importar un archivo CSV con información de ventas.
- 🔍 **Exploración inicial**:
  - Inspeccionar la estructura del DataFrame (`df.info()`).
  - Detectar valores nulos y filas duplicadas.
- 🧹 **Limpieza de datos**:
  - Eliminar duplicados para evitar sesgos.
  - Imputar valores nulos en la columna `Precio` usando el promedio.
  - Eliminar filas con valores nulos restantes.
  - Reiniciar el índice del DataFrame final.
- 📊 **Detección de outliers**:
  - Calcular el rango intercuartílico (IQR) para la columna `Cantidad`.
  - Identificar valores atípicos fuera de los límites definidos.
  - Corregir manualmente ciertos valores extremos.
- ✅ **Preparación del dataset final**:
  - Obtener un DataFrame limpio, sin duplicados, sin nulos y sin outliers, listo para análisis posteriores.

## 📚 Contexto del ejercicio

Este ejercicio forma parte del módulo 3, sesión 4 del curso de Ciencias de Datos. El dataset simula registros de ventas y permite aplicar técnicas esenciales de preprocesamiento antes de realizar análisis descriptivos o modelos predictivos.

El objetivo pedagógico es fortalecer la capacidad de:

- Identificar y corregir problemas comunes en datasets reales.
- Aplicar buenas prácticas de manipulación de datos con pandas.
- Preparar un conjunto de datos confiable para futuras etapas del pipeline de ciencia de datos.

Este ejercicio también contribuye a consolidar el portafolio profesional, mostrando dominio técnico, claridad metodológica y capacidad de aplicar herramientas analíticas en contextos prácticos.

---
