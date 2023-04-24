def solution(name, yearning, photo):
    answer = []
    score = {}

    for i in range(len(name)):
        score[name[i]] = yearning[i]

    for i in range(len(photo)):
        cnt = 0
        for j in range(len(photo[i])):
            if photo[i][j] in score:
                cnt += score[photo[i][j]]
        answer.append(cnt)

    return answer