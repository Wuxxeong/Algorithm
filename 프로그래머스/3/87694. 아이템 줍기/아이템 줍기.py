from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 1000000
    arr = [[0]*102 for _ in range(102)]
    
    for x1,y1,x2,y2 in rectangle:
        x1,y1,x2,y2 = x1*2,y1*2,x2*2,y2*2
        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                arr[i][j]=1
        
        
    for x1, y1, x2, y2 in rectangle:
        x1, y1, x2, y2 = x1*2+1, y1*2+1, x2*2-1, y2*2-1
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                arr[i][j] = 0
    
    q = deque()
    cx, cy, ix, iy = characterX*2, characterY*2, itemX*2, itemY*2
    q.append((cx, cy, 0))
    v = [[0]*102 for _ in range(102)]
    v[cx][cy]=1
    
    while q:
        x,y,dist = q.popleft()
        if (x,y)==(ix,iy):
            answer = dist//2
                
        for dx,dy in ((-1,0),(1,0),(0,1),(0,-1)):
            nx,ny = x+dx,y+dy
            if 0<=nx<102 and 0<=ny<102 and arr[nx][ny]==1 and not v[nx][ny]:
                q.append((nx,ny,dist+1))
                v[nx][ny]=1
    
    return answer