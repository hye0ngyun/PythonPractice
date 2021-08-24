#6071
i = True
while(i):
    num = int(input())
    if(num == 0):
        i = False
    else:
        print(num)
#6072
num = int(input())
while(num > 0):
    print(num)
    num -= 1
#6073
num = int(input())
while(num > 0):
    num -= 1
    print(num)
#6074
a = input()
count = 0
while(count <= ord(a)-97):
    print(chr(97+count), end=' ')
    count += 1
#6075
n = int(input())
for i in range(n + 1):
    print(i)
#6076
n = int(input())
for i in range(n + 1):
    print(i)