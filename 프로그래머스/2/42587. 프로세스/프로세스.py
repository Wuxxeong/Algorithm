from collections import deque
def solution(priorities, location):
    queue = deque([(i, p) for i, p in enumerate(priorities)])
    result = []
    
    while queue:
        current = queue.popleft()
        if any(current[1] < q[1] for q in queue):
            queue.append(current)
        else:
            result.append(current[0])
    
    return result.index(location) + 1

