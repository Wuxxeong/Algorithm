from collections import deque

N, M, V = map(int, input().split())
G = [[0]*(N+1) for _ in range(N+1)]

for i in range(M):
    x, y = map(int, input().split())
    G[x][y] = 1
    G[y][x] = 1

visited1 = [False]*(N+1)
visited2 = [False]*(N+1)

def dfs(v):
    visited1[v] = True
    print(v, end=" ")
    
    for i in range(1, N+1):
        if not visited1[i] and G[v][i] == 1:
            dfs(i)
            
def bfs(v):
    q = deque([v])
    visited2[v] = True
    
    while q:
        v = q.popleft()
        print(v, end=" ")
        for i in range(1, N+1):
            if not visited2[i] and G[v][i] == 1:
                q.append(i)
                visited2[i] = True
                
dfs(V)
print()
bfs(V)