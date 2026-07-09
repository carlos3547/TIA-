# Este script fue realizado por nuestra auditoria TIA 


#LIMPIEZA Y HOMOLOGACIÓN DE DATOS
# Base: base_cr.xlsx
# Librería utilizada: Pandas
# Variables del modelo:
# X = Registros_X (miles de registros comprometidos)
# Y = Costo_Y (miles de USD)
import pandas as pd


# 1. Lectura del archivo Excel

df = pd.read_excel("base_cr.xlsx")

print("Registros iniciales:", len(df))


# 2. Selección de variables necesarias para el modelo

df = df[
    [
        "Sector",
        "Vector_Ataque",
        "Registros_X",
        "Costo_Y"
    ]
]



# 3. Limpieza de texto


df["Sector"] = (
    df["Sector"]
    .astype(str)
    .str.strip()
)

df["Vector_Ataque"] = (
    df["Vector_Ataque"]
    .astype(str)
    .str.strip()
)



# 4. Conversión de variables cuantitativas

df["Registros_X"] = pd.to_numeric(
    df["Registros_X"],
    errors="coerce"
)

df["Costo_Y"] = pd.to_numeric(
    df["Costo_Y"],
    errors="coerce"
)



# 5. Eliminación de datos faltantes

nulos = df.isnull().sum()

print("\nValores nulos encontrados:")
print(nulos)

df = df.dropna()



# 6. Eliminación de registros duplicados

duplicados = df.duplicated().sum()

print("\nDuplicados encontrados:", duplicados)

df = df.drop_duplicates()



# 7. Validación de valores negativos

df = df[
    (df["Registros_X"] >= 0) &
    (df["Costo_Y"] >= 0)
]

# 8. Validación de categorías esperadas

print("\nSectores disponibles:")
print(df["Sector"].unique())


print("\nVectores de ataque disponibles:")
print(df["Vector_Ataque"].unique())


# 9. Reiniciar índice

df.reset_index(drop=True, inplace=True)


# 10. Resumen final de la base limpia

print("\n========== BASE FINAL ==========")

print("\nCantidad de registros:")
print(len(df))


print("\nPrimeros registros:")
print(df.head())


print("\nInformación de variables:")
print(df.info())


print("\nResumen estadístico:")
print(df.describe())


print("\nDistribución por Sector:")
print(df["Sector"].value_counts())


print("\nDistribución por Vector de Ataque:")
print(df["Vector_Ataque"].value_counts())


# 11. Exportar base limpia

df.to_excel(
    "dataset_limpio.xlsx",
    index=False
)


print("\n================================")
print("Archivo dataset_limpio.xlsx generado correctamente")
print("================================")