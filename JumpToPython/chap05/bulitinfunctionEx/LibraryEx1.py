# 명령 행에서 인수 전달하기 #argv_test.py
import sys
print(sys.argv)
# 도스창에서 argv_test.py you need python
# 결과 : ['argv_test.py', 'you', 'need', 'python']
# 강제로 스크립트 종료하기 sys.exit == ctrl + z, ctrl + d
sys.exit()
# 자신이 만든 모듈 불러와 사용하기 sys.path
sys.path
sys.path.append("") # 이 디렉토리에 있는 파이썬 모듈을 사용할 수 있게 경로명 추가

# pickle은 객체의 형태를 그대로 유지하면서 파일을 저장하고 불러올 수 있게하는 모듈이다.
import pickle
f = open('test.txt', 'wb')
data = {1: 'python', 2: 'you need'}
pickle.dump(data, f)
f.close()
f = open('test.txt', 'rb')
data = pickle.load(f)
print(data)
