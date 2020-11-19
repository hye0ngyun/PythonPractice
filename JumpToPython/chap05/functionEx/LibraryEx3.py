# random
import random
# random.random()은 0.0과 1.0사이의 실수 중에서 난수를 리턴한다.
print(random.random())
# random.randit(시작값, 끝값)은 시작값과 끝값 사이의 정수 중에 난수값을 리턴한다.
print(random.randint(1, 10))
print('-'*20)
# random 모듈을 사용한 함수
def random_pop(data):
    number = random.randint(0, len(data)-1)
    return data.pop(number)
if __name__ == "__main__":
    data = [1,3,5,6,2]
    while data:
        print(random_pop(data))
# random.choice()함수를 사용하면 보다 간편하게 리스트에서 값을 가져올 수 있다.
def random_pop2(data):
    number = random.choice(data)
    data.remove(number)
    return number
data = [10,20,30,40,50]
while data:
    print(random_pop2(data))
# random.shuffle함수는 리스트의 항목을 무작위로 섞는다.
data = [1,2,3,4,5]
random.shuffle(data)
print(data)
# webbrowser
import webbrowser
# webbrowser.open('url')함수는 웹브라우저를 열고 입력된 url로 이동한다. 
webbrowser.open('http://google.com')    # 기본으로 설정된 웹브라우저를 실행시키고 해당 주소로 이동한다.