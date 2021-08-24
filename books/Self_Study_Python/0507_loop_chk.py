# check
# 2
key_list = ['name', 'hp', 'mp', 'level']
value_list = ['기사', 200, 30, 5]
character = {}
i = 0
for key in key_list:
    character[key] = value_list[i]
    i += 1
print(character)

# 3
limits = 10000
i = 1
sum_value = 0
while limits > sum_value:
    sum_value += i
    i += 1
print(f'{i-1}을 더할 때 {limits}를 넘으며 그때의 값은 {sum_value}입니다.')

# 4
max_value = 0
a = 0
b = 0

for i in range(1, 100):
    j = 100 - i
    temp = i * j
    if max_value < temp:
        max_value = temp
        a = i
        b = j

print(f'최대가 되는 경우: {a} * {b} = {max_value}')