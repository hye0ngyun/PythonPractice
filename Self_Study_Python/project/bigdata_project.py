 

import matplotlib as mpl 
import matplotlib.pyplot as plt 
import matplotlib.font_manager as fm  
path = '/usr/share/fonts/truetype/nanum/NanumBarunGothic.ttf' 
font_name = fm.FontProperties(fname=path, size=10).get_name()
print(font_name)
plt.rc('font', family=font_name)

fm._rebuild()
mpl.rcParams['axes.unicode_minus'] = False
# 

import pandas as pd
import matplotlib.pyplot as plt


year_use_19 = pd.read_csv('C:/Users/CPB06GameN/Downloads/2020sum.csv', encoding='cp949')
print(year_use_19)


year_use_19_gu = year_use_19['자치구']
year_use_19_gu
year_use_19_tot = year_use_19['총합계'].sort_values()
year_use_19_tot
# top5_19[0]은 자치구, top5_19[1]은 총사용량
top5_19 = [year_use_19_gu[year_use_19_tot[-1:-6:-1].index], year_use_19_tot[-1:-6:-1]]
top5_19[1]
# worst5_19 = year_use_19_gu[year_use_19_tot[:5].index]
# worst5_19

# ratio = [34, 32, 16, 18]
ratio = top5_19[1]
# labels = ['apple', 'banana', 'melon', 'grapes']
labels = top5_19[0] + ': ' +top5_19[1].astype('string')

plt.pie(ratio, labels=labels, autopct='%.f%%')
plt.title('2019년 공공자전거 구별 대여 건수 Top5')
plt.show()