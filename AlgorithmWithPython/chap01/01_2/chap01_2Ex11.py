# 비교 연산자를 연속으로 사용하는 방법과 드모르간의 법칙
# 2자리 양수(10~99) 입력받기
print('2자리 양수를 입력하세요.')

while True:
    n = int(input('값을 입력하세요.: '))
    if n >= 10 and n <= 99:
        break

print(f'입력받은 양수는 {n}입니다.')

# 위 코드에서 7번라인 if n >= 10 and n <= 99:을 다른 방법으로 써보기
'''
# 비교 연산자를 연속으로 사용한 방법
if 10 <= n <= 99:
# 드모르간의 법칙을 사용한 방법
if not(n < 10 or n > 99):
'''