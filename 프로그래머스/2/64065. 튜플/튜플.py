import re

def solution(s):
    answer = []
    
    l = re.split(r'[{}]', s)
    l.sort(key=lambda x:len(x))
    
    for nums in l:
        if nums=='' or nums==',': continue
        tmp = nums.split(',')
        for k in tmp:
            if int(k) not in answer:
                answer.append(int(k))
    
    return answer