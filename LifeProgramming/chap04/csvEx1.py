import csv, os  # csv와 os 모듈을 임포트한다.
os.chdir(r'C:\Users\shg72\Documents\GitHub\PythonProject\LifeProgramming\chap04')   # 'a.csv'파일이 있는 폴더로 이동한다.
f = open('a.csv', 'r')  # 읽기모드'r'로 'a.csv'파일을 연다.
# 만약 열리지 않는다면 f = open('a.csv', 'r', encoding = 'utf-8')로 열어야 한다.
new = csv.reader(f)
print(new)
a_list=[]
for i in new:
    print(i)
    a_list.append(i)
print(a_list)

def opencsv(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        output = []
        for i in reader:
            output.append(i)
    return output

    
print(opencsv('example2.csv'))