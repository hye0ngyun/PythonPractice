# for문으로 작성한 선형 검색 알고리즘

from typing import Any, Sequence

def seq_search(a: Sequence, key: Any) -> int:
    """시퀀스 a에서 key와 값이 같은 원소를 선형 검색(for문)"""
    for i in range(len(a)):
        if a[i] == key:
            return i
    return -1

if __name__ == '__main__':
    n = int(input("배열의 개수를 입력하세요: "))
    List = [None] * n
    print(List)
    for i in range(n):
        List[i] = int(input())
    print(List)

    ky = int(input('찾는 키값을 입력하세요: '))
    idx = seq_search(List, ky)

    print(f'키값 {ky}은 List[{idx}]에 존재합니다.')
