# 숫자 카드 게임
# my solution
def solution():
  N, M = map(int, input().split())

  card_list = []
  for r in range(N):
    _list = list(map(int, input().split()))
    card_list.append(_list)
  temp_list = []
  for r in card_list:
    temp_list.append(min(r))
  
  result = max(temp_list)

  return result

# print(solution())

# book solution1
def book_solution1():
  n, m = map(int, input().split())
  result = 0
  for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)

    result = max(result, min_value)
  
  return result

# print(book_solution1())

def book_solution2():
  n, m = map(int, input().split())
  result = 0
  for i in range(n):
    data = list(map(int, input().split()))
    min_value = 10001
    for a in data:
      min_value = min(min_value, a)
    result = max(result, min_value)

  return result

print(book_solution2())
