# bs4를 이용해 url읽어들인 후 태그 스크래핑
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/page1.html")
bsObj = BeautifulSoup(html.read(), "html.parser")
print(bsObj.h1) # html 사이트 내의 h1 태그를 스크래핑해라
#print(bsObj.html.body.h1, bsObj.body.h1, bsObj.html.h1) # 모두 같은 결과를 보여준다.

# BeautifulSoup 객체에 있는 태그에 접근할 때 태그가 실존하는지 체크하는 방법
#print(bsObj.nonExistentTag.someTag)
# AttributeError: 'NoneType' object has no attribute 'someTag'
try:
    badContent = bsObj.nonExistentTag.anotherTag
except AttributeError as e:
    print('Tag was not found')
else:
    if badContent == None:
        print('Tag was not found')
    else:
        print(badContent)