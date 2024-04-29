from collections import deque

def solution(n, results):
    answer = 0
    win = [[] for _ in range(n+1)]
    lose = [[] for _ in range(n+1)]
    k = []
    for result in results:
        a, b = result
        win[a].append(b)
        lose[b].append(a)
        
    for i in range(1, n+1):
        wins , loses = [], []
        wq, lq = deque(), deque()
        wq.append(i)
        lq.append(i)
        
        while wq:
            wp = wq.popleft()
            for p in win[wp]:
                if p not in wins:
                    wins.append(p)
                    wq.append(p)
        
        while lq:
            lp = lq.popleft()
            for p in lose[lp]:
                if p not in loses:
                    loses.append(p)
                    lq.append(p)
                    
        if len(wins)+len(loses)+1 == n: 
            answer+=1
    
    return answer