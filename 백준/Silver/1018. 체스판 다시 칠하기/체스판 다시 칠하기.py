def check(mini_bard):
    start_with_white = ['WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW']
    start_with_black = ['BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB']
    change=64
    bc,wc = 0,0
    
    for row in range(8):
        mr = mini_board[row]
        br = start_with_black[row]
        wr = start_with_white[row]
        for col in range(8):
            if br[col]!=mr[col]: bc+=1
            if wr[col]!=mr[col]: wc+=1

    change = min(change,min(bc,wc))
    
    return change

N,M = map(int, input().split())
board = [input() for _ in range(N)]

mn = 64
#[1]8x8 보드 하나씩 선정
for sr in range(N-8+1):
    for sc in range(M-8+1): #start row, start col 일때,
        mini_board = [board[r][sc:sc+8] for r in range(sr,sr+8)]
        cnt = check(mini_board)
        if cnt<mn:
            mn=cnt

print(mn)
