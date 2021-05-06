# try except
# try:
#     print('나누기 전용 계산기입니다.')
#     nums = []
#     nums.append(int(input('첫 번째 숫자를 입력하세요: ')))
#     nums.append(int(input('두 번째 숫자를 입력하세요: ')))
#     # nums.append(nums[0] / nums[1])
#     print(f'{nums[0]} / {nums[1]} = {nums[2]}')
# except ValueError:
#     print('에러! 잘못된 값을 입력하였습니다.')
# except ZeroDivisionError as err:
#     print('err')
# except Exception as err:
#     print('알 수 없는 에러가 발생하였습니다.')
#     print(err)

# raise
# try:
#     print('한 자리 숫자 나누기 전용 계산기입니다.')
#     nums = []
#     nums.append(int(input('첫 번째 숫자를 입력하세요: ')))
#     nums.append(int(input('두 번째 숫자를 입력하세요: ')))
#     if nums[0] >= 10 or nums[1] >= 10:
#         raise ValueError
#     nums.append(nums[0] / nums[1])
#     print(f'{nums[0]} / {nums[1]} = {nums[2]}')
# except ValueError:
#     print('잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.')

# 사용자 정의 에러
# class BigNumberError(Exception):
#     def __init__(self, msg):
#         self.msg = msg
#     def __str__(self):
#         return self.msg

# try:
#     print('한 자리 숫자 나누기 전용 계산기입니다.')
#     nums = []
#     nums.append(int(input('첫 번째 숫자를 입력하세요: ')))
#     nums.append(int(input('두 번째 숫자를 입력하세요: ')))
#     if nums[0] >= 10 or nums[1] >= 10:
#         raise BigNumberError(f'입력값: {nums[0]}, {nums[1]}')
#     nums.append(nums[0] / nums[1])
#     print(f'{nums[0]} / {nums[1]} = {nums[2]}')
# except ValueError:
#     print('잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.')
# except BigNumberError as err:
#     print('에러가 발생하였습니다. 한 자리 숫자만 입력하세요.')
#     print(err)

# finally
class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return self.msg

try:
    print('한 자리 숫자 나누기 전용 계산기입니다.')
    nums = []
    nums.append(int(input('첫 번째 숫자를 입력하세요: ')))
    nums.append(int(input('두 번째 숫자를 입력하세요: ')))
    if nums[0] >= 10 or nums[1] >= 10:
        raise BigNumberError(f'입력값: {nums[0]}, {nums[1]}')
    nums.append(nums[0] / nums[1])
    print(f'{nums[0]} / {nums[1]} = {nums[2]}')
except ValueError:
    print('잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.')
except BigNumberError as err:
    print('에러가 발생하였습니다. 한 자리 숫자만 입력하세요.')
    print(err)
finally:
    print('계산기를 이용해 주셔서 감사합니다.')