# (재귀 함수) 1부터 n까지 출력하기
def rec(n, counter = 1):
	if(n == 0):
		return
	else:
		print(counter)
		counter += 1
		return rec(n-1, counter)
rec(int(input()))