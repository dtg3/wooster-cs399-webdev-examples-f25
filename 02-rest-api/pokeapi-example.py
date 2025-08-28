import requests
import json

api_base_url = "https://pokeapi.co/api/v2/"

poke_response = requests.get(api_base_url+'pokemon/charizard')
print(poke_response.headers)
print(json.dumps(poke_response.json(), indent=4))