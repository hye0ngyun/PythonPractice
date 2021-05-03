cabinet = {3: '유재석', 100: '김태호'}
print(f'cabinet[3]: {cabinet[3]}')
print(f'cabinet[100]: {cabinet[100]}')
print(f'cabinet.get(3): {cabinet.get(3)}')
# print(f'cabinet[100]: {cabinet[5]}')
print(f'cabinet.get(3): {cabinet.get(5)}')
print(f'cabinet.get(3): {cabinet.get(5, "사용가능")}')

print(3 in cabinet)
print(5 in cabinet)

cabinet = {'A-3':'유재석', 'B-100':'김태호'}
print(cabinet)
cabinet['A-3'] = '김종국'
cabinet['C-20'] = '조세호'
print(cabinet)

del cabinet['A-3']
print(cabinet)

# key 출력
print(cabinet.keys())

# value 출력
print(cabinet.values())

print(f'for i in cabinet:')
for i in cabinet:
    print(i)
print(f'for i in cabinet.keys()')
for i in cabinet.keys():
    print(i)
print(f'for i in cabinet.values()')
for i in cabinet.values():
    print(i)
print(f'for i, j in cabinet.items()')
for i, j in cabinet.items():
    print(i, j)

cabinet.clear()
print(cabinet)

# tuple
menu = ('돈까스', '치즈까스')
print(menu[0])
print(menu[1])

name = '김종국'
age = 20
hobby = '코딩'
print(name, age, hobby)

name, age, hobby = '김종국', 20, '코딩'
print(name, age, hobby)

# set
my_set = {1,2,3,3,3}
print(my_set)

java = {'유재석', '김태호', '양세형'}
python = set(['유재석', '박명수'])

# 교집합 (java와 python을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

# 합집합 (java할 수 있거나 python할 수 있는 개발자)
print(java | python)
print(java.union(python))

# 차집합 (java할 수 있지만 python은 할 줄 모르는 개발자)
print(java - python)
print(java.difference(python))

# python을 할 줄 아는 사람이 늘어남
python.add('김태호')
print(python)

# java를 잊은사람
java.remove('김태호')
print(java)

# 자료구조의 변경
# 커피숍
menu = {'커피', '우유', '주스'}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))

# 퀴즈
# random.shuffle(), random.sample() 활용예제
from random import *
lst = [1,2,3,4,5]
print(lst)
shuffle(lst)
print(lst)
print(sample(lst, 1))

lst = [x for x in range(1, 21)]
shuffle(lst)
first = (sample(lst, 1))
lst.pop(first[0])
print(' -- 당첨자 발표 -- ')
print(f'치킨 당첨자: {first}')
print(f'커피 당첨자: {(sample(lst, 3))}')
print(' -- 축하합니다. --')