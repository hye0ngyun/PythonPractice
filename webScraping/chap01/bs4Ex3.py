# BeautifulSoup 객체에 있는 태그에 접근할 때 태그가 실존하는지 체크하는 방법
from urllib.request import urlopen
from urllib.request import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), 'html.parser')
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title
title = getTitle('http://www.pythonscraping.com/pages/page1.html')
if title == None:
    print('Title could not be found')
else:
    print(title)