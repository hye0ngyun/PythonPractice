_code = 'CAMBRIDGE'

_str = input()
_new_str = ''
for s in _str:
    if s in _code:
        continue
    _new_str += s
print(_new_str)