from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('https://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')

# 정규 표현식과 BeautifulSoup
images = bs.findAll('img', {'src': re.compile('\.\.\/img\/gifts/img.*\.jpg')})
for image in images:
    print(image['src'])
# 속성에 접근하기
# myTag.attrs
# myImgTag.attrs['src']

# 람다 표현식
print(bs.findAll(lambda tag: len(tag.attrs) == 2)[:2])
print(bs.findAll(lambda tag: tag.get_text() == 'Or maybe he\'s only resting?'))
print(bs.findAll('', text='Or maybe he\'s only resting?'))