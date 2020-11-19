# abs(x) x의 값을 절대값으로 리턴
print(abs(3))
print(abs(-3))
print(abs(-1.2))

# all(x)는 반복 가능한(iterable) 자료형 x를 입력 인수로 받으며, 이 x가 모두 참이면 True, 거짓이 하나라도 있다면 False를 리턴한다.
print(all([1,2,3]))     # 1,2,3 모두 0이 아닌 정수값이기 때문에 True 리턴
print(all([1,2,3,0]))   # 1,2,3,0중 0(False) 가 있기 때문에 False 리턴

# any(x)는 x중 하나라도 참이 있을 경우 True를 리턴하고, x가 모두 거짓일 경우 False를 리턴 --- *, or
print(any([1,2,3,0]))
print(any(['', 0]))
print(any([0, -1, -2]))

# chr(i)는 아스키(ASCII)코드값을 입력받아 그 코드에 해당하는 문자를 출력하는 함수이다.
print(chr(65))
print(chr(90))
print(chr(97))
print(chr(48))

# ord(c)는 아스키 코드값을 리턴하는 함수이다. --- chr(i)와 반대
print(ord('a'))

# dir은 객체가 자체적으로 가지고 있는 변수나 함수를 보여준다.
print(dir([1,2,3]))

# divmod(a,b)는 2개의 숫자를 입력받아 a를 b로 나눈 몫과 나머지를 튜플형태로 리턴한다.
print(divmod(7,3))  # (2,1)
print(divmod(6.0, 0.2)) # (29.0, 0.19999999999999968)

# enumerate '열거하다'라는 뜻이다. 이 함수는 순서가 있는 자료형(리스트, 튜플, 문자열)을 입력받아 인덱스 값을 포함하는 enumerate 객체를 리턴한다.
for i, name in enumerate(['body', 'foo', 'bar']):
    print(i, name)
# eval(expression)은 실행 가능한 문자열(1+2, 'hi' + 'a' 같은것)을 입력받아 문자열을 실행한 결과값을 리턴하는 함수이다.
print(eval('1+2'))
print(eval('divmod(4,3)'))

# positive함수는 리스트중 양수만 리턴한다.
def positive(numberList):
    result=[]
    for num in numberList:
        if num > 0:
            result.append(num)
    return result

print(positive([1,-2,3,-4,5,-6,7]))

# filter(함수, 인자)는 인자를 받은 함수에서 참인 값만 리턴한다.
def positive(x):
    return x > 0
print(list(filter(positive, [1,-2,3,-4,5,-6,7])))   # list함수

# 위의 두 코드를 lambda식 사용 시 한줄로 만들 수 있다.
print(list(filter(lambda x: x>0, [1,-2,3,-4,5,-6,7])))

# id(object)는 객체를 입력받아 객체의 고유 주소값(레퍼런스)를 리턴하는 함수다.
a = 3
b = a
print(id(a), id(3), id(b))  # a, 3, b 모두 같은 주소값을 갖는다. -> 모두 같은 객체를 가리킨다.

# input([prompt])은 사용자 입력을 받는 함수이다.
# b = input('Enter: ')

# int(x)정수, float(x)실수, str(x)문자열, bin(x)2진수, oct(X)8진수, hex(x)16진수
print(int(10.0))
print(float(10))
print(str(10))
print(bin(10))
print(oct(10))
print(hex(10))

# isinstance(object, class or type or tuple) 인스턴스와 클래스의 인스턴스인지 판단하여 참이면 True, 거짓이면 False 리턴
class Person: pass
a = Person()
print(isinstance(a, Person))
b = 3
print(isinstance(b, Person))
print(isinstance(b, int))

# type(object)은 입력값의 자료형을 리턴한다.
print(type('a'))
print(type(Person))
print(type(b))
print(type([]))

# lambda 인수1, 인수2 .. : 인수를 이용한 표현식
sum = lambda a, b: a+b
print(sum(3,4))
myList = [lambda a,b:a+b, lambda a,b:a*b]
print(myList[0](3,4))
print(myList[1](3,4))

# len(s)는 입력값 s의 길이(요소의 전체 개수)를 리턴하는 함수이다.
print(len('python'))    # 6
print(len([1,2,3]))     # 3
print(len((1,3)))       # 2

# list(s)리스트, tuple(s), set(s)
print(list([1,2,3,1,5,2]))
print(tuple([1,2,3,1,5,2]))
print(set([1,2,3,1,5,2]))

# map(f, iterable)은 함수(f)와 반복 가능한(iterable) 자료형을 입력으로 받는다. map은 입력 받은 자료형의 각 요소가 함수 f에 의해 수행된 결과를 묶어서 리턴한다.
def two_times(numberList):
    result=[]
    for number in numberList:
        result.append(number*2)
    return result
result = two_times([1,2,3,4])
print(result)

def two_times(x): return x*2
print(list(map(two_times, [1,2,3,4])))
print(list(map(two_times, [1,2,3,4])))
print(list(map(lambda x:x*2, [1,2,3,4])))
print(list(map(lambda x:x+1, [1,2,3,4])))

# max(iterable), min(iterable)
print(max([1,2,3]))
print(max('python'))
print(min([1,2,3]))
print(min('python'))

# open(filename, [mode]) mode=['w','r'(default),'a','b'] w:쓰기, r:읽기, a:추가, b:바이너리

# pow(x, y) x의 y제곱 == x**y
print(pow(3,4))
print(3**4)

# range([start,] stop [,step])은 for문과 함께 자주 사용되며 입력받은 범위의 값을 반복 가능한 객체로 만들어 리턴한다.
print(list(range(5)))
print(list(range(5, 10)))
print(list(range(1, 10, 2)))
print(list(range(0, -10, -1)))

# sorted(iterable) 함수는 입력값을 정렬항 후 그 결과를 리스트로 리턴하는 함수이다.
print(sorted([3,2,1]))
print(sorted(['b','c','a']))
a = [3,1,2]
result = a.sort()
print(result, a)

# zip(iterable*)은 동일한 개수로 이루어진 자료형을 묶어 주는 역할을 하는 함수이다.
print(list(zip([1,2,3],[4,5,6])))
print(list(zip([1,2,3],[4,5,6],[7,8,9])))
print(list(zip('abc','def')))
