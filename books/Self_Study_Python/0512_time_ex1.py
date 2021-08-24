# 1970.01.01 0시 기준으로 현재까지 흘러온 시간
# UTC, GMT 표준 시
import time as t

# gmtime() --> 그리니치 표준 시
t1 = t.gmtime()
print('-'*20+'time: GMT(gmtime)'+'-'*20)
print(f'{t1.tm_year}/{t1.tm_mon}/{t1.tm_mday}/{t1.tm_hour}/{t1.tm_min}')

print('-'*20+'time: local time(localtime)'+'-'*20)
t2 = t.localtime()
print(f'{t2.tm_year}/{t2.tm_mon}/{t2.tm_mday}/{t2.tm_hour}/{t2.tm_min}')

import datetime as d
d1 = d.datetime.now()
print('-'*20+'datetime: datetime(datetime)'+'-'*20)
print(d1)
print(f'{d1.year}/{d1.month}/{d1.day}/{d1.hour}/{d1.minute}/{d1.second}')

import calendar as cal
now = cal.calendar(1998)
print(cal.month(1998, 1))


