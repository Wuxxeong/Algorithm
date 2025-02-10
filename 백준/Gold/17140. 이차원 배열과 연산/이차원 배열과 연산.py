from collections import defaultdict

# 입력 받기
r, c, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(3)]

time = 0

# (수, 등장 횟수)로 정렬하는 함수
def calculate(arr):
    updated_arr = []
    max_len = 0

    for row in arr:
        freq = defaultdict(int)

        # 빈도 계산
        for num in row:
            if num != 0:  # 0은 무시
                freq[num] += 1

        # (수, 등장 횟수) 형태로 변환 후 정렬
        sorted_row = sorted(freq.items(), key=lambda x: (x[1], x[0]))
        
        # [수, 등장 횟수, 수, 등장 횟수 ...] 형태로 변환
        flat_row = [item for sublist in sorted_row for item in sublist]

        max_len = max(max_len, len(flat_row))
        updated_arr.append(flat_row)

    # 행 길이를 최대 길이에 맞추고, 최대 100개까지 유지
    for i in range(len(updated_arr)):
        updated_arr[i].extend([0] * (max_len - len(updated_arr[i])))
        if len(updated_arr[i]) > 100:
            updated_arr[i] = updated_arr[i][:100]

    return updated_arr

# 배열 회전 함수
def rotate(arr):
    return list(zip(*arr))

# 시뮬레이션 시작
while True:
    # 조건이 만족되면 종료
    if len(A) > r - 1 and len(A[0]) > c - 1 and A[r - 1][c - 1] == k:
        break

    if time > 100:
        time = -1
        break

    # R 연산 또는 C 연산 수행
    if len(A) >= len(A[0]):
        A = calculate(A)  # R 연산
    else:
        A = rotate(A)  # 90도 회전
        A = calculate(A)  # C 연산
        A = rotate(A)  # 다시 원래 상태로 회전

    time += 1

# 결과 출력
print(time)
