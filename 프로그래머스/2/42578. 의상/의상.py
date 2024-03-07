from collections import defaultdict

def solution(clothes):
    answer = 1
    wear = defaultdict(int)
    
    for c in clothes:
        wear[c[1]] += 1
    
    wearNum = list(wear.values())
    
    for num in wearNum:
        answer *= (num+1)
    answer -= 1
    return answer