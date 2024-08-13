N,M = map(int, input().split())
r, c, d = map(int, input().split())
section = [list(map(int, input().split())) for _ in range(N)]
cleaned = [[0]*M for _ in range(N)]
dr, dc = [-1,0,1,0],[0,1,0,-1]

canMove = True
cnt = 0
while canMove:
    if cleaned[r][c] == 0:
        cleaned[r][c] = 1
        cnt += 1
    notCleaned = False
    for i in range(4):
        nr, nc = r+dr[i], c+dc[i]
        if section[nr][nc] == 0 and cleaned[nr][nc] == 0:
            notCleaned = True
            break

    if notCleaned:
        d = (d+3)%4 #반시계 90도 회전
        nr, nc = r+dr[d], c+dc[d]
        if section[nr][nc] == 0 and cleaned[nr][nc] == 0:
            r, c = nr, nc

    else:
        nr, nc = r+dr[(d+2)%4], c+dc[(d+2)%4]
        if 0<=nr<N and 0<=nc<M:
            if section[nr][nc]==0:
                r, c = nr, nc
            elif section[nr][nc]==1:
                canMove = False
        else:
            canMove = False


print(cnt)