H, M = map(int, input().split())
M -= 45
if M < 0:
    if H == 0:
        H = 23
        M += 60
    else:
        H -= 1
        M += 60
print(H, M)