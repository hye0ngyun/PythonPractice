from typing import Sequence, Any

def seq_search(a: Sequence, key: Any) -> int:
    i = 0
    while True:
        if i == len(a):
            return -1
        elif a[i] == key:
            return i
        i += 1

if __name__ == "__main__":
    a = [1,2,3,4,5,10,20,30,40,50]
    
    
    ky = int(input(f'{a}\n찾을 키를 입력하세요: '))
    idx = seq_search(a, ky)
    print(f'{ky}의 값은 a[{idx}]에 존재합니다.')