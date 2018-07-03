from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

slickdeals = 'https://slickdeals.net'

raw_page = urlopen(slickdeals)
html = raw_page.read()
raw_page.close()

page = soup(html, 'html.parser')
item_list = page.findAll("a", {"class": "itemTitle"})

item_info = page.findAll("div", {"class": "priceLine"})

titles = []
prices = []

filename = "televisions.csv"
f = open(filename, "w")
headers = "Product, Price\n"
f.write(headers)

for item in item_info:
    itemTitle = item["title"]
    titles.append(itemTitle)
    price = item.find("div", {"class": "itemPrice"})
    price = price.text
    price = price.strip()
    prices.append(price)
    f.write(itemTitle.replace(",", ";") + "," + price + "\n")

f.close()

print(len(prices), len(titles))
print()

item_prices = page.findAll("div", {"class": "itemPrice"})
"""
for price in page.findAll("div", "itemPrice"):
    println(price.text)

for item in item_list:
    print(item.text)
    print(item_prices.text)
"""