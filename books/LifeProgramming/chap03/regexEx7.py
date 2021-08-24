# 특정 단어의 예문만 모아 파일로 저장하기
import os, re   # os, re 모듈을 임포트한다.
os.chdir(r'C:\Users\shg72\Documents\GitHub\PythonProject\LifeProgramming\chap03')   # 자신이 드라마 대사를 저장해둔 폴더로 간다.
f = open('friends101.txt', 'r') # friends101.txt 파일을 읽기 모드로 열어 객체 f에 저장한다.
print(f.read(100))  # 100번째 글자까지만 읽어본다.
f.seek(0) # 읽은 다음에는 커서를 맨 앞으로 이동한다.
sentences = f.readlines()
print(sentences[:3])
f.seek(0)
for i in sentences[:20]:
    if re.match(r'[A-Z][a-z]+:', i):
        print(i)
lines = [i for i in sentences if re.match(r'[A-Z][a-z]+:', i)]
print(lines[:10])
would = [i for i in sentences if re.match(r'[A-Z][a-z]+:', i) and re.search('would', i)]
print(would)
take = [i for i in sentences if re.match(r'[A-Z][a-z]+:', i) and re.search('take', i)]
for i in take:
    print(i)
newf = open('would.txt', 'w')
newf.writelines(would)
newf.close()