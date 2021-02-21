a = input()


for i in range(len(a)):
    temp = (list(a[i].zfill(len(a)-i)))
    temp.reverse()
    temp = ''.join(temp)
    print('[' + temp + ']')



# for i in range(len(a)):
#     temp = list(a[i].zfill(len(a)-i))
#     temp = temp.reverse()
#     print(temp)
#     temp = ''.join(temp)
#     print(temp)
#     # print(temp)


# for i in range(len(a)):
# 	temp = []
#     temp.append(list(a[i].zfill(len(a)-i)))
#     temp.reverse()
#     print(temp)