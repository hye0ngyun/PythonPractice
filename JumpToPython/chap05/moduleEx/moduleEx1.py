def sum(a, b):
    return a+b
def safe_sum(a, b):
    if type(a) != type(b):
        print('더할 수 있는 것이 아닙니다.')
        return
    else:
        result = sum(a,b)
        return result

# python moduleEx1.py처럼 직접 이 파일을 실행시켰을 때는 __name__ = '__main__'이 참이 돼서 if문 다음 문장들을 수행한다.
# 반대로 모듈로 사용될 때는 __name__ == '__main__'이 거짓이 돼서 if문 다음 문장들을 수행하지 않는다.
if __name__ == '__main__':
    print(sum(1,2))
    print(safe_sum(3,4))
    print(safe_sum(3,'a'))
    print(sum(10, 10.4))