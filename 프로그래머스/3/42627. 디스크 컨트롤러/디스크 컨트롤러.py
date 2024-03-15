import heapq

def solution(jobs):
    answer = 0
    now = 0 #현재시간
    i = 0   #처리개수
    start = -1 #마지막 완료시간
    heap = []
    
    while i < len(jobs):
        for job in jobs:
            if start < job[0] <= now:
                heapq.heappush(heap,[job[1],job[0]])
        
        if heap:
            current = heapq.heappop(heap)
            start = now
            now += current[0]
            answer += now - current[1] 
            i += 1
        else:
            now += 1
            
    return answer // len(jobs)

# def solution(jobs):
#     answer = 0
#     total = 0
#     finish = 0
    
#     jobs.sort(key = lambda x:x[1]-x[0])
    
#     for job in jobs:
#         waiting = finish-job[0]
#         if waiting > 0:
#             total = total+waiting+job[1]
#             finish += job[1]
#         else:
#             total += job[1]
#             finish += job[1]
    
#     answer = total//len(jobs)
#     return answer