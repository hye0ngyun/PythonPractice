# (재귀함수) 피보나치 수열
def fibo_rec(n):
    if(n < 2):
        return 1
    else:
        return fibo_rec(n-2) + fibo_rec(n-1)

n = int(input())
print(fibo_rec(n-1))
