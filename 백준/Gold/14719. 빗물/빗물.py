H, W = list(map(int, input().split()))
blocks = list(map(int, input().split()))
ans = 0

for i in range(1, W-1):
    left_top = max(blocks[:i])
    right_top = max(blocks[i+1:])
    m = min(left_top, right_top)
    
    if m > blocks[i]:
        ans += m-blocks[i]

print(ans)