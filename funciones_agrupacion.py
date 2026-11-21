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

# 73. Filtrar mediante expresión en cadena con query (evita repetir el nombre del DataFrame)
consulta = df.query("grupo == 'A' and nota > 8.5")
print("--- 73. Consulta query ---\n", consulta)

# 74. Combinar columnas conservando la serie cuya suma total sea menor
df_a = pd.DataFrame({"c1": [10, 20], "c2": [5, 5]})
df_b = pd.DataFrame({"c1": [15, 25], "c2": [1, 2]})
df_combinado_min = df_a.combine(df_b, lambda s1, s2: s1 if s1.sum() < s2.sum() else s2)
print("\n--- 74. Combinación por suma mínima ---\n", df_combinado_min)

# 75. Aplicar función vectorizada por columnas (axis=0) con apply
df_cuadrado = df_num.apply(lambda col: col ** 2, axis=0)
print("\n--- 75. Cuadrado con apply ---\n", df_cuadrado)

# 76. Formatear celda a celda con DataFrame.map() (sustituto actual de applymap)
df_formateado = df_num.map(lambda val: f"{val:.2f}")
print("\n--- 76. Formato texto elemento a elemento ---\n", df_formateado)

# 77. Sustituir categorías de una Series mediante diccionario en map
df["grupo"] = df["grupo"].map({"A": "Alpha", "B": "Beta"})

# 78. Agrupar por categoría y contar registros por grupo con size() (refleja el cambio de 77)
conteo_por_grupo = df.groupby("grupo").size()
print("\n--- 78. Conteo por grupo ---\n", conteo_por_grupo)

# 79. Calcular múltiples estadísticos por columna (axis=0) en una sola pasada con agg
resumen_agg = df_num.agg(["sum", "mean", "std"], axis=0)
print("\n--- 79. Resumen múltiple agg ---\n", resumen_agg)

# 80. Filtrar registros que cumplen el umbral mínimo mediante máscara booleana
df_aprobados = df[df["nota"] >= 7.0].copy()
print("\n--- 80. Registros aprobados ---\n", df_aprobados)

# 81. Agrupar por categoría y calcular la media de las variables numéricas
promedio_por_grupo = df.groupby("grupo")[["edad", "nota"]].mean()
print("\n--- 81. Promedio por grupo ---\n", promedio_por_grupo)

# 82. Evaluar cuantificadores lógicos por columna: todos (all) y al menos uno (any)
todos_positivos = (df_num > 0).all()
algun_positivo = (df_num > 0).any()
print("\n--- 82. Cuantificadores all / any ---\n", todos_positivos, "\n", algun_positivo)

# 83. Calcular el máximo por columna (axis=0) y por fila (axis=1)
max_columna = df_num.max(axis=0)
max_fila = df_num.max(axis=1)
print("\n--- 83. Máximo por columna y fila ---\n", max_columna, "\n", max_fila)

# 84. Calcular media y mediana por columna (axis=0) y por fila (axis=1)
media_col, media_fila = df_num.mean(axis=0), df_num.mean(axis=1)
mediana_col, mediana_fila = df_num.median(axis=0), df_num.median(axis=1)
print("\n--- 84. Media y mediana (col / fila) ---\n", media_col, "\n", media_fila, "\n", mediana_col, "\n", mediana_fila)

# 85. Calcular el mínimo por columna (axis=0) y por fila (axis=1)
min_columna = df_num.min(axis=0)
min_fila = df_num.min(axis=1)
print("\n--- 85. Mínimo por columna y fila ---\n", min_columna, "\n", min_fila)

# 86. Redondear valores flotantes a un decimal con round()
df_redondeado = df_num.round(1)
print("\n--- 86. Valores redondeados ---\n", df_redondeado)

# 87. Sumar todos los valores de una columna individual
suma_notas = df["nota"].sum()
print("\n--- 87. Suma de notas ---\n", suma_notas)

# 88. Calcular la media aritmética de una columna individual
promedio_notas = df["nota"].mean()
print("\n--- 88. Promedio de notas ---\n", promedio_notas)

# 89. Calcular el módulo (valor absoluto |x|) de cada entrada de la matriz
df_modulo = df_num.abs()
print("\n--- 89. Módulo matricial ---\n", df_modulo)

# 90. Calcular el producto punto alineando columnas del primero con el índice del segundo
df_matriz_b = pd.DataFrame({"p1": [1.0, 0.5], "p2": [0.0, 2.0]}, index=["x", "y"])
producto_punto = df_num.dot(df_matriz_b)
print("\n--- 90. Producto punto ---\n", producto_punto)

# 91. Transponer filas por columnas mediante el atributo T
df_transpuesta = df_num.T
print("\n--- 91. Matriz transpuesta ---\n", df_transpuesta)

# 92. Comparar elemento a elemento dos DataFrames homólogos con operadores relacionales
df_referencia = pd.DataFrame({"x": [0.0, 0.0, 0.0], "y": [0.0, 0.0, 0.0]})
comparacion_relacional = df_num > df_referencia
print("\n--- 92. Comparación relacional ---\n", comparacion_relacional)

# 93. Verificar igualdad exacta de estructura, etiquetas y valores con equals()
son_identicos = df_num.equals(df_num.copy())
print("\n--- 93. Igualdad exacta ---\n", son_identicos)