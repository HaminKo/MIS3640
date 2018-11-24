: from urllib.request import urlopen

URL = 'https://www.imdb.com/chart/top'

response = urlopen(URL)

html = response.read()

from bs4 import BeautifulSoup

soup = BeautifulSoup(html, 'lxml')