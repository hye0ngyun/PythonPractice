# https://www.daniweb.com/programming/software-development/threads/468450/nameerror-name-tk-is-not-defined
# 파일명을 tkinter.py로 한 경우 
# from tkinter import *
# root = Tk() # 이부분에서 NameError: name 'Tk' is not defined 라는 에러가 발생한다.
# 해결 방안으로 파일명을 tkinterEx1.py와 같이 tkinter.py와 다른 이름으로 만들어주면 해결된다.
from tkinter import *
root = Tk()

lbl = Label(root, text="라벨1") # 라벨 위젯 만들기
lbl.pack() # 라벨 위젯 적재하기

input = Entry(root)
input.pack()

btn = Button(root, text="입력")
btn.pack()
def func1():
  print(1)
btn.bind(func1)

root.mainloop() # 이벤트 메시지 루프로서 키보드가 나무스 혹은 화면 Redraw와 같은 다양한 이벤트로부터 오는 메시지를 받고 전달하는 역할을 한다.
