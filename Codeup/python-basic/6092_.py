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