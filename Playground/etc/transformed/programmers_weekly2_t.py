def solution(scores):
    students_dict = {}
    answer = ''
    # 1. scores.length가 아닌 len(scores) 자바스크립트와 동시에 공부하다보니 헷갈림
    for i in range(len(scores)):
        students_dict[i] = []

    for students in scores:
        for score_idx, score in enumerate(students):
            students_dict[score_idx].append(score)
    
    for key, value in students_dict.items():
      # 2. 동일한 점수인 경우도 빼버리는 문제
      # 3. (or) 괄호 문제
        if (min(value) == value[key] or max(value) == value[key]) and value.count(value[key]) == 1:
            temp = students_dict[key].pop(key)
    
    for _, score in students_dict.items():
        mean_score = sum(score) / len(score)
        if 90 <= mean_score:
            answer += 'A'
        elif 80 <= mean_score:
            answer += 'B'
        elif 70 <= mean_score:
            answer += 'C'
        elif 50 <= mean_score:
            answer += 'D'
        else:
            answer += 'F'
    
    return answerend of transform