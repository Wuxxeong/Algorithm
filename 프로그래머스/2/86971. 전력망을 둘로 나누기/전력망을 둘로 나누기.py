from collections import deque
def bfs(g,k,wires):
    tmp = [g[0]]
    
    q = deque()
    q.append(g[0])
    v = set()
    
    while q:
        cur = q.popleft()
        for i in range(len(wires)):
            if i==k: continue
            if cur in wires[i] and i not in v:
                q.append(wires[i][0])
                q.append(wires[i][1])
                v.add(i)
                tmp.append(wires[i][0])
                tmp.append(wires[i][1])
    return len(set(tmp))

def solution(n, wires):
    answer = n
    
    for k in range(n-1): #k번째 송전망을 끊을 때.
        G1 = [wires[k][0]]
        G2 = [wires[k][1]]
        
        l1 = bfs(G1,k,wires)
        l2 = n-l1
        answer = min(abs(l1-l2),answer)
        
    return answer