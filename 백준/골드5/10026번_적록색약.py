from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n = int(input())
paint = []
for _ in range(n):
    paint.append(list(input()))

visit = [[0 for _ in range(n)] for _ in range(n)]

cnt = 0
blind_cnt = 0
q = deque()
def bfs(a, b):
    q.append([a, b])
    visit[a][b] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0 <= ny < n and visit[nx][ny] == 0 and paint[nx][ny] == paint[x][y]:
                visit[nx][ny] = 1
                q.append([nx, ny])

for i in range(n):
    for j in range(n):
        if visit[i][j] == 0:
            bfs(i, j)
            cnt += 1


visit = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if paint[i][j] == 'G':
            paint[i][j] = 'R'

for i in range(n):
    for j in range(n):
        if visit[i][j] == 0:
            blind_cnt += 1
            bfs(i, j)

print(cnt, blind_cnt)