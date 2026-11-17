import numpy as np
import pandas as pd

df = pd.DataFrame({
    "id": [101, 102, 103, 104],
    "nombre": ["Ana", "Luis", "Eva", "Ana"],
    "edad": [23, 30, 27, 23],
    "nota": [8.5, 7.0, 9.2, 6.8],
})

# 27. Extraer una fila como Series indexando por posición escalar (el índice resultante son las columnas)
fila_series = df.iloc[0]

# 28. Reordenar columnas pasando una lista con la nueva secuencia de etiquetas al operador de indexación
df = df[["id", "edad", "nombre", "nota"]]

# 29. Crear un sub-DataFrame independiente con .copy() para evitar advertencias SettingWithCopyWarning al mutarlo
df_sub = df[["nombre", "nota"]].copy()

# 30. Excluir una columna concreta mediante drop(columns=...) sin alterar el DataFrame original
df_sin_edad = df.drop(columns=["edad"])

# 31. Seleccionar rango contiguo de columnas con slicing de etiquetas en loc (ambos extremos son inclusivos)
df_slice_cols = df.loc[:, "edad":"nota"]

# 32. Comprobar existencia de etiqueta en el eje de columnas usando el operador de pertenencia in
existe_nota = "nota" in df.columns

# 33. Validar celda a celda si algún elemento de la lista coincide con los valores del DataFrame
mascara_isin = df.isin(["Ana", 30])

# 34. Extraer registros específicos mediante sus posiciones enteras base 0 con iloc
registros_pos = df.iloc[[0, 2]]

# 35. Subseleccionar simultáneamente filas (límite superior exclusivo) y columnas por posición con iloc
sub_iloc = df.iloc[0:2, [1, 3]]

# 36. Subseleccionar filas y columnas simultáneamente por sus nombres explícitos de índice y columna con loc
sub_loc = df.loc[[0, 2], ["nombre", "nota"]]

# 37. Filtrar registros dentro de un intervalo cerrado [24, 30] mediante evaluación booleana vectorizada
en_rango = df[df["edad"].between(24, 30)]

# 38. Filtrar registros aplicando una máscara booleana relacional sobre una columna
aprobados_altos = df[df["nota"] >= 8.0]

# 39. Modificar una celda puntual con loc[fila, columna] para garantizar asignación directa en memoria
df.loc[1, "nota"] = 7.8

# 40. Insertar una nueva columna en la posición entera loc=2 desplazando a la derecha las existentes (in-place)
df.insert(loc=2, column="curso", value=["IA", "Big Data", "IA", "Big Data"])

# 41. Añadir una nueva fila asignando una lista completa a una etiqueta de índice inexistente en loc
df.loc[len(df)] = [105, 29, "IA", "Carlos", 8.9]

# 42. Iterar sobre las columnas obteniendo pares (etiqueta_columna, Series_datos) de forma perezosa
for nombre_col, serie_col in df.items():
    pass

# 43. Agregar una columna en una posición específica invocando el método de clase DataFrame.insert
pd.DataFrame.insert(df, loc=1, column="activo", value=True)

# 45. Eliminar un registro puntual indicando su etiqueta de índice en drop
df = df.drop(index=4)

# 46. Extraer una columna como Series y eliminarla simultáneamente del DataFrame con pop
col_extraida = df.pop("activo")

# 47. Sustituir valores específicos dentro de una columna mediante mapeo diccionario en replace
df["curso"] = df["curso"].replace({"IA": "Inteligencia Artificial"})

# 48. Conservar valores que cumplen la condición y reemplazar por other=0 los que no la cumplen con where
df_where = df[["edad", "nota"]].where(df[["edad", "nota"]] >= 8, other=0)

# 49. Añadir una nueva fila al final usando notación de slicing abierto sobre el eje de filas en loc
df.loc[len(df):] = [[105, 29, "Big Data", "Carlos", 8.9]]

# 50. Reemplazar por np.nan los valores que sí cumplen la condición (operación inversa a where) mediante mask
df_mask = df[["edad", "nota"]].mask(df[["edad", "nota"]] < 7.0, other=np.nan)

# 51. Iterar fila por fila obteniendo tuplas (etiqueta_índice, Series_fila) con iterrows
for indice, fila in df.iterrows():
    pass

# 52. Eliminar múltiples registros mediante el método de clase DataFrame.drop sobre el eje 0 (filas)
df = pd.DataFrame.drop(df, labels=[3, 4], axis=0)

# 53. Apilar verticalmente dos DataFrames con mismo esquema regenerando un índice continuo con ignore_index=True
df_extra = pd.DataFrame({
    "id": [106],
    "edad": [31],
    "curso": ["Big Data"],
    "nombre": ["Marta"],
    "nota": [9.5],
})
df_concat = pd.concat([df, df_extra], ignore_index=True)

# 54. Combinar relacionalmente dos DataFrames mediante intersección (inner join) sobre la clave común "id"
df_becas = pd.DataFrame({"id": [101, 103], "beca": [True, False]})
df_merged = pd.merge(df, df_becas, on="id", how="inner")

# 55. Eliminar filas duplicadas evaluando unicidad exclusivamente en la columna "curso" y conservando la primera
df_sin_duplicados = df_concat.drop_duplicates(subset=["curso"], keep="first")

# 56. Permutar aleatoriamente el 100% de las filas (frac=1.0) fijando semilla para reproducibilidad
df_aleatorio = df_concat.sample(frac=1.0, random_state=42)

# 57. Reemplazar múltiples valores de forma global en todo el DataFrame mediante un diccionario
df_reemplazado = df_concat.replace({"Ana": "Ana María", "Big Data": "BD"})

# 58. Convertir infinitos IEEE 754 (-np.inf y np.inf) en NaN con replace para poder purgar esas filas con dropna
df_inf = pd.DataFrame({"a": [1.0, np.inf, -np.inf, 4.0]})
df_sin_inf = df_inf.replace([np.inf, -np.inf], np.nan).dropna()

# 59. Descartar las primeras n=2 filas iniciando el slicing posicional de iloc en el índice 2
sin_primeras_n = df_concat.iloc[2:]

# 60. Descartar las últimas n=2 filas acotando el slicing posicional de iloc hasta el índice negativo -2
sin_ultimas_n = df_concat.iloc[:-2]
