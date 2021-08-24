# 실제 시간(real time)은 벽 시계(wall time)시간으로 부르기도 합니다.
import datetime
import time
print(datetime.datetime.now() + datetime.timedelta(minutes=1))