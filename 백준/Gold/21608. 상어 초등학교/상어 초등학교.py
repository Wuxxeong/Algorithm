N = int(input())
best_friends = [list(map(int, input().split())) for _ in range(N*N)]
classes = [[0]*(N+1) for i in range(N+1)]

dr, dc = [1,0,-1,0], [0,1,0,-1]
#학생 배치
for best_friend in best_friends:
    student, friends = best_friend[0], best_friend[1:]
    tmp = []
    for i in range(1, N+1):
        for j in range(1, N+1):
            if classes[i][j] == 0: #비어있는 칸
                like, blank = 0, 0
                for k in range(4):
                    r, c = dr[k]+i, dc[k]+j
                    if 1<=r<=N and 1<=c<=N:
                        if classes[r][c] in friends:
                            like += 1
                        if classes[r][c] == 0:
                            blank += 1
                tmp.append([like, blank, i, j])
    
    tmp.sort(key=lambda x:(-x[0],-x[1],x[2],x[3])) ##1,2,3 조건을 모두 만족시킬 수 있음
    classes[tmp[0][2]][tmp[0][3]] = student

best_friends.sort()
result = 0
#만족도 조사 인접한 모든칸 탐색 필요
for i in range(1, N+1):
    for j in range(1, N+1):
        ans = 0
        friends = best_friends[classes[i][j]-1][1:]
        for k in range(4):
            r, c = dr[k]+i, dc[k]+j
            if 1<=r<=N and 1<=c<=N:
                if classes[r][c] in friends:
                    ans += 1
        if ans != 0:
            result += 10 ** (ans - 1)
print(result)