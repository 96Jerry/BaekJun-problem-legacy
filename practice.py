def solution(cacheSize, cities):
    c = cacheSize
    n = len(cities)
    
    # 캐시가 없다면 5를 곱해서 리턴
    if c == 0:
        return 5 * n
    
    # cities 소문자로 바꿔주기
    for i in range(n):
        cities[i] = cities[i].lower()

    # 처음 도시는 무조건 캐시에 포함되며 5의 시간이 걸림
    cache = [cities[0]]
    count = 5
    
    for i in range(1,c):
        if i >= n:
            return count
        if cities[i] in cache:
            count += 1
        else:
            count += 5
        cache.append(cities[i])
        
    if c < n:
        # i 가 3 부터 9까지
        # c 는 3
        # cities의 0부터 3까지
        for i in range(c, n):
            cache = cities[i-c+1:i+1]
            if cities[i] in cache:
                count += 1
            else:
                count += 5
    return count

result = solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"])
print(result)