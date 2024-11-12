import config
import pandas as pd
import subprocess
from sqlalchemy import create_engine
from datetime import datetime
#Versión en inglés del script que exporta a excel
def exportarExcel(id_inicial, id_final):
    # Crea motor de SQLAlchemy
    engine = create_engine(f"mysql+mysqlconnector://{config.DB_USER}:{config.DB_PASSWORD}@{config.DB_HOST}/{config.DB_NAME}")

    # Construye la consulta SQL con el rango de IDs
    consulta_sql = f"SELECT * FROM lecturas WHERE id BETWEEN {id_inicial} AND {id_final}"

    # Crea un Dataframe de pandas
    df = pd.read_sql_query(consulta_sql, engine)
    # Define a dictionary to map Spanish column names to English column names
    column_mapping = {
        'id': 'id',
        'tiempo': 'Time',
        'temperatura': 'Temperature',
        'pH': 'pH',
        'conductividad': 'Electrical Conductivity',
        'indice': 'WQI',
        'calidad': 'Quality'
    }

    # Rename the columns using the dictionary
    df = df.rename(columns=column_mapping)

    print(df)
    # Obtener la fecha y hora actual
    timestampFormat = datetime.now().strftime("%d-%m-%Y %H-%M-%S")

    # Definir el nombre del archivo con el formato deseado
    nombre_archivo = f"Measurents from {timestampFormat}.xlsx"

    # Definir la ruta de la carpeta
    ruta_carpeta = "/home/pi/Desktop/ArchivosExportados/"
    # Guardar el DataFrame en un archivo Excel en la carpeta especificada
    df.to_excel(ruta_carpeta + nombre_archivo, index=False)

    # Abre la carpeta en el explorador de archivos por defecto en Linux
    subprocess.run(["xdg-open", ruta_carpeta])
    # Abre la carpeta en el Finder en macOS
    #subprocess.run(["open", ruta_carpeta])
    return True


# Ejemplo de uso de la funcion
if __name__ == "__main__":
    exportarExcel(1, 12)
