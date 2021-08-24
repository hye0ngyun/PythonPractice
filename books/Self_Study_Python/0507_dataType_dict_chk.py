# check
# 1
dict_a = {}
dict_a['name'] = '구름'
print(dict_a)
del dict_a['name']
print(dict_a)

# 2
pets = [
    {'name': '구름', 'age': 5},
    {'name': '초코', 'age': 3},
    {'name': '아지', 'age': 1},
    {'name': '호랑이', 'age': 1}
]
print('# 우리 동네 애완 동물들')
for dic in pets:
    print(f'{dic["name"]} {dic["age"]}살')

# 3
import random
numbers = [random.randint(1, 9) for x in range(20)]
counter = {}
for number in numbers:
    if number in counter:
        counter[number] += 1
    else:
        counter[number] = 1
print(f'numbers: {numbers}\ncounter: {counter}')
sorted_kv = sorted(counter.items())
print(f'sorted_kv: {sorted_kv}')
sorted_cnt = {}
for key, value in sorted_kv:
    sorted_cnt[key] = value
print('after sort')
print(f'numbers: {numbers}\ncounter: {sorted_cnt}')

# 4
character = {
    'name': '기사',
    'level': 12,
    'items': {
        'sword': '불꽃의 검',
        'armor': '풀플레이트'
    },
    'skill': ['베기', '세게 베기', '아주 세게 베기']
}

for key, value in character.items():
    if type(value) is dict:
        for k, v in value.items():
            print(k, v, sep=' : ')
    elif type(value) is list:
        for v in value:
            print(key, v, sep=' : ')
    else:
        print(key, value, sep=' : ')
# for key in character:
#     if type(character[key]) is dict:
#         for k in key:
#             print(f'k-{k} : key-{key[k]}')
#     elif type(character[key]) is list:
#         for k in character[key]
#     print(f'{key} : {character[key]}')