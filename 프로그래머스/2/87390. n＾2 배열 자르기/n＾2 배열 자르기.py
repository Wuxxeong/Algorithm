def solution(n, left, right):
    arr = []
    
    for i in range(left, right+1):
        q , r = i//n, i%n
        if q >= r:
            arr.append(q+1)
        else:
            arr.append(r+1)
    
    return arr