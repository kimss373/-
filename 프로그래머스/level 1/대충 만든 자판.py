def solution(keymap, targets):
    answer = []

    alphaMap = {}

    for i in range(len(keymap)):
        for j in range(len(keymap[i])):
            alpha = keymap[i][j]
            if alpha in alphaMap:
                if alphaMap[alpha]>j+1:
                    alphaMap[alpha] = j+1
            else:
                alphaMap[alpha] = j+1

    for i in range(len(targets)):
        sum = 0
        isComplete = True
        for j in range(len(targets[i])):
            alpha = targets[i][j]
            if alpha in alphaMap:
                sum += alphaMap[alpha]
            else:
                answer.append(-1)
                isComplete = False
                break

        if isComplete:
            answer.append(sum)

    return answer