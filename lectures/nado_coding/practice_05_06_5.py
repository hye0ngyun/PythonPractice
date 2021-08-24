# try except 퀴즈
chicken = 10
waiting = 1 # 홀 안에는 현재 만석, 대기번호 1부터 시작
class SoldOutError(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return self.msg
while(True):
    try:
        print(f'남은 치킨: {chicken}')
        order = int(input('치킨 몇 마리 주문하시겠습니까?'))
        if not isinstance(order, int) or order < 1:
            raise ValueError()
        if order > chicken or order > 10: # 남은 치킨보다 주문량이 많을 때
            print('재료가 부족합니다.')
            raise SoldOutError('재고가 소진되어 더 이상 주문을 받지 않습니다.')
        else:
            print(f'[대기번호 {waiting}] {order}마리 주문이 완료됐습니다.')
            waiting += 1
            chicken -= order
    except ValueError as err:
        print('잘못된 값을 입력하였습니다.')
        print(err)
        # break
    except SoldOutError as err:
        print(err)
        break