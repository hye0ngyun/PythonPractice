# 1. 다음 중 정규식 'a[.]{3,}b'과 매치되는 문자열은? B. a....b
# A. acccb  B. a....b   C. aaab D. a.cccb
''' 2. 다음 코드의 결과값은? 2 + 8 = 10
import re
p = re.complie('[a-z]+')
m = p.search('5 python')
m.start() + m.end()
'''
import re
p = re.compile('[a-z]+')
m = p.search('5 python')
print(m.start(), m.end())
print(m.start() + m.end())
# 3. 다음과 같은 문자열에서 핸드폰 번호 뒷자리인 숫자 4개를 ####로 바꾸는 프로그램을 정규식으로 작성해보자.
s = '''
park 010-9999-9988
kim 010-9909-7789
lee 010-8789-7768
'''
p = re.compile(r'(?P<a>\w+\s\d+[-]\d+[-])\d+')
m = p.sub(r'\g<a>####', s)
print(m)
''' result
park 010-9999-####
kim 010-9909-####
lee 010-8789-####
'''
''' 4.다음은 이메일 주소를 나타내는 정규식이다. 이 정규식은 park@naver.com, kim@daum.net, lee@myhome.co.kr 등과 매치된다. 긍정형 전방 탐색 기법을 이용하여 .com, .net이 아닌 이메일 주소는 제외시키는 정규식을 작성해 보자
'''
s = ['park@naver.com', 'kim@daum.net', 'lee@myhome.co.kr']
p = re.compile(r'.*[@].*[.](?=com|net).*$')
for i in s:
    print((p.match(i)))
''' result
<re.Match object; span=(0, 14), match='park@naver.com'>
<re.Match object; span=(0, 12), match='kim@daum.net'>
None
'''
# 5. ElementTree를 이용하여 다음 XML 문서를 작성하고 파일에 저장해 보자.
from xml.etree.ElementTree import Element, dump, SubElement, ElementTree, parse
blog = Element('blog')
blog.attrib['date'] = '20151231'
SubElement(blog, 'subject').text = 'Why python?'
SubElement(blog, 'author').text = 'Eric'
SubElement(blog, 'content').text = 'Life is too short, You need Python!'
def indent(elem, level=0):
    i = '\n' + level*' '
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + ' '
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level + 1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

indent(blog)
ElementTree(blog).write('blog.xml')
dump(blog)
''' result
<blog date="20151231">
 <subject>Why python?</subject>
 <author>Eric</author>
 <content>Life is too short, You need Python!</content>
</blog>
'''