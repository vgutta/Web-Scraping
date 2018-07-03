from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

slickdeals = 'https://slickdeals.net'

raw_page = urlopen(slickdeals)
html = raw_page.read()
raw_page.close()

page = soup(html, 'html.parser')
item_list = page.findAll("a", {"class": "itemTitle"})

item_prices = page.findAll("div", {"class": "itemPrice"})

for price in page.findAll("div", "itemPrice"):
    print(price.text)

for item in item_list:
    print(item.text)
    """print(item_prices.text)"""
