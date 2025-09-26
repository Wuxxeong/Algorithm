from collections import deque

def solution(k, dungeons):
    answer = -1
    n = len(dungeons)
    
    q = deque()
    q.append((k, [False]*n, []))
    
    while q:
        ck, used, path = q.popleft()
        isChange = False
        for i in range(n):
            if used[i]==False and ck>=dungeons[i][0]:
                new_used = used[:]
                new_used[i]=True
                q.append((ck-dungeons[i][1], new_used, path+[i]))
                isChange = True
        if not isChange:
            answer = max(answer,sum(used))
        
    return answer