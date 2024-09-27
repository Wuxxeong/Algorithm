def solution(files):
    answer = []
    seperated_files = []
    #head, number, tail 구분
    for file in files:
        head, number, tail = "", "", ""
        for ch in file:
            if head == "":
                head += ch
            elif ("A"<=ch<="z" or ch==" " or ch=="." or ch=="-") and number =="":
                head += ch
            elif "0"<=ch<="9" and tail=="":
                number += ch
            else:
                tail += ch
        seperated_files.append([head, number, tail])
    #정렬
    seperated_files.sort(key=lambda x:(x[0].upper(), int(x[1])))    
    answer = ["".join(sf) for sf in seperated_files]
    return answer