# Refactor your web scraping script and wrap all the functionality into
# separate functions. This is a great exercise to revisit writing functions
# as well as for refactoring your code. It'll also help you in an upcoming
# section of the course when you'll write tests for your web scraper.

import requests
from bs4 import BeautifulSoup

def scrape(url): # Input url string, outputs Beautiful Soup Object
    response = requests.get(url)
    data = BeautifulSoup(response, features="html.parser")
    return data

def parse(data): # Input Beautiful Soup Object, outputs data string.
    paras = data.find_all("p")
    my_str = str(paras[0]) + "\n" + str(paras[1])
    return my_str

def make_file(my_str): # Input data string, write it to a .txt file.
    with open("scraped_text.txt", "w") as fout:
        fout.write(my_str)