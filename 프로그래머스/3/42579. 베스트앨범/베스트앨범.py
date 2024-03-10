from collections import defaultdict

def solution(genres, plays):
    answer = []
    gp = defaultdict(list)
    total = defaultdict(int)
    
    for i in range(len(genres)):
        gp[genres[i]].append([plays[i],i])
        total[genres[i]] += plays[i]
        
    for key in gp.keys():
        gp[key].sort(reverse=True, key=lambda x:x[0])
    
    genre_order = sorted(total.keys(), key=lambda x: total[x], reverse=True)
    
    for genre in genre_order:
        answer.append(gp[genre][0][1])
        if len(gp[genre]) > 1:
            answer.append(gp[genre][1][1])
    return answer