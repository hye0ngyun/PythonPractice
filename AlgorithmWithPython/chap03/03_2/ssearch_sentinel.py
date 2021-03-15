# 선형 검색 알고리즘(실습 3-1)을 보초법으로 수정

from typing import Sequence, Any
import copy

def seq_search(seq: Sequence, key: Any) -> int:
    a = copy.deepcopy(seq)
    a.append(key)
    i = 0
    print(a)
    while True:
        if a[i] == key:
            break
        i += 1
    print(f'a: {a}\nlen(a): {len(a)}\ni: {i}')
    return -1 if i == len(seq) else  i
    # return -1 if i == len(a)-1 else  i --- 내가 생각한 코드(똑같이 작동)

if __name__ == '__main__':
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))
    
    ky = int(input('검색할 값을 입력하세요: '))

    idx = seq_search(x, ky)

    if idx == -1:
        print('검색값을 갖는 원소가 존재하지 않습니다.')
    else:
        print(f'검색값은 x[{idx}]에 있습니다.')