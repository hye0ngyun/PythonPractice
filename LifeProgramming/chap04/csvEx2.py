import csv, os
os.chdir(r'C:\Users\shg72\Documents\GitHub\PythonProject\LifeProgramming\chap04')
a = [['구',	'전체',	'내국인',	'외국인'],
['관악구',	'519864',	'502089',	'17775'],
['강남구',	'547602',	'542498',	'5104'],
['송파구',	'686181',	'679248',	'6934'],
['강동구',	'428547',	'424235',	'4312']]
f = open('abc.csv', 'w', newline='')    # newline=''을 입력하지 않으면 줄바꿈이 한번 더 일어난다.
csvobject = csv.writer(f, delimiter = ',')  # delimiter는 구분자를 의미한다.
# csv형 리스트가 저장된 객체를 파일에 쓸 때는 writerows()를 사용합니다.
# 대부분 csv파일을 만들 때는 완성된 리스트형태로 자료를 만든 후에 한번에 입력하므로 writerows()를 주로 사용합니다.
csvobject.writerows(a)
f.close()
# filename은 만들 파일 이름, the_list는 csv형 리스트를 저장한 객체
def write_csv(filename, the_list):
    # 파일을 바로 닫기 위해 with문을 사용
    with open(filename, 'w', newline='') as f:
        csvobject = csv.reader(f, delimiter=',')
        csvobject.writerows(the_list)