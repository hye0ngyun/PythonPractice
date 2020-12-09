# 리스트에서 임의의 원솟값을 업데이트하기(뮤터블 예제)

def change(lst, idx, val):
    """lst[idx]의 값을 val로 업데이트"""
    lst[idx] = val

x = [11,22,33,44,55]
print(f'x:{x}')

index = int(input('업데이트할 인덱스를 선택하세요.: '))
value = int(input('새로운 값을 입력하세요.: '))

change(x, index, value)
print(f'x:{x}')
'''
x:[11, 22, 33, 44, 55]  // 실제인수 x가 [11,22,33,44,55] list를 참조함
업데이트할 인덱스를 선택하세요.: 2
새로운 값을 입력하세요.: 99
change(x, index, value) // 실제인수 x와 change함수내의 매개변수 lst가 [11,22,33,44,55]를 참조함
x:[11, 22, 99, 44, 55]
'''