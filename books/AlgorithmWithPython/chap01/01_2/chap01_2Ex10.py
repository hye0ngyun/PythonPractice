# 반복문 건너뛰기와 여러 범위 스캔하기
# 1~12까지 8을 건너뛰고 출력하기 1

for i in range(1, 13):
    if i == 8:
        continue
    print(i, end=' ')
print()

# 1~12까지 8을 건너뛰고 출력하기 2
# 아래 코드는 건너뛰어야 하는 부분을 확실히 아는경우 위 코드보다 굉장히 효율적이다.
for i in list(range(1,8)) + list(range(9,13)):
    print(i, end=' ')
print()