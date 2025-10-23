'''
관점을 바꾸어서, 각 심사대가 어떤 시간(mid)동안 총 몇명의 인원을 심사할 수 있는지?
'''

def solution(n, times):
    answer = 0
    left = 1
    right = max(times)*n
    
    while left<=right:
        mid = (left+right)//2
        people = 0 #심사할 수 있는 인원 수
        
        for time in times:
            people += mid//time
            if people>=n:
                break
        if people>=n:
            right = mid-1
        else:
            left = mid+1
    answer = left
    return answer