from collections import deque
from collections import defaultdict

def solution(priorities, location):
    answer = 1
    result = []
    d = defaultdict(int)
    
    for idx,p in enumerate(priorities):
        d[idx] = p
        
    
    q = deque(range(len(priorities)))
    while q:
        cur = q.popleft()
        isAny = False
        for sub in list(q):
            if d[sub] > d[cur]:
                q.append(cur)
                isAny = True
                break
        if not isAny:
            result.append(cur)
            if cur == location:
                return answer
            answer+=1
            
    return answer