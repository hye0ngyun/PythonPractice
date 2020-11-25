import urllib.request as ur
from bs4 import BeautifulSoup as bs
import re, os, codecs, datetime, requests

os.chdir(r'C:\Users\shg72\Documents\GitHub\PythonProject\LifeProgramming\chpa06')

url = 'https://news.daum.net/'
soup = bs(ur.urlopen(url).read(), 'html.parser')
f = codecs.open(str(datetime.date.today()) + 'articles.txt', 'w', 'utf-8')
for i in soup.find_all('div', {'class' : 'item_issue'}):
    try:
        # 예외 처리
        # 제목을 추출해 파일에 쓰기
        f.write(i.text + '\n')
        # URL 주소를 추출해 파일을 씁니다.
        f.write(i.find_all('a')[0].get('href') + '\n')
        # URL 주소에 해당하는 웹 문서를 열어 새 뷰티풀수프 객체로 저장합니다.
        soup2 = bs(ur.urlopen(i.find_all('a')[0].get('href')).read(), 'html.parser')
        for j in soup2.find_all('p'):
            # <p>태그에서 본문만 추출
            f.write(j.text)
    except: # 예외 처리할때 except문 반드시 삽입
        pass

f.close()
