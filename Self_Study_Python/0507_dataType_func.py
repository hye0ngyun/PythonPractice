# string, list, dictionary function
# 리스트에 적용할 수 있는 기본 함수: minI(), max(), sum()
# 리스트 뒤집기: reversed()
# 현재 인덱스가 몇 번쨰인지 확인하기: enumerate()
# 딕셔너리로 쉽게 반복문 작성하기: items()
# 리스트 안에 for문 사용하기: 리스트 내포

numbers = [103, 52, 273, 32, 77]
print(numbers)
print(f'min(numbers): {min(numbers)}')
print(f'max(numbers): {max(numbers)}')
print(f'sum(numbers): {sum(numbers)}')

list_a = [1, 2, 3, 4, 5]
list_reversed = reversed(list_a)

print('# reversed()함수: ', list_reversed)
print('reversed([1, 2, 3, 4, 5]): ', list(list_reversed))
print()

# 반복문 적용
print('# reversed() 함수와 반복문')
print(f'for i in reversed([1, 2, 3, 4, 5])')
for i in reversed(list_a):
    print('-', i)

# 제너레이터 특성
temp = reversed([x for x in range(1, 7)])
for i in temp:
    print(f'첫 번째 반복문: {i}')

# reversed()함수의 결과가 제너레이터이기 때문에 결과를 여러 번 활용할 수 없다.
for i in temp:
    print(f'두 번째 반복문: {i}')

numbers = [x for x in range(1, 7)]
for i in reversed(numbers):
    print(f'첫 번째 반복문: {i}')

# reversed()함수의 결과가 제너레이터이기 때문에 결과를 여러 번 활용할 수 없다.
for i in reversed(numbers):
    print(f'두 번째 반복문: {i}')

# enumerate()함수와 반복문 조합하기

# 방법 1
example_list = ['요소A', '요소B', '요소C']
i = 0
for item in example_list:
    print(f'{i}번째 요소는 {item}입니다.')
    i += 1

# 방법 2
example_list = ['요소A', '요소B', '요소C']
for i in range(len(example_list)):
    print(f'{i}번째 요소는 {example_list[i]}입니다.')

# 방법 3 enumerate() 사용
example_list = ['요소A', '요소B', '요소C']

print('# 단순 출력')
print(example_list)
print()
print('# enumerate() 함수 적용 출력')
print(enumerate(example_list))
print()

print('# list()함수로 강제 변환 출력')
print(list(enumerate(example_list)))
for i, j in enumerate(example_list):
    print(f'[{i}]: {j}')

# 딕셔너리의 items()함수와 반복문 조합하기
example_dictionary = {
    '키A': '값A',
    '키B': '값B',
    '키C': '값C'
}

print('# 딕셔너리의 items()함수')
print(f'items(): {example_dictionary.items()}')
print()

print('# 딕셔너리의 items() 함수와 반복문 조합하기')
print(example_dictionary)
for key, value in example_dictionary:
    print(f'dictionary[{key}] = {value}')
for key, value in example_dictionary.items():
    print(f'dictionary[{key}] = {value}')

# 리스트 내포
array = []

for i in  range(0, 20, 2):
    array.append(i * i)
print(array)

array = [x * x for x in range(0, 20, 2)]
print(array)

array = ['사과', '자두', '초콜릿', '바나나', '체리']
output = [fruit for fruit in array if fruit != '초콜릿']
print(output)

# number = int(input('정수 입력> '))

# if number % 2 == 0:
#     print(f'\
# 입력한 정수는 {number}입니다.\
# {number}은 짝수입니다.\
# ')

test = (
    '이렇게 입력해도 '
    '하나의 문자열로 연결되어 '
    '생성됩니다.'
)

print(f'test: {test}')
print(f'type(test): {type(test)}')

# *args, **kwargs
def blog_printer(name, *blogs, **blog_benefits):
	print(name)
	for post in blogs:
		print(post)
	for blog, benefits in blog_benefits.items():
		print(blog, '수익은 >>', benefits)

	
bloger = 'Chris'
blogs = ['first blog', 'second blog', 'third blog']
benefits = {
	'블로그 수익1': 40,
	'블로그 수익2': 20,
	'블로그 수익3': 60,
    'cccc': 50
	}
blog_printer(bloger, *blogs, **benefits)
blog_printer('shin', 'fb', 'sb', 'tb', benefit1=100, benefit2=200, benefit3=300, a = 400)

# 문자열의 join()함수
print('::'.join(['1','2','3','4','5']))
numbers = [1, 2, 3, 4, 5, 6]
r_num = reversed(numbers)

print(f'reversed_numbers: {r_num}')
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))