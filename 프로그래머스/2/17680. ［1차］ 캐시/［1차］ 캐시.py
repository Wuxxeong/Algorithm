from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = deque()
    
    cities_lower = [city.upper() for city in cities]
    
    for city in cities_lower:
        if cacheSize == 0:
            answer = 5 * len(cities)
            break
        elif city in cache:
            cache.remove(city)
            cache.append(city)
            answer += 1
        else:
            if len(cache) < cacheSize:
                cache.append(city)
            else:
                cache.popleft()
                cache.append(city)
            answer += 5
                
    return answer