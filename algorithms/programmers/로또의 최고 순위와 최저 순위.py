# 77484 - 

def solution(lottos, win_nums):
    answer = []
    rank = [6,5,4,3,2]
    counts = len([l for l in lottos if win_nums.count(l) != 0])
    z_counts = lottos.count(0)
    b_rank = rank.index(counts+z_counts) + 1 if rank.count(counts+z_counts) != 0 else 6
    w_rank = rank.index(counts) + 1 if rank.count(counts) != 0 else 6
    answer = [b_rank, w_rank]
    return answer

# 77484 - 22.04.20 13:00 ~ 13:24 (24m)
def solution(lottos, win_nums):
    answer = []
    lottos_rank = [6, 5, 4, 3, 2, 1, 6] # 일치하는 숫자의 개수에 따라 순위를 결정할 리스트
    best_cnt = 0 # 최고의 경우에 일치하는 숫자의 개수
    worst_cnt = 0 # 최저의 경우에 일치하는 숫자의 개수
    
    # 0인 개수 파악
    zero_cnt = lottos.count(0)
    for lotto in lottos:
        if lotto in win_nums: # 존재한다면 True 존재하지 않는다면 False이므로
            worst_cnt += 1
            
    best_cnt = worst_cnt + zero_cnt

    answer = [lottos_rank[best_cnt - 1], lottos_rank[worst_cnt - 1]]
    return answer