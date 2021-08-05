# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

a = [1,2,3,4]
b = [1,4,9,16]
c = ['kbs', 'mbc', 'sbs', 'ytn']
d = {'이름': '손흥민', '나이': 30, '직업': '운동선수', '연봉': 200}
s1 = {1,2,3,4}
s2 = [2,4,6,8]

t1 = np.ndarray(a)

type(t1)

type(a)

a[3]

a.append(6)

a.append('string')

a

t1

t2 = np.ndarray([2,2])
t2

t3 = pd.Series(b)
list(t3.index)
for i in t3.values:
  print(i)

t4 = pd.Series(c)
t4

t5 = pd.Series(d)
t5

t6 = pd.DataFrame(t5)
t6

# Commented out IPython magic to ensure Python compatibility.
# %hist

d.values()

print(type(t4))
for i in t4.items():
  print(i)

w = {
    '월': 'qwer',
    '화': 'asdf',
    '수': 'zxcv'
}

t7 = pd.DataFrame(w.items())
t7

c = ['요일', '일과']
t7.columns = c

t7

t8 = np.array([[1,2], [3,4]])
list(t8.flatten())

tips = sns.load_dataset('tips')
tips

tips.info()

# for i, j in tips.items():
#   print(i, j)
# list(tips.items())

t = tips.copy()

sns.set(style='darkgrid')
# relation plot
sns.relplot(x='total_bill', y='tip', data=t, hue='sex')
plt.show()

sns.set(style='darkgrid')
# categori plot
sns.boxplot(x='day', y='total_bill', data=t)
plt.show()
print(t.describe())

sns.set(style='darkgrid')
# categori plot
sns.catplot(x='day', y='total_bill', data=t, hue='sex', kind='violin')
plt.show()

"""# Titanic"""

titanic = sns.load_dataset('titanic')

t = titanic.copy()

t
# survived 0 - dead, 1 - alive

sns.countplot(x='class', hue='who', data=t, palette='Blues')
plt.show()

sns.catplot(x='sex', y='survived', hue='class', kind='violin', data=t)
plt.show()

t.head(3)

sur = t.survived.sum() /t.survived.count()
print(round(sur * 100, 2),'%')

t.shape[0] - t.survived.sum()

t.shape[0]

t['pclass'].value_counts()

t['fare'].value_counts()

t[t.fare > 20].head()

t['embark_town'].value_counts()

t['age'].median()

k1 = [0, 18, 35, 60, 100]
k2 = ['아기', '청년', '장년', '노년']
t['연령대'] = pd.cut(t['age'], bins=k1, labels=k2)
t['연령대'].value_counts()

t['age'].max()

t['age'].min()

# %matplotlib inline  

# import matplotlib as mpl 
# import matplotlib.pyplot as plt 
# import matplotlib.font_manager as fm  

# !apt-get update -qq
# !apt-get install fonts-nanum* -qq

# path = '/usr/share/fonts/truetype/nanum/NanumBarunGothic.ttf' 
# font_name = fm.FontProperties(fname=path, size=10).get_name()
# print(font_name)
# plt.rc('font', family=font_name)

# fm._rebuild()
# mpl.rcParams['axes.unicode_minus'] = False

sns.barplot(x = '연령대', y = 'survived', data=t)
plt.show()

sns.countplot(y = 'class', data=t)
plt.show()

sns.countplot(y = 'age', data=t)
plt.show()

sns.countplot(y = 'sex', data=t)
plt.show()

sns.countplot(y = 'alive', data=t)
plt.show()

sns.countplot(y = 'alone', data=t)
plt.show()

t.groupby('class').std()

t.groupby('class')['fare'].median()

t.query('alive == "yes"').count()

t.query('alive == "yes"').groupby('class').count()

t.groupby('class')['age'].describe()

t.groupby('sex')['age'].aggregate([min, np.median, max])

# 30세 이상인 사람은?
# t[t.age >= 30].shape[0]
t.query('age >= 30').shape[0]
# t.query('age >= 30').groupby('class')

sns.catplot(x='who', y='fare', hue='class', kind='bar', data=t)
plt.show()

sns.catplot(x='who', y='survived', hue='class', kind='bar', data=t)
plt.show()

age = pd.cut(t['age'], [0, 18, 40, 80])
t.pivot_table('survived', ['sex', age], 'class')

age = pd.qcut(t['fare'], 3)
print(type(t))
t.pivot_table('survived', ['who', age], 'class')

# pd.cut() 길이
# pd.qcut() 개수
# test = np.arange(1, 10, 0.2)
# test
# pd.qcut()과 비슷한 np.linspace(start, end, num)
np.linspace(1, 21, 7)

sns.catplot(x='survived', y='embark_town', hue='class', kind='bar', data=t)
plt.show()

sns.catplot(x='sibsp', y='survived', hue='class', kind='bar', data=t)
plt.show()

sns.catplot(x='parch', y='survived', hue='class', kind='bar', data=t)
plt.show()

sns.catplot(x='alone', y='survived', hue='class', kind='bar', data=t)
plt.show()

