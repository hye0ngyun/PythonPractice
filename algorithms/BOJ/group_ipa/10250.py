# 1
T = int(input())
for i in range(T):
    H, W, N = map(int, input().split())
    if N % H == 0:
        Y = H
        X = (N // H)
    else:
        Y = N % H
        X = (N // H) + 1
    print(f'{Y}{X:02d}')

# 2
T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    YY = ((N - 1) % H) + 1
    XX = ((N - 1) // H) + 1
    print(f'{YY}{XX:02d}')