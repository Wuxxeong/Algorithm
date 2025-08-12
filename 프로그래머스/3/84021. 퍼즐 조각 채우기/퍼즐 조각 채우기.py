from collections import deque

# 좌표 리스트들을 추출 (k=0: 빈칸, k=1: 퍼즐)
def bfs(board, k):
    lst = []
    r, c = len(board), len(board[0])
    v = set()

    for i in range(r):
        for j in range(c):
            if board[i][j] == k and (i, j) not in v:
                sub = []
                q = deque([(i, j)])
                v.add((i, j))
                while q:
                    x, y = q.popleft()
                    sub.append((x, y))
                    for di, dj in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                        ni, nj = x + di, y + dj
                        if 0 <= ni < r and 0 <= nj < c and (ni, nj) not in v and board[ni][nj] == k:
                            v.add((ni, nj))
                            q.append((ni, nj))
                sub.sort(key=lambda x: (x[0], x[1]))
                lst.append(sub)
    return lst

# 좌표 리스트 -> 좌상단 기준으로 정규화된 2D 테이블(행렬)로 변환
def to_table(coords):
    xs = [x for x, _ in coords]
    ys = [y for _, y in coords]
    minx, miny = min(xs), min(ys)
    maxx, maxy = max(xs), max(ys)
    h, w = maxx - minx + 1, maxy - miny + 1
    table = [[0] * w for _ in range(h)]
    for x, y in coords:
        table[x - minx][y - miny] = 1
    return table

# 시계 방향 90도 회전 (정답 코드의 rotate와 동일한 동작)
def rotate(mat):
    h, w = len(mat), len(mat[0])
    res = [[0] * h for _ in range(w)]
    for i in range(h):
        for j in range(w):
            res[j][h - 1 - i] = mat[i][j]
    return res

def ones(mat):
    return sum(sum(row) for row in mat)

def solution(game_board, table):
    answer = 0

    # 1) 빈칸/퍼즐 좌표 추출
    empty_game_lst = bfs(game_board, 0)
    puzzle_lst = bfs(table, 1)

    # 2) 좌표 -> 정규화 테이블로 변환
    empty_tables = [to_table(glst) for glst in empty_game_lst]
    puzzle_tables = [to_table(plst) for plst in puzzle_lst]

    # 퍼즐 소모 관리
    used = [False] * len(puzzle_tables)

    # 3) 빈칸별로 퍼즐 매칭 (회전 4번까지 시도)
    for gt in empty_tables:
        matched = False
        for j, pt in enumerate(puzzle_tables):
            if used[j]:
                continue
            cur = pt
            for _ in range(4):
                if len(gt) == len(cur) and len(gt[0]) == len(cur[0]) and gt == cur:
                    answer += ones(cur)
                    used[j] = True  # 퍼즐 소모
                    matched = True
                    break
                cur = rotate(cur)
            if matched:
                break

    return answer
