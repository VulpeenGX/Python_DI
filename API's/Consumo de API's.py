# %% Consumo de API's
import requests
# url
url = 'https://pokeapi.co/api/v2/pokemon?limit=150'
# Respuesta
respuesta = requests.get(url)
#  Convertir nuestra respuesta a un archivo
lista_pokemon = respuesta.json()['results']

for pokemon in lista_pokemon:
    print(pokemon['name'])



