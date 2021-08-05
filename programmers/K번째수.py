def solution(array, commands):
    answer = []
    for comm in commands:
        answer.append(sorted(array[comm[0]-1:comm[1]])[comm[2]-1])
    return answer