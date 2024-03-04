from itertools import permutations

def solution(k, dungeons):    
    pers = list(permutations(dungeons, len(dungeons)))
    count = []
    for per in pers:
        tmp = k
        c = 0
        for p in per:
            if p[0] <= tmp:
                tmp -= p[1]
                c += 1
        count.append(c)
    
    return max(count)