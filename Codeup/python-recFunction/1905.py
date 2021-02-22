# (재귀함수) 1부터 n까지 합 구하기 -- 입력값이
import sys
sys.setrecursionlimit(1000000)
def rec(n, s = 0):
	if(0 < n):
		s += n
		return rec(n-1, s)
	else:
		return s
print(rec(int(input())))

# 가우스 공식 -- 시간복잡도 O(1)
# def gauss(n):
#     return n*(n+1)/2
# print(round(gauss(int(input()))))