# 인턴을 시작하며 월급을 받는 사회초년생으로 돈 관리를 하기 위한 프로젝트
# salary: 급여, spending: 지출, reserve_fund: 예비자금

salary = '1,835,140'
salary = int(salary.replace(',', ''));

# 고정지출: 보험금, 청약금
fixed_spending = {
  '보장성 보험': 185000, 
  '실비 보험': 8000, 
  '주택청약': 100000
}

# 변동지출: 교통비, 식비 등
variable_spending = 300000

remaining = salary - (sum(fixed_spending.values()) + variable_spending)
print(remaining)

investment = {
  '주식': 300000, 
  '비트코인': 200000, 
}

reserved_fund = 250000

remaining -= (sum(investment.values()) + reserved_fund)
print(remaining)
