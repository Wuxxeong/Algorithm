from collections import deque

def solution(n, wires):
    answer = 101
    G = [[0]*(n+1) for _ in range(n+1)]
    for wire in wires:
        w1,w2 = wire
        G[w1][w2]=1
        G[w2][w1]=1
    
    for i in range(len(wires)): #i번째 전력망을 끊기
        r1,r2 = wires[i]
        G[r1][r2]=0
        G[r2][r1]=0
        
        sub_G = deque()
        sub_G.append(r1) #r1을 root로 하는 그래프의 개수
        visited = set()
        visited.add(r1)
        while sub_G:
            cur = sub_G.popleft()
            for j in range(1,n+1):
                if G[cur][j]==1 and j not in visited:
                    sub_G.append(j)
                    visited.add(j)
        
        G[r1][r2]=1
        G[r2][r1]=1
        l1 = len(visited)
        l2 = n-l1
        cnt = abs(l1-l2)
        
        answer = min(answer,cnt)
    return answer