# 인턴을 시작하며 월급을 받는 사회초년생으로 돈 관리를 하기 위한 프로젝트
# salary: 급여, spending: 지출, reserve_fund: 예비자금

# salary = '1,810,330'
# salary = int(salary.replace(',', ''));

# # 고정지출: 보험금, 청약금
# fixed_spending = {
#   '보장성 보험': 185000, 
#   '실비 보험': 8000, 
#   '암 보험': 50000, 
#   '상해 보험': 40000, 
#   '주택청약': 100000, 
#   '갚을 보험금': 250000
# }

# # 변동지출: 교통비, 식비 등
# variable_spending = 300000

# remaining = salary - (sum(fixed_spending.values()) + variable_spending)
# print(remaining)

# # 투자금
# investment = {
#   '주식': 300000, 
#   '비트코인': 200000, 
# }

# # 예비자금
# reserved_fund = 200000

# remaining -= (sum(investment.values()) + reserved_fund)
# print(remaining)

#########################################################################

# 급여일
pay_day = 31

# 입력 받을 때 ','있던 없던 인식할 수 있도록 해야 함
salary_account = '1,810,330'
# consumption_account = variable_spending
investment_account = ''
preliminary_account = ''

# 입력된 spending dict들의 총값을 구하는 함수
def get_money(*args):
  total_money = 0
  for arg in args:
    for money in arg.values():
      total_money += money
  return total_money

# 자료 찾아서 자동적으로 계산할 수 있도록 해야 함
public_spending = {
  '소득세': 123, 
  '국민연금': 123, 
  '건강보험료': 123,
}
# 매월 정기적으로 나가는 금액
fixed_spending = {
  '암 보험': 50000, 
  '상해 보험': 40000, 
  '실비 보험': 10000, 
}
# 생활비, 매월
variable_spending = {
  '식비': 200000, 
  '교통비': 62000
}

seasonal_spending = {
  '휴가비': 0
}

print(get_money(public_spending, fixed_spending, variable_spending, seasonal_spending))

# 지출 제외한 금액
# remain_money = salary_account - (public_spending.values())

investment_money = {

}