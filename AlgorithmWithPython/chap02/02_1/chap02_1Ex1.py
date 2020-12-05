# 학생 5명의 시험 점수를 입력받아 합계와 평균을 출력하기
print('학생 그룹 점수의 합계와 평균을 구합니다.')

score1 = int(input('1번 학생의 점수를 입력하세요.: '))
score2 = int(input('2번 학생의 점수를 입력하세요.: '))
score3 = int(input('3번 학생의 점수를 입력하세요.: '))
score4 = int(input('4번 학생의 점수를 입력하세요.: '))
score5 = int(input('5번 학생의 점수를 입력하세요.: '))

total = 0
total += score1
total += score2
total += score3
total += score4
total += score5

print(f'합계는 {total}점입니다.')
print(f'평균은 {total/5}점입니다.')

'''
요구사항 1: 학생 수를 변경하는 경우
요구사항 2: 특정 학생의 점수를 확인하거나 변경하는 경우
요구사항 3: 최저점과 최고점을 구하거나 정렬이 필요한 경우
'''