# 이진 검색 알고리즘

from typing import Sequence, Any

def bin_search(a: Sequence, key: Any) -> int:
    pl = 0
    pr = len(a) - 1
    
    while True:
        pc = (pl + pr) // 2
        if a[pc] == key:
            return pc
        elif a[pc] < key:
            pl = pc + 1
        else:
            pr = pc - 1
        if pl > pr:
            break
    return -1

if __name__ == '__main__':
    num = int(input('원소 수를 입력하세요: '))
    print('배열 데이터를 오름차순으로 입력하세요.')
    # li = []
    # li.append(int(input('x[0]: ')))
    # 빈 리스트를 생성하는 또다른 방법
    li = [None] * num
    li[0] = int(input('x[0]: '))


    for i in range(1, num):
        while True:
            # li.append(int(input(f'x[{i}]: ')))
            li[i] = int(input(f'x[{i}]: '))
            if li[i] >= li[i-1]:
                break
    
    ky = int(input('찾을 값(key)를 입력하세요: '))
    idx = bin_search(li, ky)
    print(f'li: {li}\n{ky}의 위치는 li[{idx}]입니다.')