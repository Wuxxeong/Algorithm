from collections import deque

def solution(numbers, target):
    answer = 0
    q = deque()
    q.append((0,-1))
    
    while q:
        cur,i = q.popleft()
        if i==len(numbers)-1:
            if cur==target:
                answer+=1
        else:
            q.append((cur+numbers[i+1],i+1))
            q.append((cur-numbers[i+1],i+1))
        
    return answer