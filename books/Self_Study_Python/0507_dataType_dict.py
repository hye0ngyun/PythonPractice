# --- define dictionary ---
print('--- define dictionary ---')
dict_a = {
    'name': '어벤저스 엔드게임',
    'type': '히어로 무비'
}

# --- print dictionary ---
print('--- print dictionary ---')
print(f'dict_a: {dict_a}')
print(f'dict_a.keys(): {dict_a.keys()}')
print(f'dict_a.values(): {dict_a.values()}')
print(f'dict_a.items(): {dict_a.items()}')

# --- for loop with dict---
print('--- for loop with dict---')
print(f'for dic in dict_a:')
for key in dict_a:
    print(key)
print(f'for key in dict_a.keys():')
for key in dict_a:
    print(key)
print(f'for value in dict_a.values():')
for value in dict_a.values():
    print(value)
print(f'for key in dict_a.items():')
for key in dict_a.items():
    print(key)
print(f'for key, value in dict_a.items():')
for key, value in dict_a.items():
    print(key, value)

# --- get value from key---
print('--- get value from key---')
print(f"dict_a['name']: {dict_a['name']}")
print(f"dict_a.get('name'): {dict_a.get('name')}")

print(f"dict_a['type']: {dict_a['type']}")
print(f"dict_a.get('type'): {dict_a.get('type')}")

# --- set value form key---
print('--- set value form key---')
dict_a['name'] = '아이언맨'
print(f">>> dict_a['name'] = 아이언맨")
print(f"dict_a['name']: {dict_a['name']}")

# --- add key and value in dict ---
# Ex) dict[newKey] = newValue
print('--- add value in dict ---')
dict_a['runtime'] = 120
print(f">>> dict_a['runtime'] = 120")
print(f"dict_a['runtime']: {dict_a['runtime']}")
for key, value in dict_a.items():
    print(key, value)

# --- del key and value ---
# Ex) del dict[delKey]
print('--- del key and value ---')
del dict_a['type']
print(f">>> del dict_a['type']")
print(f'dict_a: {dict_a}')

# --- handle except with dict ---
dictionary = {}
# dictionary['key'] # KeyError: 'key'
dictionary = {
    'name': '7D 건조 망고',
    'type': '당절임',
    'ingredient': ['망고', '설탕', '메타중아황산나트륨', '치자황색소'],
    'origin': '필리핀'
}

# ==키가 존재하는지 확인하고 값에 접근하기==
print(f'dictionary.keys(): {dictionary.keys()}')
# key = input('> 접근하고자 하는 키: ')

# if key in dictionary:
#     print(f'{key}: {dictionary[key]}')
# else:
#     print('존재하지 않는 키에 접근하고 있습니다.')

# ==키가 존재하지 않을 때 None을 출력하는지 확인하기==
# key = input('> 접근하고자 하는 키: ')
# value = dictionary.get(key)
# print(f'값: {value}')

# # None 확인 방법
# if value == None:
#     print('존재하지 않는 키에 접근했습니다.')
