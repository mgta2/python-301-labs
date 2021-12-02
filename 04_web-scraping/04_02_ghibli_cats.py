# Read through the documentation of the Ghibli API and reproduce the example
# listed at https://ghibliapi.herokuapp.com/#section/Use-Case in Python.
# Try skim the Haskell code example and see if you can understand anything.
# Don't worry if you don't, it's a completely different language :)
#
# Your task is to use the API to find information about all the cats that
# appear in Studio Ghibli films.

import requests
import json

BASE_URL = "https://ghibliapi.herokuapp.com/"
response = requests.get(BASE_URL+"people")
data = response.json()

cats = []

for entry in data:
    if entry['species'] == BASE_URL+"species/603428ba-8a86-4b0b-a9f1-65df6abef3d3":
        my_list = {'name': entry['name'], 'gender': entry['gender'], 'hair_color': entry['hair_color'], 'eye_color': entry['eye_color']}
        cats.append(my_list)

with open("cats.json", "w") as fout:
    json.dump(cats,fout)