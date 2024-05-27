def solution(n, s):
    #자연수 n개의 합이 s인 집합들 중 곱이 최대
    answer = []
    if n>s : 
        return [-1]
    q = s//n
    r = s%n
    for _ in range(n):
        answer.append(q)
        
    i = 0
    while r:
        answer[i] += 1
        r -= 1
        i += 1
        
    answer.sort()
    return answer