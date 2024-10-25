import math
def solution(brown, yellow):
    answer = []
    n = brown+yellow
    
    candidate = []
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            candidate.append([n//i,i])
    
    for row,col in candidate:
        new_brown = (row+col)*2-4
        if brown==new_brown:
            answer=[row,col]
            break
    return answer