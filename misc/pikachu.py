import requests
# Retreiving data from poke api
pikachu = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu')
data = pikachu.json()
# Printing cool message on console
print("A wild", data["name"], "appeared with height", data["height"], "and weight", data["weight"])
