# 시퀀스 원소의 최댓값 출력하기

from typing import Any, Sequence
'''
Any는 제약이 없는 임의의 자료형을 의미하며, Sequence는 시퀀스형을 의미합니다.
또한 시퀀스형에는 리스트형, 바이트 배열형, 문자열형, 튜플형, 바이트열형이 있습니다.
'''

# 건네받는 매개변수 a의 자료형은 Sequence입니다.
# 반환하는 것은 임의의 자료형인 Any 입니다.
def max_of(a: Sequence) -> Any:
    """시퀀스형 a원소의 최댓값을 반환"""
    maximun = a[0]
    for i in range(1, len(a)):
        if a[i] > maximun:
            maximun = a[i]
    return maximun

# 스크립트 프로그램이 직접 실행될 때 변수 __name__은 '__main__'입니다.
# 스크립트 프로그램이 임포트될 때 변수 __name__은 원래 모듈의 이름입니다.
if __name__ == '__main__':
    print('배열의 최댓값을 구합니다.')
    num = int(input('원소 수를 입력해주세요.: '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]의 값을 입력해주세요.: '))
    print(f'최댓값은 {max_of(x)}입니다.')