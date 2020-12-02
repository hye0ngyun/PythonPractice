# 반복 과정에서 조건 판단하기 1
# a부터 b까지 정수의 합 구하기 1
print('a부터 b까지 정수의 합 구하기.')
a = int(input('a를 입력해주세요.: '))
b = int(input('b를 입력해주세요.: '))

if a > b:
    a, b = b, a

sum = 0
for i in range(a, b+1):
    sum += i
    if i < b:
        print(f'{i} + ', end='')
    else:
        print(f'{i} = ', end='')
print(sum)

print('-'*50)

# a부터 b까지 정수의 합 구하기 2(1보다 효율적)
print('a부터 b까지 정수의 합 구하기.')
a = int(input('a를 입력해주세요.: '))
b = int(input('b를 입력해주세요.: '))

if a > b:
    a, b = b, a

sum = 0
for i in range(a, b):
    print(f'{i} + ', end='')
    sum += i
print(f'{b} = ', end='')
sum += b
print(sum)

''' 두 값 교환하기 2
a, b, t를 이용해 교환
a = 3
b = 5

t = a
a = b
b = t
'''