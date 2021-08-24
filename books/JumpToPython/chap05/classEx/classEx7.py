class Character:
    char_cnt = 0

    def __init__(self, hp, damage, defence):
        self.info = {
            'hp' : hp,
            'damage' : damage,
            'defence' : defence,
        }

        Character.char_cnt += 1

        print('player가 생성되었습니다. 생성된 유닛 수 : {}'.format(Character.char_cnt))
    
    def __call__(self):
        print('htp : {}, damage : {}, defence : {}'.format(self.info['hp'], self.info['damage'], self.info['defence']))
    
    def __del__(self):
        Character.char_cnt -= 1
        print('player가 제거되었습니다. 생성된 유닛 수 : {}'.format(Character.char_cnt))

player_a = Character(10, 20, 30)
player_b = Character(100, 200, 300)
player_c = Character(100, 200, 300)
player_d = Character(100, 200, 300)
player_e = Character(100, 200, 300)

del player_c

print('program end')