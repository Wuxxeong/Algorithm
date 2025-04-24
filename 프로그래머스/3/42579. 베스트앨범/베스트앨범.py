from collections import defaultdict

def solution(genres, plays):
    answer = []
    dict = defaultdict(list)
    L = len(genres)
    
    for idx in range(L):
        dict[genres[idx]].append([plays[idx],idx])
        
    for key in dict:
        dict[key].sort(key=lambda x:(-x[0],x[1]))  #고유번호 낮은 순
    
    #속한 노래가 많이 재생된 순
    genres_key = list(dict.keys())
    genres_key.sort(key=lambda x:-sum(play for play,_ in dict[x]))
    
    for gk in genres_key:
        dict_sub = dict[gk][:2]
        for play,idx in dict_sub:
            answer.append(idx)
    return answer