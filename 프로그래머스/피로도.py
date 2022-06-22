from itertools import permutations

def solution(k, dungeons):
    x = len(dungeons)
    g = k
    xlist = [i for i in range(x)]
    xcombi = list(permutations(xlist, x))
    answer = 0
    for i in xcombi:
        tmp = 0
        k = g
        for j in i:
            a, b = dungeons[j]
            if k >= a:
                k-=b
                tmp += 1
        if tmp > answer:
            answer = tmp


    return answer

print(solution(80, [[80,20],[50,40],[30,10]]))