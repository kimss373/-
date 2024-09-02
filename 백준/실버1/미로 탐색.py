from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n, m = map(int, input().split())
maze = []
for i in range(n):
    maze.append(list(map(int, input())))

q = deque()
q.append([0, 0])
while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if maze[nx][ny] == 1 or maze[nx][ny] > maze[x][y] + 1:
                q.append([nx, ny])
                maze[nx][ny] = maze[x][y] + 1

print(maze[n-1][m-1])