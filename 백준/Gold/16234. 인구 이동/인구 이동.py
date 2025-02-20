from collections import deque



N,L,R = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]
day = 0

def bfs(i,j,v):
    queue = deque()
    union = []
    queue.append((i,j))
    union.append((i,j))
    while queue:
        x,y = queue.popleft()
        for dx,dy in ((-1,0),(1,0),(0,1),(0,-1)):
            nx,ny = x+dx,y+dy
            if 0<=nx<N and 0<=ny<N and v[nx][ny]==0:
                if L<=abs(A[nx][ny]-A[x][y])<=R:
                    visited[nx][ny]=1
                    queue.append((nx,ny))
                    union.append((nx,ny))

    return union

day = 0
while True:
    visited = [[0]*N for _ in range(N)]
    canMove = False
    for r in range(N):
        for c in range(N):
            if visited[r][c] == 0:
                visited[r][c] = 1
                country = bfs(r,c,visited)
                if len(country)>1:
                    canMove = True
                    people = sum(A[x][y] for x,y in country)//len(country)
                    for x,y in country:
                        A[x][y] = people
    if not canMove:
        print(day)
        break

    day += 1