def solution(triangle):
    answer = 0
    S = [[0 for _ in range(len(triangle))] for _ in range(len(triangle))]
    S[0][0] = triangle[0][0]

    for i in range(1,len(triangle)):
        for j in range(i+1):
            if j==0: 
                S[i][j] = S[i-1][j] + triangle[i][j]
            else:
                S[i][j] = max(S[i-1][j] + triangle[i][j], S[i-1][j-1] + triangle[i][j])
    
    answer = max(S[len(triangle)-1])
    
    return answer