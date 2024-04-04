from collections import deque
import copy

def bfs():
    tmp_lab = copy.deepcopy(lab)
    queue = deque([])
    
    for i in range(N):
            for j in range(M):
                if tmp_lab[i][j] == 2:
                    queue.append([i,j])
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
                    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < M and tmp_lab[nx][ny] == 0:
                tmp_lab[nx][ny] = 2
                queue.append([nx, ny])

    global answer  
    cnt = 0     
    
    for row in tmp_lab:
        cnt += row.count(0)
    
    answer = max(answer, cnt)


def makewall(cnt):
    if cnt == 3:
        bfs()
        return
    
    for i in range(N):
        for j in range(M):
            if lab[i][j] == 0:
                lab[i][j] = 1
                makewall(cnt+1)
                lab[i][j] = 0


N, M = list(map(int, input().split()))
lab = [list(map(int, input().split())) for _ in range(N)]              
answer = 0
makewall(0)
print(answer)