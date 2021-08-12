# 정사각형의 크기인 n과 간격 k를 입력받는다.
n, k = map(int, input().split())

# 출력 형태을 살펴보면
# 첫번째 줄과 마지막 줄은 n만큼 * 출력하고
# 이외의 줄은 첫 번째 열과 마지막 열은 *을 출력하며
# 이후 간격의 
# 오른쪽으로 빗금
# for i in range(n):
#     if i in [0, n-1]:
#         print('*' * n)
#     else:
#         for j in range(n):
#             if j in [0, n-1]:
#                 print('*', end='')
#             else:
#                 if (j-i) % k == 0:
#                     print('*', end='')
#                 else:
#                     print(' ', end='')
#         print()
# n-1, -1, -1
for i in range(n):
    if i in [0, n-1]:
        print('*' * n)
    else:
        for j in range(n):
            if j in [0, n-1]:
                print('*', end='')
            else:
                if (i-j-2) % k == j % k:
                    print('*', end='')
                else:
                    print(' ', end='')
        print()