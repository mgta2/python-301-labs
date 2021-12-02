# Install `pytest` in a virtual environment and rewrite the test suite
# for your web scraper using `pytest` instead of `unittest`.

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://codingnomads.github.io/recipes/"
url = f"{BASE_URL}recipes/11-making-my-own-baguet.html"

def get_page_content(url):
    """Gets the response from a HTTP call to the URL."""
    page = requests.get(url)
    return page

def get_html_content(url):
    """Gets the HTML from a page."""
    html = get_page_content(url).text
    return html

def make_soup(html):
    """Converts an HTML string to a BeautifulSoup object."""
    soup = BeautifulSoup(html, "html.parser")
    return soup

def get_recipe_links(soup):
    """Extracts the URLs of all links on a page, given a bs4 object."""
    links = [link["href"] for link in soup.find_all("a")]
    return links

def get_author(soup):
    """Extracts the name of the author of a recipe."""
    author = soup.find("p", class_="author").text.strip("by ")
    return author

def get_recipe(soup):
    """Extracts the recipe text from a bs4 object."""
    recipe = soup.find("div", class_="md").text
    return recipe

# Tests:

def test_get_page_content():
    index_page = get_page_content(BASE_URL)
    page = get_page_content(url)
    assert index_page.status_code == 200
    assert page.status_code == 200

def test_get_html_content():
    index_html = get_html_content(BASE_URL)
    html = get_html_content(url)
    assert "<!DOCTYPE html>" in index_html
    assert "<!DOCTYPE html>" in html

def test_make_soup():
    html = get_html_content(url)
    soup = make_soup(html)
    assert "<class 'bs4.BeautifulSoup'>" == str(type(soup))

def test_get_recipe_links():
    index_html = get_html_content(BASE_URL)
    index_soup = make_soup(index_html)
    assert len(get_recipe_links(index_soup)) > 0

def test_get_author():
    html = get_html_content(url)
    soup = make_soup(html)
    author = get_author(soup)
    assert len(author) != 0
    assert "Jadafaa" == author

def test_get_recipe():
    html = get_html_content(url)
    soup = make_soup(html)
    recipe = get_recipe(soup)
    assert isinstance(recipe, str)
    assert len(recipe) > 0

# Output below: (the two additional tests run were from previous lab exercises.)
"""
collected 8 items

test_scrape.py ......                                                                                            [ 75%]
06_02_mymath-tester/test_mymath.py ..                                                                            [100%]

================================================== 8 passed in 2.33s ===================================================
"""