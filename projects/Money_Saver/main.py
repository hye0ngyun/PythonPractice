# 사용자 정의 모듈
from deduction import *

# 인턴을 시작하며 월급을 받는 사회초년생으로 돈 관리를 하기 위한 프로젝트

# before_tax_salary: 세전 월급
# after_tax_salary: 세후 월급
# income_tax: 소득세

#########################################################################

accounts = {
  "salary": 0,      # 급여
  "consumption": 0, # 소비
  "investment": 0,  # 투자
  "preliminary": 0, # 예비
}
spendings = {
  "public": {},      # 공적
  "fixed": {},       # 고정
  "variable": {},    # 소비
  "seasonal": {},    # 계절
}


def get_accounts():
  for account, money in accounts.items():
    print(account, money)


def get_spendings():
  for name, spending in spendings.items():
    print(name, spending)
spendings['variable'] = {'식비': 10}
get_accounts()
get_spendings()
#####################################################################################
# 입력된 spending dict들의 총값을 구하는 함수
def get_spendings(*args):
  total_money = 0
  for arg in args:
    for money in arg.values():
      total_money += money
  return total_money


# 급여일
pay_day = 31
# dependents: 부양가족
dependents = 1
# 입력 받을 때 ','있던 없던 인식할 수 있도록 해야 함
# 세전 월급
before_tax_salary = '2,000,000'
before_tax_salary = int(before_tax_salary.replace(',', ''))
print(f'세전 금액: {before_tax_salary}')

# 공적 지출
spending["public"] = get_deduction(before_tax_salary, dependents)
print(f'공제 금액: {spending["public"]}')

# 세후 월급
after_tax_salary = before_tax_salary - spending["public"]
print(f'세후 금액: {after_tax_salary}')

# 급여 통장
account["salary"] = after_tax_salary
# 소비 통장
account["consumption"] = 0
# 투자 통장
account["investment"] = 0
# 예비 통장
account["preliminary"] = 0
investment_account = ''
preliminary_account = ''

money = after_tax_salary


# 공제금: 자료 찾아서 자동적으로 계산할 수 있도록 해야 함
public_spending = get_deduction(money, dependents)
print(public_spending)

# 고정 지출
spending["fixed"] = {
  '암 보험': 50000, 
  '상해 보험': 36200, 
  '실비 보험': 7827, 
  '사망 보험': 185000,
  '주택 청약': 100000, 
  '보험 할부': 500000, # 2022. 08. 까지 11회 남음
}
# 변동성 지출
spending["variable"] = {
  # '식비': 200000, 
  # '교통비': 62000, 
  '생활비': 300000, 
}

# 계절성 지출
spending["seasonal"] = {
  '휴가비': 0
}

# 현재 public_spending이 세후 금액으로 돼있음 추후 수정 해야함
# print(public_spending - get_money(fixed_spending, variable_spending, seasonal_spending))
print(spending)

# 지출 제외한 금액
# remain_money = salary_account - (public_spending.values())

investment_money = {
  '적금': 200000, 
  '주식': 200000
}

def display(spending):
  for name, money in spending.items():
    print(f'{name}: {money}원')
  print(f'총 지출: {get_spendings(spending)}원')


def display_all():
  for spd in spending.values():
    print(spd)
    print('-'*20)


  # 투자 금액 리스트와 총합계 출력
  display(investment_money)
  print('-'*20)

display_all()