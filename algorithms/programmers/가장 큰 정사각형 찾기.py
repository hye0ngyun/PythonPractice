# 22.04.23 22:00 ~ 22:30
'''
채점 결과
정확성: 47.1
효율성: 40.4
합계: 87.4 / 100.0
'''
def solution(board):
    answer = 0

    for i in range(len(board)): # 행 순회
        for j in range(len(board[0])): # 열 순회
            if board[i][j] == 1:
                board[i][j] = 1 + min(board[i-1][j], board[i][j-1], board[i-1][j-1])
    max_line = 0
    for line in board:
        max_line = max(max_line, max(line))
    answer = max_line ** 2
    
    return answer