'''
큐 = 작업 번호, 요청 시각, 소요 시간
하드디스크 작업 X and 대기 큐 존재 -> 우선순위가 높은 작업 꺼내서 실행
    우선순위 = 소요시간 작, 요청시각 작, 작업 번호 작 순으로 높음
하나의 작업만 실행
요청이 들어오면 작업을 대기 큐에 저장

모든 작업의 반환 시간을 알아내어 이들의 평균을 출력

-> 매번 작업이 추가될 때마다 sort를 할 수 없으니 heapify로 풀자!
'''

import heapq

def solution(jobs):
    answer,time,i = 0,0,0
    jobs.sort()
    L = len(jobs)
    
    waiting = []
    heapq.heapify(waiting)
    
    while i<L or waiting:
        #[1] 현재 time에 작업을 시행할 수 있는지 process들을 waiting 
        while jobs and jobs[0][0]<=time:
            start,total = jobs.pop(0)
            heapq.heappush(waiting,[total,start,i])
            i+=1
        
        if waiting:
            ct,cs,ci = heapq.heappop(waiting)
            time += ct
            answer += time-cs            
        else:
            time += 1

    return answer//L