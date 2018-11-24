#warning - I had trouble running beautifulsoup, so I downgraded html5 as advised by the website below. apparently this may cause problems for the package named bleach, which I've never heard of before.

'''
https://stackoverflow.com/questions/38447738/beautifulsoup-html5lib-module-object-has-no-attribute-base

sudo pip install --upgrade html5lib==1.0b8
The directory '/home/danielle/.cache/pip/http' or its parent directory is not owned by the current user and the cache has been disabled. Please check the permissions and owner of that directory. If executing pip with sudo, you may want sudo's -H flag.
The directory '/home/danielle/.cache/pip' or its parent directory is not owned by the current user and caching wheels has been disabled. check the permissions and owner of that directory. If executing pip with sudo, you may want sudo's -H flag.
Collecting html5lib==1.0b8
Requirement already satisfied, skipping upgrade: six in /usr/lib/python3/dist-packages (from html5lib==1.0b8) (1.10.0)
bleach 2.1.1 has requirement html5lib!=1.0b1,!=1.0b2,!=1.0b3,!=1.0b4,!=1.0b5,!=1.0b6,!=1.0b7,!=1.0b8,>=0.99999999pre, but you'll have html5lib 1.0b8 which is incompatible.
Installing collected packages: html5lib
  Found existing installation: html5lib 1.0.1
    Uninstalling html5lib-1.0.1:
      Successfully uninstalled html5lib-1.0.1
Successfully installed html5lib-1.0b8
'''

#beautiful soup is designed to scrap the web
#https://www.crummy.com/software/BeautifulSoup/

from bs4 import BeautifulSoup
import requests

page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")

#print(page)

#get the web parser to do it for me
soup = BeautifulSoup(page.content, 'html.parser')

#Getting Oriented with print statements

'''#non soup orientations
#status_code
#note that I expect a 200, where the 2 indicates success
print(page.status_code)

#
#content
print(page.content)
'''

#soup orientations
'''
print(soup.prettify())

print()

print(list(soup.children))

print()

print([type(item) for item in list(soup.children)])
'''

#identify the final tag of the children, which is the 'html' tag
'''
html = list(soup.children)[2]
print(list(html.children))

body = list(html.children)[3]
print(list(body.children))

p = list(body.children)[1]
print(p.get_text())
'''

print(soup.find_all('p'))

print(soup.find_all('p')[0].get_text())
