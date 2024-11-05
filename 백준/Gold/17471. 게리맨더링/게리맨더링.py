from itertools import combinations
from collections import deque

# bfs 함수에서 두 구역이 연결되어 있는지 확인하고, 인구 차이를 반환합니다.
def bfs(lst, nums, G):
    isConnected = [False, False]  # 각 구역이 연결되어 있는지 확인
    people = [0, 0]               # 각 구역의 인구수를 저장

    for i in range(len(lst)):
        t = lst[i]
        cur = t[0]
        q = deque([cur])
        v = set([cur])

        while q:
            r = q.popleft()
            for c in t:
                if c not in v and G[r][c] == 1 and c in t:
                    q.append(c)
                    v.add(c)

        if len(v) == len(t):  # 모든 노드가 연결되어 있으면
            isConnected[i] = True
            people[i] = sum(nums[k] for k in t)  # 인구수를 합산

    # 두 구역이 모두 연결된 경우 인구 차이를 반환하고, 아니면 -1 반환
    return abs(people[0] - people[1]) if all(isConnected) else -1

# 입력을 받아 초기화
N = int(input())
nums = [0] + list(map(int, input().split()))  # 인구수
G = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    lst = list(map(int, input().split()))
    n, connect = lst[0], lst[1:]
    for j in connect:
        G[i][j] = G[j][i] = 1  # 무방향 그래프

diff = float('inf')
all_districts = list(range(1, N + 1))

# 가능한 모든 조합을 통해 구역을 나누어 최소 인구수 차이를 계산
for i in range(1, N // 2 + 1):
    for s1 in combinations(all_districts, i):
        s2 = tuple(set(all_districts) - set(s1))
        result = bfs([s1, s2], nums, G)
        if result != -1:
            diff = min(diff, result)

# 결과 출력
print(diff if diff != float('inf') else -1)
