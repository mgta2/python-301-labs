# Write a unittest test suite to test the rescrape module

import unittest
import rescrape

class TestRescrape(unittest.TestCase):
    def setUp(self):
        self.BASE_URL = "https://codingnomads.github.io/recipes/"
        self.url = "https://codingnomads.github.io/recipes/recipes/1-garlic-butter-steak.html"
    
    def test_get_page_content(self):
        # Status code of 200 means success.
        base_page = rescrape.get_page_content(self.BASE_URL)
        specific_page = rescrape.get_page_content(self.url)
        self.assertEqual(base_page.status_code, 200)
        self.assertEqual(specific_page.status_code, 200)
    
    def test_get_html_content(self):
        # All well formatted HTML documents will contain '<!DOCTYPE html>'.
        base_html = rescrape.get_html_content(self.BASE_URL)
        specific_html = rescrape.get_html_content(self.url)
        self.assertIn("<!DOCTYPE html>", base_html)
        self.assertIn("<!DOCTYPE html>", specific_html)
    
    def test_make_soup(self):
        # Check custom class is of expected type.
        base_html = rescrape.get_html_content(self.BASE_URL)
        specific_html = rescrape.get_html_content(self.url)
        base_soup = rescrape.make_soup(base_html)
        specific_soup = rescrape.make_soup(specific_html)
        self.assertEqual("<class 'bs4.BeautifulSoup'>", str(type(base_soup)))
        self.assertEqual("<class 'bs4.BeautifulSoup'>", str(type(specific_soup)))
    
    def test_get_recipe_links(self):
        # Check we have at least one link on the base page.
        base_html = rescrape.get_html_content(self.BASE_URL)
        base_soup = rescrape.make_soup(base_html)
        self.assertGreater(len(rescrape.get_recipe_links(base_soup)), 0)
    
    def test_get_author(self):
        # The author on self.url is "Divider1".
        specific_html = rescrape.get_html_content(self.url)
        specific_soup = rescrape.make_soup(specific_html)
        recipe_1_author = rescrape.get_author(specific_soup)
        self.assertEqual("Divider1", recipe_1_author)
    
    def test_get_recipe(self):
        # The recipe should be a string of non-zero length.
        specific_html = rescrape.get_html_content(self.url)
        specific_soup = rescrape.make_soup(specific_html)
        recipe_1 = rescrape.get_recipe(specific_soup)
        self.assertIsInstance(recipe_1, str)
        self.assertGreater(len(recipe_1), 0)

if __name__ == "__main__":
    unittest.main()

# Output below:
"""
......
----------------------------------------------------------------------
Ran 6 tests in 1.119s

OK
"""