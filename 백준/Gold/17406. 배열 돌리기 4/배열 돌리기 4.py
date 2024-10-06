import copy

# 배열을 회전시키는 함수
def rotate(arr, r, c, s):
    r, c = r - 1, c - 1  # 0-index로 변환
    new_arr = copy.deepcopy(arr)

    for i in range(1, s + 1):
        # 상단 행 회전
        for col in range(c - i, c + i):
            new_arr[r - i][col + 1] = arr[r - i][col]
        # 우측 열 회전
        for row in range(r - i, r + i):
            new_arr[row + 1][c + i] = arr[row][c + i]
        # 하단 행 회전
        for col in range(c + i, c - i, -1):
            new_arr[r + i][col - 1] = arr[r + i][col]
        # 좌측 열 회전
        for row in range(r + i, r - i, -1):
            new_arr[row - 1][c - i] = arr[row][c - i]

    return new_arr

# 배열의 행 합 중 최소 값을 반환하는 함수
def get_min_value(arr):
    return min([sum(row) for row in arr])

# 백트래킹을 이용해 최적의 순서를 찾는 함수
def backtrack(arr, operations, selected, depth, K):
    global min_value

    # 모든 회전 연산이 선택된 경우
    if depth == K:
        temp_arr = copy.deepcopy(arr)
        
        # 선택된 순서대로 배열 회전 적용
        for idx in selected:
            r, c, s = operations[idx]
            temp_arr = rotate(temp_arr, r, c, s)
        
        # 배열의 최소 행 합 계산
        min_value = min(min_value, get_min_value(temp_arr))
        return

    # 각 회전 연산 선택 (백트래킹)
    for i in range(K):
        if i not in selected:
            selected.append(i)
            backtrack(arr, operations, selected, depth + 1, K)
            selected.pop()

# 메인 함수
def solution(N, M, K, arr, operations):
    global min_value
    min_value = float('inf')
    
    backtrack(arr, operations, [], 0, K)
    
    return min_value

# 입력 처리
N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
operations = [tuple(map(int, input().split())) for _ in range(K)]

# 결과 출력
print(solution(N, M, K, arr, operations))
