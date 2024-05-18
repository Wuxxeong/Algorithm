def isChange(r,c):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    cnt = 0
    for i in range(4):
        nx, ny = r+dx[i], c+dy[i]
        if nx <0 or nx >= R or ny < 0 or ny >= C :
            cnt += 1
        elif m[nx][ny] == '.':
            cnt += 1
    
    if cnt >= 3: return True
    return False


R, C = list(map(int, input().split()))
m = []

for _ in range(R):
    m.append(list(input()))

change, X = [], []
for r in range(R):
    for c in range(C):
        if m[r][c] == 'X' and isChange(r,c):
            change.append((r,c))
        if m[r][c] == 'X'and not isChange(r,c):
            X.append((r,c))

for ch in change:
    r, c = ch
    m[r][c] = '.'
max_row , max_col, min_row, min_col = -1, -1, R, C
for x in X:
    r, c = x
    if r > max_row : max_row = r
    if c > max_col : max_col = c
    if r < min_row : min_row = r
    if c < min_col : min_col = c


for r in range(min_row, max_row+1):
    for c in range(min_col, max_col+1):
        print(m[r][c], end='')
    print()