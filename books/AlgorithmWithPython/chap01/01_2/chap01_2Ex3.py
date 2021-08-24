# a부터 b까지 정수의 합 구하기(for문)
print('a부터 b까지 정수의 합을 구합니다.')
a = int(input('정수 a를 입력해주세요.: '))
b = int(input('정수 b를 입력해주세요.: '))

if a > b:
    a, b = b, a # a와 b를 오름차순으로 정렬

sum = 0
for i in range(a, b + 1):
    sum += i

print(f'{a}부터 {b}까지 정수의 합은 {sum}입니다.')

# 두 값 교환하기1
'''
a, b = b, a
1. 우변의 b, a에 의해 두 값을 압축한 튜플 (b, a)가 생성됩니다.
2. 대입할 때 튜플 (b,a)를 다시 풀어 b, a로 만든 다음 각각 a와 b에 대입합니다.
'''
