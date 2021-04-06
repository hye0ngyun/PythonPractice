# 6-1
class You:
    def setname(self, n):
        self.name = n
    def setage(self, a):
        self.age = a
    def show(self):
        print('이름:', self.name, '나이:', self.age)
my = You()
my.setname('준서')
my.setage(21)
my.show()

# 6-2
class Calc:
    def __init__(self, n):
        self.a = n
    def plus(self, value):
        print(self.a, '+', value, '=', self.a + value)
    def mult(self, value):
        print(self.a, '*', value, '=', self.a * value)
my = Calc(3)
my.plus(7)
my.mult(10)

# 6-3
class Calc:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
    def calcurate(self, op):
        if op == '+': print(f'{self.n1} + {self.n2} = {self.n1 + self.n2}')
        if op == '-': print(f'{self.n1} + {self.n2} = {self.n1 - self.n2}')
        if op == '*': print(f'{self.n1} + {self.n2} = {self.n1 * self.n2}')
        if op == '/': print(f'{self.n1} + {self.n2} = {self.n1 / self.n2}')
num1 = int(input('Num1: '))
num2 = int(input('Num2: '))
obj = Calc(num1, num2)
obj.calcurate('+')
obj.calcurate('*')

# 6-4
def fib(n):
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a + b
fib(8)
print()

# 6-5
a = [['도윤', 21], ['하준', 20], ['시우', 22]]
for x, y in a:
    print(x, ':', y, '세')

# 6-6
text = "AI! 나는 인공지능 로봇 입니다. 나는 'AI 로봇' 입니다."
def max_counts(text):
    skips = ['.', '!', '\'', ';', ' ', '"', ',']
    for ch in skips:
        text = text.replace(ch, ' ')
    counts = {}
    for i in text.split():
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    return counts
print(max_counts(text))

# 6-7
nums = [1, 1, 1, 2, 2, 3, 2, 3, 3, 3, 1]
def max_count(nums):
    counts = {}
    for i in nums:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    return counts
counts = max_count(nums)
first = []
max_num = max(counts.values())
for name, count in counts.items():
    print(name, ':', count, '번')
    if count == max_num:
        first.append(name)
print('1등:', first)

# 6-7
print(max(counts.values()))

# 6-8, 9
counts = {
    '홍': 3,
    '김': 2,
    '이': 1
}

# 6-8
print(counts.items())

# 6-9
for name, count in counts.items():
    print(name, count)

# 6-10
people = ['홍', '홍', '김', '이', '홍', '김']
def max_count(people):
    counts = {}
    for i in people:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    return counts
counts = max_count(people)
first = []
max_num = max(counts.values())
for name, count in counts.items():
    print(name, ':', count, '번')
    if count == max_num:
        first.append(name)
print('1등:', first)