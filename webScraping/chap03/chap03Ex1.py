from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
# html변수에 urlopen()함수로 케빈 베이컨의
html = urlopen('http://en.wikipedia.org/wiki/kevin_Bacon')
bs = BeautifulSoup(html, 'html.parser')
'''
for link in bs.findAll('a'):
    if 'href' in link.attrs:
        print(link.attrs['href'])
'''
print('-'*40)
for link in bs.find('div', {'id':'bodyContent'}).findAll('a', href = re.compile('^(/wiki/)((?!:).)*$')):
    if 'href' in link.attrs:
        print(link.attrs['href'])

