# 모스 부호 해독
morsedic = {'.-':'A', '-...':'B', '-.-.':'C', '-..':'D', '.':'E', '..-.':'F', '--.':'G', '....':'H', '..':'I', '.---':'J', '-.-':'K', '.-..':'L', '--':'M', '-.':'N', '---':'O', '.--.':'P', '--.-':'Q', '.-.':'R', '...':'S', '-':'T', '..-':'U', '...-':'V', '.--':'W', '-..-':'X', '-.--':'Y', '--..':'Z'}
'''
def ms(m):
    temp = []
    result = ''
    dtemp = ''
    for i in range(len(m)):
        if m[i] == '  ':
            temp.append(' ')
        elif m[i] == ' ':
            temp.append(m[:i])
    print(temp)
    for i in temp:
        if i == ' ':
            result += ' '
        dtemp = i   
        result += moss[dtemp]
    return result
'''
def morse(src):
    result = []
    for word in src.split('  '):
        for char in word.split(' '):
            result.append(morsedic[char])
        result.append(' ')
    return ''.join(result)
print(morse('.... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--'))
