class Service:
    secret = '영구는 배꼽이 두 개다.'
    def __init__(self, name = 'noname'):
        self.name = name
    def setName(self, name):
        self.name = name
    def sum(self, a, b):
        result = a + b
        print('%s님 %s + %s = %s 입니다.' % (self.name, a, b, result))
pey = Service()
print(pey.secret)
pey.sum(1,2)
pey.setName('홍길동')
pey.sum(1,2)
jin = Service('홍진호')
jin.sum(3,4)