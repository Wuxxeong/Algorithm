N = int(input())
people = list(map(int, input().split()))
line = [-1 for _ in range(N)]


for i in range(N):
  empty = 0
  for j in range(N):
    if people[i] == empty and line[j] == -1:
      line[j] = i+1
      break
    if line[j] == -1:
      empty += 1
    

for l in line:
  print(l, end=" ")