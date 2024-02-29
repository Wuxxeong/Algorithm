from collections import deque
def solution(n, computers):
    graph = 0
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
                    queue.append(col)
                    visited[col] = True
    return graph

