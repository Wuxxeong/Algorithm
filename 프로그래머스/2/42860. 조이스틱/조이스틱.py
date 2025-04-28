def solution(name):
    answer = 0
    L = len(name)

    # 상하 이동 (각 알파벳 최소 조작 수)
    for char in name:
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)

    # 좌우 이동 최적화
    move = L - 1
    for i in range(L):
        next_i = i + 1
        while next_i < L and name[next_i] == 'A':
            next_i += 1
        move = min(move, i + L - next_i + min(i, L - next_i))
    
    answer += move
    return answer
