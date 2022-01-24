def solution(bridge_length, weight, truck_weights):
    answer = 0
    que = []
    loading = []
    for i in truck_weights:
        if sum(loading) + i > weight:
            while sum(loading) + i > weight:
                for j in range(len(que)):
                    que[j][1] += 1
                answer += 1
                if que[0][1] == bridge_length + 1:
                    que.pop(0)
                    loading.pop(0)
            que.append([i, 1])
            loading.append(i)

        else:
            for k in range(len(que)):
                que[k][1] += 1
            que.append([i, 1])
            loading.append(i)
            answer += 1
            if que[0][1] == bridge_length + 1:
                que.pop(0)
                loading.pop(0)

    while que:
        for l in range(len(que)):
            que[l][1] += 1
        answer += 1
        if que[0][1] == bridge_length + 1:
            que.pop(0)
            loading.pop(0)

    return answer