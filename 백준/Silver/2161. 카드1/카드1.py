N = int(input())
num = [i for i in range(1, N+1)]
trash = []
while (len(num) > 1):
  trash.append(num.pop(0))
  num.append(num.pop(0))

answer = trash + num

for i in range(N):
  print(answer[i], end=" ")