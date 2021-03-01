# 반복문 사용
def sum_iter(n):
	total = 0
	for i in range(1, n+1):
		total += i
	return total
sum_iter(100)

# 재귀함수 사용
def sum_rec(n):
	if(n < 2): return 1
	else: return n + sum_rec(n-1)
sum_rec(100)

# 가우스 등차수열의 합 공식 사용
def sum_gauss(n):
	return int(n*(n+1)/2)
sum_gauss(100)