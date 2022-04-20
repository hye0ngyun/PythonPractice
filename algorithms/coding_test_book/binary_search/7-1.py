# 순차 탐색
def sequential_search(n, target, array):
  # 각 원소를 하나씩 확인
  for i in range(n):
    # 현재의 원소가 찾고자 하는 원소와 동일한 경우
    if array[i] == target:
      return i + 1 # 인덱스는 0부터 시작하므로 1 추가

print('생성할 원소의 개수를 입력한 다음 한칸 띄고 찾을 문자열을 입력하세요')
n, target = input().split()
n = int(n)

print('앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분자 띄어쓰기 한 칸으로 합니다.')
array = input().split()

# 순자 탐색 수행 결과 출력
print(sequential_search(n, target, array))
