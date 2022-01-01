# 2022-01-01 17:44 ~ 2022-01-01 18:07 (23m)

def my_solution():
  '''
  N: 배열의 크기
  M: 숫자가 더해지는 횟수
  K: 한 인덱스 값을 연속으로 더할 수 있는 횟수
  '''
  N, M, K = map(int, input().split())
  arr = list(map(int, input().split()))
  if len(arr) != N:
    return
  # 가장 큰 값과 그 다음으로 큰 값만 구하면 된다.
  max_arr = []
  max_arr.append(max(arr))
  del arr[arr.index(max_arr[0])]
  max_arr.append(max(arr))

  _sum = 0
  cnt = 0
  idx = 0
  for i in range(M):
    # 와 같아지는 경우 cnt 초기화
    if cnt == K:
      # print(max_arr[int(not bool(idx))], end=' ')
      cnt = 0
      _sum += max_arr[int(not bool(idx))]
    else: 
      # print(max_arr[idx], end=' ')
      cnt += 1
      _sum += max_arr[idx]
  
  return _sum
  
# print(my_solution())
# 5 8 3     
# 2 4 5 4 6
# 66656665

def book_solution():
  N, M, K = map(int, input().split())
  data = list(map(int, input().split()))

  # list 자료형의 sort 사용하기
  data.sort() # 입력받은 수 정렬
  first = data[N - 1] # 가장 큰 수
  second = data[N - 2] # 두 번째로 큰 수

  result = 0

  while True:
    # 가장 큰 수 더하기
    for i in range(K):
      if M == 0:
        break
      result += first
      M -= 1
    # K번 이후 두 번째로 큰 수 더하기
    if M == 0:
      break
    result += second
    M -= 1
  
  return result

# print(book_solution())

def book_solution2():
  N, M, K = map(int, input().split())
  data = list(map(int, input().split()))

  # list 자료형의 sort 사용하기
  data.sort() # 입력받은 수 정렬
  first = data[N - 1] # 가장 큰 수
  second = data[N - 2] # 두 번째로 큰 수

  result = 0

  # pattern = first * K + second
  # 큰 수가 더해지는 횟수
  count = (M // (K + 1)) * K # m과 k+1이 나누어 떨어지는 경우
  count += M % (K + 1)

  result += (count) * first
  result += (M - count) * second

  return result

print(book_solution2())
