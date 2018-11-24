#beautiful soup is designed to scrap the web
#https://www.crummy.com/software/BeautifulSoup/

from bs4 import BeautifulSoup
import requests

page = requests.get("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
soup = BeautifulSoup(page.content, 'html.parser')

print(soup.find_all('p', class_='outer-text'))

print(soup.find_all(class_="outer-text"))
