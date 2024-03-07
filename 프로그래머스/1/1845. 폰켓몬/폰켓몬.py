def solution(nums):
    choose = len(nums)/2
    types = len(set(nums))
    
    if choose > types : return types
    return choose