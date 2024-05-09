from collections import deque

N = int(input())
K = int(input())

board = [[0]*(N+1) for _ in range(N+1)]
apples = []
for _ in range(K):
    i, j = list(map(int, input().split()))
    board[i][j] = 1
    apples.append([i,j])

L = int(input())
move = []
for _ in range(L):
    t, w = input().split()
    move.append([int(t), w])

snake = deque()
snake.append([1,1])

T = 0
dx, dy = [0,1,0,-1], [1,0,-1,0] #오른쪽 90은 index+1 왼쪽 90은 index-1
i = 0
while snake:
    nxt_head = [snake[-1][0]+dx[i], snake[-1][1]+dy[i]]
    if nxt_head[0]<1 or nxt_head[0]>N or nxt_head[1]<1 or nxt_head[1]>N or nxt_head in snake: #벽 or 자신
        T += 1
        break

    snake.append(nxt_head)
    
    if board[nxt_head[0]][nxt_head[1]] == 1:
        board[nxt_head[0]][nxt_head[1]] = 0
    else:
        snake.popleft()
    
    T += 1
    
    for d in move:
        if T == d[0] and 'D' == d[1]:
            i = (i+1)%4
        elif T == d[0] and 'L' == d[1]:
            i = (i-1)%4
            
print(T)