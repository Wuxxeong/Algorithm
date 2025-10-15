import heapq

def solution(scoville, K):
    answer = 0
    
    heapq.heapify(scoville)
    
    while len(scoville)>1: ### -> 두번 pop하니까
        if scoville[0]>=K: # 가장 작은 원소가 K보다 큰가?
            return answer
        
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        heapq.heappush(scoville, a+2*b)
        answer += 1
        
    return answer if scoville[0]>=K else -1
