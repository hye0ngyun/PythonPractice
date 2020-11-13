import re
example = '이동민 교수님은 다음과 같이 설명했습니다(이동민, 2019). 그런데 다른 교수님은 이 문제에 대해서 다른 견해를 가지고 있었습니다(최재영, 2019). 또 다른 견해도 있었습니다(Lion, 2018).'
result = re.findall(r'\([A-Za-z가-힣]+, \d+\)', example)
# \( ( [A-Za-z가-힣] 문자 + 한번이상 반복 , ??? \d 숫자 + 한번이상 반복 \) )
print(result)
result = re.findall(r'\([^\d]+, \d+\)', example)
# \( ( [^\d] == [A-Za-z가-힣] 숫자 제외한 문자 + 한번이상 반복 , ??? \d 숫자 + 한번이상 반복 \) )
print(result)
result = re.findall(r'\(.+\)', example)
# \( ( . 아무문자 + 한번이상 반복 \) )
print(result)
result = re.findall(r'\(.+?\)', example)
# \( ( . 아무문자 + 한번이상 반복 ? 있냐 \) )
print(result)
