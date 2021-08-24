#6092
from random import randint
n = int(input())
temp = [0] * 23
nums = input().split()
for i in nums:
    temp[int(i)-1] += 1
for i in temp:
    print(i, end=' ')
#6093
n = int(input())
nums = input().split()
nums.reverse()
for i in nums:
    print(int(i), end=' ')
#6094
n = int(input())
nums = map(int, input().split())
print(min(nums))
#6095
li = [[0 for i in range(19)] for j in range(19)]
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    if(li[x-1][y-1] != 1):
        li[x-1][y-1] = 1
for i in li:
	print(' '.join(map(str, i)))
#6096
li = []
for i in range(19):
    li.append([])
    k = input().split()
    for e in k:
        li[i].append(int(e))
n = int(input())
x = []
y = []
for i in range(n):
    a, b = map(int, input().split())
    for j in range(19):
        li[a-1][j] = 1 if li[a-1][j] != 1 else 0
        li[j][b-1] = 1 if li[j][b-1] != 1 else 0
for i in li:
    print(' '.join(map(str, i)))
#6097
li = []
h, w = map(int, input().split())
for i in range(h):
	li.append([])
	for j in range(w):
		li[i].append(0)
n = int(input())
for i in range(n):
    l, d, x, y = map(int, input().split())
    for j in range(l):
        if d == 0:
            li[x-1][y-1] = 1
            y += 1
        else:
            li[x-1][y-1] = 1
            x += 1
for i in li:
    print(' '.join(map(str, i)))
#6098
li = []
for i in range(10):
    li.append([])
    k = input().split()
    for e in k:
        li[i].append(int(e))
x, y = 1, 1
flag = True

while flag:
    if li[x][y] == 2:
        li[x][y] = 9
        flag = False
    elif (li[x][y+1]) == 1:
        if li[x+1][y] == 1:
            li[x][y] = 9
            flag = False
        else:
            li[x][y] = 9
            x += 1
    else:
        li[x][y] = 9
        y += 1
for i in li:
    print(' '.join(map(str, i)))