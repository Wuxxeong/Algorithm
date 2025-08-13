'''
모든 섬이 서로 통행 가능하도록 만들 때 최소 cost
'''
def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x:x[2])
    
    sset = set()
    sset.add(costs[0][0])
    
    while len(sset)!=n:
        for i,j,c in costs:
            if i in sset and j in sset: continue
            if i in sset or j in sset:
                sset.add(i)
                sset.add(j)
                answer+=c
                break
    return answer