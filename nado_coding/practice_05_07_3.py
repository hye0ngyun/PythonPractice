# pip install
# import inspect
from bs4 import BeautifulSoup
# print(inspect.getfile(bs4))

soup = BeautifulSoup('<p>Some<b>bad<i>HTML')
print(type(soup))
print(soup.prettify())