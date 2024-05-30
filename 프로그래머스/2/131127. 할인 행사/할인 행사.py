def check(days, wn):
    w = wn.copy()
    for day in days:
        if day in w.keys() and w[day] != 0:
            w[day] -= 1
        elif day not in w.keys() or w[day] == 0:
            return False
    return True

def solution(want, number, discount):
    result = 0
    wn = {}
    for i in range(len(number)):
        wn[want[i]] = number[i]
    
    for d in range(0, len(discount)-9):
        days = discount[d:d+10]

        if check(days, wn): result += 1
    
    return result