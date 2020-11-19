# time
import time
print(time.time())  #  1970년 1월 1일 0시 0분 0초를 기준으로 지난 시간을 초 단위로 리턴한다.
# time.localtime()은 time.time()에 의해서 반환된 실수값을 이용해서 연도, 달, 일, 시, 분, 초, ... 의 형태로 바꿔준다.
print(time.localtime(time.time()))  # time.struct_time(tm_year=2020, tm_mon=11, tm_mday=19, tm_hour=16, tm_min=35, tm_sec=29, tm_wday=3, tm_yday=324, tm_isdst=0)
# time.asctime()은 time.localtime()에 의해 반환된 튜플 형태의 값을 인수로 받아서 날짜와 시간을 알아보기 쉬운 형태로 리턴하는 함수이다.
print(time.asctime(time.localtime(time.time())))    # Thu Nov 19 16:38:55 2020
# time.ctime()은 time.asctime(time.localtime(time.time()))을 간편하게 표시할 수 있는 함수이다. asctime과 다른점은 ctime은 항상 현재 시간만을 리턴한다.
print(time.ctime())
# time.strftime('출력할 형식 포맷 코드', time.timelocal(time.time()))은 시간에 관계된 것을 세밀하게 표현할 수 있는 여러 가지 포맷 코드를 제공한다.
print(time.strftime('%x', time.localtime(time.time()))) # %x는 현재 설정된 로케일에 기반한 날짜를 출력한다. 11/19/20
print(time.strftime('%c', time.localtime(time.time()))) # %c는 날짜와 시간을 출력한다. Thu Nov 19 16:43:46 2020
# time.sleep()함수는 주로 루프 안에서 많이 사용된다. 이 함수를 이용하면 일정한 시간간격을 두고 루프를 실행할 수 있다.
for i in range(10):
    print(i)
    #time.sleep(1)   # 1초 간격으로 0부터 9까지의 숫자를 출력한다.
# calendat는 파이썬에서 달력을 볼 수 있게 해주는 모듈이다.
import calendar
# calendar.calendar(연도)는 연도의 1~12월 달력을 출력
print(calendar.calendar(2020))  # 2020년도 1월부터 12월까지의 달력을 출력
# calendar.weekday(연도, 월, 일)는 해당 날짜의 요일을 리턴한다.
print(calendar.weekday(2020, 11, 19))   # 3을 리턴 3은 목요일을 의미 월요일은 0~ 일요일은 6을 리턴
# calendar.monthrange(연도, 월)는 입력받은 달의 1일이 무슨요일인지와 그달이 며칠까지 있는지 튜플 형태로 리턴
print(calendar.monthrange(2020, 11))    # (6, 30) --> 일, 30일
