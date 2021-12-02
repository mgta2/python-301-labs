# Research for interesting APIs online and pick two. You can also use APIs that
# you've already worked with in the course if you prefer.
# Write a program that makes calls to both APIs and find a way to combine the
# data that you receive from both of them.
# E.g.: You could use the Ghibli API to find all ghosts from their films, and
#       create an opposing team of Ghost Pokémon from the Poke API.

import requests

BASE_URL = "https://pokeapi.co/api/v2/"

response = []

for i in range(1,7):
    response.append(requests.get(BASE_URL+f"pokemon/{i}").json())
names = []
for pokemon in response:
    names.append(pokemon['forms'][0]['name'].capitalize())

copies = []
for name in names:
    length = len(name)
    api_url = f"https://uzby.com/api.php?min={length}&max={length}"
    response = requests.get(api_url)
    copies.append(response.text)

for i in range(0,6):
    print(f"{names[i]} vs. {copies[i]}")

# Example Output:
"""
Bulbasaur vs. Choodraix
Ivysaur vs. Dassesa
Venusaur vs. Koukoace
Charmander vs. Gleeksooms
Charmeleon vs. Zaupewhiho
Charizard vs. Chaurseet
"""