# 1. S1의 첫 번째 문자와 일치하는 S2의 문자위치를 찾는다. (for문 돌리면서 찾기)
# 2. S1의 첫 번쨰 문자의 다음 문자와 일치하는 S2의 문자위치를 찾는다. (찾았던 문자위치 이후부터 for문 돌리면서 찾기)
# 3. 이렇게 첫 번째 문자를 0번 인덱스부터 시작해서 마지막 인덱스까지 돌려 일치하는 길이를 모두 저장
# 4. 저장된 일치 문자열 길이 중 가장 큰 값을 출력

# S1 = input()
# S2 = input()
# LCS = ''

# for i in range(_, len(S1)):
#     for j in range(i, len(S2)):
#         if S1[i] == S2[j]:
#             LCS += S1[i]
#             break
                
        

S1 = input()
S2 = input()
LCS = {}
S2_idx = 0
# 첫 번째 문자열의 시작 인덱스
for i in range(len(S1)):
    # 첫 번째 문자열을 시작인덱스 부터 탐색
    S2_idx = 0
    LCS[i] = ''
    for j in range(i, len(S1)):
        # 두 번째 문자열을 첫 번째 문자열과 각각 검사
        
        for k in range(S2_idx, len(S2)):
            
            if S1[j] == S2[k]:
                if S1[j] not in LCS:
                    LCS[i] = ''
                LCS[i] += S1[j]
                S2_idx += k + 1
                break
            
print(LCS)