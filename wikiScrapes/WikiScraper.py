# import libraries
from urllib.request import urlopen
from beautifulsoup4 import BeautifulSoup

# specify the url
wiki = 'https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(PPP)'

# query the html and return the webpage to the variable 'page'
page = urllib2.urlopen(wiki)

# parse the html with BeautifulSoup and store in variable 'soup'
soup = BeautifulSoup(page)

print(soup.title)

# Take out the <div> of name and get its value
#name_box = soup.find(‘h1’)

#name_box_temp = name_box.attrs(‘class’: ‘name’)

# get the name
#name = name_box_temp.text.strip()

#print name

# get the index price
#price_box = soup.find(‘div’)
#price_box_temp = price_box.attrs(‘class’:’price’)
#price = price_box.text
#print price
