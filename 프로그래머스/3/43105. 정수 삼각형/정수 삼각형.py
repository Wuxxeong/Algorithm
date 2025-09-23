def solution(triangle):
    dp = [[0]*(i+1) for i in range(len(triangle))]
    dp[0][0] = triangle[0][0]
    for i in range(1,len(triangle)):
        dp[i][0] = dp[i-1][0]+triangle[i][0]

    #해당 칸은 max(왼쪽 위, 바로 위)
    for i in range(1, len(triangle)):
        for j in range(1, i):
            dp[i][j] = max(dp[i-1][j-1],dp[i-1][j])+triangle[i][j]
        dp[i][-1] = dp[i-1][-1]+triangle[i][-1]
    
    
    return max(dp[-1])