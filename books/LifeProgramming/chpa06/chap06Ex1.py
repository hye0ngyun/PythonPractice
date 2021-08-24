import urllib.request as ur
from bs4 import BeautifulSoup as bs

# ----- 1. urlopen으로 웹 사이트 정보 가져오기
url = 'http://quotes.toscrape.com'
# urlopen 사용법 urllib.request.urlopen('URL 주소')
html = ur.urlopen(url)
# url 객체에 저장된 URL 주소에 해당하는 웹 사이트를 불러옵니다.
print(html) # <http.client.HTTPResponse object at 0x0000025CF3973A60>
# html에 어떤 내용이 들어있는지 확인하기 위해 read()로 간단히 살펴본다.
print(html.read()[:100])    # b'<!DOCTYPE html>\n<html lang="en">\n<head>\n\t<meta charset="UTF-8">\n\t<title>Quotes to Scrape</title>\n -- html에 저장된 웹 사이트 자료가 일부 출력됩니다.

# ----- 2. 뷰티풀수프로 자료형 변환하기
# 뷰티풀수프를 사용해 html 객체에 저장한 자료를 정보를 쉽게 추출할 수 있는 형태, 즉 파싱(parsing)하기 쉬운 형태로 변환시킨다.
# 파싱(parsing)이란 웹 문서에서 원하는 패턴이나 순서로 자료를 추출해 가공하는 것을 말합니다.
# bs4 사용법 bs(html.read(), 'html.parser')

soup = bs(html.read(), 'html.parser')
print(soup)
print(type(html), type(soup))   # <class 'http.client.HTTPResponse'> <class 'bs4.BeautifulSoup'>

# ----- 3. 한 줄로 모든 명령을 실행하는 마법의 명령어 만들기
soup = bs(ur.urlopen('http://quotes.toscrape.com').read(), 'html.parser')

print(soup)
