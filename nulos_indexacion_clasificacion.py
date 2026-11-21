import numpy as np
import pandas as pd

df = pd.DataFrame({
    "id": [103, 101, 104, 102],
    "nombre": ["Eva", "Ana", np.nan, "Luis"],
    "edad": [27, 23, 30, 23],
    "nota": [9.2, np.nan, 6.8, 8.5],
})

# --- Gestión de valores nulos ---

# 61. Filtrar registros con valores ausentes (NaN) en "nota" mediante máscara booleana
filas_nota_nula = df[df["nota"].isna()]
print("--- 61. Filas con nota nula ---\n", filas_nota_nula)

# 62. Contar nulos por columna (axis=0) y obtener el acumulado total de la tabla
nulos_por_columna = df.isna().sum()
total_nulos = df.isna().sum().sum()
print("\n--- 62. Conteo de nulos (por columna / total) ---\n", nulos_por_columna, "\nTotal:", total_nulos)

# 63. Generar matriz booleana marcando como True las celdas nulas (NaN)
mascara_nulos = df.isna()
print("\n--- 63. Máscara de valores nulos ---\n", mascara_nulos)

# 64. Generar matriz booleana inversa marcando como True los datos válidos
mascara_no_nulos = df.notna()
print("\n--- 64. Máscara de valores no nulos ---\n", mascara_no_nulos)

# 65. Imputar nulos por columna con diccionario para conservar el tipo de dato de cada serie
df_imputado = df.fillna({"nombre": "Desconocido", "nota": 0.0})

# --- Indexación ---

# 66. Reordenar filas de forma descendente según las etiquetas de su índice (refleja imputación de 65)
df_indice_ordenado = df_imputado.sort_index(ascending=False)
print("\n--- 66. Índice ordenado descendente ---\n", df_indice_ordenado)

# 67. Promover la columna "id" como nuevo índice explícito de filas
df_indexado = df_imputado.set_index("id")
print("\n--- 67. Columna 'id' como índice ---\n", df_indexado)

# 68. Asignar etiquetas arbitrarias al eje de filas sobrescribiendo el atributo index
df_indexado.index = ["reg_c", "reg_a", "reg_d", "reg_b"]

# 69. Convertir el índice actual en columna regular y restaurar RangeIndex (refleja etiquetas de 68)
df_con_columna_indice = df_indexado.reset_index()
print("\n--- 69. Índice convertido a columna ---\n", df_con_columna_indice)

# 70. Eliminar una fila y reconstruir índice numérico contiguo descartando el previo (drop=True)
df_filtrado = df_imputado.drop(index=1)
df_reiniciado = df_filtrado.reset_index(drop=True)
print("\n--- 70. Índice reiniciado tras eliminar fila ---\n", df_reiniciado)

# --- Ordenación y clasificación ---

# 71. Ordenar registros de forma descendente según los valores de "nota"
df_ordenado_nota = df_reiniciado.sort_values(by="nota", ascending=False)
print("\n--- 71. Ordenado por nota descendente ---\n", df_ordenado_nota)

# 72. Ordenar lexicográficamente por "edad" ascendente y desempatar por "nota" descendente
df_ordenado_multiple = df_reiniciado.sort_values(
    by=["edad", "nota"], ascending=[True, False]
)
print("\n--- 72. Ordenado por edad y nota ---\n", df_ordenado_multiple)