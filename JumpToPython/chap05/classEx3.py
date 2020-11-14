# 클래스 : 사칙연산
class FourCalc:
    def setdata(self, a, b):
        self.a = a
        self.b = b
    def sum(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b
calc = FourCalc()
calc.setdata(10, 3)
print(calc.sum())
print(calc.sub())
print(calc.mul())
print(calc.div())