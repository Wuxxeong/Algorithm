import math
from collections import defaultdict

def solution(str1, str2):
    answer = 0
    s1 = defaultdict(int)
    s2 = defaultdict(int)
    for i in range(len(str1)-1):
        if str1[i:i+2].isalpha():
            s1[str1[i:i+2].lower()] += 1
    for i in range(len(str2)-1):
        if str2[i:i+2].isalpha():
            s2[str2[i:i+2].lower()] += 1
    

    interserction = list(set(s1.keys()) & set(s2.keys()))
    union = list(set(s1.keys()) | set(s2.keys()))
    
    A, B = 0, 0
    for k in interserction:
        A += min(s1[k], s2[k])
        
    for k in union:
        if k in s1.keys() and k in s2.keys():
            B += max(s1[k], s2[k])
        elif k in s1.keys():
            B += s1[k]
        elif k in s2.keys():
            B += s2[k]

    if A == 0 and B == 0:
        return 1*65536
    
    J = A/B
    answer = math.trunc(J*65536)
    
    return answer