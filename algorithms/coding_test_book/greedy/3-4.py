# 22.04.19 17:35 ~ 17:45
# 1이 될 때까지
# my solution

def my_solution():
  N, K = map(int, input().split())
  result = 0
  while N != 1:
    if N % K != 0:
      N = N - 1
      result += 1
    else:
      N = N // K
      result += 1
  
  return result

# print(my_solution())

# book solution
def book_solution():
  n, k = map(int, input().split())
  result = 0
  while True:
    target = (n // k) * k
    result += (n - target)
    n = target
    if n < k:
      break
    result += 1
    n //= k
  result += (n - 1)
  return result

print(book_solution())