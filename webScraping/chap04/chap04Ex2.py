# 수집할 정보에 대응하는 CSS선택자를 각각 문자열 하나로 만들고, 이들을 딕셔너리 객체에 모아서 BeautifulSoup select함수와 사용하는 기법
# Content는 \
import requests
from bs4 import BeautifulSoup
class Content:
    '''
    글/페이지 전체에 사용할 기반 클래스
    '''

    def __init__(self, url, title, body):
        self.url = url
        self.title = title
        self.body = body

    def print(self):
        '''
        출력 결과를 원하는 대로 바꿀 수 있는 함수
        '''
        print('URL: {}'.format(self.url))
        print('TITLE: {}'.format(self.title))
        print('BPDY: {}'.format(self.body))

# Website 클래스는 각 페이지에서 수집한 정보를 저장하는 것이 아니라, 해당 데이터를 수집하는 방법에 대한 지침을 저장합니다.
class Website:
    '''
    웹사이트 구조에 관한 정보를 저장할 클래스
    '''

    def __init__(self, name, url, titleTag, bodyTag):
        self.name = name
        self.url = url
        self.titleTag = titleTag
        self.bodyTag = bodyTag

# ----- 


class Crawler:

    def getPage(self, url):
        try:
            req = requests.get(url)
        except requests.exceptions.RequestException:
            return None
        return BeautifulSoup(req.text, 'html.parser')
    def safeGet(self, pageObj, selector):
        '''
        BeautifulSoup객체와 선택자를 받아 콘텐츠 문자열을 추출하는 함수
        주어진 선택자로 검색된 결과가 없다면 빈 문자열을 반환합니다.
        '''
        selectedElems = pageObj.select(selector)
        if selectedElems is not None and len(selectedElems) > 0:
            return '\n'.join([elem.get_text() for elem in selectedElems])
        return ''
    def parse(self, site, url):
        '''
        URL을 받아 콘텐츠를 추출합니다.
        '''
        bs = self.getPage(url)
        if bs is not None:
            title = self.safeGet(bs, site.titleTag)
            body = self.safeGet(bs, site.bodyTag)
            if title != '' and body != '':
                content = Content(url, title, body)
                content.print()

crawler = Crawler()
siteData = [
    ['O\'Reilly Media', 'http://oreilly.com', 'h1', 'section#product-description'],
    ['Reuters', 'http://reuters.com', 'h1', 'div.StandardArticleBody_body_1gnLA']
]
websites = []
urls = [
    'http://shop.oreiily.com/product/0636920028154.do',
    'http://www.reuters.com/article/us-usa-epa-pruitt-idUSKBN19W2D0'
]
for row in siteData:
    websites.append(Website(row[0], row[1], row[2], row[3]))

crawler.parse(websites[0], urls[0])
crawler.parse(websites[1], urls[1])
