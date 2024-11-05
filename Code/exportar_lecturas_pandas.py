# Exporta todas las lecturas de la base de datos a un df de pandas para posterior análisis.
import config
import pandas as pd
import mysql.connector

# Se crea la conexión
connection = mysql.connector.connect(
    host=config.DB_HOST,
    user=config.DB_USER,
    password=config.DB_PASSWORD,
    database=config.DB_NAME)

# Se crea un cursor
cursor = connection.cursor()
# Se crea la consulta
query = """
        SELECT * FROM lecturas;
        """
cursor.execute(query)

#Se obtiene la respuesta
respuesta = cursor.fetchall()

columnas = ("id", "Fecha", "Temperatura", "pH", "Conductividad_Electrica", "ICA", "Calidad")

#Se crea el dataframe de pandas
df = pd.DataFrame(respuesta, columns=columnas)

# Se ajustan los tipos de datos de las columnas resultantes
for columna in columnas[2:6]:
    df[f"{columna}"] = dfTest[f"{columna}"].astype(float)
    
df["Calidad"] = dfTest["Calidad"].astype(str)

print(f"Se Tienen {len(df)} lecturas")
