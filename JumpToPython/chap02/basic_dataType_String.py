""" 문자열 자료형 """
print('-'*15+' 문자열 자료형 '+'-'*15)
# 문자열 만드는 방법
print('-'*15+' 문자열 만드는 방법 '+'-'*15)
s = "Life is too short, You need Python"
print(s)
s = 'Life is too short, You need Python'
print(s)
s = """Life is too short, You need Python"""
print(s)
s = '''Life is too short, You need Python'''
print(s)

# 문자열 속에 ', " 포함시키는 방법
print('-'*15+' 문자열 속에 \', \" 포함시키는 방법 '+'-'*15)
s = "Python's favorite food is perl"
print(s)
s = "\"Python is very easy.\" he says."
print(s)
s = '"Python is very easy." he says.'
print(s)
s = 'Python\'s favorite food is perl'
print(s)
s = """Python's favorite food is perl"""
print(s)
s = '''"Python is very easy." he says.'''
print(s)
multiline ="""
    This is string   a
        multiline string
        """
print(multiline)

# 문자열 연산하기
print('-'*15+' 문자열 연산하기 '+'-'*15)
head = 'Python'
tail = ' is fun!'
print(head + tail)
s = 'python'
print(s * 2)

# 문자열 인덱싱과 슬라이싱
print('-'*15+' 문자열 인덱싱과 슬라이싱 '+'-'*15)
s = "Life is too short, You need Python"
print(f's[2]: {s[2]}')
print(f's[-2]: {s[-2]}')
for i in range(len(s), 0, -1):
    print(f's[{i-1:02d}]: {s[i-1]}, s[{-i:03d}]: {s[-i]}')
print(f's[12:20]: {s[12:17]}')
print(f's[19:]: {s[19:]}')
print(f's[:17]: {s[:17]}')
print(f's[19:-8]: {s[19:-7]}')
print(f's[:]: {s[:]}')

date = '20210502Sunday'
year = date[:4]
month = date[4:6]
day = date[6:8]
dayOfWeek = date[8:]
print(f'year: {year}, month: {month}, day: {day}, dayOfWeek: {dayOfWeek}')