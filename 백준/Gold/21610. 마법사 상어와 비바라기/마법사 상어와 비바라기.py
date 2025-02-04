'''
1. 비바라기 시전
2. 비구름 생성
3. 구름 M번 이동
    비구름 생성
    1) di 방향으로 si 만큼 이동
    2) 구름이 있는 칸 물 += 1
    3) 구름 두 사라짐
    4) 물이 증가한 칸에 물복사버그 마법
    == 대각성 방향으로 거리가 1인 칸에 있는 바구니의 수만큼 물 양 증가

'''

N,M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

di = [9,0,-1,-1,-1,0,1,1,1]
dj = [9,-1,-1,0,1,1,1,0,-1]

cross = [[-1,1],[1,1],[1,-1],[-1,-1]] #물복사 버그 마법 시 체크
cloud = [[N-1,0],[N-2,0],[N-1,1],[N-2,1]] #(N,1) (N,2) (N-1, 1) (N-1 2)에 비구름 생성

for _ in range(M):
    d,s = map(int, input().split())
    visited = [[0]*N for _ in range(N)] #각 turn 마다 변경 됨
    clouds = []

    while cloud:
        i,j = cloud.pop()
        ni,nj = (i+di[d]*s) % N, (j+dj[d]*s) % N
        arr[ni][nj] += 1 #이동한 구름의 칸 물 추가
        visited[ni][nj] = 1
        clouds.append([ni,nj])

    for ni,nj in clouds:
        for ci,cj in cross:
            mi,mj = ni+ci, nj+cj
            if 0<=mi<N and 0<=mj<N and arr[mi][mj]: #각 대각선마다 물이 있는지 체크 후 물복사
                arr[ni][nj] += 1

    for i in range(N):
        for j in range(N):
            if arr[i][j] >= 2 and not visited[i][j]:
                arr[i][j] -= 2
                cloud.append([i,j])

print(sum(map(sum,arr)))