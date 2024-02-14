def solution(string):
    answer = True
    
    tmp = []
    for s in string:
        if s == '(':
            tmp.append(s)
        elif s == ')' and len(tmp)==0:
            answer = False
            break
        elif s == ')' and tmp[-1] == '(':
            tmp.pop()
    if len(tmp) != 0:
        answer = False
    return answer