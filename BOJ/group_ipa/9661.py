N = int(input())
game = N
cur_n = 1
SK = False
CY = True
while N >= cur_n:
    SK, CY = not SK, not CY
    N -= cur_n
    cur_n *= 4
if game:
    if SK:
        print('SK')
    else:
        print('CY')
