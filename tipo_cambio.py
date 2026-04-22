import pandas as pd
from sqlalchemy import create_engine

# 1. Leer CSV
df=pd.read_csv(r"C:\Users\mayuc\OneDrive\Documentos\PROJECT\tipo_cambio_limpio.csv", sep=';')

# Verificar datos
print(df.head())
print(df.info())

# Leer fecha como date
df['fecha']=pd.to_datetime(df['fecha'])
print(df.info())

# Limpiar datos
df['fecha']=pd.to_datetime(df['fecha']).dt.date
df=df.dropna()

# 2. Conexion a SQL Server
engine=create_engine(f"mssql+pyodbc://@AZULON\\SQLEXPRESS/RIESGO_CAMBIARIO?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes")

# 3. Subir datos
print("Subiendo datos...")
df.to_sql('tipo_cambio',con=engine,if_exists='replace',index=False)
print("Tabla creada correctamente")