from collections import defaultdict
import math

def parkingTime(i, o):
    t = 0
    ih, im = map(int, i.split(':'))
    oh, om = map(int, o.split(':'))

    if im > om:
        oh -= 1
        om += 60
    
    th = oh-ih
    tm = om-im
    
    t = th*60+tm
    return t

def fee(time, fees):
    f = fees[1]
    if time > fees[0]:
        f = f+ math.ceil((time-fees[0])/fees[2]) * fees[3]
    return f

def solution(fees, records):
    answer = []
    dict = defaultdict(list)
    time = defaultdict(int)
    
    for record in records:
        r = record.split()
        dict[r[1]].append(r[0])
    
    for k in dict.keys():
        if len(dict[k])%2 != 0 :
            dict[k].append('23:59')
        for i in range(0, len(dict[k])-1, 2):
            time[k] += parkingTime(dict[k][i], dict[k][i+1])
    
    
    cars = sorted(time.keys())
    for car in cars:
        answer.append(fee(time[car], fees))
    return answer

