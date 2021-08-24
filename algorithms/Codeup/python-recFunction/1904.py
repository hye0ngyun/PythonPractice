# (재귀함수) 두 수 사이의 홀수 출력하기
def rec(a, b):
	if(a <= b):
		if(a % 2 != 0):	print(a, end=' ')
		return rec(a+1, b)
num = input().split()
rec(int(num[0]), int(num[1]))