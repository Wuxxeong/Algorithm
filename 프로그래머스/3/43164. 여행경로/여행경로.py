from collections import deque

def solution(tickets):
    tickets.sort()  # 사전순 우선
    n = len(tickets)
    answer = []

    # 큐에는 (현재 공항, 사용된 티켓 집합, 경로) 저장
    q = deque()
    q.append(("ICN", [False]*n, ["ICN"]))

    while q:
        cur, used, path = q.popleft()

        # 모든 티켓 사용 완료
        if len(path) == n + 1:
            return path  # 사전순 정렬 때문에 첫 번째 완성 경로가 정답

        for i, (src, dst) in enumerate(tickets):
            if not used[i] and src == cur:
                new_used = used[:]     # 상태 복사
                new_used[i] = True
                q.append((dst, new_used, path + [dst]))

    return answer
