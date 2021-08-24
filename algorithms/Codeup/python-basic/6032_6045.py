#6032
print(-int(input()))
#6033
print(chr(ord(input())+1))
#6034
a, b = input().split()
print(int(a) - int(b))
#6035
a, b = input().split()
print(float(a) * float(b))
#6036
s = input().split()
for i in range(int(s[1])):
    print(s[0], end='')
# s = input().split()
# print(s[0] * int(s[1]))
#6037
count = int(input())
s = input()
print(s * count)
#6038
a, b = input().split()
print(int(a) ** int(b))
#6039
a, b = input().split()
print(float(a) ** float(b))
#6040
a, b = input().split()
print(int(a) // int(b))
#6041
a, b = input().split()
print(int(a) % int(b))
#6042
print(round(float(input()), 2))
#6043
a, b = map(float, input().split())
print('%.3f' %round((a / b), 3))
#6044
a, b = input().split()
a = int(a)
b = int(b)
if(a >= 0 and b != 0):
    print(a + b)
    print(a - b)
    print(a * b)
    print(a // b)
    print(a % b)
    print(round((a / b), 2))
#6045
# print(a + b + c, round((a + b + c / 3), 2))
# 위 코드와 같이 작성할 경우 a + b + c / 3 부분에서 2.0값이 아닌 3.0값이 나오게 된다.
# 이 이유는 a + b + c / 3은 연산자 우선순위에 의해 a + b + (c / 3) = 1 + 2 + (3/3) = 3.0이라는 결과가 나오게 된다.
# 따라서 괄호를 적절히 사용하여 연산 우선순위를 맞춰 계산한 (a + b + c) / 3 = (1 + 2 + 3) / 3 = 2.0으로 예상한 값이 나오게 된다.
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
print(a + b + c, round(((a + b + c) / 3), 2))
