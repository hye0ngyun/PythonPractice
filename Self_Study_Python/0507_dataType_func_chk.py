# check
# 2진수
print(f'{10:06b}')
print(int('1010', 2))

# 8진수
print(f'{12:06o}')
print(int('12', 8))

# 16진수
print(f'{10:06x}')
print(int('10', 16))

output = [x for x in range(1, 100) if str(bin(x))[2:].count('0') == 1]
for i in output:
    print(f'{i} : {i:b}')
print(f'합계: {sum(output)}')