from collections import deque

def solution(numbers, target):
    answer = 0 
    q = deque()
    q.append([numbers[0], 0])
    q.append([-numbers[0],0])
    n=len(numbers)
    while q:
        num,idx = q.popleft()
        idx+=1
        if idx<n:
            q.append([num+numbers[idx],idx])
            q.append([num-numbers[idx],idx])
        else:
            if num==target:
                answer+=1
    return answer