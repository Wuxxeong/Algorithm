def solution(brown, yellow):
    answer = []
    area = brown+yellow
    
    subs = []
    for k in range(1, round(area**0.5)+1):
        if area%k == 0:
            subs.append([area//k, k])
            
    for sub in subs:
        if (sub[0]+sub[1])*2 - 4 == brown:
            answer = sub
            break
    return answer