import os, re, requests
import urllib.request as ur
from bs4 import BeautifulSoup as bs
url = 'http://quotes.toscrape.com/'
soup = bs(ur.urlopen(url).read(), 'html.parser')
print(soup.find_all('span')[:5])
#for i in soup.find_all('a'):
#    print(i.text)
print('-'*50)
for i in soup.find_all('div', {'class' : 'love'}):
    print(i.find_all('a')[0].get('href'))

# 파이썬 인스톨러
# >pyinstaller --onefile abc.py