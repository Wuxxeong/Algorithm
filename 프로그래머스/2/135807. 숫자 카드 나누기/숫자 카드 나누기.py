import math
from functools import reduce

# Helper 함수: 리스트의 최대공약수 구하기
def gcd_of_list(nums):
    return reduce(math.gcd, nums)

# Helper 함수: 특정 숫자를 모든 값으로 나눌 수 없는지 확인
def can_divide_none(nums, a):
    for num in nums:
        if num % a == 0:
            return False
    return True

def solution(arrayA, arrayB):
    # 1. 각 배열의 최대공약수 계산
    gcdA = gcd_of_list(arrayA)
    gcdB = gcd_of_list(arrayB)
    
    # 2. 조건 확인
    resultA = gcdA if can_divide_none(arrayB, gcdA) else 0
    resultB = gcdB if can_divide_none(arrayA, gcdB) else 0
    
    # 3. 결과 반환: 가장 큰 값
    return max(resultA, resultB)
