import math
# from itertools import combinations

def combinations(n, new_arr, c):
    result = []

    if len(new_arr) == n:
        return [new_arr]
    for i in range(c, len(chicken)):
        result += combinations(n, new_arr + [chicken[i]], i+1)

    return result

def calculateDistance(house, chicken):
    min_d = 0
    for h in house:
        min_h = float(math.inf)
        for ch in chicken:
            ch_dist = abs(h[0] - ch[0]) + abs(h[1] - ch[1])
            if ch_dist < min_h:
                min_h = ch_dist
        min_d += min_h
    return min_d


N, M = map(int, input().split())
cities = [[0] * (N + 1)]
for _ in range(N):
    cities.append([0] + list(map(int, input().split())))

chicken = []
house = []
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if cities[i][j] == 1:
            house.append([i, j])
        elif cities[i][j] == 2:
            chicken.append([i, j])

distance = float(math.inf)
for ch in combinations(M, [], 0):
    cd = calculateDistance(house, ch)
    if cd < distance:
        distance = cd
print(distance)
