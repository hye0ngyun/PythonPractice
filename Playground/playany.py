# T초
T = int(input())
# A: 5분, B: 1분, C: 10초
A = 300
B = 60
C = 10
cnt = [0, 0, 0]

if T % C == 0:
    if T >= A:
        cnt[0] = T // A
        T = T % A
    if T >= B:
        cnt[1] = T // B
        T = T % B
    if T >= C:
        cnt[2] = T // C
        T = T % C        
    for i in cnt:
        print(i, end=' ')
else:
    print(-1)
    

