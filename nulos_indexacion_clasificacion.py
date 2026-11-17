import numpy as np
import pandas as pd

df = pd.DataFrame({
    "id": [103, 101, 104, 102],
    "nombre": ["Eva", "Ana", np.nan, "Luis"],
    "edad": [27, 23, 30, 23],
    "nota": [9.2, np.nan, 6.8, 8.5],
})

# --- Gestión de valores nulos ---

# 61. Filtrar los registros donde "nota" presenta valores ausentes (NaN) mediante indexación booleana
filas_nota_nula = df[df["nota"].isna()]

# 62. Contar los elementos nulos por columna (axis=0) y obtener el acumulado total en todo el DataFrame
nulos_por_columna = df.isna().sum()
total_nulos = df.isna().sum().sum()

# 63. Evaluar celda a celda qué elementos son nulos devolviendo un DataFrame booleano (True en posiciones NaN)
mascara_nulos = df.isna()

# 64. Evaluar la condición inversa con notna() para identificar celdas con datos válidos disponibles
mascara_no_nulos = df.notna()

# 65. Imputar valores nulos con fillna() usando un diccionario por columna para preservar la coherencia de tipos
df_imputado = df.fillna({"nombre": "Desconocido", "nota": 0.0})

# --- Indexación ---

# 66. Reordenar las filas según las etiquetas de su índice (ascending=False invierte el orden actual)
df_indice_ordenado = df_imputado.sort_index(ascending=False)

# 67. Promover la columna "id" como nuevo índice explícito para habilitar búsquedas directas por clave
df_indexado = df_imputado.set_index("id")

# 68. Sobrescribir el atributo index para asignar etiquetas arbitrarias al eje de filas
df_indexado.index = ["reg_c", "reg_a", "reg_d", "reg_b"]

# 69. Convertir el índice actual en una columna regular y restaurar un RangeIndex numérico secuencial
df_con_columna_indice = df_indexado.reset_index()

# 70. Eliminar un registro y reconstruir un índice numérico contiguo descartando el índice previo (drop=True)
df_filtrado = df_imputado.drop(index=1)
df_reiniciado = df_filtrado.reset_index(drop=True)

# --- Ordenación y clasificación ---

# 71. Ordenar los registros según los valores de una columna específica en orden descendente
df_ordenado_nota = df_reiniciado.sort_values(by="nota", ascending=False)

# 72. Ordenar lexicográficamente por múltiples columnas: primero "edad" ascendente y, en empates, "nota" descendente
df_ordenado_multiple = df_reiniciado.sort_values(
    by=["edad", "nota"], ascending=[True, False]
)
