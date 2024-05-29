def solution(n):
    answer = 0
    A = [1,2]
    for i in range(2, n):
        A.append(A[i-1] + A[i-2]) 
    return A[n-1]%1234567