import math
def solution(progresses, speeds):
    answer = []
    days = [math.ceil((100-progresses[i])/speeds[i]) for i in range(len(progresses))]
    
    count=0
    release = days[0]
    for day in days:
        if day <= release:
            count += 1
            continue
        answer.append(count)
        release = day
        count = 1
    answer.append(count)
    return answer

'''
7, 3, 9
5, 10, 1, 1, 20, 1
'''