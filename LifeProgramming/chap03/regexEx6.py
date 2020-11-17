import os, re, codecs
os.chdir(r'C:\Users\shg72\Documents\GitHub\PythonProject\LifeProgramming\chap03')
f = codecs.open('friends101.txt', 'r', encoding = 'utf-8')
script101 = f.read()
# 지문(~)만 출력하기
print(re.findall(r'\([A-Za-z].+[a-z:\.]\)', script101)[:6])
'''
r' :문자열 앞에는 습관적으로 r을 붙인다.
\( :(를 메타 문자로 인식하지 않도록 \를 붙여준다.
[A-Za-z] :괄호 다음에는 공백 없이 영문자가 온다.
.+ :문자/숫자/빈칸 등이 자유롭게 반복된다.
[a-z:\.] :마지막 글자로 영어 소문자 또는 마침표가 온다.
\)' :)로 괄호를 닫고 문자열 작성을 끝낸다.
'''