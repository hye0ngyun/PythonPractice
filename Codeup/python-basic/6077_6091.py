#6077
n = int(input())
s = 0
for i in range(n + 1):
    if(i % 2 == 0):
        s += i
print(s)
#6078
c = ''
while(c != 'q'):
    c = input()
    print(c)
#6079
n = int(input())
i = 0
s = 0
while(s < n):
	i += 1
	s += i
print(i)
#6080
n, m = map(int, input().split())
for i in range(1, n + 1):
    for j in range(1, m + 1):
        print('{} {}'.format(i, j))
#6081
n = input()
for i in range(1, 15 + 1):
	print('%x*%x=%x'.upper() %(int(n, 16), int(hex(i), 16), (int(n, 16) * int(hex(i), 16))))
#6082
n = int(input())
for i in range(1, n + 1):
    if(i % 10 == 3 or i % 10 == 6 or i % 10 == 9):
        print('X', end = ' ')
    else:
        print(i, end = ' ')
#6083
a, b, c = map(int, input().split())
count = 0
for i in range(a):
	for j in range(b):
		for k in range(c):
			print('{} {} {}'.format(i, j, k))
			count += 1
print(count)
#6084
h, b, c, s = map(int, input().split())
mb = round((h * b * c * s / 8) / 1024 / 1024, 1)
print('{} MB'.format(mb))
#6085
w, h, b = map(int, input().split())
mb = round(((w*h*b) / 8 / 1024 / 1024), 2)
print('{:.2f} MB'.format(mb))
#6086
n = int(input())
total = 0
for i in range(1, n + 1):
    total += i
    if(total >= n):
        break
print(total)
#6087
n = int(input())
for i in range(1, n + 1):
    if(i % 3 == 0):
        pass
    else:
        print(i)
#6088
a, b, n = map(int, input().split())
total = a
for i in range(a, a + n - 1):
	total += b
print(total)
#6089
a, b, n = map(int, input().split())
total = a
for i in range(a, a + n - 1):
	total *= b
print(total)
#6090
a, m, d, n = map(int, input().split())
total = a
for i in range(a, a + n - 1):
	total = total * m + d
print(total)
#6091
a, b, c = map(int, input().split())
d = 1
while d % a != 0 or d % b != 0 or d % c != 0:
    d += 1
print(d)