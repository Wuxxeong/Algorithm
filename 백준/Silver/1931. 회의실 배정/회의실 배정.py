N = int(input())
time = [list(map(int, input().split())) for _ in range(N)]
time.sort(key=lambda x:(x[1], x[0]))
count = 1
k = 0
for i in range(1, N):
  if time[i][0] >= time[k][1]:
    count+=1
    k = i
print(count)