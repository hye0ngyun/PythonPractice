# 1부터 n까지의 정수의 합 구하기2(for문)
n = int(input('정수를 입력해주세요.: '))
nsum = 0

for i in range(1, n+1):
    nsum += i
    print(f'i의 값은 {i}입니다.')

print(f'1부터 {n}까지의 합은 {nsum}입니다.')
''' for 문 반복문 알아보기
변수가 하나만 있을 때는 while문 보다는 for문을 사용하는 것이 좋습니다.
for i in range(1, n+1)에서 n이 아닌 n+1을 해준 이유는 range(1, n)으로 할 경우 1부터 n까지 n이 되는 순간 반복문을 종료하기 때문에 우리가 원하는 n까지 더하는 반복문을 만들기 위해서 n+1을 해준 것입니다.
'''