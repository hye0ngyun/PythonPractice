# (재귀함수) 팩토리얼 계산
def rec_fac(n):
    if(n < 2):
        return 1
    else:
        return n*rec_fac(n-1)
n = int(input())
if n <= 12:
    print(rec_fac(n))
