import os
# os.system('shutdown -s')
while True:
    print('1. 메모장')
    print('2. 계산기')
    print('3. 그림판')
    print('4. 크롬')
    print('5. 종료')

    choice = int(input('select number >>> '))
    if choice == 1:
        os.system('notepad')
    if choice == 2:
        os.system('calc')
    if choice == 3:
        os.system('mspaint')
    if choice == 4:
        os.system('start chrome')
    if choice == 5:
        breakend of transform