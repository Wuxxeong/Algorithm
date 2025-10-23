def solution(distance, rocks, n):
    answer = 0
    
    rocks.append(distance)
    rocks.sort()
    left, right = 1,distance
    
    while left<=right:
        mid = (left+right)//2
        
        breakRock = 0
        previous = 0
        for rock in rocks:
            if rock-previous<mid:
                breakRock+=1
                if breakRock>n:break
            else:
                previous = rock
        if breakRock>n:
            right = mid-1
        else:
            left = mid+1
            answer = mid
    return answer