N = int(input())
tsum = 0
bsum = 0
for i in range(N):
    # 아래 점의 수
    bsum += i * (i + 1)
    # 위 점의 수
    for j in range(i):
        tsum += j
total = bsum + tsum
print(total)