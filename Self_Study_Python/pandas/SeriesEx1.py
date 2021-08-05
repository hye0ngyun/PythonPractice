import pandas as pd
import numpy as np
obj = pd.Series([4, 7, -5, 3])
print(obj)
print(f'obj.index: {obj.index}') # range(4)와 같다.
print(f'obj.values: {obj.values}')

obj2 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
print(obj2)
print(f'obj2.index: {obj2.index}') # Index(['d', 'b', 'a', 'c'], dtype='object')
print(f'obj2.values: {obj2.values}')
print(f'obj2["a"]: {obj2["a"]}')

obj2['d'] = 6
print(obj2)

print(obj2[['a', 'b', 'c']])

print(obj2 * 2)

print(np.exp(obj2))


print('d' in obj2)
print('e' in obj2)

sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}

obj3 = pd.Series(sdata)
print(obj3)

states = ['California', 'Ohio', 'Oregon', 'Texas']

obj4 = pd.Series(sdata, index=states)
print(obj4)

print(pd.isnull(obj4))
print(pd.notnull(obj4))
print(obj4.isnull())

print(obj3)
print(obj4)
print(obj3 + obj4)

obj4.name = 'population'
obj4.index.name = 'state'

print(obj4)

print(obj)
obj.index = ['Bob', 'Steve', 'Jeff', 'Ryan']
print(obj)