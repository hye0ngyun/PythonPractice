gv = 500 # 전역변수 global variable
CUR_YEAR = 2021

class Date(object):
    def __init__(self, year, month):
        # self.year 멤버 변수
        # year 전달받은 값
        self.age = self.get_age1(year)
        self.month = month
        print(id(self))
    def disp_Date(self):
        print(f'{self.year}년{self.month}월')
    def get_age1(self, year):
        return CUR_YEAR - year + 1

d1 = Date(2021, 10)
print(id(d1))

class Man(Date):

    cnt = 0 # class 변수

    # @ -> 장식자, 데코레이터
    @staticmethod
    def get_cnt1():
        return Man.cnt

    @classmethod
    def get_cnt2(cls):
        return Man.cnt

    # 객체 생성 시 자동 호출(constructor)되는 함수, 생성자
    def __init__(self, name, year, month):
        super().__init__(year, month)
        # Date.__init__(self, year, month)
        self.name = name
        self.cnt += 1
        print(f'Man __init__', self.cnt)
    
    def get_age1(self, year):
        return CUR_YEAR - year + 1

    # 객체 소멸 시 자동 호출(destructor)되는 함수, 소멸자
    def __del__(self):
        print(f'Man __del')
        self.cnt -= 1

    def __str__(self) -> str:
        return f'{self.name}님은 {self.age}살'
    
    # 아래 같은 메서드 이름으로 매개변수 개수를 다르게 정의하니 기존 메서드 사라짐
    def disp_Man(self):
        print(f'Man name: {self.name}, Man age: {self.age}')
    # method overloading 지원 안함
    # def disp_Man(self, num):
    #     print(f'Man name: {self.name}, Man age: {self.age+num}')

    @staticmethod
    def disp_Obejct(self):
        print(f'현재 객체 수: {self.cnt}')
    
    # method 재정의 overriding
    def __eq__(self, other):
        if self.name == other.name and self.age == other.age:
            return True
        else:
            return False

    def __add__(self, num):
        self.age += num
        
    def __sub__(self, num):
        self.age -= num

    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name
    
    def get_age(self):
        return self.age
    
    def set_age(self, age):
        self.age = age

    def A1(self, x):
        return x + x
    def A1(self, x, y):
        return x + y

m1 = Man('손흥민', 1992, 7)
m1.disp_Man()


# print('-'*20)
# # Man.disp_Obejct(Man)
# print(f'현재 객체의 수: {Man.cnt}')
# m1 = Man('손흥민', 30)
# m2 = Man('이강인', 24)
# m3 = Man('손흥민', 30)
# print(m1 == m3)
# print(f'id(m1): {id(m1)}, id(m3): {id(m3)}')
# # Man.disp_Obejct(Man)
# print(f'현재 객체의 수: {Man.cnt}')
# print(m1)
# print(m1.__str__())
# # m1.disp_Man()
# # m1 + m2

# # print(f'm1.age: {m1.age}, m2.age: {m2.age}')
# m1.disp_Man()
# m2.disp_Man()
# m1 + 2
# m2 - 4
# print('-'*20)
# # print(f'm1.age: {m1.age}, m2.age: {m2.age}')
# m1.disp_Man()
# m2.disp_Man()