import heapq

def solution(n, works):
    answer = 0
    
    heap = []
    for work in works:
        heapq.heappush(heap, -work)
    
    while n:
        m = -heapq.heappop(heap)
        if m == 0: break
        heapq.heappush(heap, -(m-1))
        n-=1
    
    for h in heap:
        answer += h**2
    return answer