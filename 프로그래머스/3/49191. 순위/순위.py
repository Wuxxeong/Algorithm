from collections import deque

def solution(n, results):
    answer = 0
    win = [[] for _ in range(n+1)]
    lose = [[] for _ in range(n+1)]
    k = []
    for result in results:
        a, b = result
        win[a].append(b)
        lose[b].append(a)
        
        
    def bfs(i, graph):
        visited = set()
        queue = deque()
        queue.append(i)
        while queue:
            current = queue.popleft()
            for player in graph[current]:
                if player not in visited:
                    visited.add(player)
                    queue.append(player)
        return visited
        
    for i in range(1, n+1):
        wins = bfs(i, win)
        loses = bfs(i, lose)
                    
        if len(wins)+len(loses)+1 == n: 
            answer+=1
    
    return answer