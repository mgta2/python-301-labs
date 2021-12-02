# For this project, your task is to create a CLI that takes as an input
# the names of ingredients from a user. Then, your code will fetch
# the recipe information from the CodingNomads recipe collection,
# and search through the text of the recipes to find ones that include
# the provided ingredients.
#
# Note: Feel free to integrate your custom Ingredient() and Soup() classes
# into the code base, to get some additional practice in working with your
# custom Python classes.

import requests
from bs4 import BeautifulSoup

def good_link(url, ingred_list):
    page = requests.get(url)
    soup = BeautifulSoup(page.text,features="html.parser")
    output = True
    my_str = str(soup)
    for ingred in ingred_list:
        if my_str.find(ingred) == -1:
            output = False
    return output

def print_recipe(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text,features="html.parser")
    recipe_name = soup.find_all("h1")[0].text
    
    author = soup.find("p", class_="author")
    name = author.text.strip("by ")
    
    p_list = soup.find_all("p")
    ingred_list = []
    for i in range(0,len(p_list)):
        ingred_list.append(p_list[i].text)
    
    li_list = soup.find_all("li")
    instruct_list = []
    for i in range(0,len(li_list)):
        instruct_list.append(li_list[i].text)
    print("----------------")
    print(f"{recipe_name} by {name}")
    print("Ingredients:")
    for x in ingred_list:
        print(x)
    print()
    print("Instructions:")
    for y in instruct_list:
        print(y)
    print("----------------")

URL = "https://codingnomads.github.io/recipes"

user_input = input("Enter list of ingredients, separated by spaces: ")
ingred_list = user_input.split()

page = requests.get(URL)
soup = BeautifulSoup(page.text, features="html.parser")

links = [link['href'] for link in soup.find_all("a")]

good_links = []
for link in links:
    link = URL + '/' + link
    if good_link(link, ingred_list) == True:
        good_links.append(link)

for link in good_links:
    print_recipe(link)

# Following is example output:
"""
Enter list of ingredients, separated by spaces: steak butter egg
----------------
Steak and Eggs in Cast Iron. Perfect Weekend Brunch. by irharrier2
Ingredients:
by irharrier2
Here is my recipe that is modified version of a couple online versions with extra added details that helped get it just correct. It is good enough for a brunch for two!
Ingredients:
Instruction:
Edit 1: I got the bulk of the recipe from this link. I love this guy for munchie recipes but he doesn’t write a detailed recipe and always misses out the details and cooking temperatures. So based on my experience and a couple of other online recipes, I wrote down everything that you need in order to get it correct.
Edit 2: wow guys, thank you for all the kind words and awards. It has been a pleasure spending my evening with you.
I hope I didn’t miss any questions.

Instructions:
250g or heaver ribeye steak (if your steak is below this weight, skip the oven cooking part)
2 eggs
Store bought hash brown
1 tomato cut in half or cherry tomatoes on the vine
4-5 brown mushrooms, cleaned and destemmed
0.5 tbsp. of Butter
Start by baking the hash brown according to the packaging (always go 5 mins longer to get them extra crispy)
Rub the steak with oil (something that can take high heat) and salt. Let it rest.
Wash and dry mushroom and tomato
3-5 minutes before hash browns are ready, set the cast iron on high heat (don't put any oil as steak is coated in oil).
Once hash brown is taken out, lower the oven to 130c.
Place the tomato and mushrooms in the pan along with the steak. Sear both side of steak, one minute per side. Hit your vegetables with seasoning and olive oil.
Place in oven for 5-7 minutes (or until it reaches 60c for medium), take out pan and place it on medium heat on the stove. Remove the steak and let it rest .
Add butter to the place that you wanna put the eggs, and put the excess (if any) on top of the steak. Fit the hash browns on the side to heat up while cooking.
Crack the eggs and season them. Take it of the heat before they are fully cooked.
 I like to cut the steak before returning it to the pan along with all the accumulated juices.
Serve with a slice of toasted bread (dark or sourdough bread recommended)
"""

# Another example output:
"""
Enter list of ingredients, separated by spaces: beef coconut flour
----------------
Japanese Potato Curry, simple and delicious! by mienczaczek
Ingredients:
by mienczaczek
Deep in flavour lighter version of Japanese Beef Curry. Simple and delicious!
Ingredients for 4 portions:
Instructions:
1. Heat 2tbsp of rapeseed oil in a frying pan.
2. Sweat the onions and celery on medium heat for 5 minutes.
3. Turn up the heat slightly and adds diced carrots and potatoes, fry until starts to brown (you may add little bit more oil at this step)
4. Transfer to a medium pot and add beef stock, soy and mirin.
5. Bring to boil and reduce to simmer, cook until soft (around 20 minutes)
6. In the meantime prepare the curry roux, in the frying pan heat 3tbsp of oil and fry sliced garlic, when browned add 4tsp of curry powder and 2tbsp of plain flour. Cook on medium heat for around 2 minutes.
7. When potatoes and carrots are cooked to desired texture add coconut milk and 1tsp of honey, bring to the boil and turn off the heat.
8. Stir in curry roux to thicken and serve with rice and sliced green chilli.
Enjoy!
Blog post: https://www.insightflavour.com/post/japanese-potato-curry

Instructions:
2 medium carrots, diced
2 large waxy type potatoes (this type melts in the mouth)
2 small onions finely chopped
4 garlic cloves sliced
half a celery stalk finely chopped
500ml of beef stock
200ml of coconut milk
4tsp of curry powder (I used mild madras as it is one of my favourites)
2tbsp of plain flour
1tbsp of dark soy sauce
1tsp of honey
1tbsp of mirin
rapeseed oil for frying
----------------
"""
