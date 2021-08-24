# 문자열 압축하기
def press(s):
    _c = ''
    cnt = 0
    result = ''
    for c in s:
        if c != _c:
            _c = c
            if cnt: result += str(cnt)
            result += c
            cnt = 1
        else:
            cnt += 1
    if cnt: result += str(cnt)
    return result

# aaa bb c
s = input('문자열을 입력해주세요 : ')
print(press(s))
'''
    while i < len(str):
        
        if i == 0:
            count += 1
        elif i == len(str)-1:
                print(str[i],count)
        elif str[i] == str[i-1]:
            count += 1
        else:
            print(str[i-1],count)
            count = 1
        #print(i, len(str)-1)
        i+=1'''