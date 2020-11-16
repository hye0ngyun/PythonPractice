# html = urlopen("http://www.pythonscraping.com/pages/error.html") 
# 위 라인처럼 url을 불러오는 부분에서 발생할 수 있는 두가지 문제에대한 예외처리 방법
# 1. 페이지를 찾을 수 없거나, URL 해석에서 에러가 생긴 경우
# 2. 서버를 찾을 수 없는 경우
from urllib.request import urlopen
from urllib.request import HTTPError
from bs4 import BeautifulSoup

try:
    html = urlopen("http://www.pythonscraping.com/pages/error.html")
except HTTPError as e:
    print(e)
    # null을 반환하거나, break 문을 실행하거나, 기타 다른 방법을 사용
else:
    # 프로그램을 계속 실행합니다. except 절에서 return이나 break를 사용했다면
    # 이 else 절은 필요 없습니다.
    print('end of code')
# BeautifulSoup 객체에 있는 태그에 접근할 때 태그가 실존하는지 체크하는 방법