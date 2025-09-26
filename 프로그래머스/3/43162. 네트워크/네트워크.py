from collections import deque
def solution(n, computers):
    answer = 0
    
    vset = set()
    
    for i in range(n):
        if i not in vset: #i vset에 없는 경우, 새로운 graph 탄생
            answer += 1
            vset.add(i)
            q = deque()
            q.append(i)
            while q:
                cur = q.popleft()
                lst = computers[cur]
                for j in range(i+1,n):
                    if j not in vset and lst[j]==1:
                        q.append(j)
                        vset.add(j)
    return answer