def convert_polymino(p):
    result = ''
    length = 0
    
    for char in p:
        if char == 'X':
            length += 1
        elif char == '.':
            if length%2 != 0:
                return -1
            result += 'AAAA' * (length // 4) + 'BB' * ((length%4)//2)
            result += '.'
            length = 0
            
    if length > 0:
        if length %2 != 0:
            return -1
        result += 'AAAA' * (length // 4) + 'BB' * ((length%4)//2)
    return result

p = input()
print(convert_polymino(p))