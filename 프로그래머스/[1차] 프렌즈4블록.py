def solution(m, n, board):
    for i in range(m):
        board[i] = list(board[i])
    answer = 0
    while True:

        tmp = []
        for i in range(m-1):
            for j in range(n-1):
                x = board[i][j]
                if x == 0:
                    continue
                if x == board[i][j+1] and x == board[i+1][j] and x== board[i+1][j+1]:
                    tmp.append([i, j])

        if not tmp:
            break
        else:
            while tmp:
                a, b = tmp.pop()
                if board[a][b] != 0:
                    answer += 1
                    board[a][b] = 0
                if board[a+1][b] != 0:
                    answer += 1
                    board[a+1][b] = 0
                if board[a][b+1] != 0:
                    answer += 1
                    board[a][b+1] = 0
                if board[a+1][b+1] != 0:
                    answer += 1
                    board[a+1][b+1] = 0

        for i in range(m-1, 0, -1):
            for j in range(n):
                if board[i][j] == 0:
                    x = i-1
                    while x>=0:
                        if board[x][j] != 0:
                            board[i][j] = board[x][j]
                            board[x][j] = 0
                            break
                        x -= 1



    return answer

print(solution(6, 6, 	["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))