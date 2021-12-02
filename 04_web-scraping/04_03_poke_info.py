# Use the Pokemon API at https://pokeapi.co/ to assemble a team of your
# six favorite Pokémon.
# Your task is to fetch information about six Pokémon through the
# necessary API calls and include the information in your local script.
# This information should include at least:
# - name
# - number
# - types
#
# You can improve on your project even more by writing the data to a small
# `.html` page which allows you to also display the sprites of each Pokémon.
# Check out the guides they provide: https://pokeapi-how.appspot.com/page5

import requests

BASE_URL = "https://pokeapi.co/api/v2/"

response = []

for i in range(1,7):
    response.append(requests.get(BASE_URL+f"pokemon/{i}").json())

for pokemon in response:
    print("Pokemon Name:", pokemon['forms'][0]['name'].capitalize())
    my_list = []
    for i in range(0, len(pokemon['types'])):
        my_list.append(pokemon['types'][i]['type']['name'].capitalize())
    print("Types:", my_list)
    print("--------")
