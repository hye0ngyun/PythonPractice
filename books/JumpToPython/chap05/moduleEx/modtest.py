''' # 기본적인 모듈사용
import moduleEx1
print(moduleEx1.sum(3,4))
print(moduleEx1.safe_sum(5,6))
print(moduleEx1.safe_sum(5,'a'))
'''
# from 모듈명 import 함수명으로 모듈을 사용하면 함수 호출시 모듈명을 생략할 수 있다.
from moduleEx1 import *
print(sum(3,4))
print(safe_sum(5,6))
print(safe_sum(5,'a'))

import moduleEx2
print(moduleEx2.PI)
a = moduleEx2.Math()
print(a.solv(2))