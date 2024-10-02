def solution(order):
    stack = []  # 보조 컨테이너 벨트
    current_box = 1  # 컨테이너 벨트에서 현재 처리 중인 상자 번호
    answer = 0  # 트럭에 실은 상자의 수

    for o in order:
        while current_box <= len(order) and (not stack or stack[-1] != o):
            stack.append(current_box)
            current_box += 1

        if stack and stack[-1] == o:
            stack.pop()  # 트럭에 실을 수 있는 경우 보조 벨트에서 상자 제거
            answer += 1
        else:
            break  # 더 이상 원하는 순서대로 상자를 실을 수 없으면 종료

    return answer
