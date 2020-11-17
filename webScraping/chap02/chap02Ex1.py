from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('https://www.pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html, 'html.parser')
nameList = bs.findAll('span', {'class': 'green'})
# bs.findAll(tagname, tagAttributes)는 페이지의 채그 전체를 찾는다.
for name in nameList:
    print(name.get_text())  # 리스트의 모든 이름을 name.get_text()를 호출해 태그를 제외하고 컨텐츠만 출력한다.
# find()와 findAll()
# findAll(tag, attributes, recursive, text, limit, keywords)
# find(tag, attributes, recursive, text, keywords)
# 실제로 이 함수들을 사용할 때는 매개변수 tag와 attributes만 사용한다.
print('-'*20)
tag = bs.findAll({'h1', 'h2', 'h3', 'h4', 'h5'})    # 문서의 모든 제목 태그를 반환한다.
for t in tag:
    print(t.get_text())
print('-'*20)
for a in bs.findAll('span', {'class': {'green', 'red'}}):
    print(a.get_text())
# 페이지에서 태그로 둘러싸인 'the prince'가 몇 번 나타났는지 알기 위한 코드
nameList = bs.findAll(text = 'the prince')  # 태그미포함 리스트형으로 반환
print(len(nameList))
print(nameList)
# keywords 매개변수는 특정 속성이 포함된 태그를 선택할 때 사용한다.
title = bs.findAll(id='title', class_='text')
# 아래 두 코드는 완전히 같다.
bs.findAll(id='text')           # and필터처럼 동작
bs.findAll('', {'id':'text'})   # or필터처럼 동작
# Tag 객체
bs.div.h1
# NavigableString 객체 : 태그 자체가 아니라 태그 안에 들어있는 텍스트를 나타낸다.
# Comment 객체 : 주석 태그 안에 들어있는 HTML 주석(<!-- -->)을 찾는 데 사용