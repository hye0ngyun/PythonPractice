# std input, output
print('python', 'java', sep=',', end='?')
print('무엇이 더 재밌을까요?')

import sys
print('python', 'java', file=sys.stdout)
print('python', 'java', file=sys.stderr)

# 시험 성적
scores = {'수학': 0, '영어': 50, '코딩': 100}
for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4), sep=':')

# 은행 대기 순번표
# 001, 002, 003, ...
for num in range(1, 21):
    print('대기번호: ' + str(num).zfill(3))

# answer = input('아무 값이나 입력하세요: ')
# print('입력하신 값은 ' + answer + '입니다.')

# 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print('{0:>10}'.format(500))
# 양수일 땐 +로 표시, 음수일 땐 -로 표시
print('{0: >+10}'.format(500))
print('{0: >+10}'.format(-500))
# 왼쪽 정렬하고, 빈칸으로 _채움
print('{0:_<+10}'.format(500))
# 3자리 마다 콤마를 찍어주기
print('{0:,}'.format(10000000000000000))
# 3자리 마다 콤마를 찍어주기, 부호 표시하기
print('{0:+,}'.format(10000000000000000))
print('{0:,}'.format(-10000000000000000))
# 3자리 마다 콤마를 찍어주기, 부호도 붙이고, 자릿수 확보하기
# 돈이 많으면 행복하니까 빈 자리는 ^로 채워주기
print('{0:^<+30,}'.format(10000000000000000))
# 소수점 출력
print('{0}'.format(5/3))
print('{0:f}'.format(5/3))
print('{0:.2f}'.format(5/3))
# 파일 입출력
# score_file = open('score.txt', 'w', encoding='utf8')
# print('수학: 0', file=score_file)
# print('영어: 50', file=score_file)
# score_file.close()

# score_file = open('score.txt', 'a', encoding='utf8')
# score_file.write('과학: 80')
# score_file.write('\n코딩: 100')
# score_file.close()

# score_file = open('score.txt', 'r', encoding='utf8')
# print(score_file.read())
# score_file.close()

# score_file = open('score.txt', 'r', encoding='utf8')
# print(score_file.readline(), end='')
# print(score_file.readline(), end='')
# print(score_file.readline(), end='')
# print(score_file.readline(), end='')
# score_file.close()

# score_file = open('score.txt', 'r', encoding='utf8')
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end='')
# score_file.close()

# score_file = open('score.txt', 'r', encoding='utf8')
# lines = score_file.readlines() # list 형태로 저장
# for line in lines:
#     print(line, end='')
# score_file.close()

# pickle
import pickle
import os
print(os.getcwd())
os.chdir('./PythonProject/nado_coding')
print(os.getcwd())
# profile_file = open('profile.pickle', 'wb')
# profile = {'이름': '박명수', '나이': 30, '취미': ['축구', '골프', '코딩']}
# print(profile)
# pickle.dump(profile, profile_file) # profile에 있는 정보를 file에 저장
# profile_file.close()

# profile_file = open('profile.pickle', 'rb')
# profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기
# print(profile)
# profile_file.close()

# import pickle

# with open('profile.pickle', 'rb') as profile_file:
#     print(pickle.load(profile_file))

# with open('study.txt', 'w', encoding='utf8') as study_file:
#     study_file.write('파이썬을 열심히 공부하고 있어요.')
# with open('study.txt', 'r', encoding='utf8') as study_file:
#     print(study_file.read())

# if os.path.isdir('./quiz_test'):
#     pass
# else:
#     os.mkdir('./quiz_test')
# os.chdir('./quiz_test')
# print(os.getcwd())
# for i in range(1, 50 + 1):
#     with open(f'{i}주차.txt', 'w', encoding='utf8') as report_file:
#         report_file.write(f'- {i} 주차 주간보고 -')
#         report_file.write('\n부서: ')
#         report_file.write('\n이름: ')
#         report_file.write('\n업무 요약: ')

# class
# # 마린: 공격유닛, 군인, 총을 쏠 수 있음
# name = '마린' # 유닛의 이름
# hp = 40 # 유닛의 체력
# damage = 5 # 유닛의 공격력

# print(f'{name} 유닛이 생성됐습니다.')
# print(f'체력 {hp}, 공격력 {damage}\n')

# # 탱크: 공격유닛, 탱크, 포를 쏠 수 있음
# tank_name = '탱크' # 유닛의 이름
# tank_hp = 150 # 유닛의 체력
# tank_damage = 35 # 유닛의 공격력

# print(f'{tank_name} 유닛이 생성됐습니다.')
# print(f'체력 {tank_hp}, 공격력 {tank_damage}\n')

# # 탱크: 공격유닛, 탱크, 포를 쏠 수 있음
# tank2_name = '탱크' # 유닛의 이름
# tank2_hp = 150 # 유닛의 체력
# tank2_damage = 35 # 유닛의 공격력

# print(f'{tank2_name} 유닛이 생성됐습니다.')
# print(f'체력 {tank2_hp}, 공격력 {tank2_damage}\n')

# def attack(name, location, damage):
#     print(f'{name}: {location} 방향으로 적군을 공격합니다. [공격력 {damage}]')

# attack(name, '1시', damage)
# attack(tank_name, '1시', tank_damage)
# attack(tank2_name, '1시', tank2_damage)

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print(f'{self.name} 유닛이 생성됐습니다.')
        print(f'체력 {self.hp}, 공격력 {self.damage}')


marine1 = Unit('마린', 40, 5)
marine2 = Unit('마란', 40, 5)
tank = Unit('탱크', 150, 35)

# class member method

# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
    def move(self, location):
        print('[지상 유닛 이동]')
        print(f'{self.name}: {location} 방향으로 이동합니다. [속도 {self.speed}]')
# marine1 = Unit('마린', 40, 5)
# marine2 = Unit('마란', 40, 5)
# tank = Unit('탱크', 150, 35)

# 레이스: 공중 유닛, 비행기, 클로킹(상대방에게 보이지 않음)
# wraith1 = Unit('레이스', 80, 5)
# print(f'유닛 이름: {wraith1.name}, 공격력: {wraith1.damage}')

# 마인드 컨트롤: 상대방 유닛을 내 것으로 만드는 것(빼앗음)
# wraith2 = Unit('빼앗은 레이스', 80, 5)
# wraith2.clocking = True

# if wraith2.clocking == True:
#     print(f'{wraith2.name}는 현재 클로킹 상태입니다.')

# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, damage, speed):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print(f'{self.name}: {location} 방향으로 적군을 공격 합니다. [공격력 {self.damage}]')
    
    def damaged(self, damage):
        print(f'{self.name}: {damage} 데미지를 입었씁니다.')
        self.hp -= damage
        print(f'{self.name}: 현재 체력은 {self.hp}입니다.')
        if self.hp <= 0:
            print(f'{self.name}: 파괴되었습니다.')

# 파이어뱃: 공격 유닛, 화염방사기.
firebat1 = AttackUnit('파이어뱃', 50, 16, 5)
firebat1.attack('5시')

firebat1.damaged(25)
firebat1.damaged(25)

# 다중상속
# 드랍쉽: 공중유닛, 수송기. 마린 / 파이어뱃 / 탱크 등을 수송. 공격기능 없음

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
        print('[공중 유닛 이동]')
        self.fly(self.name, location)

# 발키리 공격 유닛 클래스
valkeyrie = FlyableAttackUnit('발키리', 200, 6, 5)
valkeyrie.fly(valkeyrie.name, '3시')

# 오버라이딩
# 벌쳐: 지상 유닛, 기동성이 좋음
vulture = AttackUnit('벌쳐', 80, 20, 10)

# 배틀크루저: 공중 유닛, 체력도 굉장히 좋음, 공격력도 좋음.
battlecrusier = FlyableAttackUnit('배틀크루저', 500, 25, 3)

vulture.move('11시')
# battlecrusier.fly(battlecrusier.name, '9시')
battlecrusier.move('9시')

# super
# 건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        # Unit.__init__(self, name, hp, 0)
        super().__init__(name, hp, 0)
        self.location = location

