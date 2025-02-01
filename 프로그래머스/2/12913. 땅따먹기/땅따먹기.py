def solution(land):
    row = len(land)
    dp = [[0]*4 for _ in range(row+1)]
    
    for i in range(1,row+1):
        for j in range(4):
            dp[i][j] = land[i-1][j] + max(dp[i-1][(j+1)%4], dp[i-1][(j+2)%4], dp[i-1][(j+3)%4])
    
    return max(dp[row])