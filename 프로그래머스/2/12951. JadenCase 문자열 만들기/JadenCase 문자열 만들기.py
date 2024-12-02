def solution(s):
    lst = s.split(" ")
    cap = [word.capitalize() for word in lst]
    answer = ' '.join(cap)
    return answer