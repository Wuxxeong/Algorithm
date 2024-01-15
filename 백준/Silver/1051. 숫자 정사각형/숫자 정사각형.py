N, M = map(int, input().split())
rectangle = [list(map(int, input())) for _ in range(N)]

if N >= M:
  max_size = M
else:
  max_size = N

i , j  = 0, 0

while max_size > 0:
  if rectangle[i][j] == rectangle[i+max_size-1][j] == rectangle[i][j+max_size-1] == rectangle[i+max_size-1][j+max_size-1]:
    print(max_size**2)
    break
  
  j += 1
  
  if j+max_size-1 >= M:
    j = 0
    i += 1
    
  if i+max_size-1 >= N:
    max_size -= 1
    i = 0
    j = 0