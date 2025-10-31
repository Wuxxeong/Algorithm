def solution(n, times):
    answer = 0
    k = max(times)*n
    
    left,right = 0,k
    
    while left<=right:
        mid = (left+right)//2
        done = 0
        for time in times:
            done += mid//time
        if done<n:
            left = mid+1
        elif done>=n:
            right = mid-1
    answer = left
    return answer