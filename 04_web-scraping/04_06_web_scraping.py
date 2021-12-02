# Look for a static website online that has some information that you're
# interested in. Follow the web-scraping steps described in the course to
# inspect, scrape, and parse the information.
# BE RESPECTFUL! Don't scrape sites that don't want to be scraped, and
# limit the amount of calls you make to their page by saving the response
# to a file, and parsing the content from that file.

import requests
from bs4 import BeautifulSoup

url = "https://gowers.wordpress.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text,features="html.parser")

paras = soup.find_all("p")

my_str = str(paras[0]) + "\n" + str(paras[1])

with open("scraped_text.txt", "w") as fout:
    fout.write(my_str)
