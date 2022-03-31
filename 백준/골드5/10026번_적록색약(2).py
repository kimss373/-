from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n = int(input())
paint = []
for _ in range(n):
    paint.append(list(input()))

visit = [[0 for _ in range(n)] for _ in range(n)]
blind_visit = [[0 for _ in range(n)] for _ in range(n)]
cnt = 0
blind_cnt = 0
q = deque()
for i in range(n):
    for j in range(n):
        if visit[i][j] == 0:
            visit[i][j] = 1
            cnt += 1
            q.append([i, j])
            while q:
                x, y = q.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0<= nx < n and 0<= ny < n and paint[nx][ny] == paint[x][y] and visit[nx][ny] == 0:
                        visit[nx][ny] = 1
                        q.append([nx, ny])

        if blind_visit[i][j] == 0:
            blind_cnt += 1
            blind_visit[i][j] = 1
            q.append([i, j])
            if paint[i][j] == 'R' or 'G':
                while q:
                    x, y = q.popleft()
                    for l in range(4):
                        nx = x + dx[l]
                        ny = y + dy[l]
                        if 0<= nx < n and 0<= ny < n and paint[nx][ny] == 'R' and blind_visit[nx][ny] == 0:
                            blind_visit[nx][ny] = 1
                            q.append([nx, ny])
                        elif 0<= nx < n and 0<= ny < n and paint[nx][ny] == 'G' and blind_visit[nx][ny] == 0:
                            blind_visit[nx][ny] = 1
                            q.append([nx, ny])
            else:
                while q:
                    x, y = q.popleft()
                    for v in range(4):
                        nx = x + dx[v]
                        ny = y + dy[v]
                        if 0 <= nx < n and 0 <= ny < n and paint[nx][ny] == paint[x][y] and blind_visit[nx][ny] == 0:
                            blind_visit[nx][ny] = 1
                            q.append([nx, ny])
print(cnt, blind_cnt)
