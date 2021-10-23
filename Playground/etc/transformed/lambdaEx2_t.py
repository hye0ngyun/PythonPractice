def power(item):
    return item * item

def under_3(item):
    return item < 3

list_input_a = [1, 2, 3, 4, 5]

print(f'list_input_a: {list_input_a}')

# map() 함수를 사용합니다.
output_a = map(power, list_input_a)
print(f'list(output_a): {output_a}')
print(f'list(output_a): {list(output_a)}')

# filter() 함수를 사용합니다.
output_b = filter(under_3, list_input_a)
print(f'list(output_b): {output_b}')
print(f'list(output_b): {list(output_b)}')end of transform