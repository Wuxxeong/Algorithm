import heapq

def solution(operations):
    answer = []
    heap = []
    heapq.heapify(heap)

    for operation in operations:
        op, num = operation.split()
        if op == 'I':
            heapq.heappush(heap, int(num))
        elif op == 'D' and num == '1': #최댓값 삭제
            if len(heap) != 0:
                m = max(heap)
                heap.remove(m)
        elif op == 'D' and num == '-1': #최솟값 삭제
            if len(heap) != 0:
                heapq.heappop(heap)
    
    if len(heap) == 0:
        answer = [0, 0]
        return answer
    answer = [max(heap), heapq.heappop(heap)]
    return answer