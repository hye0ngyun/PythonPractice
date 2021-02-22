# (재귀 함수) 1부터 n까지 역순으로 출력하기
def rec(n):
	if(n == 0):
		return
	else:
		print(n)
		return rec(n-1)
rec(int(input()))