import pandas as pd

# 1. Crear un objeto de la clase DataFrame a partir de un diccionario de listas homogéneas
datos = {
    "id": [1, 2, 3, 4],
    "nombre": ["Ana", "Luis", "Eva", "Ana"],
    "edad": [23, 30, 27, 23],
    "nota": [8.5, 7.0, 9.2, 6.8],
}
df = pd.DataFrame(datos)

# 2. Leer un archivo CSV para instanciar un DataFrame (requiere que el fichero exista en disco)
df_csv = pd.read_csv("datos.csv")

# 3. Guardar registros en CSV con index=False para evitar serializar el índice numérico como columna extra
df.to_csv("datos.csv", index=False)

# 4. Obtener las primeras n filas (ej. n=2) para inspeccionar el encabezado de los datos
primeras_n = df.head(2)

# 5. Obtener las últimas n filas (ej. n=2) para comprobar el cierre de la tabla
ultimas_n = df.tail(2)

# 6. Obtener etiquetas de filas (Index) y columnas (Index) mediante sus respectivos atributos
nombres_filas = df.index
nombres_columnas = df.columns

# 7. Convertir el objeto Index de columnas a una lista nativa de Python para manipulación estándar
lista_columnas = df.columns.tolist()

# 8. Renombrar todas las columnas en bloque sobrescribiendo el atributo columns con una lista de igual longitud
df.columns = ["identificador", "nombre_alumno", "edad_anos", "calificacion"]

# 9. Renombrar una columna puntual mediante mapeo diccionario sin alterar el resto del esquema
df = df.rename(columns={"nombre_alumno": "nombre"})

# 10. Consultar los tipos de datos inferidos para cada columna
tipos_datos = df.dtypes

# 11. Mostrar reporte estructural con rango de índice, conteo de no nulos, dtypes y memoria total
df.info()

# 12. Obtener estadísticos descriptivos básicos (conteo, media, desviación típica y cuartiles)
estadisticas = df.describe()

# 13. Filtrar subconjunto de columnas según tipo de dato (ej. exclusivamente columnas numéricas)
columnas_numericas = df.select_dtypes(include=["number"])

# 14. Convertir explícitamente el tipo de dato de una o varias columnas para ajustar su representación
df = df.astype({"identificador": "str", "edad_anos": "float64"})

# 15. Obtener dimensión (ejes=2), tamaño (total de celdas = filas × columnas) y forma (filas, columnas)
dimension = df.ndim
tamano = df.size
forma = df.shape

# 16. Calcular bytes asignados por columna (deep=True inspecciona el peso real de objetos/cadenas en memoria)
memoria_columnas = df.memory_usage(deep=True)

# 17. Comprobar mediante evaluación booleana si el DataFrame carece de registros
esta_vacio = df.empty

# 18. Extraer los valores de una columna (Series) como una lista nativa de Python
lista_nombres = df["nombre"].tolist()

# 19. Contar valores únicos por columna (axis=0) y por fila (axis=1) para evaluar cardinalidad
unicos_columna = df.nunique(axis=0)
unicos_fila = df.nunique(axis=1)

# 20. Obtener un arreglo NumPy (ndarray) con los valores distintos sin repetición de una columna
nombres_distintos = df["nombre"].unique()

# 21. Recuperar la Series con los tipos de dato (dtypes) de todas las columnas del DataFrame
tipos_columnas = df.dtypes

# 22. Convertir una columna de punto flotante (float) a entero (int64), truncando su parte decimal
df["calificacion_entera"] = df["calificacion"].astype("int64")

# 23. Contar cuántas columnas pertenecen a cada tipo de dato (en DataFrame se emplea dtypes en plural)
conteo_tipos = df.dtypes.value_counts()

# 24. Contar el número total de columnas consultando el segundo eje de shape (o len(df.columns))
num_columnas = df.shape[1]

# 25. Obtener la representación matricial en NumPy mediante to_numpy() (estándar actual frente a .values)
matriz_numpy = df.to_numpy()

# 26. Construir un DataFrame ensamblando objetos Series alineados por su índice
serie_producto = pd.Series(["Teclado", "Ratón"], index=["a", "b"])
serie_precio = pd.Series([45.0, 20.5], index=["a", "b"])
df_desde_series = pd.DataFrame({"producto": serie_producto, "precio": serie_precio})
