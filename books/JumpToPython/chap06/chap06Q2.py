# Duplicate Numbers
def dupCheck(*args):
    for arg in args:
        #print(arg)
        print(len(set(arg)) == len(arg), end = ' ')
#print(len(set('123114526')) == len('123114526'))
#print(len(set('123452')) == len('123452'))
#print(dupCheck('1235', '1234562'))
nlist = input('입력 : ').split()
print('출력 : ', end = '')
for i in nlist:
    dupCheck(i)