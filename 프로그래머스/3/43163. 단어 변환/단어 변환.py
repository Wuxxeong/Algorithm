from collections import deque
def count_diff(previous, later):
    count=0
    for i in range(len(previous)):
        if previous[i] != later[i]:
            count += 1
    return count

def solution(begin, target, words):
    answer = 0
    queue = deque()
    queue.append((begin, answer))
    
    while queue:
        previous, answer = queue.popleft()
        if previous == target:
            return answer
        for i in range(len(words)):
            if count_diff(previous, words[i]) == 1:
                queue.append((words[i], answer+1))

    answer = 0
    return answer