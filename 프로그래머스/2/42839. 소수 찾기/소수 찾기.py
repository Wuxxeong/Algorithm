from itertools import permutations

def solution(numbers):
    answer = 0
    n = [number for number in numbers]
    per = []
    for i in range(1, len(numbers)+1):
        per += list(permutations(n, i))
    new_nums = list(set([int(("").join(p)) for p in per]))
    
    def isPrime(k):
        if k == 0 or k == 1: return 0
        for i in range(2, k):
            if k%i == 0:
                return 0
        return 1
    
    for k in new_nums:
        answer += isPrime(k)
    return answer