def solution(sequence, k):
    answer = []
    L = len(sequence)
    left,right = 0,0
    sub_sum = sequence[0]
    
    while right<L:
        if sub_sum<k:
            right+=1
            if right < L:
                sub_sum += sequence[right]
        elif sub_sum>k:
            sub_sum-=sequence[left]
            left+=1
        else:
            answer.append([left,right])
            sub_sum-=sequence[left]
            left+=1
    
    answer = sorted(answer, key=lambda x:(x[1]-x[0]))
    return answer[0]