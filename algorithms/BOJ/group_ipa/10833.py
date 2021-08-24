times = int(input())

remain_total = 0
for i in range(times):
    a, b = map(int, input())
    remain_total += b % a
print(remain_total)