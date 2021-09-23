t = int(input())
beer = 20
can_go = True
results = []
for i in range(t):
    n = int(input())
    sx, sy = map(int, input().split())
    m = []
    for j in range(n):
        m.append(list(map(int, input().split())))
        if j == 0:
                can_go = True if (((m[j][0] - sx) + (m[j][1] - sy)) <= (beer * 50)) else False
        elif can_go:
            can_go = True if (((m[j][0] - m[j-1][0]) + (m[j][1] - m[j-1][1])) <= (beer * 50)) else False
    ex, ey = map(int, input().split())
    results.append('happy' if (can_go and (((ex - m[j][0]) + (ey - m[j][0])) <= (beer * 50))) else 'sad')

for result in results:
    print(result)