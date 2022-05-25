import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

row, column = map(int, input().split())
island = []
for _ in range(row):
    a = list(input().strip())
    island.append(a)

q = deque()
big = 0
for i in range(row):
    for j in range(column):
        if island[i][j] == 'L':
            visit = [[0 for _ in range(column)] for _ in range(row)]
            q.append([i, j, 0])
            visit[i][j] = 1
        while q:
            x, y, z = q.popleft()
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0<=nx<row and 0<=ny<column and island[nx][ny] == 'L' and visit[nx][ny] == 0:
                    q.append([nx, ny, z+1])
                    visit[nx][ny] = z+1
                    if z+1>big:
                        big = z+1

print(big)