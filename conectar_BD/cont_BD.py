# %% Conexión a base de datos.

import mysql.connector
from mysql.connector import Error
import pandas as pd

# Función para conectarse
def connec_BD(host, database, user, password, port):
    try:
        connection = mysql.connector.connect(
            host=host,
            database=database,
            user=user,
            password=password,
            port=port
        )
        if connection.is_connected():
            print(f"La conexión ha sido exitosa {database}")
            return connection
    except Error as e:
        print(f"Error al conectarse {e}")
        return None

# Función para leer
def read_DB(connection, tabla, columnas, limite_filas):
    try:
        cursor = connection.cursor()
        # Construir consulta
        columnas_str = ",".join(columnas)
        query = f"SELECT {columnas_str} FROM {tabla} LIMIT {limite_filas};"
        # Ejecutar consulta
        cursor.execute(query)
        # Obtener resultados
        resultados = cursor.fetchall()
        # Obtener nombres de columnas
        columnas_resultado = [i[0] for i in cursor.description]
        # Crear DataFrame
        df = pd.DataFrame(resultados, columns=columnas_resultado)
        return df
    except Error as e:
        print(f"Error al leer la BD {e}")


# Ejecutar
if __name__ == '__main__':
    # Parametros de la conexión
    host = 'mysql-rfam-public.ebi.ac.uk'
    database = 'Rfam'
    user = 'rfamro'
    password = ''
    port = 4497
    # Parametros de la consulta
    tabla = 'family' #Tabla a consultar
    # Columnas que quieres extraer
    columnas = ['rfam_acc', 'rfam_id', 'description']
    limite_filas = 5 # Número de filas que quieres extraer
    # Conectar a la BD
    conexión = connec_BD(host, database, user, password, port)
    if conexión:
        # Leer 
        df_BD = read_DB(conexión, tabla, columnas, limite_filas)
        if df_BD is not None:
            print(df_BD)
        conexión.close()











