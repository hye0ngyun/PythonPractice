# 5-1
print('dosen\'t')

# 5-2
fruit = '오렌지'
print(fruit[1])
print(fruit[-2])

# 5-3-1
animal = 'frog'
print(animal[1:4:2])

# 5-3-2
animal = 'elephant'
print(animal[1:7:2])

# 5-3-3
animal = 'elephant'
print(animal[5:])

# 5-3-4
animal = 'elephant'
print(animal[:3])

# 5-3-5
animal = 'elephant'
print(animal[3:-3])

# 5-3-6
animal = 'elephant'
print(animal[:])

# 5-3-7
animal = 'elephant'
print(animal[:])

# 5-3-8
animal = 'elephant'
print(animal[::3])
print(animal[::-1])
print(animal[::])

# 5-4
seq = 'Hello!'
for s in seq:
    print(s)

# 5-5
import random
pw = str()
chars = '한글우수'
for _ in range(5):
    pw = pw + random.choice(chars)
print(pw)

# 5-6
import random
def passwd(length):
    pw = str()
    chars = 'abcdefghijklmnopqrstuvwxyz' + '0123456789' + '!@#$%^&*'
    for _ in range(length + 1):
        pw += random.choice(chars)
    return pw
print(passwd(8))

# 5-7
price = ['사과', '오렌지', '포도', '오렌지', '복숭아', '오렌지']
print(price[1::2])

# 5-8
student = ['민준', 173, '서연', 168, '현우', 171, '민선', 189]
alldata = student + ['동현', 179]
print(str(len(alldata)) + '개 데이터')

# 5-9
def new(n, x):
    n = 2
    x.append(x[-1] + 1)
    print('new: ', n, x)
def one():
    n = 1
    x = [0, 1, 2]
    print('one: ', n, x)
    new(n, x)
    print('one: ', n, x)
one()

# 5-10
bird_pos = []
animals = ['새', '코끼리', '강아지', '새', '강아지', '새']
for i, animal in enumerate(animals):
    if animal == '새':
        bird_pos.append(i)
print(bird_pos)

# 5-11
fruits = ['사과', '오렌지', '포도']
fruits.insert(-2, '키위')
print(fruits)

# 5-12
people = [31, 53, 41, 19, 15, 18, 21, 13]
adult = [i for i in people if i >= 19]
print(adult)

# 5-13
a = [1, 2, 3]
for i in a:
    print(i * 2, end=' ')
print()

# 5-14
food = ['귤', '감', '귤', '배', '사과', '귤']
print(food.count('귤'))

# 5-15-1
import random
bigdata = []
nodata = []
for i in range(100):
    bigdata.append(random.randint(1, 33))
for i in range(1, 33 + 1):
    if i not in bigdata:
        nodata.append(i)
print(f'bigdata: {bigdata}\nnodata: {nodata}')

# 5-15-2
import random
bigdata = []
nodata = []
for i in range(100):
    bigdata.append(random.randint(1, 33))
nodata = [i for i in range(1, 33 + 1) if i not in bigdata]
print(f'bigdata: {bigdata}\nnodata: {nodata}')

# 5-16-1
def times2(a):
    for i in range(len(a)):
        a[i] = a[i] * 2
    print(a)
nums = [1,2,3]
times2(nums)

# 5-16-2
def times2(k):
    k[0] = k[0] * 2
    k[1] = k[1] * 2
a = [1, 2]
b = [3, 4]
times2(a)
times2(b)
print('a=', a, 'b=', b)

# 5-16-3
fruitdb = [['사과', 1020], ['오렌지', 880], ['포도', 3160]]
for i in range(len(fruitdb)):
    print(fruitdb[i][0])

# 5-16-4
fruitdb = [['사과', 1020], ['오렌지', 880], ['포도', 3160]]
for i in range(len(fruitdb)):
    print('* 과일명: ', fruitdb[i][0], f' ( {fruitdb[i][1]} ) 원')

# 5-16-5
fruitdb = [['사과', 1020], ['오렌지', 880], ['포도', 3160]]
sum = 0
for i in range(len(fruitdb)):
    sum += fruitdb[i][1]
avg = sum / len(fruitdb)
print('%.1f원' % avg)

# 5-16-6
import random
def makelotto(a):
    while len(a) < 6:
        lotto = random.randint(1, 45)
        if lotto not in a:
            a.append(lotto)
win = []
my = []
makelotto(win)
makelotto(my)
win.sort()
my.sort()
print('금주 번호: ', win)
print('나의 번호: ', my)

# 5-17
pack = [(0, 0), (1, 1), (2, 4), (3, 9)]
for (x, y) in pack:
    print(x, y)

# 5-18
student = {'지훈': 1234, '수민':2345}
student['예원'] = 2012345
print(student)

# 5-19
fruitdb = {'사과': 1020, '오렌지': 880, '포도': 3160}
fruitdb['사과'] = 1250
print(fruitdb)

# 5-20-1
age = {'동혁': 21, '민지': 19, '준혁': 23}
print(age['동혁'])

# 5-20-2
age['민지'] = age['민지'] + 1
print(age['민지'])

# 5-20-3
student = {'GilDong':2345, 'SunSin':1234, 'SeJong': 3456}
for name in student:
    print(f'{name} : {student.get(name)}')
    # print(f'{name} : {student[name]}')

# 5-20-4
student = {'GilDong':2345, 'SunSin':1234, 'SeJong': 3456}
for name, num in student.items():
    print(name, num)

# 5-21
males = {0, 2, 4, 8, 9}
females = {1, 3, 5, 6, 7}
everyone = males | females
print(everyone & set([1, 2, 3, 10]))

# 5-22
word = 'Python Programming' # 18개 문자
letters = set(word)
print(len(letters))

# 5-23
traning_data = [
    ['연두', 3, '사과'], 
    ['노랑', 3, '사과'], 
    ['빨강', 2, '포도'], 
    ['빨강', 1, '포도'], 
    ['노랑', 3, '레몬']
]

def fruit_counts(data):
    counts = {}
    for row in data:
        color = row[0]
        if color not in counts:
            counts[color] = 0
        counts[color] += 1
    return counts
result = fruit_counts(traning_data)
print(result)