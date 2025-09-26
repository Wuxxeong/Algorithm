from collections import deque

def solution(maps):
    answer = 1
    N,M = len(maps),len(maps[0])
    si,sj,ei,ej = 0,0,N-1,M-1
    
    vset = set()
    vset.add((si,sj))

    q = deque()
    q.append((si,sj,answer))
    
    while q:
        ci,cj,dist = q.popleft()
        if (ci,cj)==(ei,ej):
            return dist
        for di,dj in ((0,1),(0,-1),(1,0),(-1,0)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<M and maps[ni][nj]==1 and (ni,nj) not in vset:
                vset.add((ni,nj))
                q.append((ni,nj,dist+1))
                
    return -1