from collections import deque
import sys
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

m, n = map(int, input().split())

tomato = []
for _ in range(n):
    row = list(map(int, input().split()))
    tomato.append(row)

def bfs(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx <n and 0<= ny <m and tomato[nx][ny] == 0:
            tomato[nx][ny] = 1
            q.append([nx, ny])

q = deque()
minus = deque()
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            q.append([i, j])
        elif tomato[i][j] == -1:
            minus.append([i, j])


cnt = -1
while q:
    cnt += 1
    for i in range(len(q)):
        a, b = q.popleft()
        bfs(a, b)

v = 0
while minus:
    a, b = minus.popleft()
    for i in range(4):
        na = dx[i] + a
        nb = dy[i] + b
        if 0 <= na < n and 0 <= nb < m:
            if tomato[na][nb] == 0:
                v = 1
                break
    if v==1:
        break


if v==1:
    print(-1)
else:
    print(cnt)