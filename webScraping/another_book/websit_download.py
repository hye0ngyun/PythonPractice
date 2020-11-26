# websit_download.py
from urllib.request import urlopen
from urllib.error import HTTPError
import requests

# URL이 전달됐을 떄 웹 페이지를 다운로드하고 HTML을 반환한다.
# 이 코드는 웹페이지를 다운로드할때 처리가 안되는 오류를 직면할 수 있다.
# 요청한 페이지가 존재하지 않는 경우다.
def download(url, user_agent = 'wswp', num_retries = 2):
    print('Downloading : ', url)
    # Forbidden 에러를 위한 헤더 에이전트 설정
    headers = {'User-agent' : user_agent}
    request = requests(url, headers)
    # 오류상황에 예외처리를 한 소스코드.
    try:
        html = urlopen(request).read().decode('utf-8')
    except HTTPError as e:
        print('Download error : ', e.reason)
        html = None
        # 다운로드 재시도
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                # 5xx HTTP 오류 시 재시도
                return download(url, num_retries - 1)
    return html

#response = requests.get('http://httpstat.us/500', headers={"User-Agent": "Mozilla/5.0"})
#print(response)
download('http://httpstat.us/500', 3)
