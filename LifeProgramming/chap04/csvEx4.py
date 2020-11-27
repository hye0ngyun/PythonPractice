import re, os, usecsv
os.chdir('./LifeProgramming/chap04')

total = usecsv.open_csv('popseoul.csv')
k = []
'''
for i in total:
    for j in i:
        try:
            i[i.index(j)] = float(re.sub(',', '', j))
        except:
            pass
        '''
print(total)

def switch(listname):
    for i in listname:
        for j in i:
            try:
                i[i.index(j)] = float(re.sub(',', '', j))
            except:
                pass
switch(total)
print(total)