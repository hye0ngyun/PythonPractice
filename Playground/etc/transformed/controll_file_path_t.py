import os
import glob
from os import listdir
from os.path import isfile, join

# os.getcwd(): 현재 작업 경로를 반환하는 함수
print(os.getcwd())
# os.chdir("경로"): 작업 경로를 입력한 경로로 변경하는 함수
print(os.chdir("./PythonPractice/Playground/etc"))
print(os.getcwd())

# os.listdir("경로"): 경로 미입력 시 현재 경로, 경로의 모든 파일과 폴더를 리스트로 반환한다.
filenames = os.listdir()
# join("경로명", "파일명"):
print("join(): " + os.path.join("/A/B/C", "file.py")) # join(): /A/B/C/file.py

onlyfiles = [f for f in listdir() if isfile(join(f))]

print(onlyfiles)
print(filenames)

if not os.path.isdir('transformed'):
  os.mkdir('transformed')
for file in filenames:
  with open(file, 'r', encoding="utf-8") as f1:
    with open(rf'.\transformed\{file[:file.find(".")]}_t.{file[file.find(".")+1:]}', 'w', encoding="utf-8") as f2:
      for line in f1.readlines():
        f2.write(line)
      f2.write('end of transform')
      
# with open('ex1.py', 'r', encoding="utf-8") as f:
#   print(f.readlines())
end of transform