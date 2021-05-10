class Korea(object):
    global gv
    gv = 100
    lv = 200
    def __init__(self, city, pop):
        self.city = city
        self.pop = pop
        print(f'Korea {self.city}__init__: 생성자 호출')
    def __del__(self):
        print(f'Korea {self.city}__del__: 소멸자 호출')

Korea('1', 'BTS')
Korea('2', 'BTS')
k2 = Korea('3', 'BTS')
Korea('2', 'BTS')
print(f'global variable gv: {gv}')
# print(f'global variable gv: {Korea.gv}')
print(f'local variable Korea.lv: {Korea.lv}')
# print(f'local variable Korea.lv: {lv}')