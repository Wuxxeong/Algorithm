import sys
from collections import deque

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]


def bfs(x, y, size, status):
    N = len(status)
    dist = [[-1] * N for _ in range(N)]
    dist[x][y] = 0
    q = deque([(x, y)])
    candidates = []

    while q:
        x, y = q.popleft()  # 큐에서 현재 위치를 꺼냄

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and dist[nx][ny] == -1:
                if status[nx][ny] <= size:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
                    if 0 < status[nx][ny] < size:
                        candidates.append((dist[nx][ny], nx, ny))

    if not candidates:
        return None

    candidates.sort()
    return candidates[0]


input = sys.stdin.readline
N = int(input())
status = [list(map(int, input().split())) for _ in range(N)]

eat, time, size = 0, 0, 2
shark = [[i, j] for i in range(N) for j in range(N) if status[i][j] == 9][0]
x, y = shark[0], shark[1]
status[x][y] = 0  # 상어 위치 초기화

while True:
    result = bfs(x, y, size, status)
    if result is None:
        break

    dist, nx, ny = result
    time += dist
    x, y = nx, ny
    status[nx][ny] = 0
    eat += 1

    if eat == size:
        size += 1
        eat = 0  # 수정된 변수 이름

print(time)
