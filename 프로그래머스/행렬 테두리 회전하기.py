def solution(rows, columns, queries):
    answer = []
    hang = [[0 for i in range(columns+1)]]
    num = 1
    for i in range(rows):
        row = [0]
        for j in range(columns):
            row.append(num)
            num += 1
        hang.append(row)

    for i in queries:
        maxnum = rows * columns + 1
        x1, y1, x2, y2 = i
        tmp = hang[x1][y2]
        if tmp < maxnum:
            maxnum = tmp
        for j in range(y2, y1, -1):
            hang[x1][j] = hang[x1][j-1]
            if hang[x1][j-1] < maxnum:
                maxnum = hang[x1][j-1]
        for j in range(x1, x2):
            hang[j][y1] = hang[j+1][y1]
            if hang[j+1][y1] < maxnum:
                maxnum = hang[j+1][y1]
        for j in range(y1, y2):
            hang[x2][j] = hang[x2][j+1]
            if hang[x2][j+1]<maxnum:
                maxnum = hang[x2][j+1]
        for j in range(x2, x1+1, -1):
            hang[j][y2] = hang[j-1][y2]
            if hang[j-1][y2]<maxnum:
                maxnum = hang[j-1][y2]
        hang[x1+1][y2] = tmp
        answer.append(maxnum)

    return answer

print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))