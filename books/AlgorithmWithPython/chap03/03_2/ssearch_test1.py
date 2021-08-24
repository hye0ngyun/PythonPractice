from ssearch_while import seq_search

print('실수를 검색합니다.')
print('주의: "End"를 입력하면 종료합니다.')

i = 0
Li = []

while True:
    value = input(f'x[{i}]: ')
    if value == 'End':
        break
    Li.append(float(value))
    i += 1

ky = float(input(('검색할 값을 입력하세요: ')))
idx = seq_search(Li, ky)
print(f'검색값은 x[{idx}]에 있습니다.')

"""
x[1]: 3.14
x[2]: 6.4
x[3]: 7.2
x[4]: End
검색값은 x[2]에 있습니다.
"""