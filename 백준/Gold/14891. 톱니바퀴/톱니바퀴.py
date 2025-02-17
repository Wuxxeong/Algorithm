from collections import deque

def left(idx,d):
    if idx<0:
        return
    else:
        if arr[idx][2]!=arr[idx+1][6]:
            left(idx-1,-d)
            arr[idx].rotate(d)


def right(idx,d):
    if idx>3:
        return
    else:
        if arr[idx-1][2]!=arr[idx][6]:
            right(idx+1,-d)
            arr[idx].rotate(d)

arr = [deque(map(int,input())) for _ in range(4)]
K = int(input())

for _ in range(K):
    n,d = map(int,input().split())
    n-=1

    left(n-1,-d)
    right(n+1,-d)

    arr[n].rotate(d)

# 점수 합 구하기
score = 0
for i in range(4):
    if arr[i][0] == 1:
        score += 2**i
print(score)