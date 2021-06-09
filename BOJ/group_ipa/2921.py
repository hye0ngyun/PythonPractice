N = int(input())
tsum = 0
bsum = 0
for i in range(N + 1):
    # 아래 점의 수
    bsum += i * (i + 1)
    # 위 점의 수
    tsum += (i * (i + 1)) // 2
total = bsum + tsum
print(total)