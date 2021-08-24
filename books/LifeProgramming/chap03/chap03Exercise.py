import re
# words 리스트에 저장된 여러 단어 중 a로 시작하는 단어만 출력하려한다.
words = ['apple','cat','brave','dream','drama','arise','blow','coat','above']
for i in words:
    m = re.match(r'a\D+', i)
    if m:
        print(m)
# a에 저장한 문자열에서 메일 주소만 추출해 리스트에 반환하려 한다.
a = '제 이메일 주소는 greatking@naver.com입니다. 오늘 저는 travel@daum.net 라는 주소로 메일을 보내려고 합니다. 저는 apple@gmail.com, life@abc.co.kr 라는 메일도 사용하고 있습니다.'
b = re.findall(r'[a-z]+@.+?[a-z.]+', a)
print(b)
# exam에 저장한 문자열에서 연도만 추출해 리스트로 반환하기 위해 다음과 같이 명령했다. 그러나 값이 제대로 나오지 않는데 제대로 나오도록 코드를 수정하라.
exam = '저는 92년에 태어났습니다. 88년에는 올림픽이 있었습니다. 지금은 2020년입니다.'
print(re.findall(r'\d.+년', exam))  # 탐욕적인 코드
print(re.findall(r'\d+년', exam))   # 탐욕제어 코드
print(re.findall(r'[\d.]+년', exam))# 탐욕제어 코드
# d에 다음과 같은 문자열이 저장되어 있을때, 문장을 하나씩 추출해 하나의 리스트에 저장하려 한다.
d = 'I have a dog. I am not a girl. You are not alone. I am happy.'
print(str(re.findall(r'[A-Z].+?\.', d)).replace('.', ''))
# 다음과 같이 e에 대사와 지분이 마구 섞인 문자열이 저장되어 있을 때, 인물만 추출해 리스트에 저장하려 한다. 이때 인물 이름이 중복될 수 있으므로 중복을 제거한 인물 이름을 출력하라.
e = 'Chandler: All right Joey, be nice. So does he have a hump? A hump and a hair-place? Phoebe: Wait, does he eat chalk? Phoebe: Just, because, I don\'t want her to go through what I went with Carl- oh!'
m = re.findall(r'[A-Za-z]+?:', e) # r'\w+?:'
print(m)
M = list(set(m))
print(M)