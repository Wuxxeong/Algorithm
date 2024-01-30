def solution(array, commands):
    answer = []
    for command in commands:
        start = command[0]
        end = command[1]
        k = command[2]
        new = array[start-1:end]
        new.sort()
        answer.append(new[k-1])
    return answer