# 3과 5의 배수 합하기
def multiple(n):
    sum = 0
    i = 0
    while i < n:
        if i % 3 == 0 or i % 5 == 0:
            sum += i
            # print(i)
        i += 1
    return sum
print(multiple(1000))