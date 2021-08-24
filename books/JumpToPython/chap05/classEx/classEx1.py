result1 = 0
result2 = 0

print('함수 이용')
def adder1(num):
    global result1
    result1 += num
    return result1
def adder2(num):
    global result2
    result2 += num
    return result2
print(adder1(3))
print(adder1(4))
print(adder2(4))
print(adder2(7))

print('클래스 이용')
class Calcurator:
    def __init__(self):
        self.result = 0
    
    def adder(self, num):
        self.result += num
        return self.result

cal1 = Calcurator() # cla1 인스턴스(객체)
# cal1은 객체, cal1은 Calcurator의 인스턴스
cal2 = Calcurator() # cal2 인스턴스(객체)

print(cal1.adder(3))
print(cal1.adder(4))
print(cal2.adder(4))
print(cal2.adder(7))
