def solution(sizes):
    answer = 0
    mx, my = -1, -1
    for size in sizes:
        if size[0] < size[1]:
            size[0], size[1] = size[1], size[0]
        if size[0] > mx:
            mx = size[0]
        if size[1] > my:
            my = size[1]
    
    
    answer = mx*my
    return answer