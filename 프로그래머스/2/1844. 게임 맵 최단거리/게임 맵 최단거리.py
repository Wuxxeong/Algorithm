from collections import deque

def solution(maps):
    row,col=len(maps), len(maps[0])
    mn_d=row*col
    si,sj=0,0
    ei,ej=row-1,col-1
    answer=[-1]
    q=deque()
    q.append((si,sj,1))
    visited=set()
    visited.add((si,sj))
    while q:
        ci,cj,d=q.popleft()
        if (ci,cj)==(ei,ej):
            answer.append(d)
        for di,dj in ((0,1),(1,0),(-1,0),(0,-1)):
            ni,nj=ci+di,cj+dj                
            if 0<=ni<row and 0<=nj<col and maps[ni][nj]==1 and (ni,nj) not in visited:
                q.append((ni,nj,d+1))
                visited.add((ni,nj))
    
    if len(answer)==1:
        return -1
    answer.sort()
    return answer[1]