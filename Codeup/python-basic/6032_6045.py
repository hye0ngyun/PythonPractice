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
a, b = input().split()
print(round((float(a) / float(b)), 3))
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
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
print(a + b + c, round(((a + b + c) / 3), 2))
