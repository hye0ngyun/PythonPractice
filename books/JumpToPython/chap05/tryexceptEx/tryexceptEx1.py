# f = open('나없는파일', 'r') # FileNotFoundError: [Errno 2] No such file or directory: '나없는파일'
# print(4/0) # ZeroDivisionError: division by zero
#a=[1,2,3]
#print(a[3]) # IndexError: list index out of range
# 오류 예외 처리 기법
# try: --- except[발생 오류[as 오류 메시지 변수]]: --- 
try:
    4/0
except ZeroDivisionError as e:
    print(e)
# try .. else
try:
    f = open('foo.txt', 'r')
except FileNotFoundError as e:
    print(e)
else:
    data = f.read()
    f.close()
f = open('foo.txt', 'w')
try:
    # 무언가를 수행한다.
    5/0
except ZeroDivisionError:
    pass # 0으로 나누더라도 오류 발생시키지 않고 통과
finally:
    f.close()