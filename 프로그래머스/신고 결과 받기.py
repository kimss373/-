def solution(id_list, report, k):
    answer = []
    stopmember=[]
    dict = {}
    for i in id_list:
        dict[i] = [0]

    for j in range(len(report)):
        a, b = report[j].split()
        if b not in dict[a]:
            dict[a].append(b)
            dict[b][0] += 1

    for l in dict:
        if dict[l][0]>=k:
            stopmember.append(l)

    for z in dict:
        cnt =0
        for q in stopmember:
            if q in dict[z]:
                cnt+=1
        answer.append(cnt)
    return answer