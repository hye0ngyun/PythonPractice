def three():
    print('three', end=' ')
    return 3

def five():
    print('five', end=' ')
    return 5

def seven():
    print('seven', end=' ')
    return 7

three() > five() > seven() # (three() > five()) and (five() > seven())
print(3 > 5 > 7) # (3 > 5) and ( 5> 7)

####
def 서류심사(): print('1.서류심사');return True
def 인적성검사(): print('2.인적성검사');return True
def 코딩테스트(): print('3.코딩테스트');return False
def 면접1차(): print('4.면접1차');return True
def 면접2차(): print('5.면접2차');return True
def 신체검사(): print('6.신체검사');return True

if 서류심사() and 인적성검사() and 코딩테스트() and 면접1차() and 면접2차() and 신체검사():
    print('최종 합격입니다.')
else:
    print('아쉽게도 탈락입니다.')

# 서류심사()