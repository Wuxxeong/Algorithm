from collections import deque

def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    sum_q1 = sum(q1)
    sum_q2 = sum(q2)
    
    total_sum = sum_q1 + sum_q2
    
    if total_sum % 2 != 0:
        return -1
    
    target_sum = total_sum // 2
    
    # 투 포인터 방식으로, p1은 q1의 요소를 이동하는 포인터
    max_len = len(q1) + len(q2)
    
    count = 0
    
    while sum_q1 != target_sum:
        # 연산 횟수가 큐 길이의 두 배 이상이면 불가능한 경우로 판단
        if count >= max_len * 2:
            return -1
        
        if sum_q1 > target_sum:
            val = q1.popleft()
            sum_q1 -= val
            q2.append(val)
        else:
            val = q2.popleft()
            sum_q1 += val
            q1.append(val)
        
        count += 1
    
    return count
