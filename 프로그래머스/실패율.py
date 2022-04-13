def solution(N, stages):
    answer=[]
    dict = {}
    result = []
    x = len(stages)
    for i in range(1, N+2):
        dict[i] = 0
    for j in stages:
        dict[j] += 1

    for k in range(1, N+1):
        if x>0:
            result.append([dict[k]/x, k])
            x -= dict[k]
        else:
            result.append([dict[k], k])


    f = sorted(result, key = lambda y : (-y[0], y[1]))
    for z in f:
        answer.append(z[1])
    return answer
print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))