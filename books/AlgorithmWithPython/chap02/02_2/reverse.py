# 뮤터블 시퀀스 원소를 역순으로 정렬

from typing import MutableSequence, Any

def reverse_array(a: MutableSequence) -> None:
    """뮤터블 시퀀스 a의 원소를 역순으로 정렬"""
    n = len(a)
    for i in range(n//2):
        a[i], a[n-i-1] = a[n-i-1], a[i]

if __name__ == '__main__':
    print('배열 원소를 역순으로 정렬합니다.')
    nx = int(input('원소 수를 입력하세요.: '))
    x = [None] * nx

    for i in range(nx):
        x[i] = int(input(f'x[{i}]의 값을  입력하세요.: '))
    
    reverse_array(x)    # x의 원소를 역순으로 정렬

    print('배열 원소를 역순으로 정렬했습니다.')
    for i in range(nx):
        print(f'x[{i}] = {x[i]}')
'''
배열 원소를 역순으로 정렬합니다.
원소 수를 입력하세요.: 5
x[0]의 값을  입력하세요.: 1
x[1]의 값을  입력하세요.: 2
x[2]의 값을  입력하세요.: 3
x[3]의 값을  입력하세요.: 4
x[4]의 값을  입력하세요.: 5
배열 원소를 역순으로 정렬했습니다.
x[0] = 5
x[1] = 4
x[2] = 3
x[3] = 2
x[4] = 1
'''