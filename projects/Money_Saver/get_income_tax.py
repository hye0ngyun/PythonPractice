import pandas as pd
df = pd.read_excel('./modified_simple_tax_amount_table.xls')
# print(df)
# 부양가족 = 1
# 월급 = 1999999
# 기준월급 = int(월급 / 1000)
# print(기준월급)
# 소득세 = df[df['미만'] > 기준월급].iloc[0][부양가족]
# print(소득세)


def get_income_tax(salary, dependents):
  """
  salary: 월급
  dependents: 부양가족
  """
  base_salary = int(salary / 1000)
  working_tax = df[df['미만'] > base_salary].iloc[0][dependents]
  # 소득세 반환
  return working_tax