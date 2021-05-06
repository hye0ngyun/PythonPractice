from random import *
# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        # print('[지상 유닛 이동]')
        print(f'{self.name}: {location} 방향으로 이동합니다. [속도 {self.speed}]')

    def damaged(self, damage):
        print(f'{self.name}: {damage} 데미지를 입었씁니다.')
        self.hp -= damage
        print(f'{self.name}: 현재 체력은 {self.hp}입니다.')
        if self.hp <= 0:
            print(f'{self.name}: 파괴되었습니다.')

# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, damage, speed):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print(f'{self.name}: {location} 방향으로 적군을 공격 합니다. [공격력 {self.damage}]')
    
# 마린
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, '마린', 40, 5, 1)
    
    # 스팀팩: 일정 시간 동안 이동 및 공격 속도를 증가, 체력 10 감소
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print(f'{self.name}: 스팀팩을 사용합니다. (HP 10 감소)')
        else:
            print(f'{self.name}: 체력이 부족하여 스팀팩을 사용하지 않습니다.')

# 탱크
class Tank(AttackUnit):
    # 시즈모드: 탱크를 지상에 고정시켜, 더 높은 파워로 공격 가능. 이동 불가.
    seize_developed = False # 시즈모드 개발 여부
    def __init__(self):
        AttackUnit.__init__(self, '탱크', 150, 35, 1)
        self.seize_mode = False
    
    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return
        # 현재 시즈모드가 아닐 때 -> 시즈모드
        if self.seize_mode == False:
            print(f'{self.name}: 시즈모드로 전환합니다.')
            self.damage *= 2
            self.seize_mode = True
        else:
            print(f'{self.name}: 시즈모드를 해제합니다.')
            self.damage /= 2
            self.seize_mode = False


class Flyable:
    def __init__(self, flying_Speed):
        self.flying_Speed = flying_Speed

    def fly(self, name, location):
        print(f'{name}: {location} 방향으로 날아갑니다. [속도 {self.flying_Speed}')

# 공중 공격 유닛
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_Speed):
        AttackUnit.__init__(self, name, hp, damage, 0)
        Flyable.__init__(self, flying_Speed)
    def move(self, location):
        # print('[공중 유닛 이동]')
        self.fly(self.name, location)

# 레이스
class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, '레이스', 80, 20, 5)
        self.clocked = False

    def clocking(self):
        if self.clocked == True:
            print(f'{self.name}: 클로킹 모드 해제합니다.')
            self.clocked = False
        else:
            print(f'{self.name}: 클로킹 모드 설정합니다.')
            self.clocked = True

def game_start():
    print('[알림] 새로운 게임을 시작합니다.')

def game_over():
    print('Player: gg')
    print('[Player] 님이 게임에서 퇴장하셨습니다.')

# 실제 게임 시작
game_start()

# 마린 3기 생성
m1 = Marine()
m2 = Marine()
m3 = Marine()

# 탱크 2기 생성
t1 = Tank()
t2 = Tank()

# 레이스 1기 생성
w1 = Wraith()

# 유닛 일괄 관리 (생성된 모든 유닛 append)
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

# 전군 이동
for unit in attack_units:
    unit.move('1시')

# 탱크 시즈모드 개발
Tank.seize_developed = True
print('[알림] 탱크 시즈모드 개발이 완료됐습니다.')

# 공격 모드 준비 (마린: 스팀팩, 탱크: 시즈모드, 레이스: 클로킹)
for unit in attack_units:
    if isinstance(unit, Marine):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()

# 전군 공격
for unit in attack_units:
    unit.attack('1시')

# 전군 피해
for unit in attack_units:
    unit.damaged(randint(5, 21))

# 게임 종료
game_over()