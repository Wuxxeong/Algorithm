from collections import defaultdict

def solution(genres, plays):
    answer = []
    gp = defaultdict(list)
    total = defaultdict(int)

    for i in range(len(genres)):
        gp[genres[i]].append([plays[i], i])
        total[genres[i]] += plays[i]

    genre_order = sorted(total.keys(), key=lambda x: total[x], reverse=True)

    for genre in genre_order:
        gp[genre].sort(key=lambda x: (-x[0], x[1]))
        answer.append(gp[genre][0][1])
        if len(gp[genre]) > 1:
            answer.append(gp[genre][1][1])

    return answer
