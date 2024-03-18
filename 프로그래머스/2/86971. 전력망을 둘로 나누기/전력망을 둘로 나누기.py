def solution(n, wires):
    answer = []
    
    for wire in wires: #O(n)
        G1, G2 = [wire[0]], [wire[1]]
        wire_list = wires.copy()
        wire_list.remove(wire) #O(n)
        
        while wire_list:
            sub = wire_list.pop(0)
            if sub[0] in G1:
                G1.append(sub[1])
            elif sub[1] in G1:
                G1.append(sub[0])
            elif sub[0] in G2:
                G2.append(sub[1])
            elif sub[1] in G2:
                G2.append(sub[0])
            else:
                wire_list.append(sub)
    
        answer.append(abs(len(list(set(G1)))-len(list(set(G2)))))
    return min(answer)