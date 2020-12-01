# 입력받은 정수의 부호(양수, 음수, 0) 출력하기
n = int(input('정수를 입력하세요.: '))

if n > 0:
    print('이 수는 양수입니다.')
elif n < 0:
    print('이 수는 음수입니다.')
else:
    print('이 수는 0입니다.')
'''
정수를 입력하세요.: 0
이 수는 0입니다.
정수를 입력하세요.: 1
이 수는 양수입니다.
정수를 입력하세요.: -1
이 수는 음수입니다.
'''

# 3개로 분기하는 조건문 -> 1, 2, 3 ~
n = int(input('정수를 입력하세요.: '))
if n == 1:
    print('A')
elif n == 2:
    print('B')
else:
    print('C')

# 4개로 분기하는 조건문 -> 1, 2, 3, 4 ~
n = int(input('정수를 입력하세요.: '))
if n == 1:
    print('A')
elif n == 2:
    print('B')
elif n == 3:
    print('C')
else:
    # pass문은 '아무것도 수행하지 말고 그냥 지나치세요'를 의미하는 키워드
    pass

''' 연산자와 피연산자
- 단항 연산자(unary operator): 피연산자 1개 ex) -a
- 이항 연산자(binary operator): 피연산자 2개 ex) a < b
- 삼항 연산자(ternary operator): 피연산자 3개 ex) a if b else c
a if b else c에서 조건 b가 참이면 a를, 거짓이면 c를 보여준다.
'''
x = 7
y = 5
a = x if x > y else y   # x > y -> 7 > 5 참이므로 x(7)이 a에 할당된다.
print(a)
c = 0
# 아래와 같이 print()안에서도 삼항 연산자인 a if b else c를 사용할 수 있다.
print('c는 0입니다.' if c == 0 else 'c는 0이 아닙니다.')