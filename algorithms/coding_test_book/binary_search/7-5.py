# 22.04.19 20:10 ~ 20:28 (18m)
from array import array


def my_solution():
  n = int(input())
  n_list = list(map(int, input().split()))
  m = int(input())
  m_list = list(map(int, input().split()))
  # start = 0
  # end = n - 1
  n_list.sort()
  for _m in m_list:
    start = 0
    end = n - 1
    while start <= end:
      mid = (start + end) // 2
      if n_list[mid] == _m:
        print('yes', end=' ')
        break
      elif n_list[mid] > _m:
        end = mid - 1
      else:
        start = mid + 1
    else:
      print('no', end=' ')


# my_solution()

# book solution1 이진 탐색
def binary_search(array, target, start, end):
  while start <= end:
    mid = (start + end) // 2
    if array[mid] == target:
      return mid
    elif array[mid] > target:
      end = mid - 1
    else:
      start = mid + 1
  return None

def book_solution1():
  n = int(input())
  array = list(map(int, input().split()))
  array.sort()

  m = int(input())
  x = list(map(int, input().split()))

  for i in x:
    result = binary_search(array, i, 0, n-1)
    if result != None:
      print('yes', end = ' ')
    else:
      print('no', end = ' ')

# book_solution1()

# book solution2 계수 정렬
def book_solution2():
  n = int(input())
  array = [0] * 1000001

  for i in input().split():
    array[int(i)] = 1
  
  m = int(input())
  x = list(map(int, input().split()))

  for i in x:
    if array[i] == 1:
      print('yes', end = ' ')
    else:
      print('no', end = ' ')

# book_solution2()

# book solution3 집합 자료형 이용
def book_solution3():
  n = int(input())
  array = set(map(int, input().split()))

  m = int(input())
  x = set(map(int, input().split()))

  for i in x:
    if i in array:
      print('yes', end = ' ')
    else:
      print('no', end = ' ')

book_solution3()