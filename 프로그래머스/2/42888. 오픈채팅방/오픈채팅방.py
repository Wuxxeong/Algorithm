def solution(record):
    answer = []
    
    people={}
    admin = []
    
    result = []
    for r in record:
        lst = r.split()
        command,uid = lst[0],lst[1]
        admin.append([command,uid])
        if command=="Enter" or command=="Change":
            name=lst[-1]
            people[uid]=name
            
    for command,uid in admin:
        if command=="Enter":
            answer.append(people[uid]+"님이 들어왔습니다.")
        elif command=="Leave":
            answer.append(people[uid]+"님이 나갔습니다.")
    return answer