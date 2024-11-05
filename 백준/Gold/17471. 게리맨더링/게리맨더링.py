from itertools import combinations
from collections import deque
#[3] bfs에서 return 값 = 인구수 차이 (나눌수 없다면 -1)
def bfs(lst,nums,G): #s1구역, s2구역, 인구수
    answer = -1
    isConnected = [0, 0]
    people = [0, 0]
    for i in range(len(lst)):
        t = lst[i]
        cur = t[0]
        q = deque()
        q.append(cur)
        v = set()
        v.add(cur)

        while q:
            r = q.popleft()
            for c in t:
                if G[r][c]==1 and c in t and c not in v:
                    q.append(c)
                    v.add(c)

            if len(v)==len(t):
                isConnected[i] = 1
                people[i] = sum([nums[k] for k in t])

    if sum(isConnected)==2:
        answer = abs(people[0]-people[1])

    return answer

N = int(input())
nums = [0]+list(map(int, input().split())) #인구수
G = [[0]*(N+1) for _ in range(N+1)]
for i in range(1,N+1):
    lst = list(map(int, input().split()))
    n, connect = lst[0], lst[1:]
    for j in range(n):
        G[i][connect[j]] = 1
        G[connect[j]][i] = 1

diff = float('inf')
all = list(range(1, N+1))
#[1] n/2개에 대해 combination 뽑기
for i in range(1,N//2+1):
    s1_lst = list(combinations(range(1, N + 1), i))
    for s1 in s1_lst:
        remain = tuple([num for num in all if num not in s1])
        cnt = bfs([s1,remain],nums,G)
        if cnt==-1: continue
        diff = min(diff, cnt)

if diff==float('inf'):
    diff = -1

print(diff)