p = input()
result = ''
length = 0
for i in range(len(p)):
    if p[i]=='X':
        length+=1
        continue
    elif p[i]=='.':
        if length%2!=0:
            result = -1
            break
        while length>0:
            if length>=4:
                result += 'AAAA'
                length -= 4
            else:
                result += 'BB'
                length -= 2
        result += '.'
if length>0:
    if length%2!=0:
        result = -1
    else:
        while length>0:
            if length>=4:
                result += 'AAAA'
                length -= 4
            else:
                result += 'BB'
                length -= 2

print(result)