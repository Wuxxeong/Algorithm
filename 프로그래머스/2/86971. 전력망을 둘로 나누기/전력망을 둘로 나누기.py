from collections import deque
def solution(n, wires):
    answer = n
    G = [[0]*n for _ in range(n)]
    for a,b in wires:
        G[a-1][b-1] = 1
        G[b-1][a-1] = 1
    
    for ra,rb in wires:
        #rb를 기준으로 탐색
        q = deque()
        visited = [0]*n
        
        q.append(rb)
        visited[rb-1]=1
        cnt = 1
        while q:
            cur = q.popleft()
            for k in range(n):
                if k==ra: continue
                if (G[cur-1][k-1]) and not visited[k-1]:
                    q.append(k)
                    visited[k-1]=1
                    cnt+=1
        
        if abs(n-cnt-cnt)<answer:
            answer = abs(n-cnt-cnt)
    return answer