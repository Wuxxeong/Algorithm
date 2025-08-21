from collections import deque

def solution(n, computers):
    answer = 0
    v = []
    for i in range(n): #i와 연결되어 있는 것들
        if i in v: continue
        
        v.append(i)
        q = deque()
        q.append(i)
        while q:
            cur = q.popleft()
            computer = computers[cur]
            for idx in range(n):
                if computer[idx]==1 and idx not in v:
                    q.append(idx)
                    v.append(idx)
        answer += 1
        
    return answer