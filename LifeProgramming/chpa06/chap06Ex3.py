import urllib.request as ur
from bs4 import BeautifulSoup as bs
import re, os

# 파일을 저장할 경로를 지정함 Raw String r''
os.chdir(r'C:\Users\shg72\Documents\GitHub\PythonProject\LifeProgramming\chpa06')
# URL을 news라는 객체에 문자열 형태로 입력
news = 'https://news.daum.net/'

soup = bs(ur.urlopen(news).read(), 'html.parser')
# print(soup)

# ----- 2. find_all로 <div> 내용 추출하기
# 머리기사 제목 추출하기
for i in soup.find_all('div', {'class' : 'item_issue'}):
    print(i.text)
print('-'*50)

# ----- 3. <a>태그만 추출하기
print(soup.find_all('a')[:5])

# ----- 4. href 속성값 추출하기
# a.get('속성')
for i in soup.find_all('a')[:5]:
    print(i.get('href'))    # i에서 href속성값만 가져옵니다.
print('-'*50)

for i in soup.find_all('div', {'class' : 'item_issue'}):
    print(i.find_all('a')[0].get('href'))
# print(i.find_all('a').get('href'))이렇게 바로 get을 사용한다면 오류가 발생한다. 그 이유는 find_all의 결괏값이 리스트형이기 떄문이다. 이는 find_all, text를 사용할때도 마찬가지이다.
''' 머리기사 4개에 해당하는 링크 추출 완료
https://news.v.daum.net/v/20201125010012854
https://news.v.daum.net/v/20201125001100542
https://news.v.daum.net/v/20201124193232488
https://news.v.daum.net/v/20201124193101395
'''

# ----- 5. 기사 제목 가져오기
article1 = 'https://news.v.daum.net/v/20201125001100542'
soup2 = bs(ur.urlopen(article1).read(), 'html.parser')
headline = soup.find_all('div', {'class' : 'item_issue'})
#for i in soup2.find_all('p'):
    #print(i.text)
print('-'*50)

for i in headline:
    # headline 객체에서 <div> 태그를 하나씩 가져옵니다.
    print(i.text, '\n')
    # 기사 제목을 출력합니다.
    soup3 = bs(ur.urlopen(i.find_all('a')[0].get('href')).read(), 'html.parser')
    # 해당 기사가 올라와 있는 웹 사이트를 열어 soup3객체에 저장합니다.
    for j in soup3.find_all('p'):
        print(j.text)