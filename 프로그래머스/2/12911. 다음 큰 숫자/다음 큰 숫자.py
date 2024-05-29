def solution(n):
    answer = n
    cnt = bin(n)[2:].count('1')
    print(cnt)
    nxt = -1
    while cnt != nxt:
        n += 1
        nxt = bin(n)[2:].count('1')
        answer = n
        
    return answer