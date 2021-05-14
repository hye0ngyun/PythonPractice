# fibonacii for loop function (반복문 함수)
fibo = 15
# 변수 정의
count = 0 # 계산 카운트
# fibo = 7 # fibonacci 7번째 값

# 함수 정의
def fibo_for(n):
    global count
    _cur, _next = 0, 1
    for i in range(n):
        print(f'for loop[{i}] _cur: {_cur}, _next: {_next}')
        _cur, _next = _next, _cur + _next
        count += 1
    print(f'fibo_for({n}): {_cur}, count: {count}')
    return _cur

# 결과 출력
print('-'*10+f'\nfibo_rec({fibo}): {fibo_for(fibo)} 계산에 활용된 반복 횟수는 {count}번입니다.\n'+'-'*10)
print()

# -----------------------------------------------------------------------------------------------------------
# fibonacii recursive function (재귀 함수)

# 변수 정의
count = 0 # 계산 카운트
# fibo = 7 # fibonacci 7번째 값

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
print('-'*10+f'\nfibo_rec({fibo}): {fibo_rec(fibo)} 계산에 활용된 함수 호출 횟수는 {count}번입니다.\n'+'-'*10)
print()

# -----------------------------------------------------------------------------------------------------------
# fibonacci recursive function memoization (재귀함수 메모화)

# 변수 정의
count = 0 # 계산 카운트
# fibo = 7 # fibonacci 7번째 값
dictionary = { # 이미 계산한 값을 저장할 딕셔너리
    1: 1,
    2: 1
}

# 함수 정의
def fibo_memo(n):
    global count
    count += 1
    print(f'fibo_memo({n}) 호출, count: {count}')
    if n in dictionary:
        return dictionary[n]
    else:
        dictionary[n] = fibo_memo(n-1) + fibo_memo(n-2)
        print(dictionary)
        return dictionary[n]

# 결과 출력
print('-'*10+f'\nfibo_memo({fibo}): {fibo_memo(fibo)} 계산에 활용된 함수 호출 횟수는 {count}번입니다.\n'+'-'*10)
print()

# -----------------------------------------------------------------------------------------------------------
# fibonacci recursive function memoization early return (재귀 함수 메모화 조기 리턴)

# 변수 정의
count = 0 # 계산 카운트
# fibo = 7 # fibonacci 7번째 값
dictionary = { # 이미 계산한 값을 저장할 딕셔너리
    1: 1,
    2: 1
}

def fibo_memo(n):
    global count
    count += 1
    print(f'fibo_memo({n}) 호출, count: {count}')
    if n in dictionary:
        return dictionary[n]
    dictionary[n] = fibo_memo(n-1) + fibo_memo(n-2)
    print(dictionary)
    return dictionary[n]

# 결과 출력
print('-'*10+f'\nfibo_memo({fibo}): {fibo_memo(fibo)} 계산에 활용된 함수 호출 횟수는 {count}번입니다.\n'+'-'*10)
print()

# -----------------------------------------------------------------------------------------------------------