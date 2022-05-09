from collections import deque
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def solution(maps):
    q = deque()
    q.append([0, 0])
    column = len(maps[0])
    row = len(maps)
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<row and 0<=ny<column and maps[nx][ny] ==1:
                maps[nx][ny] = maps[x][y] +1
                q.append([nx, ny])
    if maps[row-1][column-1] == 1:
        answer = -1
    else:
        answer = maps[row-1][column-1]
    return answer

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))