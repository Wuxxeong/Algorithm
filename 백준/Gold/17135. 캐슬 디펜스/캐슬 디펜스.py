from itertools import combinations
from collections import deque

N,M,D = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]


def kill(attacker):
    narr = [x[:] for x in arr]
    killed = [[0]*M for _ in range(N)]
    result = 0

    for i in range(N-1,-1,-1):
        this_turn = []
        for ay in attacker:
            dq = deque([(i,ay,1)]) #맨처음은 바로 위에 있는 것부터
            while dq:
                x,y,d = dq.popleft()
                if d>D:
                    break
                if narr[x][y]==1:
                    this_turn.append((x,y))
                    if killed[x][y]==0:
                        killed[x][y]=1
                        result+=1
                    break
                for dx,dy in ((0,-1),(-1,0),(0,1)):#좌상우 순으로
                    nx = x+dx
                    ny = y+dy
                    if 0<=nx<N and 0<=ny<M:
                        dq.append((nx,ny,d+1))

        for x,y in this_turn:
            narr[x][y] = 0

    return result

answer = 0
for attacker in list(combinations(range(M),3)):
    answer = max(answer, kill(attacker))

print(answer)