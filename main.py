import requests

URL = "https://pokeapi.co/api/v2/pokemon/ditto/"

res = requests.get(URL) # get the data
res = res.json() # convert data to Python format

print(res)