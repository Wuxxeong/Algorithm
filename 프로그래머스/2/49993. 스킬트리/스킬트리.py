def solution(skill, skill_trees):
    answer = 0
    
    for skill_tree in skill_trees:
        s = ""
        for ch in skill_tree:
            if ch in skill:
                s += ch
        
        if skill[:len(s)] == s:
            answer += 1
    return answer