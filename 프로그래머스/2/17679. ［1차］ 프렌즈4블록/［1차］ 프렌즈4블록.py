def solution(m, n, board):
    answer = 0
    for i in range(len(board)):
        board[i] = list(board[i])
    points = set()
    while True:
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j]==[]: continue
                if board[i][j]==board[i+1][j] and board[i][j]==board[i][j+1] and board[i][j]==board[i+1][j+1]:
                    points.add((i,j))
                    points.add((i,j+1))
                    points.add((i+1,j))
                    points.add((i+1,j+1))
        
        if points:
            answer += len(points)
            for i,j in points:
                board[i][j] = []
            points = set()
        else:
            return answer
        
        while True:
            moved = 0
            for i in range(m-1):
                for j in range(n):
                    if board[i][j] and board[i+1][j]==[]:
                        board[i+1][j] = board[i][j]
                        board[i][j] = []
                        moved = 1
            if moved == 0:
                break
                    
    return answer