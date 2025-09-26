def solution(brown, yellow):
    combi = []
    total = brown+yellow
    
    # 1) 약수의 조합을 구한다. (N x M)
    for i in range(1,total//2):
        if total%i==0:
            combi.append((total//i, i))
    
    # 2) 2*N + 2*M -4 = total 만족하는지 확인한다.
    for N,M in combi:
        if 2*N + 2*M -4 == brown:
            return [N,M]
    return -1