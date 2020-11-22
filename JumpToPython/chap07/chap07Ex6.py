# 파이썬으로 XML 처리하기
# XML 문서 생성하기
from xml.etree.ElementTree import Element, SubElement, dump, ElementTree, parse
note = Element('note')
to = Element('to')
to.text = 'Tove'
note.append(to)
dump(note)  # <note><tp>Tove</tp></note>

# SubElement
SubElement(note, 'from').text = 'Jani'
dump(note)  # <note><tp>Tove</tp><from>Jani</from></note>

# insert(), remove()
dummy = Element('dummy')
note.insert(1, dummy)
dump(note)  # <note><tp>Tove</tp><dummy /><from>Jani</from></note>
note.remove(dummy)
dump(note)  # <note><tp>Tove</tp><from>Jani</from></note>

# 에트리뷰트 추가하기
note.attrib['date'] = '20120104'    # note = Element('note', date = '20120104')와 같은 의미이다.
dump(note)  # <note date="20120104"><tp>Tove</tp><from>Jani</from></note>

SubElement(note, 'heading').text = 'Reminder'
SubElement(note, 'body').text = 'Don\'t forget me this weekend!'
dump(note)  # <note date="20120104"><to>Tove</to><from>Jani</from><heading>Reminder</heading><body>Don't forget me this weekend!</body></note>

# indent 함수를 이용해서 정렬된 형태의 xml 값으로 만들기
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

indent(note)
dump(note)
'''
<note date="20120104">
 <to>Tove</to>
 <from>Jani</from>
 <heading>Reminder</heading>
 <body>Don't forget me this weekend!</body>
</note>
'''
print('-'*20,'pares','-'*20)
# 파일에 쓰기(write) 수행하기
# ElementTree(note).write('note.xml')
# XML 문서 파싱하기
tree = parse('note.xml')
note = tree.getroot()
dump(note)

# 애트리뷰트 값 읽기
print(note.get('date')) # 20120104
print(note.get('foo', 'default'))   # default
print(note.keys())  # ['date']
print(note.items()) # [('date', '20120104')]

# XML 태그 접근하기
from_tag = note.find('from')
from_tags = note.findall('from')
from_text = note.findtext('from')

# 특정 태그의 모든 하위 앨리먼트를 순차적으로 처리할 때는 아래 메서드를 사용한다.
childs = note.getiterator()
childs = note.getchildren()