#오류 일부러 발생시키기
class Bird:
    def fly(self):
        raise NotImplementedError
#class Eagle(Bird):
#    pass   // NotImplementedError 오류 발생
class Eagle(Bird):
    def fly(self):
        print('Eagle Fly')
eagle = Eagle()
eagle.fly()
