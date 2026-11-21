import numpy as np
import pandas as pd

df = pd.DataFrame({
    "id": [101, 102, 103, 104],
    "nombre": ["Ana", "Luis", "Eva", "Ana"],
    "edad": [23, 30, 27, 23],
    "nota": [8.5, 7.0, 9.2, 6.8],
})

# 27. Extraer fila como Series por posición entera
fila_series = df.iloc[0]
print("--- 27. Fila 0 como Series ---\n", fila_series)

# 28. Reordenar columnas pasando nueva lista de etiquetas
df = df[["id", "edad", "nombre", "nota"]]

# 29. Crear copia independiente (.copy) para evitar SettingWithCopyWarning
df_sub = df[["nombre", "nota"]].copy()

# 30. Excluir columna específica sin mutar el DataFrame original
df_sin_edad = df.drop(columns=["edad"])

# 31. Seleccionar rango contiguo de columnas con slicing inclusivo en loc
df_slice_cols = df.loc[:, "edad":"nota"]
print("\n--- 28-31. Subconjunto, exclusión y slicing (refleja reordenación) ---\n", df_sub, "\n", df_sin_edad, "\n", df_slice_cols)

# 32. Comprobar existencia de columna mediante operador in
existe_nota = "nota" in df.columns

# 33. Validar pertenencia celda a celda con isin
mascara_isin = df.isin(["Ana", 30])
print("\n--- 32-33. Existencia de columna y máscara isin ---\nExiste 'nota':", existe_nota, "\n", mascara_isin)

# 34. Obtener registros por posición entera con iloc
registros_pos = df.iloc[[0, 2]]

# 35. Subseleccionar filas (fin exclusivo) y columnas por posición con iloc
sub_iloc = df.iloc[0:2, [1, 3]]

# 36. Subseleccionar filas y columnas por etiquetas explícitas con loc
sub_loc = df.loc[[0, 2], ["nombre", "nota"]]
print("\n--- 34-36. Selecciones con iloc y loc ---\n", registros_pos, "\n", sub_iloc, "\n", sub_loc)

# 37. Filtrar registros en intervalo cerrado [24, 30] con between
en_rango = df[df["edad"].between(24, 30)]

# 38. Filtrar registros mediante máscara booleana relacional
aprobados_altos = df[df["nota"] >= 8.0]
print("\n--- 37-38. Filtrado por rango y condición ---\n", en_rango, "\n", aprobados_altos)

# 39. Modificar celda puntual con loc[fila, columna]
df.loc[1, "nota"] = 7.8

# 40. Insertar columna en posición entera loc=2 (in-place)
df.insert(loc=2, column="curso", value=["IA", "Big Data", "IA", "Big Data"])

# 41. Añadir nueva fila asignando lista a etiqueta inexistente en loc
df.loc[len(df)] = [105, 29, "IA", "Carlos", 8.9]

# 42. Iterar perezosamente por columnas como pares (etiqueta, Series)
for nombre_col, serie_col in df.items():
    pass

# 43. Insertar columna invocando el método de clase DataFrame.insert
pd.DataFrame.insert(df, loc=1, column="activo", value=True)
print("\n--- 39-43. DataFrame tras edición de celda, inserciones y nueva fila ---\n", df)

# 45. Eliminar registro por etiqueta de índice con drop
df = df.drop(index=4)

# 46. Extraer columna como Series y eliminarla simultáneamente con pop
col_extraida = df.pop("activo")

# 47. Reemplazar valores en columna mediante diccionario en replace
df["curso"] = df["curso"].replace({"IA": "Inteligencia Artificial"})
print("\n--- 45-47. Tras drop, pop('activo') y replace ---\n", df, "\nColumna extraída:\n", col_extraida)

# 48. Conservar valores que cumplen condición y sustituir el resto por 0 con where
df_where = df[["edad", "nota"]].where(df[["edad", "nota"]] >= 8, other=0)

# 49. Añadir nueva fila al final mediante slicing abierto en loc
df.loc[len(df):] = [[105, 29, "Big Data", "Carlos", 8.9]]

# 50. Sustituir por NaN los valores que sí cumplen condición (inverso a where) con mask
df_mask = df[["edad", "nota"]].mask(df[["edad", "nota"]] < 7.0, other=np.nan)
print("\n--- 48-50. Filtrado where, inserción por slicing y mask ---\n", df_where, "\n", df, "\n", df_mask)

# 51. Iterar fila por fila obteniendo tuplas (índice, Series)
for indice, fila in df.iterrows():
    pass

# 52. Eliminar múltiples filas con el método de clase DataFrame.drop
df.loc[len(df)] = [105, 29, "Big Data", "Carlos", 8.9] # Rellenar data frame
df = pd.DataFrame.drop(df, labels=[3, 4], axis=0)

# 53. Apilar verticalmente dos DataFrames regenerando índice continuo
df_extra = pd.DataFrame({
    "id": [106],
    "edad": [31],
    "curso": ["Big Data"],
    "nombre": ["Marta"],
    "nota": [9.5],
})
df_concat = pd.concat([df, df_extra], ignore_index=True)

# 54. Combinar relacionalmente mediante inner join sobre clave común "id"
df_becas = pd.DataFrame({"id": [101, 103], "beca": [True, False]})
df_merged = pd.merge(df, df_becas, on="id", how="inner")
print("\n--- 52-54. Tras drop múltiple, concat y merge ---\n", df_concat, "\n", df_merged)

# 55. Eliminar duplicados evaluando unicidad en "curso"
df_sin_duplicados = df_concat.drop_duplicates(subset=["curso"], keep="first")

# 56. Permutar filas aleatoriamente con semilla reproducible
df_aleatorio = df_concat.sample(frac=1.0, random_state=42)

# 57. Reemplazar múltiples valores globalmente mediante diccionario
df_reemplazado = df_concat.replace({"Ana": "Ana María", "Big Data": "BD"})
print("\n--- 55-57. Sin duplicados, muestreo aleatorio y reemplazo global ---\n", df_sin_duplicados, "\n", df_aleatorio, "\n", df_reemplazado)

# 58. Convertir infinitos IEEE 754 en NaN con replace y eliminarlos con dropna
df_inf = pd.DataFrame({"a": [1.0, np.inf, -np.inf, 4.0]})
df_sin_inf = df_inf.replace([np.inf, -np.inf], np.nan).dropna()

# 59. Descartar primeras n=2 filas con slicing posicional en iloc
sin_primeras_n = df_concat.iloc[2:]

# 60. Descartar últimas n=2 filas con índice negativo en iloc
sin_ultimas_n = df_concat.iloc[:-2]
print("\n--- 58-60. Purga de infinitos y descartes posicionales ---\n", df_sin_inf, "\n", sin_primeras_n, "\n", sin_ultimas_n)