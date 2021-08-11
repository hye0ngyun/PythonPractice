# Flask를 사용하기 위한 모듈 임포트
from flask import Flask
# 모듈을 읽어 들입니다.(import)
from urllib import request
from bs4 import BeautifulSoup

app = Flask(__name__)

# 데코레이터 @
@app.route('/')
def hello():
  # urlopen()함수로 기상청의 전국 날씨를 읽습니다.
  target = request.urlopen('http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108')

  # BeautifulSoup을 사용해 웹 페이지를 분석합니다.
  soup = BeautifulSoup(target, 'html.parser')

  output = ''
  # location 태그를 찾습니다.
  for location in soup.select('location'):
    #내부의 city, wf, tmn, tmx 태그를 찾아 출력합니다.
    output += f'<h3>도시: {location.select_one("city").string}</h3>'
    output += f'날씨: {location.select_one("wf").string}<br>'
    # tmn은 temperature min으로 예상됨 # tmx는 temperature max로 예상됨
    output += f'최저/최고 기온: {location.select_one("tmn").string}/{location.select_one("tmx").string}'
    # 가독성을 위한 수평 줄 추가
    output += '<hr>'
  
  # 화면에 그려질 HTML 코드
  return output