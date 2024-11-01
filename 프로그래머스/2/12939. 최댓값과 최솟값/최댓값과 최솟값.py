def solution(s):
    answer = ''
    lst = list(map(int,s.split(" ")))
    
    lst.sort()
    answer+=str(lst[0])
    answer+=" "
    answer+=str(lst[-1])
    return answer