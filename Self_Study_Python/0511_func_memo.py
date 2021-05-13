# fibonacii for loop function (반복문 함수)

# 함수 정의
def fibo_for(n):
    count = 0
    _cur, _next = 0, 1
    for i in range(n):
        print(f'[{i}] _cur: {_cur}, _next: {_next}')
        _cur, _next = _next, _cur + _next
        count += 1
    print(f'fibo_for({n}): {_cur}, count: {count}')
    return _cur

# 결과 출력
for j in range(8):
    fibo_for(j)
    print()
# 0 1 1 2 3 5 8

print('-'*20)

# fibonacii recursive function (재귀 함수)

count = 0
fibo = 7

# 함수 정의
def fibo_rec(n):
    global count
    count += 1
    print(f'fibo_rec({n}) 호출, count: {count}')
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibo_rec(n-1) + fibo_rec(n-2)

# 결과 출력
print('-'*10+f'\nfibo_rec({fibo}): {fibo_rec(fibo)}계산에 활용된 함수 호출 횟수는 {count}번입니다.\n'+'-'*10)

# fibonacci recursive function memoization

dictionary = {
    1: 1,
    2: 1
}
count = 0

def fibo_memo(n):
    global count
    count += 1
    print(f'fibo_rec({n}) 호출, count: {count}')
    if n in dictionary:
        return dictionary[n]
    else:
        dictionary[n] = fibo_memo(n-1) + fibo_memo(n-2)
        print(dictionary)
        return dictionary[n]

print(fibo_memo(10))
print('-'*10+f'\nfibo_memo(10) 계산에 활용된 덧셈 횟수는 {count}번입니다.'+'-'*10)


# 조기 리턴

dictionary = {
    1: 1,
    2: 1
}

def fibo_memo(n):
    if n in dictionary:
        return dictionary[n]
    dictionary[n] = fibo_memo(n-1) + fibo_memo(n-2)
    return dictionary[n]

print(fibo_memo(10))
