# 1부터 n까지 정수의 합 구하기(이뮤터블 예제)

def sum_1ton(n):
    """1부터 n까지 정수의 합"""
    s = 0
    while n > 0:
        s += n
        n -= 1
        print(f's:{s:2}, n:{n:2}, x:{x:2}')
    return s
x = int(input('x의 값을 입력하세요.: '))
print(f'1부터 {x}까지 정수의 합은 {sum_1ton(x)}입니다.')
# 매개변수 n으로 실제 인수 x의 값이 복사(copy)되었습니다. (X)
# 매개변수 n으로 실제 인수 x의 값이 대입되었습니다. (O)
''' 파이썬은 객체 참조에 의한 전달(call by object reference)
x의 값을 입력하세요.: 5 x = 5를 참조, n은 5를 참조
s: 5, n: 4, x: 5    x = 5를 참조, n은 4를 참조
s: 9, n: 3, x: 5
s:12, n: 2, x: 5
s:14, n: 1, x: 5
s:15, n: 0, x: 5
'''