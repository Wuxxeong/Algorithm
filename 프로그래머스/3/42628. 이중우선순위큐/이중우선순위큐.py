import heapq

def solution(operations):
    answer,mxheap,mnheap = [],[],[]
    
    heapq.heapify(mxheap)
    heapq.heapify(mnheap)
    
    for op in operations:
        if op=="D 1":
            if not mxheap: continue
            x = heapq.heappop(mxheap)
            mnheap.remove(-x)
        elif op=="D -1":
            if not mnheap: continue
            x = heapq.heappop(mnheap)
            mxheap.remove(-x)
        else:
            _,num = op.split()
            num = int(num)
            heapq.heappush(mxheap,-num)
            heapq.heappush(mnheap,num)
    
    if mxheap:
        answer = [-heapq.heappop(mxheap), heapq.heappop(mnheap)]
    else:
        answer = [0,0]
    return answer