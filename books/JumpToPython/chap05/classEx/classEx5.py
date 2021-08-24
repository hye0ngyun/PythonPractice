class Character:
    # [self.변수]의 형태로 속성을 만들어준다. 해당 메소드가 종료되면 self로 선언된 속성이 아닌 변수들은 메모리 공간에서 지워집니다.
    '''
    def create(self, hp, attack, defence):
        self.hp = hp
        self.attack = attack
        self.defence = defence        
    '''
    def __init__(self, hp, damage, defence):
        self.hp = hp
        self.damage = damage
        self.defence = defence
        print('player가 생성되었습니다.')
    def move(self):
        print(self, 'move')
    def attack(self):
        print(self, 'attack')
    def show_info(self):
        print('hp : {}, damage : {}, defence : {}'.format(self.hp, self.damage, self.defence))
    
    def __call__(self):
        print('hp : {}, damage : {}, defence : {}'.format(self.hp, self.damage, self.defence))

    def __getitem__(self, name):
        return name

    def __del__(self):
        print('player가 죽었습니다.')
player_a = Character(10, 20, 30)
player_b = Character(100, 200, 300)
'''
player_a.move()
player_a.attack()
player_b.move()
player_b.attack()
'''
# player_a.create(10, 20, 30)
# player_b.create(100, 200, 300)

player_a.show_info()
player_b.show_info()

print('-'*20)
player_a()
player_b()
print('-'*20)
print(player_a.hp, player_a['damage'], player_a.defence)
print('-----program end-----')