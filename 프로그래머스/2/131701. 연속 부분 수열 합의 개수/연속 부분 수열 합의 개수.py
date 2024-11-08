def solution(elements):
    answer = 0
    L = len(elements)
    
    s = set()
    s.add(sum(elements))
    
    for i in range(1,L): #길이가 i인 연속 부분 수열
        for si in range(L):
            s.add(sum(elements[si:si+i]))
        elements.append(elements[i-1])
        # print(s)
    
    return len(s)