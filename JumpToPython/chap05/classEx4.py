# 클래스 : 신씨네 집
class HouseShin:
    lastname = '신'
    def __init__(self, firstname):  # __init__는 생성자(Constructor)라고 한다.
        self.fullname = self.lastname + firstname
    #def setname(self, firstname):
    #    self.fullname = self.lastname + firstname
    def travel(self, region):
        print('{}, {}여행을 가다.'.format(self.fullname, region))
    def love(self, other):
        print('{}, {} 사랑에 빠졌네'.format(self.fullname, other.fullname))
    def fight(self, other):
        print('{}, {} 싸우네'.format(self.fullname, other.fullname))
    def __add__(self, other):
        print('{}, {} 결혼했네'.format(self.fullname, other.fullname))
    def __sub__(self, other):
        print('{}, {} 이혼했네'.format(self.fullname, other.fullname))

# 클래스의 상속
class HouseKim(HouseShin):
    lastname = '김'
    # travel 메서드 오버라이딩
    def travel(self, region, day):
        print('%s, %s여행 %s일 가네.' %(self.fullname, region, day))

pey = HouseShin('현균')
#pey.setname('현균')
juliet = HouseKim('줄리엣')
pey.travel('포항')
juliet.travel('포항', 3)
pey.love(juliet)
pey + juliet
pey.fight(juliet)
pey - juliet