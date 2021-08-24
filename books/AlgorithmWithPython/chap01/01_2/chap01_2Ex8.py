# 직사각형 넓이로 변의 길이 구하기
# 가로, 세로 길이가 정수이고 넓이가 area인 직사각형에서 변의 길이 나열하기(약수를 나열하는 프로그램)

area = int(input('직사각형의 넓이를 입력하세요.: '))

for i in range(1, area + 1):
    if i * i > area: break  # 가능한 값이 area를 넘어가면 종료
    if area % i: continue   # 가로, 세로 곱한 값이 맞아 떨어지지 않으면 continue
    print(f'{i} x {area // i}') # {i}짧은변, {area//i}긴변

''' 32의 약수
1 x 32
2 x 16
4 x 8
'''