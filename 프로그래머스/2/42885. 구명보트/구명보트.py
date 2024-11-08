def solution(people, limit):
    answer = 0
    people.sort()
    result = []
    
    i,j=0,len(people)-1
    
    while i<=j:
        if (people[i]+people[j])<=limit:
            result.append(people[i]+people[j])
            i+=1
            j-=1
        else:
            result.append(people[j])
            j-=1
    return len(result)