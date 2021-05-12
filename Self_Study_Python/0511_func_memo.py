# fibonacii recursive function (재귀 함수)
counter = 0

def fibonacci(n):
    print(f'fibonacci({n})를 구합니다.')
    global counter
    counter += 1
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))
print('-'*10+f'\nfibonacii(10) 계산에 활용된 덧셈 횟수는 {counter}번입니다.')

# fibonacci recursive function memoization

dictionary = {
    1: 1,
    2: 1
}
counter = 0
def fibo_memo(n):
    global counter
    counter += 1
    if n in dictionary:
        print(dictionary)
        return dictionary[n]
    else:
        dictionary[n] = fibo_memo(n-1) + fibo_memo(n-2)
        print(dictionary)
        return dictionary[n]

print('-'*10)
print(fibo_memo(10))
print('-'*10+f'\nfibo_memo(10) 계산에 활용된 덧셈 횟수는 {counter}번입니다.')

dictionary = {
    1: 1,
    2: 1
}
# 조기 리턴
def fibo_memo(n):
    if n in dictionary:
        return dictionary[n]
    dictionary[n] = fibo_memo(n-1) + fibo_memo(n-2)
    return dictionary[n]

print(fibo_memo(10))
