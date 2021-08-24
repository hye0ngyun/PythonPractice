# 강력한 정규 표현식
# | 메타 문자는 or과 동일한 의미로 사용된다. A|B라는 정규식은 A 또는 B가 된다.
import re
p = re.compile('Crow|Servo')
m = p.match('CrowHello')
print(m)    # <re.Match object; span=(0, 4), match='Crow'>

# ^ 메타 문자는 문자열의 맨 처음과 일치됨을 의미한다.
# \A는 ^ 메타 문자와 동일한 의미이지만 re.MULTLINE 옵션을 적용해도 라인과 상관없이 전체 문자열의 처음하고만 매치된다.
print(re.search('^Life', 'Life is too short'))  # <re.Match object; span=(0, 4), match='Life'>
print(re.search('^Life', 'My Life'))    # None

# $ 메타 문자는 문자열의 맨 마지막과 일치됨을 의미한다.
# \Z는 $ 메타 문자와 동일한 의미이며, \A와 마찬가지로 re.MULTILINE 옵션과 상관없이 전체라인에서 마지막에만 매치된다.
print(re.search('short$', 'LIfe is too short')) # <re.Match object; span=(12, 17), match='short'>
print(re.search('short$', 'Life is too short, you need python'))    # None

# \b는 단어 구분자(Word boundary)이다. 보통 단어는 whitespace에 의해 구분이 된다.
p = re.compile(r'\bclass\b')    # \b 메타문자는 파이썬 리터럴 규칙에 의해 백스페이스로 인식하기 때문에 백스페이스가 아닌 단어 구분자임을 알려주기 위해 반드시 r'\bclass\b'처럼 Raw string임을 알려주는 r 기호를 반드시 붙여야 한다.
print(p.search('no class at all'))  # <re.Match object; span=(3, 8), match='class'>
print(p.search('the declassified algorithm'))   # None -- class 앞뒤에 whitespace가 없기때문에 매치되지 않음
print(p.search('one subclass is'))  # None -- class 앞에 whitespace가 없기때문에 매치되지 않음
# \B는 \b의 반대이다. 즉, whitespace로 구분된 단어가 아닌 경우 매치된다.
p = re.compile(r'\Bclass\B')
print(p.search('no class at all'))  # None
print(p.search('the declassified algorithm'))   # <re.Match object; span=(6, 11), match='class'>
print(p.search('one subclass is'))  # None
print('-'*20,'그룹핑','-'*20)
# 그룹핑은 문자열이 특정 패턴으로 계속해서 반복되는지 조사하고 싶을때 사용할 수 있다.
p = re.compile(r'(ABC)+')
m = p.search('ABCABCABC OK?')
print(m)    # <re.Match object; span=(0, 9), match='ABCABCABC'>
print(m.group(0))
p = re.compile(r'\w+\s+\d+[-]\d+[-]\d+')    # "이름 + ' ' + 전화번호" 패턴을 찾는 정규식
m = p.search('park 010-1234-1234')
print(m.group())
p = re.compile(r'(\w+)\s+\d+[-]\d+[-]\d+')    # "(이름) + ' ' + 전화번호" 패턴을 찾는 정규식
m = p.search('park 010-1234-1234')
print(m.group(1))
'''
group(인덱스)           설명
group(0)        매치된 전체 문자열
group(1)        첫 번째 그룹에 해당되는 문자열
group(2)        두 번째 그룹에 해당되는 문자열
group(n)        n 번째 그룹에 해당되는 문자열
'''
p = re.compile(r'(\w+)\s+((\d+)[-]\d+[-]\d+)')    # "이름 + ' ' + 전화번호" 패턴을 찾는 정규식
m = p.search('park 010-1234-1234')
print(m.group(0, 1, 2, 3))

# 그룹핑된 문자열 재참조하기(연속적 매치)
p = re.compile(r'(\b\w+)\s+\1') # (구분자 + 아무문자 1번이상 반복) + 화이트스페이스 1번이상 반복 + 그룹핑(1)문자열 재참조
m = p.search('Paris in the the spring').group()
print(m)    # the the
# \1은 정규식의 그룹 중 첫 번쨰 그룹을 지정한다. 두 번째 그룹을 참조하려면 \2를 사용하면 된다.

# 그룹핑된 문자열에 이름 붙이기
p = re.compile(r'(?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)')
m = p.search('park 010-1234-1234')
print('m.group(\'name\')', m.group('name'))  # park
# 그룹명을 이용해서 재참조하기
p = re.compile(r'(?P<word>\b\w+)\s+(?P=word)')
m = p.search('Paris in the the spring').group()
print(m)    # the the

# 전방 탐색
p = re.compile('.+:')
m = p.search('http://google.com')
print(m.group())    # http:
'''
정규식  종류                설명
(?=...) 긍정형 전방 탐색    ...에 해당되는 정규식과 매치돼야하며 조건이 통과돼도 문자열이 소모되지 않는다.
(?!...) 부정형 전방 탐색    ...에 해당되는 정규식과 매치되지 않아야 하며 조건이 통과돼도 문자열이 소모되지 않는다.
'''
p = re.compile('.+(?=:)')
m = p.search('http://google.com')
print(m.group())    # http
p = re.compile('.*[.](?!bat$).*$')  # 부정형 전방 탐색 *.bat을 제외한 확장자명 매치
# m = p.search('autoexec.bat').group()    # AttributeError: 'NoneType' object has no attribute 'group'
p = re.compile('.*[.](?!bat$|exe$).*$') # *.bat과 *.exe를 제외한 확장자명 매치

# 문자열 바꾸기 sub메서드 sub(바꿀 문자열, 대상 문자열)
p = re.compile('(blue|white|red)')
print(p.sub('colour', 'blue socks and red socks'))  # colour socks and colour socks
# 문자열 바꾸기 횟수를 지정할 때는 sub(바꿀 문자열, 대상 문자열, count = 반복할 횟수)
print(p.sub('colour', 'blue socks and red socks', count=1)) # colour socks and red socks
print(p.subn('colour', 'blue socks and red socks', count=1)) # ('colour socks and red socks', 1) -- (변경된 문자열, 변경된 횟수) 튜플형태로 리턴

# sub 메서드 사용 시 참조 구문 사용하기 \g<그룹명>
p = re.compile(r'(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)')
print(p.sub(r'\g<phone> \g<name>', 'park 010-1234-1234'))    # 010-1234-1234 park
print(p.sub(r'\g<2> \g<1>', 'park 010-1234-1234'))    # 010-1234-1234 park

# sub 메서드의 입력 인수로 함수 넣기
def hexrepl(match):
    # Return the hex string for a decimal number
    value = int(match.group())
    return hex(value)
p = re.compile(r'\d+')
m = p.sub(hexrepl, 'Call 65490 for printing, 49152 for user code.')
print(m)    # Call 0xffd2 for printing, 0xc000 for user code.

# Greedy vs Non-Greedy
s = '<html><head><title>Title</title>'
print(len(s))
print(re.match('<.*>', s).span())   # (0, 32)
# Greedy
print(re.match('<.*>', s).group())  # <html>만 매치되길 기대했으나 결과는 <html><head><title>Title</title>가 매치됨
# Non-Greedy
print(re.match('<.*?>', s).group()) # <html>만 매치됨
# non-greedy 문자인 ?를 사용해 *,+의 탐욕을 제어할 수 있다.
# ?는 *?, +?, ??, {m, n}?과 같이 사용할 수 있다.
# 가능한 한 가장 최소한의 반복을 수행하도록 도와주는 역할을 한다.