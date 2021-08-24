import urllib.request as ur
from bs4 import BeautifulSoup as bs

# ----- 3. 한 줄로 모든 명령을 실행하는 마법의 명령어 만들기
soup = bs(ur.urlopen('http://quotes.toscrape.com').read(), 'html.parser')
#print(soup)

# ----- 4. find_all로 원하는 태그만 모으기
# find_all사용법 soup.find_all(찾아낼 태그)
print('-'*50)
#print(soup.find_all('span'))    # span태그만 추출해서 가져오기
# find_all은 리스트로 결과물을 돌려준다.

# ----- 5. 태그에서 텍스트만 출력하기
quote = soup.find_all('span')   # <span> 태그만 모아 quote객체에 저장합니다.
print(quote[0]) # <span class="text" itemprop="text">“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”</span>
# <span>태그를 없앤 내용을 얻기 위해서는 quote[0].text를 이용한다.
print(quote[0].text)    # “The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”
print('-'*50)
# 전체 내용을 태그 미포함으로 출력하기
for i in quote:
    print(i.text)
print('-'*50)

# ----- 6. <div>태그 안에 정의된 특정 클래스를 찾아가는 방법
for i in soup.find_all('div', {'class' : 'quote'}):
    print(i.text)
