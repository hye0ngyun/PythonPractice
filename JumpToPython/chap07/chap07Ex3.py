# 파이썬에서 정규 표현식을 지원하는 re모듈
import re
p = re.compile('ab*')   # re.compile()함수는 정규 표현식을 컴파일해 패턴객체를 리턴한다.
''' 정규식을 이용한 문자열 검색
메서드      목적
match()     문자열의 처음부터 정규식과 매치되는지 조사한다.
search()    문자열 전체를 검색하여 정규식과 매치되는지 조사한다.
findall()   정규식과 매치되는 모든 문자열(substring)을 리스트로 리턴한다.
finditer()  정규식과 매치되는 모든 문자열(substring)을 반복 가능한 객체로 리턴한다.
- match(), search()는 정규식과 매치될 때는 match객체를 리턴하고, 매치되지 않을 때는 None을 리턴한다.
-- match() 객체란 정규식의 검색 결과로 리턴되는 객체이다.
'''
# match() 메서드는 문자열의 처음부터 정규식과 매치되는지 조사한다.
p = re.compile('[a-z]+')
m = p.match('python')
print(m)    # <re.Match object; span=(0, 6), match='python'> -- match 객체가 리턴됨
m = p.match('3 python')
print(m)    # None
'''
p = re.compile(정규 표현식)
m = p.match('조사할 문자열')
if m:
    print('Match found : ', m.group())
else:
    print('No match')
'''
# search() 메서드는 문자열의 어느부분에 있어도 정규식과 매치되는지 조사한다.
m = p.search('python')
print(m)    # <re.Match object; span=(0, 6), match='python'>
m = p.search('3 python')
print(m)    # <re.Match object; span=(2, 8), match='python'>
# findall() 메서드는 
result = p.findall('life is too short') # p는 '[a-z]+'라는 패턴을 가지고있기 때문에 ['life', 'is', 'too', 'short'] 리스트를 리턴한다.
print(result)   # ['life', 'is', 'too', 'short']
result = p.finditer('life is too short')
print(result)   # <callable_iterator object at 0x0000010EEE8627F0>
for r in result: print(r)
'''
<re.Match object; span=(0, 4), match='life'>
<re.Match object; span=(5, 7), match='is'>
<re.Match object; span=(8, 11), match='too'>
<re.Match object; span=(12, 17), match='short'>
'''
# @@@ match 객체의 메서드
'''
메서드  목적
group() 매치된 문자열을 리턴한다.
start() 매치된 문자열의 시작 위치를 리턴한다.
end()   매치된 문자열의 끝 위치를 리턴한다.
span()  매치된 문자열의 (시작, 끝)에 해당되는 튜플을 리턴한다.
'''
p = re.compile('[a-z]+')
m = p.match('python')
print('m.group :', m.group())   # python -- 매치된 문자열 리턴
print('m.start :', m.start())   # 0 -- 매치된 문자열의 시작 인덱스 리턴
print('m.end :', m.end())       # 6 -- 매치된 문자열의 마지막 인덱스 리턴
print('m.span :', m.span())     # (0,6) -- 매치된 문자열의 (시작, 끝)인덱스를 튜플로 리턴
# match() 메서드를 수행한 결과로 리턴된 match 객체의 satrt()의 결과값은 항상 0일 수밖에 없다.
m = p.search('3 python')
print('m.group :', m.group())   # python -- 매치된 문자열 리턴
print('m.start :', m.start())   # 2 -- 매치된 문자열의 시작 인덱스 리턴
print('m.end :', m.end())       # 8 -- 매치된 문자열의 마지막 인덱스 리턴
print('m.span :', m.span())     # (2,8) -- 매치된 문자열의 (시작, 끝)인덱스를 튜플로 리턴
''' re모듈을 사용한 코드 간략화
p = re.compile('[a-z]+')
m = p.match('python')
위 두줄의 코드는 re 모듈을 이용해 축약해서 사용할 수 있다.
m = re.match('[a-z]+', 'python')
'''