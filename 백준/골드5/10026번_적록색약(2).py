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

for i in range(n):
    for j in range(n):
        if visit[i][j] == 0:
            visit[i][j] = 1
            cnt += 1
            color = paint[i][j]
            q = deque()
            q.append([i, j])
            while q:
                x, y = q.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0<= nx < n and 0<= ny < n and paint[nx][ny] == color and visit[nx][ny] == 0:
                        visit[nx][ny] = 1
                        q.append([nx, ny])

        if blind_visit[i][j] == 0:
            blind_cnt += 1
            q = deque()
            blind_visit[i][j] = 1
            if paint[i][j] == 'R' or 'G':
                q.append([i, j])
                while q:
                    x, y = q.popleft()
                    for l in range(4):
                        nx = x + dx[l]
                        ny = y + dy[l]
                        if 0<= nx < n and 0<= ny < n and paint[nx][ny] == 'R' and [nx, ny] not in q and blind_visit[nx][ny] == 0:
                            blind_visit[nx][ny] = 1
                            q.append([nx, ny])
                        elif 0<= nx < n and 0<= ny < n and paint[nx][ny] == 'G' and [nx, ny] not in q and blind_visit[nx][ny] == 0:
                            blind_visit[nx][ny] = 1
                            q.append([nx, ny])
            if paint[i][j] == 'B':
                q.append([i, j])
                while q:
                    x, y = q.popleft()
                    for v in range(4):
                        nx = x + dx[v]
                        ny = y + dy[v]
                        if 0 <= nx < n and 0 <= ny < n and paint[nx][ny] == 'B' and [nx, ny] not in q and blind_visit[nx][ny] == 0:
                            blind_visit[nx][ny] = 1
                            q.append([nx, ny])
print(cnt, blind_cnt)
print(paint)
print(visit)
print(blind_visit)
