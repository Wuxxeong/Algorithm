from collections import deque

def solution(numbers, target):
    answer = 0
    
    q = deque()
    q.append((0,0))
    
    while q:
        v,i = q.popleft()
        if i==len(numbers):
            if v == target:
                answer+=1
        else:
            q.append((v+numbers[i],i+1))
            q.append((v-numbers[i],i+1))
        
    return answer