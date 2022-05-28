from deduction import *

result = Element('result')
result.element.innerText = 1
def calculate(*args):
  # 부양가족 수
  dependents = Element('dependents').value
  # 비과세액
  taxfree = Element('taxfree').value
  # 세전월급
  el_before_tax_salary = Element('salary')
  before_tax_salary = el_before_tax_salary.value
  before_tax_salary = int(before_tax_salary.replace(',', ''))

  # 세전월급과 부양가족수로 각 공제금 구하기
  deductions = get_deduction(before_tax_salary, dependents, taxfree)
  
  el_deductions = Element('deductions')
  # 실수령 금액
  result.element.innerText = before_tax_salary - sum(deductions.values())

  # 공제금 총합
  el_deductions.element.innerText = sum(deductions.values())

  # 항목별 공제금
  Element('국민연금').element.innerText = deductions['국민연금']
  Element('건강보험').element.innerText = deductions['건강보험']
  Element('장기요양').element.innerText = deductions['장기요양']
  Element('고용보험').element.innerText = deductions['고용보험']
  Element('소득세').element.innerText = deductions['소득세']
  Element('지방소득세').element.innerText = deductions['지방소득세']
  