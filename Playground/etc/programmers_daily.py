def solution(price, money, count):
    answer = -1
    result = 0
    for N in range(1, count + 1):
        result += N * price
    money -= result
    
    if money < 0:
        answer = abs(money)
    else:
        answer = money
    
    return answer

print(solution(3, 20, 4))