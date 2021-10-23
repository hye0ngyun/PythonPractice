# write 함수
f = open("newfile.txt", 'w', encoding="utf-8")
for i in range(1, 11):
  data = "%d번째 줄입니다.\n" % i
  f.write(data)
f.close()

# readline 함수
f = open('newfile.txt', 'r', encoding='utf-8')
line = f.readline()
print(line)
f.close()

# 모든 줄 읽기
f = open('newfile.txt', 'r', encoding='utf-8')
while True:
  line = f.readline()
  if not line: break
  print(line)
f.close()
print(not '')

# readlines 함수
f = open('newfile.txt', 'r', encoding='utf-8')
lines = f.readlines()
print(type(lines)) # list
for line in lines:
  print(line)
f.close()

# 줄 바꿈 문자 제거하기
f = open('newfile.txt', 'r', encoding='utf-8')
lines = f.readlines()
print(type(lines)) # list
for line in lines:
  print(line.strip())
f.close()

# read 함수
f = open('newfile.txt', 'r', encoding='utf-8')
data = f.read()
print(type(data)) # str
print(data)
f.close()