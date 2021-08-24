import re
# re.split(패턴, 문자열)
# split은 특정한 패턴이 등장할 때 문자열을 나눕니다. 
sentence = 'I have a lovely dog, really. I am not relling a lie. What a pretty dog! I love this dog.'
print(re.split(r'[.?!]', sentence))
# 문자열에서 [.?!] '.','?','!'이 나올때마다 문자열 리턴
data = 'a:3; b:4; c:5'
for i in re.split(r';', data):
    print(re.split(r':', i))

# re.sub(찾을 패턴, 대체할 문자, 찾을 문자열)
# 정규표현식 sub는 대체하다(substitute)의 줄임말이다.
print(re.sub(r'dog', r'cat', sentence))
# sentence에서 'dog' 를 'cat'으로 대체

words = 'I am home now. \n\n\nI am with my cat.\n\n'
print(words)
print(re.sub(r'\n', '', words))

# ly로 끝나는 단어 추출하기
sentence = 'I have a lovely dog, really. I am not relling a lie.'
print(re.findall(r'[A-Za-z가-힣]+ly', sentence)) # 내답
print(re.findall(r'\w+ly', sentence)) # 책 답