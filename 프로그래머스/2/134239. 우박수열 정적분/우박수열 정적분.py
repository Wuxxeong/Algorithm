def solution(k, ranges):
    answer = []
    a = [k]
    
    while a[-1] != 1:
        if a[-1]%2 == 0:
            a.append(a[-1]//2)
        else:
            a.append(a[-1]*3+1)
    #[5,16,8,4,2,1]
    
    for r in ranges:
        start, end = r[0], len(a)-1+r[1]
        area = 0
        if start>end:
            answer.append(-1)
            continue
        for i in range(start, end):
            area += (a[i] + a[i+1])/2
        answer.append(area)
    return answer