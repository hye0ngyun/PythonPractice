import pandas as pd
import numpy as np
data = {
    'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
    'year': [2000, 2001, 2002, 2001, 2002, 2003],
    'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2],
}

frame = pd.DataFrame(data)
print(frame)
print(frame.head())
print(pd.DataFrame(data, columns=['year', 'state', 'pop']))

frame2 = pd.DataFrame(data, columns=['year', 'state', 'pop', 'debt'], index=['one', 'two', 'three', 'four', 'five', 'six'])
print(frame2)
print(frame2.columns)
print(frame2['state'])
print(frame2.year)

print(frame2.loc['three'])
frame2['debt'] = 16.5
print(frame2)

frame2['debt'] = np.arange(6.)
print(frame2)

val = pd.Series([-1.2, -1.5, -1.7], index = ['two','four', 'five'])
frame2['debt'] = np.NaN
frame2['debt'] = val
print(frame2)

# 새로운 컬럼인 eastern은 frame2.eastern 형태의 문법으로는 생성되지 않는다.
frame2['eastern'] = frame2.state == 'Ohio'
print(frame2)

print(frame2.columns)
del frame2['eastern']
print(frame2.columns)

pop = {
    'Nevada': {2001: 2.4, 2002: 2.9},
    'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}
}

frame3 = pd.DataFrame(pop, index=[2000, 2001, 2002])
print(frame3)
print(frame3.T)

pdata = {
    'Ohio': frame3['Ohio'][:-1],
    'Nevada': frame3['Nevada'][:2]
}

print(pd.DataFrame(pdata))