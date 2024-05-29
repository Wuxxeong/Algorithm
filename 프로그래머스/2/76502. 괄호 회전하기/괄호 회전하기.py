def check(s):
    stack = []
    for i in range(len(s)):
        if s[i] == '[' or s[i] == '(' or s[i] == '{' :
            stack.append(s[i])
        elif s[i] == ']' and stack != [] and stack[-1] == '[':
            stack.pop()
        elif s[i] == ')' and stack != [] and stack[-1] == '(':
            stack.pop()
        elif s[i] == '}' and stack != [] and stack[-1] == '{':
            stack.pop()
        elif (s[i] == ']' or s[i] == ')' or s[i] == '}') and stack == []:
            return False
    if stack == []: return True
    return False

def solution(s):
    answer = 0
    cnt = len(s)
    
    while cnt:
        if check(s): answer += 1
        s = s[1:]+s[0]
        cnt -= 1
    
    return answer