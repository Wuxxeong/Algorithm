'''
세로 N 가로 M
목표 : 빨간 구슬을 구멍을 통해 빼기 + 파란 구슬이 들어가면 안됨
동작 : 상하좌우 기울이기
성공 : 빨간 구슬만 빠지기
실패 : 파란 구슬 or 빨+파
- 빨,파는 동시에 같은 칸 불가능

몇 번 만에 빨간 구슬을 빼낼 수 있을지? 10번 이하로 안되면 -1 출력
'''
from collections import deque
N,M = map(int,input().split())
arr = [list(input().strip()) for _ in range(N)]
visited = []

def getPos():
    rx,ry,bx,by = 0,0,0,0
    for x in range(N):
        for y in range(M):
            if arr[x][y]=="R":
                rx,ry = x,y
            if arr[x][y]=="B":
                bx,by = x,y
    return rx,ry,bx,by


'''
빨,파가 겹치는 경우에 대비하기 위해 cnt를 둔다.
겹쳤을 때, cnt로 더 많은 양을 이동한 녀석을 찾아내서 왔던 반대 방향으로 1만큼 이동 시켜준다.
'''
def move(x, y, dx, dy):
    cnt = 0
    while arr[x+dx][y+dy]!="#" and arr[x][y]!="O":
        x+=dx
        y+=dy
        cnt+=1
    return x,y,cnt


def bfs():
    rx,ry,bx,by = getPos()
    q = deque()
    q.append((rx,ry,bx,by,1))
    visited.append((rx,ry,bx,by))

    while q:
        rx,ry,bx,by,result = q.popleft()
        if result > 10:
            break

        for dx,dy in ((-1,0),(0,1),(1,0),(0,-1)):
            nrx,nry,rcnt = move(rx,ry,dx,dy)
            nbx,nby,bcnt = move(bx,by,dx,dy)

            #파란 구슬이 구멍에 들어갈 경우
            if arr[nbx][nby] == "O":
                continue

            #빨간 구슬이 들어갈 경우
            if arr[nrx][nry] == "O":
                print(result)
                return

            #둘이 겹친 경우 많이 이동한 놈을 1칸 뒤로 보냄
            if nrx == nbx and nry == nby:
                if rcnt > bcnt:
                    nrx-=dx
                    nry-=dy
                else:
                    nbx-=dx
                    nby-=dy

            if (nrx,nry,nbx,nby) not in visited:
                visited.append((nrx,nry,nbx,nby))
                q.append((nrx,nry,nbx,nby,result+1))
    print(-1)

bfs()