import re
_code = input()
_str = input()
_new_code = re.findall('\D', _code)
_new_code = ''.join(_new_code)

if _str in _new_code:
    print(1)
else:
    print(0)
