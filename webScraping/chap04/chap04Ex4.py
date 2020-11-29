import requests
from bs4 import BeautifulSoup
import re
class Website:
    def __init__(self, name, url, targetPattern, absoluteUrl, titleTag, bodyTag):
        self.name = name
        self.url = url
        self.targetPattern = targetPattern
        self.absoluteUrl = absoluteUrl
        self.titleTag = titleTag
        self.bodyTag = bodyTag
class Content:
    '''
    글 페이지 전체에 사용할 기반 클래스
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
        print('BODY: {}'.format(self.body))
class Crawler:
    def __init__(self, site):
        self.site = site
        self.visited = []
    def getPage(self, url):
        try:
            req = requests.get(url)
        except requests.exceptions.RequestException:
            return None
        return BeautifulSoup(req.text, 'html.parser')
    def safeGet(self, pageObj, selector):
        selectedElems = pageObj.select(selector)
        if selectedElems is not None and len(selectedElems) > 0:
            return '\n'.join([elem.get_text() for elem in selectedElems])
        return ''
    def parse(self, url):
        bs = self.getPage(url)
        if bs is not None:
            title = self.safeGet(bs, self.site.titleTag)
            body = self.safeGet(bs, self.site.bodyTag)
            if title != '' and body != '':
                content = Content(url, title, body)
                content.print()
    def crawl(self):
        '''
        사이트 홈페이지에서 페이지를 가져옵니다.
        '''
        bs = self.getPage(self.site.url)
        targetPages = bs.findAll('a', href=re.compile(self.site.targetPattern))
        for targetPage in targetPages:
            if targetPage not in self.visited:
                self.visited.append(targetPage)
                if not self.site.absoluteUrl:
                    targetPage = '{}{}'.format(self.site.url, targetPage)
                self.parse(targetPage)
reuters = Website(
    'Reuters',                      # Website.name
    'https://www.reuters.com',      # Website.Url    
    '^(/article/)',                 # Website.targetPattern
    False,                          # Website.absoluteUrl
    'h1',                           # Website.titleTag
    'div.StandardArticleBody_body', # Website.bodyTag
)
crawler = Crawler(reuters)
crawler.crawl()