def solution(dirs):
    x,y = 0,0
    d = {"L":[-1,0], "R":[1,0], "U":[0,1], "D":[0,-1]}
    visited = set()
    for dir in dirs:
        dx, dy = d[dir]
        nx, ny = x+dx, y+dy
        if nx>5 or nx<-5 or ny>5 or ny<-5:
            continue
        visited.add(((x,y),(nx,ny)))
        visited.add(((nx,ny),(x,y)))
        x ,y = nx, ny
        
    return len(visited)//2