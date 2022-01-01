# 거스름돈
# 500원, 100원, 50원, 10원 단위가 존재할 때 거슬러줄 동전의 최소 개수를 구하시오. (거스름돈의 최소 단위는 10원이다.)
# input: 거슬러줄 돈
# output: 최소 동전 개수

def my_solution(input):
  count = 0
  # 500 원 개수
  count += input // 500
  input %= 500
  # 100원 개수
  count += input // 100
  input %= 100
  # 50원 개수
  count += input // 50
  input %= 50
  # 10원 개수
  count += input // 10
  input %= 10

  return count

print(my_solution(int(input())))

def book_solution(input):
  count = 0

  # 큰 단위의 화폐부터 차례대로 확인
  coin_types = [500, 100, 50, 10]
  
  for coin in coin_types:
    count += input // coin
    input %= coin
  
  return count

print(book_solution(int(input())))
