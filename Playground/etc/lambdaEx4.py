list_input_a = [1,2,3,4,5]

print('# map()함수 실행 결과')
output_a = map(lambda x: x * x, list_input_a)
print(f'map(power, list_input_a): {output_a}')
print(f'list(map(power, list_input_a)): {list(output_a)}')

print('# filter()함수 실행 결과')
output_b = filter(lambda x: x < 3, list_input_a)
print(f'filter(under_3, list_input_a): {output_b}')
print(f'list(filter(under_3, list_input_a)): {list(output_b)}')
