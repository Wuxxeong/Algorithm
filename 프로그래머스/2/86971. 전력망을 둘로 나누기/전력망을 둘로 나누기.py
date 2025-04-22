from collections import deque

def bfs(idx,wires):
    v1,v2 = wires[idx]
    
    q = deque()
    visited = [0]*len(wires)
    
    q.append(v1)
    visited[idx] = 1
    
    while q:
        parent = q.popleft()
        for i in range(len(wires)):
            if parent in wires[i] and not visited[i]:
                q.append(wires[i][0])
                q.append(wires[i][1])
                visited[i]=1
    
    return sum(visited)

def solution(n, wires):
    answer = n
    
    for idx in range(n-1):
        g1_cnt = bfs(idx,wires)
        g2_cnt = n-g1_cnt
        tmp = abs(g1_cnt-g2_cnt)
        if tmp<answer:
            answer = tmp
    return answer