king, stone, N = input().split()
k = [ord(king[0]) - 64, int(king[1])]
s = [ord(stone[0]) - 64, int(stone[1])]
move = {'R': [1, 0], 'L': [-1, 0], 'B': [0, -1], 'T': [0, 1], 'RT': [1, 1], 'LT': [-1, 1], 'RB': [1, -1], 'LB': [-1, -1]}

for _ in range(int(N)):
    m = input()
    nx, ny = k[0] + move[m][0], k[1] + move[m][1]
    
    if 0 < nx <= 8 and 0 < ny <= 8:
        if [nx, ny] == s:
            sx, sy = s[0] + move[m][0], s[1] + move[m][1]
            if 0 < sx <= 8 and 0 < sy <= 8:
                k, s = [nx, ny], [sx, sy]
        else:
            k = [nx, ny]

print(f'{chr(k[0] + 64)}{k[1]}')
print(f'{chr(s[0] + 64)}{s[1]}')
