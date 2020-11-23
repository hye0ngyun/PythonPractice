class unit:
    unit_count = 0

    def __init__(self):
        print('unit create')
        unit.unit_count += 1
    def move(self):
        print('unit move')

class bird(unit):
    def __init__(self):
        print('bird create')
        super(bird, self).__init__()
    
class ground(unit):
    def __init__(self):
        print('ground create')
        super(ground, self).__init__()

b1 = bird()
b3 = bird()

b1.move()

g1 = ground()

print(unit.unit_count)