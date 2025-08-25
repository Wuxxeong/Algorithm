def solution(arrows):
    answer = 0
    
    dx = [0,1,1,1,0,-1,-1,-1]
    dy = [1,1,0,-1,-1,-1,0,1]
    
    cur = (0,0)
    v = set()
    v.add(cur)
    route = set()
    for idx in arrows:
        for _ in range(2):
            ni,nj = cur
            ci,cj = ni+dx[idx], nj+dy[idx]
            if (ci,cj) in v and (ni,nj,ci,cj) not in route: #왔던 경로가 아니면서 특정 점으로 돌아왔을 때
                answer+=1
            v.add(cur)
            route.add((ni,nj,ci,cj))
            route.add((ci,cj,ni,nj))
            cur = (ci,cj)
    return answer