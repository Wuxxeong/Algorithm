from collections import deque

def solution(prices):
    answer = []
    prices = deque(prices)
    
    while prices:
        me = prices.popleft()
        time = 0
        for price in prices:
            if me <= price:
                time += 1
            else:
                time += 1
                break
        answer.append(time)
    return answer