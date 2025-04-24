from collections import deque

def solution(maps):
    answer = 0
    n,m = len(maps),len(maps[0])
    si,sj,ei,ej = 0,0,n-1,m-1
    
    q = deque()
    v = [[0]*m for _ in range(n)]
    
    q.append((si,sj,1))
    v[si][sj]=1
    
    while q:
        ci,cj,dist = q.popleft()
        if (ci,cj)==(ei,ej):
            return dist
        for di,dj in ((0,1),(0,-1),(1,0),(-1,0)):
            ni,nj = ci+di,cj+dj
            if 0<=ni<n and 0<=nj<m and not v[ni][nj] and maps[ni][nj]==1:
                q.append((ni,nj,dist+1))
                v[ni][nj] = 1
    
    return -1