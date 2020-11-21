# 컴파일 옵션
''' 정규식을 컴파일할 때 다음과 같은 옵션을 사용할 수 있다.
옵션명      약어        설명
DOTALL      S       줄바꿈 문자를 포함하여 모든 문자와 매치할 수 있도록 한다.
IGNORECASE  I       대-소문자에 관계 없이 매치할 수 있도록 한다.
MULTILINE   M       여러 줄과 매치할 수 있도록 한다.(^, $ 메타 문자의 사용과 관계가 있는 옵션이다.)
VERBOSE     X       verbose 모드를 사용할 수 있도록 한다.(정규식을 보기 편하게 만들 수도 있고 주석 등을 사용할 수도 있다.)
'''
import re
p = re.compile('a.b')
m = p.match('a\nb')
print(m)    # None -- 문자열과 정규식이 매치되지 않음

# DOTALL, S -- .메타문자는 줄바꿈 문자(\n)을 제외한 모든 문자와 매치된다. 만약 \n문자도 포함하여 매치하고 싶다면 re.DOTALL 또는 re.S 옵션을 사용해 정규식을 컴파일하면 된다.
p = re.compile('a.b', re.DOTALL)
m = p.match('a\nb')
print(m)    # <re.Match object; span=(0, 3), match='a\nb'>
m = re.match('a.b', 'a\nb', re.DOTALL)
print(m)    # <re.Match object; span=(0, 3), match='a\nb'>

# IGNORECASE, I -- 대-소문자 구분 없이 매치를 수행하고자 할 때 사용하는 옵션이다.
p = re.compile('[a-z]+', re.I)
print(p.match('python'))    # <re.Match object; span=(0, 6), match='python'>
print(p.match('Python'))    # <re.Match object; span=(0, 6), match='Python'>
print(p.match('PYTHON'))    # <re.Match object; span=(0, 6), match='PYTHON'>

# MULTILINE, M -- ^, $ 메타 문자를 문자열의 각 라인마다 적용해 준다.
p = re.compile(r'^python\s\w+')  # 시작 문자역이 python이고 whitespace가 온뒤에 아무문자가 반복
data = '''python one
life is too short
python two
you need python
python three'''
print(p.findall(data))  # ['python one']
p = re.compile(r'^python\s\w+', re.MULTILINE)
print(p.findall(data))  # ['python one', 'python two', 'python three']

# VERBOSE, X -- 패턴에 주석을 적을 수 있고 라인 단위로 구분할 수 있다.
charref = re.compile(r'''
$[#]                    # Start of a numeric entity reference
(
        0[0-7]+         # Octal form
    |   [0-9]+          # Decimal form
    |   x[0-9a-fA-F]+   # Hexadecimal form
)
;                       # Trailing semicolon
''', re.VERBOSE)
# re.VERBOSE 옵션을 사용하면 문자열에 사용된 whitespace는 컴파일 시 제거된다.(단 []내에 사용된 whitespace는 제외). 그리고 줄 단위로 #기호를 이용해서 주석문을 작성할 수 있다.

# 백슬래시 문제
'''
\section은 [ \t\n\r\f\v]ection과 동일하다. -- 여기서 \s는 문자그대로의 \s가 아닌 [ \t\n\r\f\v]로 해석된다.
\\section은 sectio으로 해석된다.
'''
p = re.compile('\\section')     # 정규식 엔진에 의해 \\가 \로 바뀌어 원하는 결과 얻을 수 없다.
p = re.compile('\\\\section')   # 이렇게 해야 원하는 '\section'패턴을 얻을 수 있다.
p = re.compile(r'\\section')    # 위와 같이 복잡한 식을 간소하게 하기 위해 r''(Raw String)규칙을 사용한다. 문자열 앞에 r문자를 삽입하면 정규식은 Raw String 규칙에 의해서 백슬래시 2개 대신 1개만 써도 2개를 쓴 것과 동일한 의미를 갖게 된다.