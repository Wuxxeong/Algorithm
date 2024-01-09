N, K = map(int, input().split())
arr = []
for i in range(N):
  arr.append(int(input()))
arr.sort(reverse=True)

count = 0
for coin in arr:
  if coin <= K:
    count += K // coin
    K %= coin
  if K <= 0: break

print(count)