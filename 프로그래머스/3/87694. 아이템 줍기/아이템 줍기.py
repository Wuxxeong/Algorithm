from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    # 움직일 수 있는 칸을 1로 미리 만들어 둔다.
    arr = [[0]*102 for _ in range(102)]
    
    #[1] 사각형 1로 채우기
    for x1,y1,x2,y2 in rectangle:
        x1,y1,x2,y2 = x1*2,y1*2,x2*2,y2*2
        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                arr[i][j]=1
    
    #[2] 사각형 내부 0으로 비우기
    for x1,y1,x2,y2 in rectangle:
        x1,y1,x2,y2 = x1*2+1,y1*2+1,x2*2-1,y2*2-1
        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                arr[i][j] = 0
    #[3] characterX,characterY -> itemX,itemY 까지 이동
    cx,cy,ix,iy = characterX*2,characterY*2,itemX*2,itemY*2
    q = deque()
    q.append((cx,cy,0))
    v = [[0]*102 for _ in range(102)]
    v[cx][cy]=1
    
    while q:
        ci,cj,dist = q.popleft()
        if (ci,cj)==(ix,iy):
            return dist//2
        for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
            ni,nj = ci+di,cj+dj
            if 0<=ni<102 and 0<=nj<102 and arr[ni][nj]==1 and not v[ni][nj]:
                q.append((ni,nj,dist+1))
                v[ni][nj]=1
    
    return -1