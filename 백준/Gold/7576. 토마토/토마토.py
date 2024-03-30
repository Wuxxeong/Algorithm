from collections import deque

answer = 0

N, M = list(map(int, input().split()))
tomato = [list(map(int, input().split())) for _ in range(M)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

queue = deque([])

for i in range(M):
    for j in range(N):
        if tomato[i][j] == 1:
            queue.append([i, j])

while queue:
    x, y = queue.popleft()
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= M or ny < 0 or ny >= N:
            continue
        if tomato[nx][ny] == 0:
            tomato[nx][ny] = tomato[x][y] + 1
            queue.append([nx, ny])

for row in tomato:
    if 0 in row:
        answer = -1
        break
    answer = max(answer, max(row))

if answer == -1:
    print(answer)
else:
    print(answer-1)