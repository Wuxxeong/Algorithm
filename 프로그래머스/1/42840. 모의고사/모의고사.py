def solution(answers):
    answer = []
    count = [0, 0, 0]
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for i in range(len(answers)):
        if answers[i] == a[i%len(a)]:
            count[0] += 1
        if answers[i] == b[i%len(b)]:
            count[1] += 1
        if answers[i] == c[i%len(c)]:
            count[2] += 1
    
    m = max(count)
    answer = [i+1  for i in range(len(count)) if m==count[i]]
    
    return answer