def solution(n):
    ans = 0
    
    while n>0:
        if n%2 !=0:
            n -= 1
            ans += 1
        elif n&(n-1) == 0:
            ans += 1
            break
        elif n%2 == 0:
            n = n//2

    return ans