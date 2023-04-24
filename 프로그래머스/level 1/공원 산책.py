def solution(park, routes):
    answer = [0, 0]

    height = len(park)
    width = len(park[0])

    findS = False

    for i in range(height):
        if findS:
            break
        for j in range(width):
            if park[i][j] == 'S':
                answer = [j, i]
                findS = True
                break

    for i in range(len(routes)):
        direct, length = routes[i][0], int(routes[i][2])
        isGo = True
        if direct == "N" and answer[1] - length >= 0:
            for j in range(answer[1]-length, answer[1]):
                if park[j][answer[0]] == "X":
                    isGo = False
                    break
            if isGo:
                answer[1] -= length
        elif direct == "S" and answer[1] + length < height:
            for j in range(answer[1], answer[1] + length+1):
                if park[j][answer[0]] == "X":
                    isGo = False
                    break
            if isGo:
                answer[1] += length
        elif direct == "E" and answer[0] + length < width:
            for j in range(answer[0], answer[0] + length + 1):
                if park[answer[1]][j] == "X":
                    isGo = False
                    break
            if isGo:
                answer[0] += length
        elif direct == "W" and answer[0] - length >= 0:
            for j in range(answer[0]-length, answer[0]):
                if park[answer[1]][j] == "X":
                    isGo = False
                    break
            if isGo:
                answer[0] -= length

    return [answer[1], answer[0]]

solution(["SOO","OOO","OOO"], ["E 2","S 2","W 1"])