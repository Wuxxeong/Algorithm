import math

#전파가 전달이 안되는 구간의 개수들을 저장 -> 해당 구간/구간크기 의 ceiling이 정답
def solution(n, stations, w):
    answer = 0
    dist = []
    for i in range(1, len(stations)):
        dist.append((stations[i]-w-1) - (stations[i-1]+w))
    
    dist.append(stations[0]-w-1)   #앞 구간
    dist.append(n-(stations[-1]+w))  #뒷 구간
    
    for d in dist:
        if d<0:
            continue
        answer += math.ceil(d/(w*2+1))
    return answer