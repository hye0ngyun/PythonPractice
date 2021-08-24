N = int(input())
string = input().split()
first = True
result = 1
for s in string:
    if s[::] == s[::-1]:
        if first:
            first = False
        elif pres[-1] == s[0]:
            pass
        else:
            result = 0
        pres = s
print(result)