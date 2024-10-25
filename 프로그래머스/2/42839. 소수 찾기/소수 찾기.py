import itertools
def check(number):
    if number<=1:
        return False
    for i in range(2,number):
        if number%i==0:
            return False
    return True

def solution(numbers):
    answer = 0
    number = [n for n in numbers]
    tmp = set()
    for i in range(1,len(numbers)+1):
        candidates = list(itertools.permutations(number,i))
        for cand in candidates:
            num = int("".join(cand))
            if check(num):
                tmp.add(num)
    
    return len(tmp)