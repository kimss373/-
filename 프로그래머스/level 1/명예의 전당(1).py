def solution(k, score):
    answer = []
    q = []

    for i in range(len(score)):
        q.append(score[i])
        q.sort()
        if len(q) <= k:
            answer.append(q[0])

        else:
            answer.append(q[-k])

    return answer

print(solution(4, [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]))