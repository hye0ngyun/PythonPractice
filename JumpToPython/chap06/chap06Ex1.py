# 단 입력받아 구구단 출력
def GuGu(dan):
    numlist = []
    for i in range(1, 10):
        numlist.append(dan*i)
        print(dan, 'x', i, '=', numlist[i-1])
GuGu(2)