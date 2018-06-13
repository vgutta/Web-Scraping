from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

# scraping graphics cards name, prices
newEggURL = "https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20cards"

raw_page = urlopen(newEggURL)
page = raw_page.read()
raw_page.close()

page_html = soup(page, "html.parser")
items = page_html.findAll("div", {"class":"item-info"})

filename = "graphicsCards.csv"
f = open(filename, "w")
headers = "Brand, Product, Cost\n"
f.write(headers)

for item in items:
    brand = item.a.img["title"]
    item_title = item.findAll("a", {"class": "item-title"})
    product_name = item_title[0].text

    item_action = item.findAll("div", {"class":"item-action"})
    price_container = item_action[0].ul
    prices = price_container.findAll("li", {"class": "price-current"})
    price = prices[0].strong.text


    print("Brand: "+brand)
    print("Name: "+product_name)
    print("Price: "+price)
    print()

    f.write(brand + "," + product_name.replace(",", ";") + "," + price + "\n")

f.close()
