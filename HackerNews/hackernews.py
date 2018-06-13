# import libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

# specify the url
hacker_news = 'https://news.ycombinator.com/'

# query the html and return the webpage to the variable 'html'
raw_page = urlopen(hacker_news)
html = raw_page.read()
raw_page.close()

# parse the html with BeautifulSoup and store in variable 'page'
page = soup(html, "html.parser")
itemlist = page.findAll("table", {"class": "itemlist"})
athings = itemlist[0].findAll("tr", {"class": "athing"})
#print(athing)

for athing in athings:
    #title = athing.findAll("td", {"class": "title"})
    storylink = athing.findAll("a", {"class": "storylink"})
    title = storylink[0].text
    print(title)

