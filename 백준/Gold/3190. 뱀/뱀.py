from collections import deque

N = int(input()) #보드의 크기
board = [[-1]*(N+2)]+[[-1]+[0]*N+[-1]for _ in range(N)]+[[-1]*(N+2)]
K = int(input()) #사과의 수
apples = [list(map(int, input().split())) for _ in range(K)]
for apple in apples:
    row,col = apple
    board[row][col]=100
L = int(input())
d = [input().split() for _ in range(L)]


di,dj=[0,1,0,-1],[1,0,-1,0]

moved = deque()
moved.append((1,1))
i = 0
ei,ej=moved[0]
board[ei][ej]=1

time=1
while True:
    ni,nj = moved[-1][0]+di[i],moved[-1][1]+dj[i]
    # 1.머리를 다음 칸으로
    moved.append((ni,nj))
    # 2.벽이거나 자기사신과 부딪히면 종료
    if board[ni][nj]==-1 or board[ni][nj]==1:
        break
    # 3-1.사과가 존재하지 않으면 꼬리 비움
    if board[ni][nj]==0:
        ei,ej=moved.popleft()
        board[ni][nj]=1
        board[ei][ej]=0
    # 3-2.사과가 존재하면 꼬리움직이지 않음
    elif board[ni][nj]==100:
        board[ni][nj]=1
        
    #방향전환
    if d!=[]:
        time_change,direction = d[0]
        time_change=int(time_change)
        if time==time_change:
            if direction=='L':
                i = (i-1)%4
            elif direction=='D':
                i = (i+1)%4
            d.pop(0)
    
    time+=1

print(time)