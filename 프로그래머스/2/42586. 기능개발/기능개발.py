def solution(progresses, speeds):
    answer = []
    day = 0
    
    while progresses:
        L = len(progresses)
        #날짜 지남
        day += 1
        
        #진도율 업데이트
        for i in range(L):
            progresses[i] += speeds[i]
    
        #0번째 prgress 확인
        cnt = 0
        while progresses and progresses[0]>=100:
            progresses.pop(0)
            speeds.pop(0)
            cnt+=1
            
        #배포가 되었다면
        if cnt!=0:
            answer.append(cnt)
        
    return answer