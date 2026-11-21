import pandas as pd

# 1. Crear DataFrame desde diccionario de listas homogéneas
datos = {
    "id": [1, 2, 3, 4],
    "nombre": ["Ana", "Luis", "Eva", "Ana"],
    "edad": [23, 30, 27, 23],
    "nota": [8.5, 7.0, 9.2, 6.8],
}
df = pd.DataFrame(datos)

# 3. Exportar a CSV omitiendo el índice numérico (se ejecuta antes de leer para que exista el archivo)
df.to_csv("./datos.csv", index=False)

# 2. Cargar DataFrame desde archivo CSV
df_csv = pd.read_csv("datos.csv")

# 4. Obtener primeras n filas para inspeccionar cabecera
primeras_n = df.head(2)
print("--- 4. Primeras n filas ---\n", primeras_n)

# 5. Obtener últimas n filas para revisar el final de la tabla
ultimas_n = df.tail(2)
print("\n--- 5. Últimas n filas ---\n", ultimas_n)

# 6. Obtener objetos Index de filas y columnas
nombres_filas = df.index
nombres_columnas = df.columns
print("\n--- 6. Índices y columnas ---\n", nombres_filas, "\n", nombres_columnas)

# 7. Convertir etiquetas de columnas a lista nativa de Python
lista_columnas = df.columns.tolist()
print("\n--- 7. Lista de columnas ---\n", lista_columnas)

# 8. Renombrar todas las columnas en bloque asignando nueva lista
df.columns = ["identificador", "nombre_alumno", "edad_anos", "calificacion"]

# 9. Renombrar columna puntual mediante mapeo diccionario
df = df.rename(columns={"nombre_alumno": "nombre"})

# 10. Obtener tipos de datos inferidos por columna (refleja los renombrados de 8 y 9)
tipos_datos = df.dtypes
print("\n--- 10. Tipos de datos ---\n", tipos_datos)

# 11. Mostrar resumen estructural, conteo de no nulos y memoria
print("\n--- 11. Información básica ---")
df.info()

# 12. Obtener estadísticos descriptivos de variables numéricas
estadisticas = df.describe()
print("\n--- 12. Estadísticas básicas ---\n", estadisticas)

# 13. Obtener columnas filtrando por tipo numérico
columnas_numericas = df.select_dtypes(include=["number"])
print("\n--- 13. Columnas numéricas ---\n", columnas_numericas)

# 14. Convertir explícitamente el tipo de dato de columnas seleccionadas
df = df.astype({"identificador": "str", "edad_anos": "float64"})

# 15. Obtener ejes (ndim), total de celdas (size) y dimensiones (shape)
dimension = df.ndim
tamano = df.size
forma = df.shape
print("\n--- 15. Dimensión, tamaño y forma ---\n", dimension, tamano, forma)

# 16. Obtener bytes en memoria por columna (deep=True mide cadenas reales tras astype en 14)
memoria_columnas = df.memory_usage(deep=True)
print("\n--- 16. Memoria por columna (bytes) ---\n", memoria_columnas)

# 17. Comprobar si el DataFrame está vacío
esta_vacio = df.empty

# 18. Obtener valores de una columna como lista de Python
lista_nombres = df["nombre"].tolist()
print("\n--- 18. Lista de nombres ---\n", lista_nombres)

# 19. Contar valores únicos por columna (axis=0) y fila (axis=1)
unicos_columna = df.nunique(axis=0)
unicos_fila = df.nunique(axis=1)
print("\n--- 19. Únicos por columna y fila ---\n", unicos_columna, "\n", unicos_fila)

# 20. Obtener array con valores únicos de una columna
nombres_distintos = df["nombre"].unique()
print("\n--- 20. Nombres distintos ---\n", nombres_distintos)

# 21. Obtener tipos de datos actuales tras las conversiones
tipos_columnas = df.dtypes
print("\n--- 21. Tipos de datos actuales ---\n", tipos_columnas)

# 22. Convertir columna float a entero truncando decimales
df["calificacion_entera"] = df["calificacion"].astype("int64")

# 23. Contar columnas agrupadas por tipo de dato (refleja la nueva columna de 22)
conteo_tipos = df.dtypes.value_counts()
print("\n--- 23. Conteo por tipo de dato ---\n", conteo_tipos)

# 24. Contar total de columnas mediante el segundo eje de shape
num_columnas = df.shape[1]
print("\n--- 24. Total de columnas ---\n", num_columnas)

# 25. Obtener representación matricial como ndarray de NumPy
matriz_numpy = df.to_numpy()
print("\n--- 25. Matriz NumPy ---\n", matriz_numpy)

# 26. Crear DataFrame alineando objetos Series por su índice
serie_producto = pd.Series(["Teclado", "Ratón"], index=["a", "b"])
serie_precio = pd.Series([45.0, 20.5], index=["a", "b"])
df_desde_series = pd.DataFrame({"producto": serie_producto, "precio": serie_precio})