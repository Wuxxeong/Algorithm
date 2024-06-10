from itertools import permutations
from re import split

def solution(expression):
    answer = 0
    results = []
    

    for priority in permutations(['*','-','+'],3):
        operands = list(map(int, split('[\+\*\-]', expression)))
        operator = [c for c in expression if c in '+-*']
        i,v = 0, 0
        for op in priority:
            while op in operator:
                i = operator.index(op)
                if operator[i] == '*':
                    v = operands[i] * operands[i+1]
                elif operator[i] == '+':
                    v = operands[i] + operands[i+1]
                elif operator[i] == '-':
                    v = operands[i] - operands[i+1]
                
                operator.pop(i)
                operands[i] = v
                operands.pop(i+1)
        
        results.append(abs(operands[0]))
    
    answer = max(results)
    return answer