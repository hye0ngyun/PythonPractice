# # 1
# def f(x):
#     return x
# print(f(10))

# def f(x):
#     return 2*x+1
# print(f(10))

# def f(x):
#     return x**2+2*x+1
# print(f(10))

# # 2
# def mul(*values):
#     s = 1
#     for i in values:
#         s *= i
#     return s
# print(mul(5, 7, 9, 10))

# # 3
# # def function(*values, valueA, valueB):
# #     pass
# # function(1,2,3,4,5)
# def function(*values, valueA = 10, valueB = 20):
#     pass
# function(1,2,3,4,5)
# def function(valueA, valueB, *values):
#     pass
# function(1,2,3,4,5)
# def function(valueA = 10, valueB = 20, *values):
#     pass
# function(1,2,3,4,5)

def factorial(n):
    output = 1
    for i in range(1, n+1):
        output *= i
    return output

print(factorial(4))

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

# memoization

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
print('-'*10)
print(fibo_memo(10))