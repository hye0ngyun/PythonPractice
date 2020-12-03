# 10~99 사이의 난수 n개 생성하기(13이 나오면 중단)
import random

print('10~99 사이의 난수 n개 생성하기(13이 나오면 중단)')

n = int(input('난수의 개수를 입력하세요.: '))

for _ in range(n):
    rn = random.randint(10, 99)
    print(rn,'', end='')
    if rn == 13:
        print('\n프로그램을 중단합니다.')
        break
else:
    print('\n난수 생성을 중단합니다.')