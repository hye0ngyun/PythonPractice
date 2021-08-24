""" 숫자형 자료형 """
print('-'*15+' 숫자형 자료형 '+'-'*15)
# 정수형
a = 123
b = -178
c = 0

print('정수형')
print(f'a: {a}, b: {b}, c: {c}\n')

# 실수형
a = 1.2
b = -3.45
c = 1.0

print('실수형')
print(f'a: {a}, b: {b}, c: {c}\n')

# 8진수
a = 0o177
b = 0o11
c = 0o123

print('8진수')
print(f'a(0o177): {a}, b(0o11): {b}, c(0o123): {c}\n')

# 16진수
a = 0x8ff
b = 0xABC
c = 0x123

print('16진수')
print(f'a(0x8ff): {a}, b(0xABC): {b}, c(0x123): {c}\n')

# 복소수
a = 1+2j
b = 3-4J

print(f'a(1+2j).real: {a.real}, a(1+2j).imag: {a.imag}')
print(f'a(1+2j).conjugate: {a.conjugate()}, abs(a(1+2j)): {abs(a)}\n')

# 사칙연산
a = 17
b = 4
print(f'a+b = {a+b}')
print(f'a-b = {a-b}')
print(f'a*b = {a*b}')
print(f'a**b = {a**b}')
print(f'a/b = {a/b}')
print(f'a//b = {a//b}')
print(f'a%b = {a%b}\n')
