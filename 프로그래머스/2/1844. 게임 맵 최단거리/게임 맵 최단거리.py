from collections import deque

def solution(maps):
    n,m = len(maps),len(maps[0])
    v = [[0]*m for _ in range(n)]
    v[0][0] = 1
    q = deque()
    q.append([0,0])    
    while q:
        ci,cj = q.popleft()
        if (ci,cj)==(n-1,m-1):
            return v[n-1][m-1]
        for di,dj in ((0,1),(0,-1),(1,0),(-1,0)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<n and 0<=nj<m and maps[ni][nj]==1 and v[ni][nj]==0:
                v[ni][nj] = v[ci][cj]+1
                q.append([ni,nj])
    
    return -1