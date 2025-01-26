def solution(board):
    row, col = len(board), len(board[0])
    dp = [[0] * col for _ in range(row)]
    max_length = 0
    
    # DP 테이블 채우기
    for i in range(row):
        for j in range(col):
            if board[i][j] == 1:
                # 첫 행이나 첫 열은 그대로 복사
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                max_length = max(max_length, dp[i][j])
    
    # 가장 큰 정사각형의 면적 반환
    return max_length * max_length
