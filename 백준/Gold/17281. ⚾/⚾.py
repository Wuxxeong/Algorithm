import sys
from itertools import permutations

N = int(sys.stdin.readline())
inning = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

result = float('-inf')

for line_ups in permutations(range(1,9), 8):
    line_ups = list(line_ups)
    batter = line_ups[:3] + [0] + line_ups[3:]
    
    number, point = 0, 0
    for i in range(N):
        out = 0
        b1, b2, b3 = 0, 0, 0
        while out < 3:
            if inning[i][batter[number]] == 0:
                out += 1
            elif inning[i][batter[number]] == 1:
                point += b3
                b1, b2, b3 = 1, b1, b2
            elif inning[i][batter[number]] == 2:
                point += b2 + b3
                b1, b2, b3 = 0, 1, b1
            elif inning[i][batter[number]] == 3:
                point += b1 + b2 + b3
                b1, b2, b3 = 0, 0, 1
            elif inning[i][batter[number]] == 4:
                point += b1 + b2 + b3 + 1
                b1, b2, b3 = 0, 0, 0
            number = (number+1)%9
    result = max(result, point)

print(result)