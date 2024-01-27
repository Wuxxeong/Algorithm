from collections import deque
def solution(n, computers):
    graph = 0
    parent = [-1 for _ in range(n)]
    visited = [False for _ in range(n)]
    queue = deque()
    
    for start_node in range(n):
        if visited[start_node] == False:
            queue.append(start_node)
            visited[start_node] = True
            graph += 1
        while queue:
            row = queue.popleft()
            for col in range(0, n):
                if computers[row][col] == 1  and not visited[col]:
                    parent[col] = row
                    queue.append(col)
                    visited[col] = True
    
    return graph

