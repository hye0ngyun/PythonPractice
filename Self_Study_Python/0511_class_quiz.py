# Human 클래스 정의
# Human 클래스는 이름, 나이, 성별 멤버 변수를 가짐
# Human 클래스는 '안녕하세요 {나이} 살 {성별} {이름}입니다.'라고 출력하는 Hello 멤버 메서드를 가짐

# Human 클래스를 상속받는 Teacher 클래스 정의
# Teacher 클래스는 

class Human:
    def __init__(self, name, age, gender) -> None:
        self.name = name
        self.age = age
        self.gender = gender

    def hello(self):
        print(f'안녕하세요 {self.age} 살 {self.gender} {self.name}입니다.')

class Teacher(Human):
    def __init__(self, name, age, gender, object) -> None:
        super().__init__(name, age, gender)
        self.object = object
    
    def hello(self):
        print(f'안녕하세요 {self.object} 과목을 맡고있는 {self.age} 살 {self.gender} {self.name}입니다.')

h1 = Human('shin', 24, '남자')
t1 = Teacher('kim', 30, '여자', 'python')

t1.hello()