from collections import defaultdict
def solution(tickets):
    answer = []
    graph = defaultdict(list)
    
    for start, end in tickets:
        graph[start].append(end)
        
    for key in graph:
        graph[key].sort(reverse=True)  # 알파벳 역순으로 정렬
    
    stack = ["ICN"]
    while stack:
        now = stack[-1]
        
        if now not in graph or not graph[now]:
            # 현재 노드가 더 이상 갈 수 있는 곳이 없으면 경로에 추가
            answer.append(stack.pop())
        else:
            # 갈 수 있는 곳이 있으면 다음 노드로 이동
            stack.append(graph[now].pop())

    # 경로가 스택에 역순으로 저장되었으므로 뒤집어서 반환
    return answer[::-1]