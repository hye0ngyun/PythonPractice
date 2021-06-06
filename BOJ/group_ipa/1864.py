_code = {'-': 0, '\\': 1, '(': 2, '@': 3, '?': 4, '>': 5, '&': 6, '%': 7, '/': -1}


while True:
    total = 0
    _str = input()
    if _str == '#':
        break
    for i in range(len(_str) - 1, -1, -1):
        total += _code[_str[i]] * (8 ** (len(_str) - i - 1))
    print(total)

