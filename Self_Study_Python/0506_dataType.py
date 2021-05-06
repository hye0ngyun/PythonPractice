# list
# 2
numbers = [263, 103, 5, 32, 65, 9, 72, 800, 99]
for number in numbers:
    if number >= 100:
        print('- 100 이상의 수:', number)

# 3
numbers = [263, 103, 5, 32, 65, 9, 72, 800, 99]
for number in numbers:
    if number % 2 == 0:
        print(f'{number} 는 짝수입니다.')
    else:
        print(f'{number} 는 홀수입니다.')
count = 1
for number in numbers:
    count = 1
    if number // 100 > 0:
        count = 3
    elif number // 10 > 0:
        count = 2
    print(f'{number} 는 {count} 자릿수입니다.')

# 4
list_of_list = [
    [1, 2, 3],
    [4, 5, 6, 7],
    [8, 9]
]
for i in list_of_list:
    for j in i:
        print(j)

# 5
numbers = [1,2,3,4,5,6,7,8,9]
output = [[], [], []]

for number in numbers:
    output[number % 3 - 1].append(number)
print(output)