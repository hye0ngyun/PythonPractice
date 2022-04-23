# 신고 결과 받기 - 22.04.19 14:00 ~ 14:30 (30m)
def solution(id_list, report, k):
    answer = []
    reporter_list = []
    reported_list = []
    for idx, val in enumerate(set(report)): # 동일 아이디 중복 신고 삭제
        val = val.split()
        reporter_list.append(val[0]) # reporter
        reported_list.append(val[1]) # reported
    reported_idx_list = []
    for idx, val in enumerate(reported_list):
        count = reported_list.count(val)
        if count >= k:
            reported_idx_list.append(idx)
    for _id in id_list:
        count = 0
        for idx in reported_idx_list:
            if _id == reporter_list[idx]:
                count += 1
        answer.append(count)
    
    return answer

'''
채점 결과
정확성: 66.7
합계: 66.7 / 100.0

시간 초과가 되기 때문에 코드 수정 필요
22.04.19
'''