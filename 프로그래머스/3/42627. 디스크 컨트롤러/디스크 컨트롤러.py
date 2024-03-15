def solution(jobs):
    answer = 0
    total = 0
    finish = 0
    
    jobs.sort(key = lambda x:x[1]-x[0])
    
    for job in jobs:
        waiting = finish-job[0]
        if waiting > 0:
            total = total+waiting+job[1]
            finish += job[1]
        else:
            total += job[1]
            finish += job[1]
    
    answer = total//len(jobs)
    return answer