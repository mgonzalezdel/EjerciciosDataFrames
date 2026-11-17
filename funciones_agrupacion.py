import numpy as np
import pandas as pd

df = pd.DataFrame({
    "grupo": ["A", "B", "A", "B"],
    "edad": [22, 31, 25, 29],
    "nota": [8.456, 6.234, 9.128, 7.891],
})

df_num = pd.DataFrame({
    "x": [-2.456, 4.123, -6.789],
    "y": [3.512, -5.987, 8.341],
})

# 73. Filtrar registros mediante expresión booleana en cadena con query (evita repetir el nombre del DataFrame)
consulta = df.query("grupo == 'A' and nota > 8.5")

# 74. Combinar dos DataFrames columna a columna conservando la serie cuya suma total sea menor
df_a = pd.DataFrame({"c1": [10, 20], "c2": [5, 5]})
df_b = pd.DataFrame({"c1": [15, 25], "c2": [1, 2]})
df_combinado_min = df_a.combine(df_b, lambda s1, s2: s1 if s1.sum() < s2.sum() else s2)

# 75. Aplicar una función a lo largo de un eje (axis=0 por columnas) mediante apply
df_cuadrado = df_num.apply(lambda col: col ** 2, axis=0)

# 76. Aplicar una transformación elemento a elemento para formatear valores como texto
# Nota: DataFrame.map() reemplaza al deprecado applymap() en versiones modernas de Pandas (>= 2.1)
df_formateado = df_num.map(lambda val: f"{val:.2f}")

# 77. Mapear y sustituir los valores de una columna (Series) usando un diccionario de correspondencia
df["grupo"] = df["grupo"].map({"A": "Alpha", "B": "Beta"})

# 78. Agrupar por categoría y contabilizar el número de registros por cada grupo con size()
conteo_por_grupo = df.groupby("grupo").size()

# 79. Calcular múltiples métricas de agregación simultáneamente sobre el eje de filas (axis=0) con agg
resumen_agg = df_num.agg(["sum", "mean", "std"], axis=0)

# 80. Descartar registros que no satisfacen el umbral mínimo filtrando mediante máscara booleana
df_aprobados = df[df["nota"] >= 7.0].copy()

# 81. Agrupar por columna categórica y calcular la media aritmética de las variables numéricas
promedio_por_grupo = df.groupby("grupo")[["edad", "nota"]].mean()

# 82. Evaluar cuantificadores lógicos por columna: all() exige que todos cumplan; any() que al menos uno cumpla
todos_positivos = (df_num > 0).all()
algun_positivo = (df_num > 0).any()

# 83. Obtener el valor máximo por columna (axis=0) y por fila (axis=1)
max_columna = df_num.max(axis=0)
max_fila = df_num.max(axis=1)

# 84. Calcular media y mediana tanto verticalmente por columna (axis=0) como horizontalmente por fila (axis=1)
media_col, media_fila = df_num.mean(axis=0), df_num.mean(axis=1)
mediana_col, mediana_fila = df_num.median(axis=0), df_num.median(axis=1)

# 85. Obtener el valor mínimo por columna (axis=0) y por fila (axis=1)
min_columna = df_num.min(axis=0)
min_fila = df_num.min(axis=1)

# 86. Redondear los valores de punto flotante a una cifra decimal específica con round()
df_redondeado = df_num.round(1)

# 87. Calcular la suma acumulada de todos los elementos de una columna individual
suma_notas = df["nota"].sum()

# 88. Calcular la media aritmética de los elementos de una columna individual
promedio_notas = df["nota"].mean()

# 89. Calcular el módulo (valor absoluto |x|) de cada entrada de la matriz numérica (para resto aritmético: df_num % 2)
df_modulo = df_num.abs()

# 90. Calcular el producto matricial (producto punto) alineando columnas del primero con el índice del segundo
df_matriz_b = pd.DataFrame({"p1": [1.0, 0.5], "p2": [0.0, 2.0]}, index=["x", "y"])
producto_punto = df_num.dot(df_matriz_b)

# 91. Transponer filas por columnas mediante el atributo T (alias directo de transpose())
df_transpuesta = df_num.T

# 92. Comparar elemento a elemento dos DataFrames homólogos con operadores relacionales devolviendo una matriz booleana
df_referencia = pd.DataFrame({"x": [0.0, 0.0, 0.0], "y": [0.0, 0.0, 0.0]})
comparacion_relacional = df_num > df_referencia

# 93. Verificar igualdad estructural y de valores exactos (incluyendo posición de NaN y etiquetas) con equals()
son_identicos = df_num.equals(df_num.copy())
