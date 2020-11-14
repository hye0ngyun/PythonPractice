import os, re, codecs
os.chdir(r'C:\Users\shg72\Documents\GitHub\PythonProject\LifeProgramming\chap03')
f = codecs.open('friends101.txt', 'r', encoding = 'utf-8')
script101 = f.read()
Line = re.findall(r'Monica:.+', script101)
# 'Monica:' 이후 아무문자가 1번이상 반복되는 패턴을 script101에서 찾아 리스트로 반환
#for i in Line[:3]:
#    print(i)
f.close()
f = open('monica.txt', 'w', encoding = 'utf-8')
monica = ''
for i in Line:
    monica += i
print(monica)
f.write(monica)
f.close()

char = re.compile(r'[A-Z][a-z]+:')
# [A-Z]는 대문자 전체, [a-z]는 소문자 전체를 의미한다.
# 대문자로 시작해서 소문자 1번이상 반복되며 :으로 끝나는 패턴
# print(re.findall(char, script101))
# 등장인물의 이름이 중복되게 출력
y = set(re.findall(char, script101))
# 중복 출력되는 등장인물의 이름은 set()집합으로 만들어 중복 제거
z = list(y)
character = []
for i in z:
    character += [i[:-1]]

print(character)

# 등장인물을 뽑아내는 코드를 한줄로 작성하기
character2 = [x[:-1] for x in list(set(re.findall(r'[A-Z][a-z]+:', script101)))]
print(character2)
r'\(+[A-Za-z ]\)'