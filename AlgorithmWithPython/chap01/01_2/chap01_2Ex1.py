# 1부터 n까지의 정수의 합 구하기1(while문)
n = int(input('정수를 입력해주세요.: '))
i = 1   # 카운터용 변수
nsum = 0
while i <= n:
    nsum += i
    i += 1
print(f'1부터 {n}까지의 합은 {nsum}입니다.')
print(f'i의 값은{i}입니다.')
''' while 문 반복 알아보기
어떤 조건이 성립하는 동안 처리하는것을 반복구조(repetition structure)라고 하고 일반적으로 루프(loop)라고 합니다.
이때 while문은 실행하기 전에 반복을 계속 할 것인지 판단하는데 이를 판단 반복 구조라고 합니다.
while 조건식: 명령문(루프 본문)
'''