import usecsv, os
os.chdir('./LifeProgramming/chap04')
print(usecsv.open_csv('a.csv'))
a = [['국어', '수학', '영어'],[99,88,100]]
usecsv.write_csv('b.csv', a)
print(usecsv.open_csv('b.csv'))
