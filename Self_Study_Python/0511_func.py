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