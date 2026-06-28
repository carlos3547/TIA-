#creación del script 
#muestra inferencial incidentes de ciberseguridad 
import pandas as pd

# Cargar la base de datos
archivo = "dataset_final_100.csv"

df = pd.read_csv(archivo)

print("=" * 50)
print("BASE DE DATOS ORIGINAL")
print("=" * 50)
print(df.head())

print("\nRegistros originales:", len(df))

# Información general
print("\nInformación del dataset")
print(df.info())

# Eliminar filas vacías
df = df.dropna(how="all")

# Eliminar duplicados
df = df.drop_duplicates()

# Eliminar espacios
df["Sector"] = df["Sector"].astype(str).str.strip()
df["Tipo"] = df["Tipo"].astype(str).str.strip()

# Homologar nombres
df["Sector"] = df["Sector"].str.title()
df["Tipo"] = df["Tipo"].str.title()

# Convertir columnas numéricas
df["Dias_Deteccion"] = pd.to_numeric(
    df["Dias_Deteccion"],
    errors="coerce"
)

df["Registros"] = pd.to_numeric(
    df["Registros"],
    errors="coerce"
)

# Eliminar registros con datos faltantes
df = df.dropna()

# Eliminar valores negativos
df = df[
    (df["Dias_Deteccion"] >= 0) &
    (df["Registros"] >= 0)
]

# Reiniciar índice
df.reset_index(drop=True, inplace=True)

# Guardar base limpia
salida = "dataset_final_100_limpio.csv"
df.to_csv(salida, index=False)

# Resumen final
print("\n" + "=" * 50)
print("BASE LIMPIA")
print("=" * 50)

print(df.head())

print("\nNúmero final de registros:", len(df))

print("\nValores nulos por columna")
print(df.isnull().sum())

print("\nTipos de datos")
print(df.dtypes)

print("\nLa base limpia fue guardada como:")
print(salida)
