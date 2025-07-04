def solution(m, n, puddles):
    answer = 0
    dp = [[0]*(n+1) for _ in range(m+1)]
    dp[1][1]=1
    for i in range(1,m+1):
        for j in range(1,n+1):
            if [i,j]==[1,1]: continue
            if [i,j] in puddles: continue
            dp[i][j] = dp[i-1][j]+dp[i][j-1]
    return dp[-1][-1]%1000000007