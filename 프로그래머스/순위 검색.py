from itertools import combinations
import bisect

def solution(info, query):
    answer = []
    dict = {}
    for i in info:
        tmplist = i.split()
        key = tmplist[:-1]
        value = tmplist[-1]

        for j in range(5):
            for k in combinations(key, j):
                tmp = "".join(k)
                if tmp in dict:
                    dict[tmp].append(int(value))
                else:
                    dict[tmp] = [int(value)]

    for key in dict:
        dict[key].sort()
    for i in query:
        tmplist = i.split()
        for j in range(3):
            tmplist.remove('and')
        while '-' in tmplist:
            tmplist.remove('-')

        key = tmplist[:-1]
        value = tmplist[-1]
        key = "".join(key)

        if key in dict:
            codingtests = dict[key]

            if codingtests:
                idx = bisect.bisect_left(codingtests, int(value))
                answer.append(len(codingtests) - idx)

        else:
            answer.append(0)



    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))