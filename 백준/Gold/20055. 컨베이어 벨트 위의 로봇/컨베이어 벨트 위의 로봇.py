from collections import deque
N, K = list(map(int, input().split()))
A = deque(list(map(int, input().split())))
robot = deque([0]*N)

res = 1
while True:
    A.rotate(1)
    robot.rotate(1)
    robot[-1] = 0
    
    if robot:
        for i in range(N-2, -1, -1):
            if robot[i] == 1 and robot[i+1] == 0 and A[i+1] >=1:
                robot[i+1] = 1
                robot[i] = 0
                A[i+1] -= 1
        robot[-1] = 0
        
    if robot[0] == 0 and A[0] >= 1:
        robot[0] = 1
        A[0] -= 1
        
    if A.count(0) >= K:
        break
    
    res += 1
    
print(res)