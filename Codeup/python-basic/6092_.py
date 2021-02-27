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
