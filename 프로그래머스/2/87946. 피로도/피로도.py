'''
최소 필요 피로도, 소모 피로도
''' 
from itertools import permutations
def solution(k, dungeons):
    answer = -1
    L = len(dungeons)

    for lst in list(permutations(dungeons,L)):
        t = k
        cnt = 0
        for mn,use in lst:
            if t>=mn:
                t-=use
                cnt+=1
        answer = max(answer,cnt)
        
    return answer