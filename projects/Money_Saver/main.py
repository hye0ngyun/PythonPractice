# 사용자 정의 모듈
from deduction import *

# 인턴을 시작하며 월급을 받는 사회초년생으로 돈 관리를 하기 위한 프로젝트

# before_tax_salary: 세전 월급
# after_tax_salary: 세후 월급
# income_tax: 소득세

#########################################################################

# 급여일
pay_day = 31
# dependents: 부양가족
dependents = 1
# 세전월급
before_tax_salary = '2,000,000'
before_tax_salary = int(before_tax_salary.replace(',', ''))

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
# 입력받은 지출을 항목마다 넣기
spendings = {k: v for k, v in spendings.items()}
# print(sum(accounts.values()))

def get_accounts(accounts):
  for account, money in accounts.items():
    print(account, money)


def get_spendings(spendings):
  for name, spending in spendings.items():
    print(name, spending)

# get_accounts()


deductions = get_deduction(before_tax_salary, dependents)
print(f'총 공제금: {sum(deductions.values())}')
# get_spendings(deductions)

## 입금 후

## 
accounts["salary"] = before_tax_salary
print(f'세전 급여: {accounts["salary"]}')
# 공적 지출
spendings['public'] = deductions
accounts["salary"] -= sum(spendings['public'].values())
print('급여일: 31일')
print(f'공적 지출: {sum(spendings["public"].values())}')
print(f'세후 급여: {accounts["salary"]}')
get_accounts(accounts)
print('-' * 20)
import numpy as np
# 고정 지출
spendings['fixed'] = {
  "암 보험": [50000, 5], 
  "상해 보험": [36200, 5], 
  "사망 보험": [185000, 5], 
  "실비 보험": [7827, 5], 
  "주택 청약": [100000, 1], 
  "보험 할부": [500000, 1], 
  "유튜브 프리미엄": [8960, 1], 
  "넷플릭스": [3000, 1], 
  "핸드폰 요금": [23650, 9], 
}
print('고정지출 금액')
print(np.array(list(spendings["fixed"].values()))[:, 0])
print('고정지출 날짜')
print(np.array(list(spendings["fixed"].values()))[:, 1].max())
accounts["salary"] -= np.array(list(spendings["fixed"].values()))[:, 0].sum()
print(f'고정 지출 마지막 날짜: {np.array(list(spendings["fixed"].values()))[:, 1].max()}일')
print(f'고정 지출: {np.array(list(spendings["fixed"].values()))[:, 0].sum()}')
print(f'급여 잔액: {accounts["salary"]}')
get_accounts(accounts)
print('-' * 20)

# 소비 지출
spendings['variable'] = {
  "생활비": 300000
}
accounts['consumption'] = sum(spendings['variable'].values())
accounts["salary"] -= sum(spendings['variable'].values())
print('소비 금액 자동이체일: 5일')
print(f'소비 지출: {sum(spendings["variable"].values())}')
print(f'급여 잔액: {accounts["salary"]}')
get_accounts(accounts)
print('-' * 20)

# 계절 지출
spendings['seasonal'] = {
  '휴가비': 0
}

investment_money = {
  "주식": 200000, 
  "비트코인": 200000
}
accounts['investment'] = sum(investment_money.values())
accounts["salary"] -= sum(investment_money.values())
print('투자 금액 자동이체일: 5일')
print(f'투자 금액: {sum(investment_money.values())}')
print(f'급여 잔액: {accounts["salary"]}')
print('-' * 20)

# 급여 통장에 남은 모든 금액을 예비 통장으로 옮기기
print('직접 확인하는 날: 5일 저녁')
accounts['salary'], accounts['preliminary'] = accounts['preliminary'], accounts['salary']
get_accounts(accounts)
