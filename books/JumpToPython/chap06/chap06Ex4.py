# 간단한 메모장 만들기
import sys
option = sys.argv[1]    # sys.argv[0]은 chap06Ex4.py이다

if option == '-a':
    memo = sys.argv[2]
    f = open('memo.txt', 'a')
    f.write(memo)
    f.write('\n')
    f.close()
elif option == '-v':
    f = open('memo.txt')
    memo = f.read()
    f.close()
    print(memo)
    