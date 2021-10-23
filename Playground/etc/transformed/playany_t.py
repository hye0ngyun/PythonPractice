# <<<<<<< HEAD
### 성적 처리
st = []
with open('c:\\dd\\ss.txt', 'r', encoding='utf8') as f:
    for i in range(10):
        st.append(f.readline().split()) ## 라인단위로 읽어드림 
        st[i][1] = int(st[i][1])  ## str ==> int형으로 변환 
        st[i][2] = int(st[i][2])
        st[i][3] = int(st[i][3])
        
        ## 총점, 평균
        total = st[i][1] +  st[i][2] +  st[i][3] 
        avg = total / 3
        st[i].append(total)
        st[i].append(avg)

## 과목별 평균, 반전체 평균
total_kor = total_eng = total_mat = 0

for i in range(10):
    total_kor = total_kor + st[i][1]
    total_eng = total_eng + st[i][2]
    total_mat = total_mat + st[i][3]

avg_kor = total_kor / len(st)
avg_eng = total_eng / len(st)
avg_mat = total_mat / len(st)


for i in range(10):
    print(st[i])


print(' 국어 평균 : {} 영어 평균 : {} 수학 평균 : {}, 반 평균 : {}'\
    .format(avg_kor, avg_eng, avg_mat, (avg_kor + avg_eng + avg_mat) / 3))

# T초
T = int(input())
# A: 5분, B: 1분, C: 10초
A = 300
B = 60
C = 10
cnt = [0, 0, 0]

if T % C == 0:
    if T >= A:
        cnt[0] = T // A
        T = T % A
    if T >= B:
        cnt[1] = T // B
        T = T % B
    if T >= C:
        cnt[2] = T // C
        T = T % C        
    for i in cnt:
        print(i, end=' ')
else:
    print(-1)
    

# >>>>>>> 0d43b06b108a911d5982ee7c01231272da7708a6
end of transform