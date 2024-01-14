import heapq
N = int(input())
cards = []
for _ in range(N):
  heapq.heappush(cards, int(input()))

result = 0

while len(cards) > 1:
  a = heapq.heappop(cards)
  b = heapq.heappop(cards)
  heapq.heappush(cards, a+b)
  result = result + a+b

print(result)