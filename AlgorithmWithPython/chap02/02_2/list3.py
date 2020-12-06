# 리스트의 모든 원소를 enumerate() 함수로 스캔하기(1부터 카운트)

x = ['John', 'George', 'Paul', 'Ringo']

for i, name in enumerate(x, 1):
    print(f'x[{i}] = {name}')
'''
x[1] = John
x[2] = George
x[3] = Paul
x[4] = Ringo
'''