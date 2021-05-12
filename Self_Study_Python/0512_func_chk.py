# 1
# _list = []
# def flatten(data):
#     global _list
#     print(f'data: {data}, len: {len(data)}')
#     for i in range(len(data)):
#         if isinstance(data[i], list):
#             return flatten(data[i])
#         else:
#             _list.append(data[i])
#             print(_list)
#     return _list

def flatten(data):
    output = []
    for i in data:
        if type(i) == list:
            output += flatten(i)
        else:
            output.append(i)
    return output
example = [[1,2,3], [4,[5,6], 7, [8,9]]]
print(f'before: {example}')
print(f'after: {flatten(example)}')

# 2
min_sit = 2
max_sit = 10
total = 100
memo = {}

