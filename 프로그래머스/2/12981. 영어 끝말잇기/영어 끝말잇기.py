def solution(n, words):
    answer = [0,0]
    
    stack = []
    for index, word in enumerate(words):
        if stack and (word in stack or stack[-1][-1] != word[0]):
            answer[0] = index%n + 1
            answer[1] = index//n + 1
            break
        
        stack.append(word)
    

    return answer