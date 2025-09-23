from collections import deque
def solution(n, computers):
    answer = 0
    vset = set()
    for i in range(len(computers)): #i번째 컴퓨터를 기준으로
        if i in vset: continue
        q = deque()
        q.append(i)
        while q:
            target = q.popleft()
            for j in range(i+1,len(computers)): #j 행에서 target이랑 연결된 것 찾기
                if computers[j][target]==1 and j not in vset:
                    q.append(j)
                    vset.add(j)
        answer+=1
                
    return answer