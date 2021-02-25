num1, num2 = map(int, input("Enter two numbers through space").split())
choice = 1
print(choice)
while(choice != 0):
    print('1. sum\n2. sub\n3. mul\n4. div\n5. mod\n0. exit')
    choice = int(input('choice your instruction: '))
    if(choice == 1):
        print(num1 + num2)
    elif(choice == 2):
        print(num1 - num2)
    elif(choice == 3):
        print(num1 * num2)
    elif(choice == 4):
        print(num1 // num2)
    elif(choice == 1):
        print(num1 % num2)
    elif(choice == 0):
        print('exit program')