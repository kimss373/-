import sys
from collections import deque
input = sys.stdin.readline
m, n = map(int, input().split())

cnt = 0
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

q = deque()
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            q.append([i, j, 0])

day = 0
while q:
    x, y, c = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0:
            day = c+1
            arr[nx][ny] = c+1
            q.append([nx,ny,c+1])

isAll = True
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            isAll = False
            break
if isAll:
    print(day)
else:
    print(-1)