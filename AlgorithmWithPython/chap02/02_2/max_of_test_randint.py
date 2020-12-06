# 배열 원소의 최댓값을 구해서 출력하기(원솟값을 난수로 생성)

import random
from max import max_of

print('난수의 최댓값을 구합니다.')
number = int(input('난수의 개수를 입력하세요.: '))
rmin = int(input('난수의 최솟값을 입력하세요.: '))
rmax = int(input('난수의 최댓값을 입력하세요.: '))
x = []  # 내가 생각한 코드
# x = None * number # 책 코드

for i in range(number):
    rnum = random.randint(rmin, rmax)
    x.append(rnum)  # 내가 생각한 코드
    # x [i] = random.randint(rmin, rmax)    # 책 코드

print(f'{x}')
print(f'이 가운데 최댓값은 {max_of(x)}입니다.')