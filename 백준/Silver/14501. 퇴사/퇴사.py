N = int(input())
TP = [list(map(int, input().split())) for _ in range(N)]
dp = [0] * (N+1)

#Top-down approach
for i in range(N-1, -1, -1):
    if i + TP[i][0] > N:
        dp[i] = dp[i+1]
    else:
        #i번째 날 상담 할지 안할지 정함
        dp[i] = max(dp[i+1], TP[i][1]+dp[i + TP[i][0]])

print(dp[0])