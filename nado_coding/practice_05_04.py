# def ex1
def open_account():
    print('새로운 계좌가 생성됐습니다.')

def deposit(balance, money):
    print('입금이 완료됐습니다. 잔액은 {}원입니다.'.format(balance + money))
    return balance + money

def withdraw(balance, money):
    if balance >= money:
        print('출금이 완료됐습니다. 잔액은 {}원입니다.'.format(balance-money))
        return balance - money
    else:
        print('출금이 완료되지 않았습니다. 잔액은 {}원입니다.'.format(balance))
        return balance

def withdraw_night(balnce, money):
    commission = 100
    return commission, balance - money - commission

balance = 0
balance = deposit(balance, 1000)
balance = withdraw(balance, 2000)
commission, balance = withdraw_night(balance, 500)
print(f'수수료는 {commission}원이며, 잔액은 {balance}원입니다.')
print(balance)


# def ex2 기본값
# def profile(name, age, main_lang):
#     print(f'이름: {name}\t나이: {age}\t주 사용 언어: {main_lang}')

# profile('유재석', 20, '파이썬')
# profile('김태호', 25, '자바')

def profile(name, age = 17, main_lang = '파이썬'):
    print(f'이름: {name}\t나이: {age}\t주 사용 언어: {main_lang}')

profile('유재석')
profile('김태호')

# def ex3 키워드값
def profile(name, age, main_lang):
    print(name, age, main_lang)
profile(name='유재석', main_lang='파이썬', age=20)

# def ex4 가변인자
def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print(f'이름: {name}\t나이: {age}\t', end=' ')
    print(lang1, lang2, lang3, lang4, lang5)

profile('유재석', 20, 'python', 'java', 'c', 'c++', 'c#')
profile('김태호', 25, 'kotlin', 'swift', '', '', '')

print('-' * 10 + ' 가변인자 ' + '-' * 10)
def profile(name, age, *language):
    print(f'이름: {name}\t나이: {age}\t', end=' ')
    for lang in language:
        print(lang, end=' ')
    print()

profile('유재석', 20, 'python', 'java', 'c', 'c++', 'c#', 'ruby')
profile('김태호', 25, 'kotlin', 'swift')

# local variable, global variable
gun = 10
def checkpoint(soldiers):
    global gun
    gun = gun - soldiers
    print(f'[함수 내] 남은 총: {gun}')

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print(f'[함수 내] 남은 총: {gun}')
    return gun

print(f'전체 총: {gun}')
# checkpoint(2)
gun = checkpoint_ret(gun, 2)
print(f'남은 총: {gun}')

# 퀴즈
def std_weight(height, gender):
    if gender == '남자':
        return (height/100) ** 2 * 22
    elif gender == '여자':
        return height ** 2 * 21
    else:
        print('Error: incorrect input')

height = 175
gender = '남자'
weight = std_weight(height, gender)
print(f'키 {height}cm {gender}의 표준 체중은 {weight:.2f}kg 입니다.')