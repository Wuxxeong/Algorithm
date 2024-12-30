arr = [list(map(int, input().split())) for _ in range(10)]
used_papers = [0] * 5  # 각 크기별 사용된 종이 수
min_papers = float('inf')

def can_cover(si, sj, size):
    """지정된 위치에 종이를 덮을 수 있는지 확인"""
    if si + size > 10 or sj + size > 10:  # 범위 초과
        return False
    for i in range(si, si + size):
        for j in range(sj, sj + size):
            if arr[i][j] == 0:  # 덮을 수 없는 곳
                return False
    return True

def set_cover(si, sj, size, value):
    """지정된 크기의 종이를 덮거나 떼기"""
    for i in range(si, si + size):
        for j in range(sj, sj + size):
            arr[i][j] = value

def solve(idx, used):
    global min_papers
    if idx == 100:  # 모든 칸 탐색 완료
        min_papers = min(min_papers, used)
        return
    si, sj = divmod(idx, 10)  # 1차원 인덱스를 2차원 좌표로 변환
    if arr[si][sj] == 0:  # 덮을 필요 없는 칸
        solve(idx + 1, used)
        return

    for size in range(5, 0, -1):  # 큰 종이부터 시도
        if used_papers[size - 1] < 5 and can_cover(si, sj, size):
            # 종이를 덮는다
            set_cover(si, sj, size, 0)
            used_papers[size - 1] += 1
            solve(idx + 1, used + 1)
            # 원상복구
            set_cover(si, sj, size, 1)
            used_papers[size - 1] -= 1

solve(0, 0)
print(min_papers if min_papers != float('inf') else -1)
