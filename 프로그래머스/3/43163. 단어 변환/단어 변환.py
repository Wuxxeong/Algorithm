from collections import deque

def solution(begin, target, words):
    q = deque()
    q.append((begin, 0))
    visited = set()
    visited.add(begin)
    
    while q:
        cur, answer = q.popleft()
        if cur == target:
            return answer
        
        for word in words:
            if word not in visited:
                cnt = 0
                for i in range(len(word)):
                    if word[i] != cur[i]:
                        cnt += 1
                if cnt == 1:
                    visited.add(word)
                    q.append((word, answer + 1))
    return 0
