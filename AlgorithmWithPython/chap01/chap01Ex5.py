# 세 정수의를 입력받아 중앙값 구하기 2
def med3(a,b,c):
    '''a, b, c의 중앙값을 구하여 반환(다른 방법)'''
    if(b >= a and a >= c) or (b <= a and a <= c):
        return a
    elif(a >= b and b >= c) or (a <= b and b <= c):
        return b
    else:
        return c

print('세 정수의 중앙값을 구합니다.')
a = int(input('정수 a의 값을 입력하세요.: '))
b = int(input('정수 b의 값을 입력하세요.: '))
c = int(input('정수 c의 값을 입력하세요.: '))

print(f'중앙값은 {med3(a,b,c)}입니다.')
'''
세 정수의 중앙값을 구합니다.
정수 a의 값을 입력하세요.: 15
정수 b의 값을 입력하세요.: 7
정수 c의 값을 입력하세요.: 12
중앙값은 12입니다.
'''