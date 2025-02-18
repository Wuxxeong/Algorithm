'''
status = 0 -> 청소되지 않은 빈 칸
         1 -> 벽

로봇 청소기가 있는 칸 == 빈 칸

청소하는 영역의 개수
'''

N,M = map(int,input().split())
r,c,d = map(int,input().split()) #초기 (r,c) 방향 d 방향
status = [list(map(int,input().split())) for _ in range(N)]

dr,dc = [-1,0,1,0],[0,1,0,-1] #북동남서

cnt = 0

visited = set()
def isCleaned(r, c):
    for i in range(4):
        nr,nc = r+dr[i],c+dc[i]
        if 0<=nr<N and 0<=nc<M and (nr,nc) not in visited and status[nr][nc] == 0: #청소되지 않은 빈칸
            return True
    return False

canMove = True
while canMove:
    # [1] 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
    if (r,c) not in visited and status[r][c] == 0:
        # status[r][c] = 1
        visited.add((r,c))
        cnt += 1
    # [2] 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸(0) 확인
    if not isCleaned(r,c):
        nr,nc = r-dr[d],c-dc[d]
        if 0<=nr<N and 0<=nc<M and status[nr][nc] != 1:
            r,c = nr,nc
        else:
            canMove = False
    else: #[3]
        d = (d-1)%4
        nr,nc = r+dr[d], c+dc[d]
        if 0<=nr<N and 0<=nc<M and (nr,nc) not in visited and status[nr][nc] == 0:
            r,c = nr,nc


print(cnt)