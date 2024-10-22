# %% Conectarse a BD no relacional
# mongodb+srv://DI:<db_password>@clusterdi.yjk8x.mongodb.net/?retryWrites=true&w=majority&appName=ClusterDI

# Importar módulos
import pymongo
import pandas as pd

# Conexión
try:
    cliente = pymongo.MongoClient(
        "mongodb+srv://DI:<db_password>@clusterdi.yjk8x.mongodb.net/?retryWrites=true&w=majority&appName=ClusterDI")
    print("Conexión exitosa")
except Exception as e:
    print(f"Error en la conexión: {e}")
    exit()

# Extraer la información
db = cliente["sample_mflix"]
coleccion = db["movies"]

# Hacer la consulta
try:
    resultados = coleccion.find().limit(10)
    lista_resultados = list(resultados)
    # Verificar si se han extraído los resultados
    if not lista_resultados:
        print("No se han encontrado datos")
    else:
        print(f"Se han encontrado {len(lista_resultados)} documentos")
except Exception as e:
    print(f"Error al realizar la consulta: {e}")

# Lista --> DataFrame
df = pd.DataFrame(lista_resultados)






