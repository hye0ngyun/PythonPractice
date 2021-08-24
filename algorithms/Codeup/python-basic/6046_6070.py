#6046
print(int(input())<<1)
#6047
a, b = map(int, input().split())
print(a * (2 ** b))
#6048
a, b = map(int, input().split())
print(a < b)
#6049
a, b = map(int, input().split())
print(a == b)
#6050
a, b = map(int, input().split())
print(a <= b)
#6051
a, b = map(int, input().split())
print(a != b)
#6052
print(bool(int(input())))
#6053
print(not bool(int(input())))
#6054
a, b = map(int, input().split())
print(bool(a) and bool(b))
#6055
a, b = map(int, input().split())
print(bool(a) or bool(b))
#6056
a, b = map(int, input().split())
if (bool(a) != bool(b)):
    print(True)
else:
    print(False)
#6057
a, b = map(int, input().split())
if (bool(a) == bool(b)):
    print(True)
else:
    print(False)
#6058
a, b = map(int, input().split())
print(bool(a) is False and bool(b) is False)
#6059
print(~int(input()))
#6060
a, b = map(int, input().split())
print(a & b)
#6061
a, b = map(int, input().split())
print(a | b)
#6062
a, b = map(int, input().split())
print(a ^ b)
#6063
a, b = map(int, input().split())
print(a if a > b else b)
#6064
a, b, c = map(int, input().split())
print((a if a < b else b) if (a if a < b else b) < c else c)
#6065
data = input().split()
for i in data:
    if(int(i) % 2 == 0):
        print(int(i))
#6066
data = input().split()
for i in data:
    if(int(i) % 2 == 0):
        print('even')
    else:
        print('odd')
#6067
data = int(input())
if(data % 2 == 0 and data < 0):
    print('A')
elif(data % 2 != 0 and data < 0):
    print('B')
elif(data % 2 == 0 and data > 0):
    print('C')
elif(data % 2 != 0 and data > 0):
    print('D')
#6068
score = int(input())
if(score >= 90):
    print('A')
elif(score >= 70):
    print('B')
elif(score >= 40):
    print('C')
elif(score >= 0):
    print('D')
#6069
grade = input()
if(grade == 'A'):
    print('best!!!')
elif(grade == 'B'):
    print('good!!')
elif(grade == 'C'):
    print('run!')
elif(grade == 'D'):
    print('slowly~')
else:
    print('what?')
#6070
month = int(input())
season = ''
if(month in [12, 1, 2]):
    season = 'winter'
elif(month in [3, 4, 5]):
    season = 'spring'
elif(month in [6, 7, 8]):
    season = 'summer'
else:
    season = 'fall'
print(season)