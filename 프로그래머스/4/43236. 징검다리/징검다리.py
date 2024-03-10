def solution(distance, rocks, n):
    answer = 0
    rocks.append(distance)
    rocks.sort()
    left , right = 1, distance
    
    while left <= right:
        mid = (left+right)//2   #가정한 거리의 최솟값
        
        breakRock = 0
        previous = 0
        for rock in rocks:
            if rock - previous < mid:
                breakRock += 1
                if breakRock > n: break
            else:
                previous = rock
        
        if breakRock > n:
            right = mid-1
        else:
            answer = mid
            left = mid+1
                
    return answer