from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

website = 'https://techcrunch.com/tag/blockchain/'

raw_page = urlopen(website)
html = raw_page.read()
raw_page.close()

page = soup(html, "html.parser")
articles = page.findAll('a', {"class": "post-block__title__link"})

article_titles = []
article_links = []

for article in articles:
    article_titles.append(article.text)
    article_links.append(article['href'])
