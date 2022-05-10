def solution(cacheSize, cities):
    answer = 0
    tmp = [' '] * cacheSize
    for i in cities:
        i = i.lower()
        if i in tmp:
            answer += 1
            tmp.remove(i)
            tmp.append(i)
        else:
            answer += 5

            tmp.append(i)
            tmp.pop(0)
    return answer