def open_account():
    print('새로운 계좌가 생성됐습니다.')

def deposit(balance, money):
    print('입금이 완료됐습니다. 잔액은 {}원입니다.'.format(balance + money))
    return balance + money

balance = 0
balance = deposit(balance, 1000)
print(balance)