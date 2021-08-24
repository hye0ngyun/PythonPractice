T = int(input())
_list = []
for i in range(T):
    a, b = map(int, input().split())
    _list.append(a + b)
for i in _list:
    print(i)