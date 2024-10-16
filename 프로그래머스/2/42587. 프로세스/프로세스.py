from collections import deque
def solution(priorities, location):
    result = [] #result[location]에 있는 수 -> priorities에서 index+1
    pq = deque()
    for idx,priority in enumerate(priorities):
        pq.append((idx,priority))
    
    priorities.sort(reverse=True)
    mx_i=0
    while pq:
        #find max index
        ci,cp=pq.popleft()
        if cp==priorities[mx_i]:
            result.append(ci)
            mx_i+=1
        else:
            pq.append((ci,cp))
        if mx_i==len(priorities):break
    #priorities[location]이 몇번째로 실행되는지
    return result.index(location)+1