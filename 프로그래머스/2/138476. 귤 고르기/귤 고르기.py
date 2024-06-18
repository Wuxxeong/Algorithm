from collections import defaultdict
from itertools import combinations

def solution(k, tangerine):
    answer = 0
    dict = defaultdict(int)
    
    for tan in tangerine:
        dict[tan] += 1
    
    values = list(dict.values())
    values.sort(reverse=True)
    
    for value in values:
        if value > k:
            k = 0
            answer += 1
            break
        else:
            k -= value
            answer += 1
        
        if k == 0:
            break
    
    return answer