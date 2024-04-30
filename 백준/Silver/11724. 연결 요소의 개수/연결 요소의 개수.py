from collections import deque
import sys

input = sys.stdin.readline

N, M = list(map(int, input().split()))
vertex = [list(map(int, input().split())) for _ in range(M)]

graph = [[] for _ in range(N+1)]
visited = [0]*(N+1)

for vt in vertex:
    u, v = vt
    graph[u].append(v)
    graph[v].append(u)
    

component = 0

for i in range(1, N+1):
    queue = deque()
    if not visited[i]:
        queue.append(i)
        visited[i] = 1
        component+=1

    while queue:
        node = queue.popleft()
        for n in graph[node]:
            if not visited[n]:
                visited[n] = 1
                queue.append(n)

print(component)