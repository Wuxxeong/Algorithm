import math

def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def changeK(n, k):
    q = n
    k_number = ''
    
    while q != 0:
        k_number = str((q%k))+ k_number
        q = q//k
        
    return k_number

def findP(nk):
    p_list = []
    l = list(filter(lambda x:nk[x] == '0', range(len(nk))))
    p = ''
    for i in range(len(nk)):
        if i in l:
            if p!='':
                p_list.append(int(p))
                p = ''
                continue
            continue
        
        p += nk[i]
    
    if p != '':
        p_list.append(int(p))
    
    return p_list

def solution(n, k):
    answer = 0
    # 1. k 진수로 변환 (string으로 반환)
    nk = changeK(n, k)
    # 2. 조건을 만족하는 P의 집합 구하기
    P = findP(nk)
    # 3. P 집합 중 (k진법 && 10진법) 소수의 개수
    for p in P:
        if isPrime(p):
            answer += 1
    return answer