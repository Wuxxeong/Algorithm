def solution(n, lost, reserve):
    answer = n
    lost_but_reserve = set(lost)&set(reserve)
    
    # for k in lost_but_reserve:
    #     lost.remove(k)
    #     reserve.remove(k)
    lost = sorted(list(filter(lambda x : x not in lost_but_reserve, lost)))
    reserve = sorted(list(filter(lambda x : x not in lost_but_reserve, reserve)))
    
    for l in lost:
        if l-1 in reserve:
            reserve.remove(l-1)
        elif l+1 in reserve:
            reserve.remove(l+1)
        else:
            answer -= 1
    return answer