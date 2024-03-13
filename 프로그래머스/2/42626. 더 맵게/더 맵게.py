import heapq
def solution(scoville, K):
    answer = 0
    mixed = 0
    
    heapq.heapify(scoville)
    while len(scoville) > 0: 
        if scoville[0] >= K: break
        
        if len(scoville) >= 2:
            a = heapq.heappop(scoville)
            b = heapq.heappop(scoville)
            mixed = a + b*2
            answer += 1
            heapq.heappush(scoville, mixed)
        elif len(scoville) == 1:
            heapq.heappop(scoville)
            answer = -1
    return answer