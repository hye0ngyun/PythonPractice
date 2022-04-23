# 1 첫 번째 풀이 - a와 b가 같은 조에 있는지 파악 불가능해서 88점
'''
정확성: 88.0
합계: 88.0 / 100.0
'''
import math
def solution(n,a,b):
    answer = 0

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    while n > 0:
        answer += 1
        print(f'{answer}번째 라운드')
        if b - a == 1 or a - b == 1:
            print(f'b: {b}, a: {a}')
            break
        else:
            print(f'1 >> b: {b}, a: {a}, n: {n}')
            a = math.ceil(a / 2)
            b = math.ceil(b / 2)
            n = n // 2
            print(f'2 >> b: {b}, a: {a}, n: {n}')

            
    print(answer)

    return answer


# 1 두 번째 풀이 - a와 b가 같은 조에 있는지 파악하는 코드 추가 100점
'''
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''
import math
def solution(n,a,b):
    answer = 0
    while True:
        answer += 1
        if (math.ceil(a / 2) == math.ceil(b / 2)) and ((a - b == 1) or (b - a == 1)):
            break
        else:
            a = math.ceil(a / 2)
            b = math.ceil(b / 2)
            n = n // 2
    return answer