# 1
import random
for i in range(1, 100):
    n1 = random.randint(1, 100)
    n2 = random.randint(1, 100)
    q = n1 + n2
    print(f'{n1} + {n2} = ', end='')
    a = int(input())
    if q == a:
        print('=> "맞음!"')
    else:
        print('=> "틀림!"')
        break
    

# 2
size = float(input('지진의 리히터 규모를 입력하세요: '))
if size < 2.0:
    print('지진계에 의해서만 가능합니다.')
elif size < 4.0:
    print('물건들이 흔들리거나 떨어집니다.')
elif size < 7.0:
    print('빈약한 건물에 큰 피해가 있습니다.')
elif size < 8.0:
    print('지표면에 균열이 발생합니다.')
elif size <= 9.0:
    print('대부분의 구조물이 파괴됩니다.')

# 3
for i in range(1, 10):
    print('*' * i)

# 4
class Car:
    def __init__(self, name, color, speed):
        self.name = name
        self.color = color
        self.speed = speed
    def display(self):
        print(self.name, '의 색상은', self.color, '이며, 현재 속도는', self.speed, 'km입니다.')
car1 = Car('자동차1', '빨강', '30')
car2 = Car('자동차2', '파랑', '60')
car1.display()
car2.display()

# 5
i = 1
j = 2
while i <= 9:
    while j <= 9:
        print(f'{j} * {i} = {i*j}', end='\t')
        j += 1
    j = 2
    i += 1
    print()

# 6
import turtle
import random
rad = random.randint(50, 100)
turtle.circle(rad)


# 7
f = open("C:/Users/shg72/OneDrive/바탕 화면/NM_207618.2.fasta", "r")
sequence = f.read()
print(sequence)end of transform