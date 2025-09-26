from itertools import permutations
def check(number):
    if number<2:
        return False
    for i in range(2,number):
        if number%i==0:
            return False
    return True

def solution(numbers):
    answer = 0
    
    nums = [num for num in numbers]
    all_numbers = set()
    for i in range(1,len(nums)+1):
        for tpl in permutations(nums,i):
            new_number = ''
            for num in tpl:
                new_number += num
            all_numbers.add(int(new_number))
    
    for number in all_numbers:
        if check(number):
            answer+=1
    return answer